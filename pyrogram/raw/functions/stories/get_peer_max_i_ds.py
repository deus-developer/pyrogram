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
    Vector,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class GetPeerMaxIDs(TLFunction[list[int]]):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``535983C3``

    Parameters:
        id (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: list[str] = ["id"]

    ID = 0x535983C3
    QUALNAME = "functions.stories.GetPeerMaxIDs"

    def __init__(self, *, id: list["raw.base.InputPeer"]) -> None:
        self.id = id  # Vector<InputPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerMaxIDs":
        # No flags

        id = TLObject.read(b)

        return GetPeerMaxIDs(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.id))

        return b.getvalue()
