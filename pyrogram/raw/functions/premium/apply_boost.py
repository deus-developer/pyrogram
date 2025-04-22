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


class ApplyBoost(TLFunction["raw.base.premium.MyBoosts"]):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``6B7DA746``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        slots (List of ``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`premium.MyBoosts <pyrogram.raw.base.premium.MyBoosts>`
    """

    __slots__: list[str] = ["peer", "slots"]

    ID = 0x6B7DA746
    QUALNAME = "functions.premium.ApplyBoost"

    def __init__(
        self,
        *,
        peer: "raw.base.InputPeer",
        slots: list[int] | None = None,
    ) -> None:
        self.peer = peer  # InputPeer
        self.slots = slots  # flags.0?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ApplyBoost":
        flags = Int.read(b)

        slots = TLObject.read(b, Int) if flags & (1 << 0) else []

        peer = TLObject.read(b)

        return ApplyBoost(peer=peer, slots=slots)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.slots else 0
        b.write(Int(flags))

        if self.slots is not None:
            b.write(Vector(self.slots, Int))

        b.write(self.peer.write())

        return b.getvalue()
