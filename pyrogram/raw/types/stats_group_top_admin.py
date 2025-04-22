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
    Long,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class StatsGroupTopAdmin(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StatsGroupTopAdmin`.

    Details:
        - Layer: ``181``
        - ID: ``D7584C87``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        deleted (``int`` ``32-bit``):
            N/A

        kicked (``int`` ``32-bit``):
            N/A

        banned (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["banned", "deleted", "kicked", "user_id"]

    ID = 0xD7584C87
    QUALNAME = "types.StatsGroupTopAdmin"

    def __init__(self, *, user_id: int, deleted: int, kicked: int, banned: int) -> None:
        self.user_id = user_id  # long
        self.deleted = deleted  # int
        self.kicked = kicked  # int
        self.banned = banned  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGroupTopAdmin":
        # No flags

        user_id = Long.read(b)

        deleted = Int.read(b)

        kicked = Int.read(b)

        banned = Int.read(b)

        return StatsGroupTopAdmin(
            user_id=user_id,
            deleted=deleted,
            kicked=kicked,
            banned=banned,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        b.write(Int(self.deleted))

        b.write(Int(self.kicked))

        b.write(Int(self.banned))

        return b.getvalue()
