import asyncio
import logging
from collections.abc import Awaitable, Callable
from typing import (
    Any,
    Final,
)


class Termination: ...


termination: Final[Termination] = Termination()

logger = logging.getLogger(__name__)


class AsyncioWorkerPool[I]:
    def __init__(
        self,
        name: str,
        func: Callable[[I], Awaitable[Any]],
        queue: asyncio.Queue[I | Termination],
        concurrency: int = 1,
    ) -> None:
        if concurrency < 1:
            raise ValueError("concurrency must be greater than 0")

        self._name = name
        self._func = func
        self._concurrency = concurrency
        self._queue = queue

        self._workers: set[asyncio.Task[None]] = set()

    async def start(self) -> None:
        logger.debug("Starting %d workers for %s", self._concurrency, self._name)
        for index in range(self._concurrency):
            name = f"pool-worker-{self._name}-{index}"
            task = asyncio.create_task(
                self._worker(
                    name=name,
                ),
                name=name,
            )
            self._workers.add(task)
            task.add_done_callback(self._workers.discard)

        logger.debug("Started %d workers for %s", self._concurrency, self._name)

    async def stop(self) -> None:
        logger.debug("Stopping %d workers for %s", self._concurrency, self._name)
        for _ in range(self._concurrency):
            await self._queue.put(termination)

        logger.debug(
            "Waiting for %d workers for %s to stop",
            len(self._workers),
            self._name,
        )
        if self._workers:
            await asyncio.wait(self._workers)
        logger.debug("All workers for %s stopped", self._name)

    async def _worker(self, name: str) -> None:
        logger.debug("Starting worker %s", name)
        while True:
            try:
                logger.debug("Waiting for an item in queue for worker %s", name)
                item = await self._queue.get()
                if item is termination:
                    logger.debug("Got termination item in queue for worker %s", name)
                    break

                logger.debug("Got an item in queue for worker %s", name)

                try:
                    await self._func(item)
                except (asyncio.CancelledError, asyncio.InvalidStateError):
                    break
                except Exception as exc:
                    logger.exception(
                        "Unhandled exception in worker %s",
                        name,
                        exc_info=exc,
                    )
                else:
                    logger.debug("Worker %s finished processing an item", name)
                finally:
                    self._queue.task_done()
            except (asyncio.CancelledError, asyncio.InvalidStateError):
                break

    @property
    def concurrency(self) -> int:
        return self._concurrency
