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
from pyrogram.raw.core import TLObject
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


class CheckedGiftCode(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.CheckedGiftCode`.

    Details:
        - Layer: ``181``
        - ID: ``284A1096``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        months (``int`` ``32-bit``):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        via_giveaway (``bool``, *optional*):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        giveaway_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        to_id (``int`` ``64-bit``, *optional*):
            N/A

        used_date (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.CheckGiftCode
    """

    __slots__: list[str] = [
        "chats",
        "date",
        "from_id",
        "giveaway_msg_id",
        "months",
        "to_id",
        "used_date",
        "users",
        "via_giveaway",
    ]

    ID = 0x284A1096
    QUALNAME = "types.payments.CheckedGiftCode"

    def __init__(
        self,
        *,
        date: int,
        months: int,
        chats: list["raw.base.Chat"],
        users: list["raw.base.User"],
        via_giveaway: bool | None = None,
        from_id: "raw.base.Peer" = None,
        giveaway_msg_id: int | None = None,
        to_id: int | None = None,
        used_date: int | None = None,
    ) -> None:
        self.date = date  # int
        self.months = months  # int
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.via_giveaway = via_giveaway  # flags.2?true
        self.from_id = from_id  # flags.4?Peer
        self.giveaway_msg_id = giveaway_msg_id  # flags.3?int
        self.to_id = to_id  # flags.0?long
        self.used_date = used_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckedGiftCode":
        flags = Int.read(b)

        via_giveaway = bool(flags & 1 << 2)
        from_id = TLObject.read(b) if flags & (1 << 4) else None

        giveaway_msg_id = Int.read(b) if flags & (1 << 3) else None
        to_id = Long.read(b) if flags & (1 << 0) else None
        date = Int.read(b)

        months = Int.read(b)

        used_date = Int.read(b) if flags & (1 << 1) else None
        chats = TLObject.read(b)

        users = TLObject.read(b)

        return CheckedGiftCode(
            date=date,
            months=months,
            chats=chats,
            users=users,
            via_giveaway=via_giveaway,
            from_id=from_id,
            giveaway_msg_id=giveaway_msg_id,
            to_id=to_id,
            used_date=used_date,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.via_giveaway else 0
        flags |= (1 << 4) if self.from_id is not None else 0
        flags |= (1 << 3) if self.giveaway_msg_id is not None else 0
        flags |= (1 << 0) if self.to_id is not None else 0
        flags |= (1 << 1) if self.used_date is not None else 0
        b.write(Int(flags))

        if self.from_id is not None:
            b.write(self.from_id.write())

        if self.giveaway_msg_id is not None:
            b.write(Int(self.giveaway_msg_id))

        if self.to_id is not None:
            b.write(Long(self.to_id))

        b.write(Int(self.date))

        b.write(Int(self.months))

        if self.used_date is not None:
            b.write(Int(self.used_date))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
