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
import inspect
import logging
from collections import OrderedDict

import pyrogram
from pyrogram import errors
from pyrogram import utils
from pyrogram import raw
from pyrogram.handlers import (
    CallbackQueryHandler, MessageHandler, EditedMessageHandler, DeletedMessagesHandler,
    UserStatusHandler, RawUpdateHandler, InlineQueryHandler, PollHandler, PreCheckoutQueryHandler,
    ChosenInlineResultHandler, ChatMemberUpdatedHandler, ChatJoinRequestHandler, StoryHandler
)
from pyrogram.raw.core import TLObject
from pyrogram.raw.types import (
    UpdateNewMessage, UpdateNewChannelMessage, UpdateNewScheduledMessage,
    UpdateBotNewBusinessMessage, UpdateBotEditBusinessMessage, UpdateBotDeleteBusinessMessage,
    UpdateEditMessage, UpdateEditChannelMessage,
    UpdateDeleteMessages, UpdateDeleteChannelMessages,
    UpdateBotCallbackQuery, UpdateInlineBotCallbackQuery, UpdateBotPrecheckoutQuery,
    UpdateUserStatus, UpdateBotInlineQuery, UpdateMessagePoll,
    UpdateBotInlineSend, UpdateChatParticipant, UpdateChannelParticipant,
    UpdateBotChatInviteRequester, UpdateStory
)

log = logging.getLogger(__name__)


class Dispatcher:
    NEW_MESSAGE_UPDATES = (UpdateNewMessage, UpdateNewChannelMessage, UpdateNewScheduledMessage, UpdateBotNewBusinessMessage)
    EDIT_MESSAGE_UPDATES = (UpdateEditMessage, UpdateEditChannelMessage, UpdateBotEditBusinessMessage)
    DELETE_MESSAGES_UPDATES = (UpdateDeleteMessages, UpdateDeleteChannelMessages, UpdateBotDeleteBusinessMessage)
    CALLBACK_QUERY_UPDATES = (UpdateBotCallbackQuery, UpdateInlineBotCallbackQuery)
    CHAT_MEMBER_UPDATES = (UpdateChatParticipant, UpdateChannelParticipant)
    USER_STATUS_UPDATES = (UpdateUserStatus,)
    BOT_INLINE_QUERY_UPDATES = (UpdateBotInlineQuery,)
    POLL_UPDATES = (UpdateMessagePoll,)
    CHOSEN_INLINE_RESULT_UPDATES = (UpdateBotInlineSend,)
    CHAT_JOIN_REQUEST_UPDATES = (UpdateBotChatInviteRequester,)
    NEW_STORY_UPDATES = (UpdateStory,)
    PRE_CHECKOUT_QUERY_UPDATES = (UpdateBotPrecheckoutQuery,)

    def __init__(self, client: "pyrogram.Client"):
        self.client = client

        self.handler_worker_tasks = []
        self.locks_list = []

        self.updates_queue = asyncio.Queue[TLObject | None]()
        self.groups = OrderedDict()

        async def messagefrom_raw_tlr(update):
            return (
                await pyrogram.types.Message.from_raw_tl(
                    self.client,
                    update.message,
                    is_scheduled=isinstance(update, UpdateNewScheduledMessage),
                    business_connection_id=getattr(update, "connection_id", None),
                    reply_to_message=getattr(update, "reply_to_message", None)
                ),
                MessageHandler
            )

        async def edited_messagefrom_raw_tlr(update):
            # Edited messages are parsed the same way as new messages, but the handler is different
            parsed, _ = await messagefrom_raw_tlr(update)

            return (
                parsed,
                EditedMessageHandler
            )

        async def deleted_messagesfrom_raw_tlr(update):
            return (
                utils.parse_deleted_messages(self.client, update),
                DeletedMessagesHandler,
            )

        async def callback_queryfrom_raw_tlr(update):
            return (
                await pyrogram.types.CallbackQuery.from_raw_tl(self.client, update),
                CallbackQueryHandler
            )

        async def user_statusfrom_raw_tlr(update):
            return (
                pyrogram.types.User.from_raw_tl_user_status(self.client, update),
                UserStatusHandler
            )

        async def inline_queryfrom_raw_tlr(update):
            return (
                pyrogram.types.InlineQuery.from_raw_tl(self.client, update),
                InlineQueryHandler
            )

        async def pollfrom_raw_tlr(update):
            return (
                pyrogram.types.Poll.from_raw_tl_update(self.client, update),
                PollHandler
            )

        async def chosen_inline_resultfrom_raw_tlr(update):
            return (
                pyrogram.types.ChosenInlineResult.from_raw_tl(self.client, update),
                ChosenInlineResultHandler
            )

        async def chat_member_updatedfrom_raw_tlr(update):
            return (
                pyrogram.types.ChatMemberUpdated.from_raw_tl(self.client, update),
                ChatMemberUpdatedHandler
            )

        async def chat_join_requestfrom_raw_tlr(update):
            return (
                pyrogram.types.ChatJoinRequest.from_raw_tl(self.client, update),
                ChatJoinRequestHandler
            )

        async def storyfrom_raw_tlr(update):
            return (
                await pyrogram.types.Story.from_raw_tl(self.client, update.story, update.peer),
                StoryHandler
            )

        async def pre_checkout_queryfrom_raw_tlr(update):
            return (
                await pyrogram.types.PreCheckoutQuery.from_raw_tl(self.client, update),
                PreCheckoutQueryHandler
            )

        self.updatefrom_raw_tlrs = {
            Dispatcher.NEW_MESSAGE_UPDATES: messagefrom_raw_tlr,
            Dispatcher.EDIT_MESSAGE_UPDATES: edited_messagefrom_raw_tlr,
            Dispatcher.DELETE_MESSAGES_UPDATES: deleted_messagesfrom_raw_tlr,
            Dispatcher.CALLBACK_QUERY_UPDATES: callback_queryfrom_raw_tlr,
            Dispatcher.USER_STATUS_UPDATES: user_statusfrom_raw_tlr,
            Dispatcher.BOT_INLINE_QUERY_UPDATES: inline_queryfrom_raw_tlr,
            Dispatcher.POLL_UPDATES: pollfrom_raw_tlr,
            Dispatcher.CHOSEN_INLINE_RESULT_UPDATES: chosen_inline_resultfrom_raw_tlr,
            Dispatcher.CHAT_MEMBER_UPDATES: chat_member_updatedfrom_raw_tlr,
            Dispatcher.CHAT_JOIN_REQUEST_UPDATES: chat_join_requestfrom_raw_tlr,
            Dispatcher.NEW_STORY_UPDATES: storyfrom_raw_tlr,
            Dispatcher.PRE_CHECKOUT_QUERY_UPDATES: pre_checkout_queryfrom_raw_tlr
        }

        self.updatefrom_raw_tlrs = {key: value for key_tuple, value in self.updatefrom_raw_tlrs.items() for key in key_tuple}

    async def start(self):
        if self.client.no_updates:
            return

        for i in range(self.client.workers):
            self.locks_list.append(asyncio.Lock())

            self.handler_worker_tasks.append(
                asyncio.create_task(self.handler_worker(self.locks_list[-1]))
            )

        log.info("Started %s HandlerTasks", self.client.workers)

    async def stop(self):
        if self.client.no_updates:
            return

        for i in range(self.client.workers):
            self.updates_queue.put_nowait(None)

        for i in self.handler_worker_tasks:
            await i

        self.handler_worker_tasks.clear()
        self.groups.clear()

        log.info("Stopped %s HandlerTasks", self.client.workers)

    def add_handler(self, handler, group: int):
        async def fn():
            for lock in self.locks_list:
                await lock.acquire()

            try:
                if group not in self.groups:
                    self.groups[group] = []
                    self.groups = OrderedDict(sorted(self.groups.items()))

                self.groups[group].append(handler)
            finally:
                for lock in self.locks_list:
                    lock.release()

        asyncio.create_task(fn())

    def remove_handler(self, handler, group: int):
        async def fn():
            for lock in self.locks_list:
                await lock.acquire()

            try:
                if group not in self.groups:
                    raise ValueError(f"Group {group} does not exist. Handler was not removed.")

                self.groups[group].remove(handler)
            finally:
                for lock in self.locks_list:
                    lock.release()

        asyncio.create_task(fn())

    async def handler_worker(self, lock):
        while True:
            update = await self.updates_queue.get()

            if update is None:
                break

            try:
                parser = self.updatefrom_raw_tlrs.get(type(update), None)

                parsed_update, handler_type = (
                    await parser(update)
                    if parser is not None
                    else (None, type(None))
                )

                async with lock:
                    for group in self.groups.values():
                        for handler in group:
                            args = None

                            if isinstance(handler, handler_type):
                                try:
                                    if await handler.check(self.client, parsed_update):
                                        args = (parsed_update,)
                                except Exception as e:
                                    log.exception(e)
                                    continue

                            elif isinstance(handler, RawUpdateHandler):
                                args = (update, {}, {})

                            if args is None:
                                continue

                            try:
                                await handler.callback(self.client, *args)
                            except pyrogram.StopPropagation:
                                raise
                            except pyrogram.ContinuePropagation:
                                continue
                            except Exception as e:
                                log.exception(e)

                            break
            except pyrogram.StopPropagation:
                pass
            except Exception as e:
                log.exception(e)
