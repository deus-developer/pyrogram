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
    String,
    Vector,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class GroupCall(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.phone.GroupCall`.

    Details:
        - Layer: ``199``
        - ID: ``9E727AAD``

    Parameters:
        call (:obj:`GroupCall <pyrogram.raw.base.GroupCall>`):
            N/A

        participants (List of :obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`):
            N/A

        participants_next_offset (``str``):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCall
    """

    __slots__: list[str] = [
        "call",
        "chats",
        "participants",
        "participants_next_offset",
        "users",
    ]

    ID = 0x9E727AAD
    QUALNAME = "types.phone.GroupCall"

    def __init__(
        self,
        *,
        call: "raw.base.GroupCall",
        participants: list["raw.base.GroupCallParticipant"],
        participants_next_offset: str,
        chats: list["raw.base.Chat"],
        users: list["raw.base.User"],
    ) -> None:
        self.call = call  # GroupCall
        self.participants = participants  # Vector<GroupCallParticipant>
        self.participants_next_offset = participants_next_offset  # string
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCall":
        # No flags

        call = TLObject.read(b)

        participants = TLObject.read(b)

        participants_next_offset = String.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return GroupCall(
            call=call,
            participants=participants,
            participants_next_offset=participants_next_offset,
            chats=chats,
            users=users,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(Vector(self.participants))

        b.write(String(self.participants_next_offset))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
