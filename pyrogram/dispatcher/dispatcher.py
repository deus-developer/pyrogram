#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
import logging
from collections.abc import Awaitable, Callable
from enum import IntEnum
from typing import (
    NamedTuple,
    assert_never,
)

from aiorwlock import RWLock

import pyrogram
from pyrogram.dispatcher.pool import AsyncioWorkerPool
from pyrogram.dispatcher.schemas import (
    TelegramRawUpdate,
    TelegramUpdate,
)
from pyrogram.handlers import (
    Handler,
)

log = logging.getLogger(__name__)


class DispatcherState(IntEnum):
    CONTINUE_GROUP = 1
    BREAK_GROUP = 2
    BREAK_UPDATE = 3


class DispatcherAddHandlerOperation(NamedTuple):
    handler: Handler
    group: int


class DispatcherRemoveHandlerOperation(NamedTuple):
    handler: Handler
    group: int


DispatcherOperation = DispatcherAddHandlerOperation | DispatcherRemoveHandlerOperation


class Dispatcher:
    def __init__(
        self,
        name: str,
        parser: Callable[
            ["pyrogram.Client", TelegramRawUpdate],
            Awaitable[TelegramUpdate],
        ],
        concurrency: int,
    ) -> None:
        if concurrency < 1:
            raise ValueError("Concurrency must be at least 1")

        self._name = name
        self._parser = parser
        self._concurrency = concurrency

        self.raw_updates_queue = asyncio.Queue[
            tuple[pyrogram.Client, TelegramRawUpdate]
        ]()
        self.updates_queue = asyncio.Queue[tuple[pyrogram.Client, TelegramUpdate]]()
        self.operations_queue = asyncio.Queue[DispatcherOperation]()

        self._raw_updates_worker_pool = AsyncioWorkerPool(
            name=f"dispatcher-{name}-raws",
            func=self.process_raw_update_stage,
            queue=self.raw_updates_queue,
            concurrency=self._concurrency,
        )
        self._updates_worker_pool = AsyncioWorkerPool(
            name=f"dispatcher-{name}-updates",
            func=self.process_update_stage,
            queue=self.updates_queue,
            concurrency=self._concurrency,
        )
        self._operations_worker_pool = AsyncioWorkerPool(
            name=f"dispatcher-{name}-operations",
            func=self.process_operation,
            queue=self.operations_queue,
            concurrency=1,
        )

        self.rw_lock = RWLock()

        self._handlers_by_group: dict[int, list[Handler]] = {}
        self._groups: list[int] = []

        self._started = asyncio.Event()

    def enqueue_raw_update(
        self,
        client: "pyrogram.Client",
        update: TelegramRawUpdate,
    ) -> None:
        self.raw_updates_queue.put_nowait((client, update))

    def enqueue_update(self, client: "pyrogram.Client", update: TelegramUpdate) -> None:
        self.updates_queue.put_nowait((client, update))

    def enqueue_operation(self, operation: DispatcherOperation) -> None:
        self.operations_queue.put_nowait(operation)

    async def start(self) -> None:
        log.debug("Starting dispatcher %s", self._name)
        async with self.rw_lock.writer:
            if self._started.is_set():
                raise RuntimeError("Dispatcher already started")

            self._started.set()

            await self._operations_worker_pool.start()
            await self._updates_worker_pool.start()
            await self._raw_updates_worker_pool.start()

            log.debug("Dispatcher %s started", self._name)

    async def stop(self) -> None:
        log.debug("Stopping dispatcher %s", self._name)
        async with self.rw_lock.writer:
            if not self._started.is_set():
                raise RuntimeError("Dispatcher already stopped")

            self._started.clear()
            await self._raw_updates_worker_pool.stop()
            await self._updates_worker_pool.stop()
            await self._operations_worker_pool.stop()

            log.debug("Dispatcher %s stopped", self._name)

    async def __aenter__(self) -> "Dispatcher":
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.stop()

    def _add_handler(self, handler: Handler, group: int = 0) -> None:
        handlers = self._handlers_by_group.setdefault(group, [])
        handlers.append(handler)

        if group in self._groups:
            return

        self._groups.append(group)
        self._groups.sort()
        return

    def add_handler(self, handler: Handler, group: int = 0) -> None:
        if self._started.is_set():
            self.enqueue_operation(
                DispatcherAddHandlerOperation(
                    handler=handler,
                    group=group,
                ),
            )
        else:
            self._add_handler(
                handler=handler,
                group=group,
            )

    def _remove_handler(self, handler: Handler, group: int) -> None:
        try:
            handlers = self._handlers_by_group[group]
        except KeyError as exc:
            raise ValueError(
                f"Group {group} does not exist. Handler was not removed.",
            ) from exc

        handlers.remove(handler)

    def remove_handler(self, handler: Handler, group: int) -> None:
        if self._started.is_set():
            self.enqueue_operation(
                DispatcherRemoveHandlerOperation(
                    handler=handler,
                    group=group,
                ),
            )
        else:
            self._remove_handler(
                handler=handler,
                group=group,
            )

    async def process_operation(self, item: DispatcherOperation) -> None:
        async with self.rw_lock.writer:
            if isinstance(item, DispatcherAddHandlerOperation):
                self._add_handler(
                    handler=item.handler,
                    group=item.group,
                )
            elif isinstance(item, DispatcherRemoveHandlerOperation):
                self._remove_handler(
                    handler=item.handler,
                    group=item.group,
                )
            else:
                assert_never(item)

    async def join_operations(self) -> None:
        if not self._started.is_set():
            return
        await self.operations_queue.join()

    async def process_handler_stage(
        self,
        client: "pyrogram.Client",
        handler: Handler,
        update: TelegramUpdate,
    ) -> DispatcherState:
        args = None

        if handler.event_type == "raw":
            if await handler.check(client, update.raw):
                args = (
                    update.raw.update,
                    update.raw.users,
                    update.raw.chats,
                )
        elif handler.event_type == update.event_type:
            if await handler.check(client, update.event):
                args = (update.event,)

        if args is None:
            return DispatcherState.CONTINUE_GROUP

        try:
            await handler.callback(client, *args)
        except pyrogram.StopPropagation:
            return DispatcherState.BREAK_UPDATE
        except pyrogram.ContinuePropagation:
            return DispatcherState.CONTINUE_GROUP
        except Exception as e:
            log.exception(e)

        return DispatcherState.BREAK_GROUP

    async def process_group_stage(
        self,
        group: int,
        client: "pyrogram.Client",
        update: TelegramUpdate,
    ) -> DispatcherState:
        for handler in self._handlers_by_group[group]:
            state = await self.process_handler_stage(
                client=client,
                handler=handler,
                update=update,
            )

            if state == DispatcherState.CONTINUE_GROUP:
                continue
            if state == DispatcherState.BREAK_GROUP:
                break
            if state == DispatcherState.BREAK_UPDATE:
                return DispatcherState.BREAK_UPDATE
            assert_never(state)

        return DispatcherState.BREAK_GROUP

    async def process_update_stage(
        self,
        item: tuple["pyrogram.Client", TelegramUpdate],
    ) -> None:
        client, update = item

        async with self.rw_lock.reader:
            for group in self._groups:
                state = await self.process_group_stage(
                    group=group,
                    client=client,
                    update=update,
                )
                if state in (
                    DispatcherState.CONTINUE_GROUP,
                    DispatcherState.BREAK_GROUP,
                ):
                    continue

                if state == DispatcherState.BREAK_UPDATE:
                    return

                assert_never(state)

    async def process_raw_update_stage(
        self,
        item: tuple["pyrogram.Client", TelegramRawUpdate],
    ) -> None:
        client, raw = item

        update = await self._parser(client, raw)
        self.enqueue_update(client, update)
