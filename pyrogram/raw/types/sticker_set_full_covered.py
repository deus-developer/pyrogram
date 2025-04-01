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
    Vector,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class StickerSetFullCovered(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StickerSetCovered`.

    Details:
        - Layer: ``199``
        - ID: ``40D13C0E``

    Parameters:
        set (:obj:`StickerSet <pyrogram.raw.base.StickerSet>`):
            N/A

        packs (List of :obj:`StickerPack <pyrogram.raw.base.StickerPack>`):
            N/A

        keywords (List of :obj:`StickerKeyword <pyrogram.raw.base.StickerKeyword>`):
            N/A

        documents (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachedStickers
    """

    __slots__: list[str] = ["documents", "keywords", "packs", "set"]

    ID = 0x40D13C0E
    QUALNAME = "types.StickerSetFullCovered"

    def __init__(
        self,
        *,
        set: "raw.base.StickerSet",
        packs: list["raw.base.StickerPack"],
        keywords: list["raw.base.StickerKeyword"],
        documents: list["raw.base.Document"],
    ) -> None:
        self.set = set  # StickerSet
        self.packs = packs  # Vector<StickerPack>
        self.keywords = keywords  # Vector<StickerKeyword>
        self.documents = documents  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSetFullCovered":
        # No flags

        set = TLObject.read(b)

        packs = TLObject.read(b)

        keywords = TLObject.read(b)

        documents = TLObject.read(b)

        return StickerSetFullCovered(
            set=set, packs=packs, keywords=keywords, documents=documents,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.set.write())

        b.write(Vector(self.packs))

        b.write(Vector(self.keywords))

        b.write(Vector(self.documents))

        return b.getvalue()
