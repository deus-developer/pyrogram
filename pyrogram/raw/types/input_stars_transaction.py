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
    String,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class InputStarsTransaction(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStarsTransaction`.

    Details:
        - Layer: ``199``
        - ID: ``206AE6D1``

    Parameters:
        id (``str``):
            N/A

        refund (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "refund"]

    ID = 0x206AE6D1
    QUALNAME = "types.InputStarsTransaction"

    def __init__(self, *, id: str, refund: bool | None = None) -> None:
        self.id = id  # string
        self.refund = refund  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStarsTransaction":
        flags = Int.read(b)

        refund = True if flags & (1 << 0) else False
        id = String.read(b)

        return InputStarsTransaction(id=id, refund=refund)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.refund else 0
        b.write(Int(flags))

        b.write(String(self.id))

        return b.getvalue()
