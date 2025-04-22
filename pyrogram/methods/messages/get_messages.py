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

import logging
from collections.abc import Iterable
from typing import Union

import pyrogram
from pyrogram import raw, types, utils

log = logging.getLogger(__name__)


# TODO: Rewrite using a flag for replied messages and have message_ids non-optional


class GetMessages:
    async def get_messages(
        self: "pyrogram.Client",
        chat_id: int | str,
        message_ids: int | Iterable[int] | None = None,
        reply_to_message_ids: int | Iterable[int] | None = None,
        replies: int = 1,
    ) -> Union["types.Message", list["types.Message"]]:
        """Get one or more messages from a chat by using message identifiers.

        You can retrieve up to 200 messages at once.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_ids (``int`` | Iterable of ``int``, *optional*):
                Pass a single message identifier or an iterable of message ids (as integers) to get the content of the
                message themselves.

            reply_to_message_ids (``int`` | Iterable of ``int``, *optional*):
                Pass a single message identifier or an iterable of message ids (as integers) to get the content of
                the previous message you replied to using this message.
                If *message_ids* is set, this argument will be ignored.

            replies (``int``, *optional*):
                The number of subsequent replies to get for each message.
                Pass 0 for no reply at all or -1 for unlimited replies.
                Defaults to 1.

        Returns:
            :obj:`~pyrogram.types.Message` | List of :obj:`~pyrogram.types.Message`: In case *message_ids* was not
            a list, a single message is returned, otherwise a list of messages is returned.

        Example:
            .. code-block:: python

                # Get one message
                await app.get_messages(chat_id, 12345)

                # Get more than one message (list of messages)
                await app.get_messages(chat_id, [12345, 12346])

                # Get message by ignoring any replied-to message
                await app.get_messages(chat_id, message_id, replies=0)

                # Get message with all chained replied-to messages
                await app.get_messages(chat_id, message_id, replies=-1)

                # Get the replied-to message of a message
                await app.get_messages(chat_id, reply_to_message_ids=message_id)

        Raises:
            ValueError: In case of invalid arguments.
        """
        if reply_to_message_ids:
            return await self.get_reply_messages(
                chat_id=chat_id,
                message_ids=reply_to_message_ids,
                replies=replies,
            )

        is_iterable = not isinstance(message_ids, int)
        ids: list[raw.types.InputMessageID] = []

        if is_iterable:
            ids.extend(
                raw.types.InputMessageID(id=message_id) for message_id in message_ids
            )
        else:
            ids.append(raw.types.InputMessageID(id=message_ids))

        messages = await self._get_messages(
            chat_id=chat_id,
            message_ids=ids,
            replies=replies,
        )

        if is_iterable:
            return messages
        return messages[0] if messages else None

    async def _get_messages(
        self: "pyrogram.Client",
        chat_id: int,
        message_ids: list[raw.base.InputMessage],
        replies: int = 1,
    ) -> list[types.Message]:
        if len(message_ids) < 1:
            raise ValueError("No message_ids were provided")

        if replies < 0:
            replies = (1 << 31) - 1

        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerChannel):
            rpc = raw.functions.channels.GetMessages(channel=peer, id=message_ids)
        else:
            rpc = raw.functions.messages.GetMessages(id=message_ids)

        r = await self.invoke(rpc, sleep_threshold=-1)
        return await utils.parse_messages(self, r, replies=replies)

    def get_cached_message(
        self: "pyrogram.Client",
        *,
        chat_id: int,
        message_id: int,
    ) -> types.Message | None:
        try:
            return self.message_cache[(chat_id, message_id)]
        except (KeyError, IndexError):
            return None

    async def get_callback_query_message(
        self: "pyrogram.Client",
        *,
        chat_id: int,
        message_id: int,
        query_id: int,
        replies: int = 1,
        force: bool = False,
    ) -> types.Message | None:
        if not force:
            cached_message = self.get_cached_message(
                chat_id=chat_id,
                message_id=message_id,
            )
            if cached_message:
                return cached_message

        messages = await self._get_messages(
            chat_id=chat_id,
            message_ids=[
                raw.types.InputMessageCallbackQuery(
                    id=message_id,
                    query_id=query_id,
                ),
            ],
            replies=replies,
        )

        for message in messages:
            return message
        return None

    async def get_reply_messages(
        self: "pyrogram.Client",
        *,
        chat_id: int,
        message_ids: int | list[int],
        replies: int = 1,
    ) -> list[types.Message] | types.Message | None:
        is_iterable = not isinstance(message_ids, int)

        ids: list[raw.types.InputMessageReplyTo] = []

        if is_iterable:
            ids.extend(
                raw.types.InputMessageReplyTo(id=message_id)
                for message_id in message_ids
            )
        else:
            ids.append(raw.types.InputMessageReplyTo(id=message_ids))

        messages = await self._get_messages(
            chat_id=chat_id,
            message_ids=ids,
            replies=replies,
        )

        if is_iterable:
            return messages
        return messages[0] if messages else None
