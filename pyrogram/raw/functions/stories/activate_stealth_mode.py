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

from pyrogram.raw.core import TLFunction
from pyrogram.raw.core.primitives import (
    Int,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ActivateStealthMode(TLFunction["raw.base.Updates"]):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``57BBD166``

    Parameters:
        past (``bool``, *optional*):
            N/A

        future (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: list[str] = ["future", "past"]

    ID = 0x57BBD166
    QUALNAME = "functions.stories.ActivateStealthMode"

    def __init__(
        self,
        *,
        past: bool | None = None,
        future: bool | None = None,
    ) -> None:
        self.past = past  # flags.0?true
        self.future = future  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ActivateStealthMode":
        flags = Int.read(b)

        past = bool(flags & 1 << 0)
        future = bool(flags & 1 << 1)
        return ActivateStealthMode(past=past, future=future)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.past else 0
        flags |= (1 << 1) if self.future else 0
        b.write(Int(flags))

        return b.getvalue()
