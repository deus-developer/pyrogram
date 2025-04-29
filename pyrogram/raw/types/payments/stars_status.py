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
    String,
    Vector,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class StarsStatus(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarsStatus`.

    Details:
        - Layer: ``181``
        - ID: ``8CF4EE60``

    Parameters:
        balance (``int`` ``64-bit``):
            N/A

        history (List of :obj:`StarsTransaction <pyrogram.raw.base.StarsTransaction>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarsStatus
            payments.GetStarsTransactions
    """

    __slots__: list[str] = ["balance", "chats", "history", "next_offset", "users"]

    ID = 0x8CF4EE60
    QUALNAME = "types.payments.StarsStatus"

    def __init__(
        self,
        *,
        balance: int,
        history: list["raw.base.StarsTransaction"],
        chats: list["raw.base.Chat"],
        users: list["raw.base.User"],
        next_offset: str | None = None,
    ) -> None:
        self.balance = balance  # long
        self.history = history  # Vector<StarsTransaction>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsStatus":
        flags = Int.read(b)

        balance = Long.read(b)

        history = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        chats = TLObject.read(b)

        users = TLObject.read(b)

        return StarsStatus(
            balance=balance,
            history=history,
            chats=chats,
            users=users,
            next_offset=next_offset,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        b.write(Long(self.balance))

        b.write(Vector(self.history))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
