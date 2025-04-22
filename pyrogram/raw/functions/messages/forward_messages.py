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

from pyrogram import raw
from pyrogram.raw.core import TLFunction, TLObject
from pyrogram.raw.core.primitives import (
    Int,
    Long,
    Vector,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ForwardMessages(TLFunction["raw.base.Updates"]):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D5039208``

    Parameters:
        from_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (List of ``int`` ``32-bit``):
            N/A

        random_id (List of ``int`` ``64-bit``):
            N/A

        to_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        silent (``bool``, *optional*):
            N/A

        background (``bool``, *optional*):
            N/A

        with_my_score (``bool``, *optional*):
            N/A

        drop_author (``bool``, *optional*):
            N/A

        drop_media_captions (``bool``, *optional*):
            N/A

        noforwards (``bool``, *optional*):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        quick_reply_shortcut (:obj:`InputQuickReplyShortcut <pyrogram.raw.base.InputQuickReplyShortcut>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: list[str] = [
        "background",
        "drop_author",
        "drop_media_captions",
        "from_peer",
        "id",
        "noforwards",
        "quick_reply_shortcut",
        "random_id",
        "schedule_date",
        "send_as",
        "silent",
        "to_peer",
        "top_msg_id",
        "with_my_score",
    ]

    ID = 0xD5039208
    QUALNAME = "functions.messages.ForwardMessages"

    def __init__(
        self,
        *,
        from_peer: "raw.base.InputPeer",
        id: list[int],
        random_id: list[int],
        to_peer: "raw.base.InputPeer",
        silent: bool | None = None,
        background: bool | None = None,
        with_my_score: bool | None = None,
        drop_author: bool | None = None,
        drop_media_captions: bool | None = None,
        noforwards: bool | None = None,
        top_msg_id: int | None = None,
        schedule_date: int | None = None,
        send_as: "raw.base.InputPeer" = None,
        quick_reply_shortcut: "raw.base.InputQuickReplyShortcut" = None,
    ) -> None:
        self.from_peer = from_peer  # InputPeer
        self.id = id  # Vector<int>
        self.random_id = random_id  # Vector<long>
        self.to_peer = to_peer  # InputPeer
        self.silent = silent  # flags.5?true
        self.background = background  # flags.6?true
        self.with_my_score = with_my_score  # flags.8?true
        self.drop_author = drop_author  # flags.11?true
        self.drop_media_captions = drop_media_captions  # flags.12?true
        self.noforwards = noforwards  # flags.14?true
        self.top_msg_id = top_msg_id  # flags.9?int
        self.schedule_date = schedule_date  # flags.10?int
        self.send_as = send_as  # flags.13?InputPeer
        self.quick_reply_shortcut = (
            quick_reply_shortcut  # flags.17?InputQuickReplyShortcut
        )

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForwardMessages":
        flags = Int.read(b)

        silent = bool(flags & 1 << 5)
        background = bool(flags & 1 << 6)
        with_my_score = bool(flags & 1 << 8)
        drop_author = bool(flags & 1 << 11)
        drop_media_captions = bool(flags & 1 << 12)
        noforwards = bool(flags & 1 << 14)
        from_peer = TLObject.read(b)

        id = TLObject.read(b, Int)

        random_id = TLObject.read(b, Long)

        to_peer = TLObject.read(b)

        top_msg_id = Int.read(b) if flags & (1 << 9) else None
        schedule_date = Int.read(b) if flags & (1 << 10) else None
        send_as = TLObject.read(b) if flags & (1 << 13) else None

        quick_reply_shortcut = TLObject.read(b) if flags & (1 << 17) else None

        return ForwardMessages(
            from_peer=from_peer,
            id=id,
            random_id=random_id,
            to_peer=to_peer,
            silent=silent,
            background=background,
            with_my_score=with_my_score,
            drop_author=drop_author,
            drop_media_captions=drop_media_captions,
            noforwards=noforwards,
            top_msg_id=top_msg_id,
            schedule_date=schedule_date,
            send_as=send_as,
            quick_reply_shortcut=quick_reply_shortcut,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 8) if self.with_my_score else 0
        flags |= (1 << 11) if self.drop_author else 0
        flags |= (1 << 12) if self.drop_media_captions else 0
        flags |= (1 << 14) if self.noforwards else 0
        flags |= (1 << 9) if self.top_msg_id is not None else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        flags |= (1 << 17) if self.quick_reply_shortcut is not None else 0
        b.write(Int(flags))

        b.write(self.from_peer.write())

        b.write(Vector(self.id, Int))

        b.write(Vector(self.random_id, Long))

        b.write(self.to_peer.write())

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))

        if self.send_as is not None:
            b.write(self.send_as.write())

        if self.quick_reply_shortcut is not None:
            b.write(self.quick_reply_shortcut.write())

        return b.getvalue()
