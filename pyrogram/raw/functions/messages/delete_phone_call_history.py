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


class DeletePhoneCallHistory(TLFunction["raw.base.messages.AffectedFoundMessages"]):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F9CBE409``

    Parameters:
        revoke (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.AffectedFoundMessages <pyrogram.raw.base.messages.AffectedFoundMessages>`
    """

    __slots__: list[str] = ["revoke"]

    ID = 0xF9CBE409
    QUALNAME = "functions.messages.DeletePhoneCallHistory"

    def __init__(self, *, revoke: bool | None = None) -> None:
        self.revoke = revoke  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePhoneCallHistory":
        flags = Int.read(b)

        revoke = bool(flags & 1 << 0)
        return DeletePhoneCallHistory(revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke else 0
        b.write(Int(flags))

        return b.getvalue()
