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
import base64
import functools
import hashlib
import os
import re
import struct
from collections import defaultdict
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import UTC, datetime
from getpass import getpass
from typing import (
    Union,
    assert_never,
)

import pyrogram
from pyrogram import enums, raw, types
from pyrogram.enums import MessageServiceType
from pyrogram.file_id import DOCUMENT_TYPES, PHOTO_TYPES, FileId, FileType


async def ainput(prompt: str = "", *, hide: bool = False):
    """Just like the built-in input, but async"""
    with ThreadPoolExecutor(1) as executor:
        func = functools.partial(getpass if hide else input, prompt)
        return await asyncio.get_event_loop().run_in_executor(executor, func)


def get_input_media_from_file_id(
    file_id: str,
    expected_file_type: FileType = None,
    ttl_seconds: int | None = None,
    has_spoiler: bool | None = None,
) -> Union["raw.types.InputMediaPhoto", "raw.types.InputMediaDocument"]:
    try:
        decoded = FileId.decode(file_id)
    except Exception as exc:
        raise ValueError(
            f'Failed to decode "{file_id}". The value does not represent an existing local file, '
            f"HTTP URL, or valid file id.",
        ) from exc

    file_type = decoded.file_type

    if expected_file_type is not None and file_type != expected_file_type:
        raise ValueError(
            f"Expected {expected_file_type.name}, got {file_type.name} file id instead",
        )

    if file_type in (FileType.THUMBNAIL, FileType.CHAT_PHOTO):
        raise ValueError(f"This file id can only be used for download: {file_id}")

    if file_type in PHOTO_TYPES:
        return raw.types.InputMediaPhoto(
            id=raw.types.InputPhoto(
                id=decoded.media_id,
                access_hash=decoded.access_hash,
                file_reference=decoded.file_reference,
            ),
            spoiler=has_spoiler,
            ttl_seconds=ttl_seconds,
        )

    if file_type in DOCUMENT_TYPES:
        return raw.types.InputMediaDocument(
            id=raw.types.InputDocument(
                id=decoded.media_id,
                access_hash=decoded.access_hash,
                file_reference=decoded.file_reference,
            ),
            spoiler=has_spoiler,
            ttl_seconds=ttl_seconds,
        )

    raise ValueError(f"Unknown file id: {file_id}")


async def parse_messages(
    client,
    messages: "raw.base.messages.Messages",
    replies: int = 1,
    business_connection_id: str | None = None,
) -> list["types.Message"]:
    raw_messages: list[raw.base.Message] = []
    raw_chats: list[raw.base.Chat] = []
    raw_users: list[raw.base.User] = []
    raw_topics: list[raw.base.ForumTopic] = []

    if messages is None:
        return types.List()
    if isinstance(
        messages,
        (
            raw.types.messages.Messages,
            raw.types.messages.MessagesSlice,
            raw.types.messages.ChannelMessages,
        ),
    ):
        raw_messages.extend(messages.messages)
        raw_chats.extend(messages.chats)
        raw_users.extend(messages.users)
    elif isinstance(messages, raw.types.messages.MessagesNotModified):
        return types.List()
    else:
        assert_never(messages)

    if isinstance(messages, raw.types.messages.ChannelMessages):
        raw_topics.extend(messages.topics)

    topics: dict[int, raw.base.ForumTopic] = {topic.id: topic for topic in raw_topics}

    parsed_messages: list[types.Message | None] = []
    parsed_message_map: dict[tuple[int, int], types.Message] = {}

    messages_with_replies: dict[tuple[int, int], raw.types.MessageReplyHeader] = {}

    for raw_message in raw_messages:
        if isinstance(
            raw_message,
            (
                raw.types.Message,
                raw.types.MessageService,
            ),
        ):
            if isinstance(raw_message.reply_to, raw.types.MessageReplyHeader):
                messages_with_replies[
                    (
                        get_peer_id(raw_message.peer_id),
                        raw_message.id,
                    )
                ] = raw_message.reply_to

        parsed_message = await types.Message.from_raw_tl(
            client,
            raw_message,
            topics,
            replies=0,
            business_connection_id=business_connection_id,
        )
        parsed_messages.append(parsed_message)
        parsed_message_map[(parsed_message.chat.id, parsed_message.id)] = parsed_message

    if replies == 0:
        return types.List(parsed_messages)

    reply_message_by_id = await get_reply_messages(
        client=client,
        messages_with_replies=messages_with_replies,
        replies=replies,
    )

    for (chat_id, message_id), reply_to in raw_messages:
        parsed_message = parsed_message_map.get((chat_id, message_id))
        if parsed_message is None:
            continue

        if reply_to.reply_to_msg_id is None:
            continue

        if reply_to.reply_to_peer_id:
            reply_chat_id = get_peer_id(reply_to.reply_to_peer_id)
        else:
            reply_chat_id = chat_id

        reply_to_message = reply_message_by_id.get(
            (reply_chat_id, reply_to.reply_to_message_id),
        )
        if reply_to_message is None:
            continue

        if reply_to_message.service == MessageServiceType.FORUM_TOPIC_CREATED:
            continue

        parsed_message.reply_to_message = reply_to_message

    return types.List(parsed_messages)


async def get_reply_messages(
    client,
    messages_with_replies: dict[tuple[int, int], raw.types.MessageReplyHeader],
    replies: int,
) -> dict[tuple[int, int], types.Message]:
    queries: defaultdict[int, set[int]] = defaultdict(set)

    for (chat_id, _), reply_to in messages_with_replies.items():
        if reply_to.reply_to_msg_id is None:
            continue

        if reply_to.reply_to_peer_id:
            reply_chat_id = get_peer_id(reply_to.reply_to_peer_id)
        else:
            reply_chat_id = chat_id

        queries[reply_chat_id].add(reply_to.reply_to_msg_id)

    result: dict[tuple[int, int], types.Message] = {}

    for chat_id, message_ids in queries.items():
        messages = await client.get_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            replies=replies - 1,
        )
        if isinstance(messages, list):
            for message in filter(None, messages):
                result[(message.chat.id, message.id)] = message
        elif isinstance(messages, types.Message):
            result[(messages.chat.id, messages.id)] = messages

    return result


def parse_deleted_messages(client, update) -> list["types.Message"]:
    messages = update.messages
    channel_id = getattr(update, "channel_id", None)
    business_connection_id = getattr(update, "connection_id", None)
    peer = getattr(update, "peer", None)

    chat = None

    if channel_id:
        chat = types.Chat(
            id=get_channel_id(channel_id),
            type=enums.ChatType.CHANNEL,
            client=client,
        )
    if peer:
        chat_id = get_raw_peer_id(peer)
        if chat_id:
            if isinstance(peer, raw.types.PeerUser):
                chat = types.Chat.from_raw_tl_user_chat(
                    client,
                    client.entity_cache.get_peer(peer=peer),
                )

            elif isinstance(peer, raw.types.PeerChat):
                chat = types.Chat.from_raw_tl_chat_chat(
                    client,
                    client.entity_cache.get_peer(peer=peer),
                )

            else:
                chat = types.Chat.from_raw_tl_channel_chat(
                    client,
                    client.entity_cache.get_peer(peer=peer),
                )

    parsed_messages = []

    for message in messages:
        parsed_messages.append(
            types.Message(
                id=message,
                chat=chat,
                business_connection_id=business_connection_id,
                client=client,
            ),
        )

    return types.List(parsed_messages)


def pack_inline_message_id(msg_id: "raw.base.InputBotInlineMessageID"):
    if isinstance(msg_id, raw.types.InputBotInlineMessageID):
        inline_message_id_packed = struct.pack(
            "<iqq",
            msg_id.dc_id,
            msg_id.id,
            msg_id.access_hash,
        )
    else:
        inline_message_id_packed = struct.pack(
            "<iqiq",
            msg_id.dc_id,
            msg_id.owner_id,
            msg_id.id,
            msg_id.access_hash,
        )

    return base64.urlsafe_b64encode(inline_message_id_packed).decode().rstrip("=")


def unpack_inline_message_id(
    inline_message_id: str,
) -> "raw.base.InputBotInlineMessageID":
    padded = inline_message_id + "=" * (-len(inline_message_id) % 4)
    decoded = base64.urlsafe_b64decode(padded)

    if len(decoded) == 20:
        unpacked = struct.unpack("<iqq", decoded)

        return raw.types.InputBotInlineMessageID(
            dc_id=unpacked[0],
            id=unpacked[1],
            access_hash=unpacked[2],
        )
    unpacked = struct.unpack("<iqiq", decoded)

    return raw.types.InputBotInlineMessageID64(
        dc_id=unpacked[0],
        owner_id=unpacked[1],
        id=unpacked[2],
        access_hash=unpacked[3],
    )


MIN_CHANNEL_ID_OLD = -1002147483647
MIN_CHANNEL_ID = -100999999999999
MAX_CHANNEL_ID = -1000000000000
MIN_CHAT_ID = -999999999999
MAX_USER_ID_OLD = 2147483647
MAX_USER_ID = 999999999999


def get_raw_peer_id(
    peer: raw.base.Peer | raw.base.InputPeer | raw.base.RequestedPeer,
) -> int | None:
    """Get the raw peer id from a Peer object"""
    if isinstance(
        peer,
        (raw.types.PeerUser, raw.types.InputPeerUser, raw.types.RequestedPeerUser),
    ):
        return peer.user_id

    if isinstance(
        peer,
        (raw.types.PeerChat, raw.types.InputPeerChat, raw.types.RequestedPeerChat),
    ):
        return peer.chat_id

    if isinstance(
        peer,
        (
            raw.types.PeerChannel,
            raw.types.InputPeerChannel,
            raw.types.RequestedPeerChannel,
        ),
    ):
        return peer.channel_id

    return None


def get_peer_id(
    peer: raw.base.Peer | raw.base.InputPeer | raw.base.RequestedPeer,
) -> int:
    """Get the non-raw peer id from a Peer object"""
    if isinstance(
        peer,
        (raw.types.PeerUser, raw.types.InputPeerUser, raw.types.RequestedPeerUser),
    ):
        return peer.user_id

    if isinstance(
        peer,
        (raw.types.PeerChat, raw.types.InputPeerChat, raw.types.RequestedPeerChat),
    ):
        return -peer.chat_id

    if isinstance(
        peer,
        (
            raw.types.PeerChannel,
            raw.types.InputPeerChannel,
            raw.types.RequestedPeerChannel,
        ),
    ):
        return MAX_CHANNEL_ID - peer.channel_id

    raise ValueError(f"Peer type invalid: {peer}")


def get_peer_type(peer_id: int) -> str:
    if peer_id < 0:
        if peer_id >= MIN_CHAT_ID:
            return "chat"

        if MIN_CHANNEL_ID <= peer_id < MAX_CHANNEL_ID:
            return "channel"
    elif 0 < peer_id <= MAX_USER_ID:
        return "user"

    raise ValueError(f"Peer id invalid: {peer_id}")


def get_reply_to(
    reply_to_message_id: int | None = None,
    message_thread_id: int | None = None,
    reply_to_peer: raw.base.InputPeer | None = None,
    quote_text: str | None = None,
    quote_entities: list[raw.base.MessageEntity] | None = None,
    quote_offset: int | None = None,
    reply_to_story_id: int | None = None,
) -> raw.types.InputReplyToMessage | raw.types.InputReplyToStory | None:
    """Get InputReply for reply_to argument"""
    if all((reply_to_peer, reply_to_story_id)):
        return raw.types.InputReplyToStory(
            peer=reply_to_peer,
            story_id=reply_to_story_id,
        )  # type: ignore[arg-type]

    if any((reply_to_message_id, message_thread_id)):
        return raw.types.InputReplyToMessage(
            reply_to_msg_id=reply_to_message_id or message_thread_id,  # type: ignore[arg-type]
            top_msg_id=message_thread_id if reply_to_message_id else None,
            reply_to_peer_id=reply_to_peer,
            quote_text=quote_text,
            quote_entities=quote_entities,
            quote_offset=quote_offset,
        )

    return None


def get_channel_id(peer_id: int) -> int:
    return MAX_CHANNEL_ID - peer_id


def btoi(b: bytes) -> int:
    return int.from_bytes(b, "big")


def itob(i: int) -> bytes:
    return i.to_bytes(256, "big")


def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def xor(a: bytes, b: bytes) -> bytes:
    return bytes(i ^ j for i, j in zip(a, b, strict=False))


def compute_password_hash(
    algo: raw.types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow,
    password: str,
) -> bytes:
    hash1 = sha256(algo.salt1 + password.encode() + algo.salt1)
    hash2 = sha256(algo.salt2 + hash1 + algo.salt2)
    hash3 = hashlib.pbkdf2_hmac("sha512", hash2, algo.salt1, 100000)

    return sha256(algo.salt2 + hash3 + algo.salt2)


# noinspection PyPep8Naming
def compute_password_check(
    r: raw.types.account.Password,
    password: str,
) -> raw.types.InputCheckPasswordSRP:
    algo = r.current_algo

    p_bytes = algo.p
    p = btoi(algo.p)

    g_bytes = itob(algo.g)
    g = algo.g

    B_bytes = r.srp_B
    B = btoi(B_bytes)

    srp_id = r.srp_id

    x_bytes = compute_password_hash(algo, password)
    x = btoi(x_bytes)

    g_x = pow(g, x, p)

    k_bytes = sha256(p_bytes + g_bytes)
    k = btoi(k_bytes)

    kg_x = (k * g_x) % p

    while True:
        a_bytes = os.urandom(256)
        a = btoi(a_bytes)

        A = pow(g, a, p)
        A_bytes = itob(A)

        u = btoi(sha256(A_bytes + B_bytes))

        if u > 0:
            break

    g_b = (B - kg_x) % p

    ux = u * x
    a_ux = a + ux
    S = pow(g_b, a_ux, p)
    S_bytes = itob(S)

    K_bytes = sha256(S_bytes)

    M1_bytes = sha256(
        xor(sha256(p_bytes), sha256(g_bytes))
        + sha256(algo.salt1)
        + sha256(algo.salt2)
        + A_bytes
        + B_bytes
        + K_bytes,
    )

    return raw.types.InputCheckPasswordSRP(srp_id=srp_id, A=A_bytes, M1=M1_bytes)


async def parse_text_entities(
    client: "pyrogram.Client",
    text: str,
    parse_mode: enums.ParseMode,
    entities: list["types.MessageEntity"],
) -> dict[str, str | list[raw.base.MessageEntity]]:
    if entities:
        # Inject the client instance because parsing user mentions requires it
        for entity in entities:
            entity.bind(client)

        text, entities = text, [await entity.write() for entity in entities] or None
    else:
        text, entities = (await client.parser.parse(text, parse_mode)).values()

    return {
        "message": text,
        "entities": entities,
    }


def zero_datetime() -> datetime:
    return datetime.fromtimestamp(0, UTC)


def max_datetime() -> datetime:
    return datetime.fromtimestamp((1 << 31) - 1, UTC)


def timestamp_to_datetime(ts: int | None) -> datetime | None:
    return datetime.fromtimestamp(ts) if ts else None


def datetime_to_timestamp(dt: datetime | None) -> int | None:
    return int(dt.timestamp()) if dt else None


def get_first_url(text: str) -> str | None:
    text = re.sub(r"^\s*(<[\w<>=\s\"]*>)\s*", r"\1", text)
    text = re.sub(r"\s*(</[\w</>]*>)\s*$", r"\1", text)

    matches = re.findall(
        r"(https?):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])",
        text,
    )

    return f"{matches[0][0]}://{matches[0][1]}{matches[0][2]}" if matches else None
