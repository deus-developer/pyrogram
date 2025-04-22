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
    String,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class DeleteAccount(TLFunction[bool]):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A2C0CF74``

    Parameters:
        reason (``str``):
            N/A

        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["password", "reason"]

    ID = 0xA2C0CF74
    QUALNAME = "functions.account.DeleteAccount"

    def __init__(
        self,
        *,
        reason: str,
        password: "raw.base.InputCheckPasswordSRP" = None,
    ) -> None:
        self.reason = reason  # string
        self.password = password  # flags.0?InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteAccount":
        flags = Int.read(b)

        reason = String.read(b)

        password = TLObject.read(b) if flags & (1 << 0) else None

        return DeleteAccount(reason=reason, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.password is not None else 0
        b.write(Int(flags))

        b.write(String(self.reason))

        if self.password is not None:
            b.write(self.password.write())

        return b.getvalue()
