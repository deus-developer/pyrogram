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


class ReplyKeyboardForceReply(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``181``
        - ID: ``86B40B08``

    Parameters:
        single_use (``bool``, *optional*):
            N/A

        selective (``bool``, *optional*):
            N/A

        placeholder (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["placeholder", "selective", "single_use"]

    ID = 0x86B40B08
    QUALNAME = "types.ReplyKeyboardForceReply"

    def __init__(
        self,
        *,
        single_use: bool | None = None,
        selective: bool | None = None,
        placeholder: str | None = None,
    ) -> None:
        self.single_use = single_use  # flags.1?true
        self.selective = selective  # flags.2?true
        self.placeholder = placeholder  # flags.3?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyKeyboardForceReply":
        flags = Int.read(b)

        single_use = bool(flags & 1 << 1)
        selective = bool(flags & 1 << 2)
        placeholder = String.read(b) if flags & (1 << 3) else None
        return ReplyKeyboardForceReply(
            single_use=single_use,
            selective=selective,
            placeholder=placeholder,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.single_use else 0
        flags |= (1 << 2) if self.selective else 0
        flags |= (1 << 3) if self.placeholder is not None else 0
        b.write(Int(flags))

        if self.placeholder is not None:
            b.write(String(self.placeholder))

        return b.getvalue()
