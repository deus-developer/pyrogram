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

from io import BytesIO
from typing import Any

from pyrogram.raw.core import TLObject
from pyrogram.raw.core.primitives import (
    Int,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ChatBannedRights(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatBannedRights`.

    Details:
        - Layer: ``181``
        - ID: ``9F120418``

    Parameters:
        until_date (``int`` ``32-bit``):
            N/A

        view_messages (``bool``, *optional*):
            N/A

        send_messages (``bool``, *optional*):
            N/A

        send_media (``bool``, *optional*):
            N/A

        send_stickers (``bool``, *optional*):
            N/A

        send_gifs (``bool``, *optional*):
            N/A

        send_games (``bool``, *optional*):
            N/A

        send_inline (``bool``, *optional*):
            N/A

        embed_links (``bool``, *optional*):
            N/A

        send_polls (``bool``, *optional*):
            N/A

        change_info (``bool``, *optional*):
            N/A

        invite_users (``bool``, *optional*):
            N/A

        pin_messages (``bool``, *optional*):
            N/A

        manage_topics (``bool``, *optional*):
            N/A

        send_photos (``bool``, *optional*):
            N/A

        send_videos (``bool``, *optional*):
            N/A

        send_roundvideos (``bool``, *optional*):
            N/A

        send_audios (``bool``, *optional*):
            N/A

        send_voices (``bool``, *optional*):
            N/A

        send_docs (``bool``, *optional*):
            N/A

        send_plain (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = [
        "change_info",
        "embed_links",
        "invite_users",
        "manage_topics",
        "pin_messages",
        "send_audios",
        "send_docs",
        "send_games",
        "send_gifs",
        "send_inline",
        "send_media",
        "send_messages",
        "send_photos",
        "send_plain",
        "send_polls",
        "send_roundvideos",
        "send_stickers",
        "send_videos",
        "send_voices",
        "until_date",
        "view_messages",
    ]

    ID = 0x9F120418
    QUALNAME = "types.ChatBannedRights"

    def __init__(
        self,
        *,
        until_date: int,
        view_messages: bool | None = None,
        send_messages: bool | None = None,
        send_media: bool | None = None,
        send_stickers: bool | None = None,
        send_gifs: bool | None = None,
        send_games: bool | None = None,
        send_inline: bool | None = None,
        embed_links: bool | None = None,
        send_polls: bool | None = None,
        change_info: bool | None = None,
        invite_users: bool | None = None,
        pin_messages: bool | None = None,
        manage_topics: bool | None = None,
        send_photos: bool | None = None,
        send_videos: bool | None = None,
        send_roundvideos: bool | None = None,
        send_audios: bool | None = None,
        send_voices: bool | None = None,
        send_docs: bool | None = None,
        send_plain: bool | None = None,
    ) -> None:
        self.until_date = until_date  # int
        self.view_messages = view_messages  # flags.0?true
        self.send_messages = send_messages  # flags.1?true
        self.send_media = send_media  # flags.2?true
        self.send_stickers = send_stickers  # flags.3?true
        self.send_gifs = send_gifs  # flags.4?true
        self.send_games = send_games  # flags.5?true
        self.send_inline = send_inline  # flags.6?true
        self.embed_links = embed_links  # flags.7?true
        self.send_polls = send_polls  # flags.8?true
        self.change_info = change_info  # flags.10?true
        self.invite_users = invite_users  # flags.15?true
        self.pin_messages = pin_messages  # flags.17?true
        self.manage_topics = manage_topics  # flags.18?true
        self.send_photos = send_photos  # flags.19?true
        self.send_videos = send_videos  # flags.20?true
        self.send_roundvideos = send_roundvideos  # flags.21?true
        self.send_audios = send_audios  # flags.22?true
        self.send_voices = send_voices  # flags.23?true
        self.send_docs = send_docs  # flags.24?true
        self.send_plain = send_plain  # flags.25?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatBannedRights":
        flags = Int.read(b)

        view_messages = bool(flags & 1 << 0)
        send_messages = bool(flags & 1 << 1)
        send_media = bool(flags & 1 << 2)
        send_stickers = bool(flags & 1 << 3)
        send_gifs = bool(flags & 1 << 4)
        send_games = bool(flags & 1 << 5)
        send_inline = bool(flags & 1 << 6)
        embed_links = bool(flags & 1 << 7)
        send_polls = bool(flags & 1 << 8)
        change_info = bool(flags & 1 << 10)
        invite_users = bool(flags & 1 << 15)
        pin_messages = bool(flags & 1 << 17)
        manage_topics = bool(flags & 1 << 18)
        send_photos = bool(flags & 1 << 19)
        send_videos = bool(flags & 1 << 20)
        send_roundvideos = bool(flags & 1 << 21)
        send_audios = bool(flags & 1 << 22)
        send_voices = bool(flags & 1 << 23)
        send_docs = bool(flags & 1 << 24)
        send_plain = bool(flags & 1 << 25)
        until_date = Int.read(b)

        return ChatBannedRights(
            until_date=until_date,
            view_messages=view_messages,
            send_messages=send_messages,
            send_media=send_media,
            send_stickers=send_stickers,
            send_gifs=send_gifs,
            send_games=send_games,
            send_inline=send_inline,
            embed_links=embed_links,
            send_polls=send_polls,
            change_info=change_info,
            invite_users=invite_users,
            pin_messages=pin_messages,
            manage_topics=manage_topics,
            send_photos=send_photos,
            send_videos=send_videos,
            send_roundvideos=send_roundvideos,
            send_audios=send_audios,
            send_voices=send_voices,
            send_docs=send_docs,
            send_plain=send_plain,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.view_messages else 0
        flags |= (1 << 1) if self.send_messages else 0
        flags |= (1 << 2) if self.send_media else 0
        flags |= (1 << 3) if self.send_stickers else 0
        flags |= (1 << 4) if self.send_gifs else 0
        flags |= (1 << 5) if self.send_games else 0
        flags |= (1 << 6) if self.send_inline else 0
        flags |= (1 << 7) if self.embed_links else 0
        flags |= (1 << 8) if self.send_polls else 0
        flags |= (1 << 10) if self.change_info else 0
        flags |= (1 << 15) if self.invite_users else 0
        flags |= (1 << 17) if self.pin_messages else 0
        flags |= (1 << 18) if self.manage_topics else 0
        flags |= (1 << 19) if self.send_photos else 0
        flags |= (1 << 20) if self.send_videos else 0
        flags |= (1 << 21) if self.send_roundvideos else 0
        flags |= (1 << 22) if self.send_audios else 0
        flags |= (1 << 23) if self.send_voices else 0
        flags |= (1 << 24) if self.send_docs else 0
        flags |= (1 << 25) if self.send_plain else 0
        b.write(Int(flags))

        b.write(Int(self.until_date))

        return b.getvalue()
