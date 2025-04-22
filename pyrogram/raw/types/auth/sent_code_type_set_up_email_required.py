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
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class SentCodeTypeSetUpEmailRequired(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``A5491DEA``

    Parameters:
        apple_signin_allowed (``bool``, *optional*):
            N/A

        google_signin_allowed (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["apple_signin_allowed", "google_signin_allowed"]

    ID = 0xA5491DEA
    QUALNAME = "types.auth.SentCodeTypeSetUpEmailRequired"

    def __init__(
        self,
        *,
        apple_signin_allowed: bool | None = None,
        google_signin_allowed: bool | None = None,
    ) -> None:
        self.apple_signin_allowed = apple_signin_allowed  # flags.0?true
        self.google_signin_allowed = google_signin_allowed  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeSetUpEmailRequired":
        flags = Int.read(b)

        apple_signin_allowed = bool(flags & 1 << 0)
        google_signin_allowed = bool(flags & 1 << 1)
        return SentCodeTypeSetUpEmailRequired(
            apple_signin_allowed=apple_signin_allowed,
            google_signin_allowed=google_signin_allowed,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.apple_signin_allowed else 0
        flags |= (1 << 1) if self.google_signin_allowed else 0
        b.write(Int(flags))

        return b.getvalue()
