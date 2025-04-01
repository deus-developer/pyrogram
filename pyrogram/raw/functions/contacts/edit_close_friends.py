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
    Vector,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class EditCloseFriends(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``199``
        - ID: ``BA6705F0``

    Parameters:
        id (List of ``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["id"]

    ID = 0xBA6705F0
    QUALNAME = "functions.contacts.EditCloseFriends"

    def __init__(self, *, id: list[int]) -> None:
        self.id = id  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditCloseFriends":
        # No flags

        id = TLObject.read(b, Long)

        return EditCloseFriends(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.id, Long))

        return b.getvalue()
