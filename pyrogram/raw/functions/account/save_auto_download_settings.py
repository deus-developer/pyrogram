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
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class SaveAutoDownloadSettings(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``199``
        - ID: ``76F36233``

    Parameters:
        settings (:obj:`AutoDownloadSettings <pyrogram.raw.base.AutoDownloadSettings>`):
            N/A

        low (``bool``, *optional*):
            N/A

        high (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["high", "low", "settings"]

    ID = 0x76F36233
    QUALNAME = "functions.account.SaveAutoDownloadSettings"

    def __init__(
        self,
        *,
        settings: "raw.base.AutoDownloadSettings",
        low: bool | None = None,
        high: bool | None = None,
    ) -> None:
        self.settings = settings  # AutoDownloadSettings
        self.low = low  # flags.0?true
        self.high = high  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveAutoDownloadSettings":
        flags = Int.read(b)

        low = True if flags & (1 << 0) else False
        high = True if flags & (1 << 1) else False
        settings = TLObject.read(b)

        return SaveAutoDownloadSettings(settings=settings, low=low, high=high)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.low else 0
        flags |= (1 << 1) if self.high else 0
        b.write(Int(flags))

        b.write(self.settings.write())

        return b.getvalue()
