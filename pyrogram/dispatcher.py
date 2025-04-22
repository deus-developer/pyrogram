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
from collections import OrderedDict

import pyrogram
from pyrogram import utils
from pyrogram.handlers import (
    CallbackQueryHandler,
    ChatJoinRequestHandler,
    ChatMemberUpdatedHandler,
    ChosenInlineResultHandler,
    DeletedMessagesHandler,
    EditedMessageHandler,
    InlineQueryHandler,
    MessageHandler,
    PollHandler,
    PreCheckoutQueryHandler,
    RawUpdateHandler,
    StoryHandler,
    UserStatusHandler,
)
from pyrogram.raw.core import TLObject
from pyrogram.raw.types import (
    UpdateBotCallbackQuery,
    UpdateBotChatInviteRequester,
    UpdateBotDeleteBusinessMessage,
    UpdateBotEditBusinessMessage,
    UpdateBotInlineQuery,
    UpdateBotInlineSend,
    UpdateBotNewBusinessMessage,
    UpdateBotPrecheckoutQuery,
    UpdateChannelParticipant,
    UpdateChatParticipant,
    UpdateDeleteChannelMessages,
    UpdateDeleteMessages,
    UpdateEditChannelMessage,
    UpdateEditMessage,
    UpdateInlineBotCallbackQuery,
    UpdateMessagePoll,
    UpdateNewChannelMessage,
    UpdateNewMessage,
    UpdateNewScheduledMessage,
    UpdateStory,
    UpdateUserStatus,
)

log = logging.getLogger(__name__)


class Dispatcher:
    NEW_MESSAGE_UPDATES = (
        UpdateNewMessage,
        UpdateNewChannelMessage,
        UpdateNewScheduledMessage,
        UpdateBotNewBusinessMessage,
    )
    EDIT_MESSAGE_UPDATES = (
        UpdateEditMessage,
        UpdateEditChannelMessage,
        UpdateBotEditBusinessMessage,
    )
    DELETE_MESSAGES_UPDATES = (
        UpdateDeleteMessages,
        UpdateDeleteChannelMessages,
        UpdateBotDeleteBusinessMessage,
    )
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

        async def message_parser(update):
            return (
                await pyrogram.types.Message.from_raw_tl(
                    self.client,
                    update.message,
                    is_scheduled=isinstance(update, UpdateNewScheduledMessage),
                    business_connection_id=getattr(update, "connection_id", None),
                    reply_to_message=getattr(update, "reply_to_message", None),
                ),
                MessageHandler,
            )

        async def edited_message_parser(update):
            # Edited messages are parsed the same way as new messages, but the handler is different
            parsed, _ = await message_parser(update)

            return (
                parsed,
                EditedMessageHandler,
            )

        async def deleted_messages_parser(update):
            return (
                utils.parse_deleted_messages(self.client, update),
                DeletedMessagesHandler,
            )

        async def callback_query_parser(update):
            return (
                await pyrogram.types.CallbackQuery.from_raw_tl(self.client, update),
                CallbackQueryHandler,
            )

        async def user_status_parser(update):
            return (
                pyrogram.types.User.from_raw_tl_user_status(self.client, update),
                UserStatusHandler,
            )

        async def inline_query_parser(update):
            return (
                pyrogram.types.InlineQuery.from_raw_tl(self.client, update),
                InlineQueryHandler,
            )

        async def poll_parser(update):
            return (
                pyrogram.types.Poll.from_raw_tl_update(self.client, update),
                PollHandler,
            )

        async def chosen_inline_result_parser(update):
            return (
                pyrogram.types.ChosenInlineResult.from_raw_tl(self.client, update),
                ChosenInlineResultHandler,
            )

        async def chat_member_updated_parser(update):
            return (
                pyrogram.types.ChatMemberUpdated.from_raw_tl(self.client, update),
                ChatMemberUpdatedHandler,
            )

        async def chat_join_request_parser(update):
            return (
                pyrogram.types.ChatJoinRequest.from_raw_tl(self.client, update),
                ChatJoinRequestHandler,
            )

        async def story_parser(update):
            return (
                await pyrogram.types.Story.from_raw_tl(
                    self.client,
                    update.story,
                    update.peer,
                ),
                StoryHandler,
            )

        async def pre_checkout_query_parser(update):
            return (
                await pyrogram.types.PreCheckoutQuery.from_raw_tl(self.client, update),
                PreCheckoutQueryHandler,
            )

        self.update_parsers = {
            Dispatcher.NEW_MESSAGE_UPDATES: message_parser,
            Dispatcher.EDIT_MESSAGE_UPDATES: edited_message_parser,
            Dispatcher.DELETE_MESSAGES_UPDATES: deleted_messages_parser,
            Dispatcher.CALLBACK_QUERY_UPDATES: callback_query_parser,
            Dispatcher.USER_STATUS_UPDATES: user_status_parser,
            Dispatcher.BOT_INLINE_QUERY_UPDATES: inline_query_parser,
            Dispatcher.POLL_UPDATES: poll_parser,
            Dispatcher.CHOSEN_INLINE_RESULT_UPDATES: chosen_inline_result_parser,
            Dispatcher.CHAT_MEMBER_UPDATES: chat_member_updated_parser,
            Dispatcher.CHAT_JOIN_REQUEST_UPDATES: chat_join_request_parser,
            Dispatcher.NEW_STORY_UPDATES: story_parser,
            Dispatcher.PRE_CHECKOUT_QUERY_UPDATES: pre_checkout_query_parser,
        }

        self.update_parsers = {
            key: value
            for key_tuple, value in self.update_parsers.items()
            for key in key_tuple
        }

    async def start(self):
        if self.client.no_updates:
            return

        for _ in range(self.client.workers):
            self.locks_list.append(asyncio.Lock())

            self.handler_worker_tasks.append(
                asyncio.create_task(self.handler_worker(self.locks_list[-1])),
            )
        log.info("Started %s HandlerTasks", self.client.workers)

    async def stop(self):
        if self.client.no_updates:
            return

        for _ in range(self.client.workers):
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
                    raise ValueError(
                        f"Group {group} does not exist. Handler was not removed.",
                    )

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
                parser = self.update_parsers.get(type(update), None)

                parsed_update, handler_type = (
                    await parser(update) if parser is not None else (None, type(None))
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
