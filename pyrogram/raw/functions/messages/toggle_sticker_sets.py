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


class ToggleStickerSets(TLFunction[bool]):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B5052FEA``

    Parameters:
        stickersets (List of :obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        uninstall (``bool``, *optional*):
            N/A

        archive (``bool``, *optional*):
            N/A

        unarchive (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["archive", "stickersets", "unarchive", "uninstall"]

    ID = 0xB5052FEA
    QUALNAME = "functions.messages.ToggleStickerSets"

    def __init__(
        self,
        *,
        stickersets: list["raw.base.InputStickerSet"],
        uninstall: bool | None = None,
        archive: bool | None = None,
        unarchive: bool | None = None,
    ) -> None:
        self.stickersets = stickersets  # Vector<InputStickerSet>
        self.uninstall = uninstall  # flags.0?true
        self.archive = archive  # flags.1?true
        self.unarchive = unarchive  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleStickerSets":
        flags = Int.read(b)

        uninstall = bool(flags & 1 << 0)
        archive = bool(flags & 1 << 1)
        unarchive = bool(flags & 1 << 2)
        stickersets = TLObject.read(b)

        return ToggleStickerSets(
            stickersets=stickersets,
            uninstall=uninstall,
            archive=archive,
            unarchive=unarchive,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.uninstall else 0
        flags |= (1 << 1) if self.archive else 0
        flags |= (1 << 2) if self.unarchive else 0
        b.write(Int(flags))

        b.write(Vector(self.stickersets))

        return b.getvalue()
