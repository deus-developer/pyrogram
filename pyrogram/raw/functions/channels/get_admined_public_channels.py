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


class GetAdminedPublicChannels(TLFunction["raw.base.messages.Chats"]):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F8B036AF``

    Parameters:
        by_location (``bool``, *optional*):
            N/A

        check_limit (``bool``, *optional*):
            N/A

        for_personal (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: list[str] = ["by_location", "check_limit", "for_personal"]

    ID = 0xF8B036AF
    QUALNAME = "functions.channels.GetAdminedPublicChannels"

    def __init__(
        self,
        *,
        by_location: bool | None = None,
        check_limit: bool | None = None,
        for_personal: bool | None = None,
    ) -> None:
        self.by_location = by_location  # flags.0?true
        self.check_limit = check_limit  # flags.1?true
        self.for_personal = for_personal  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAdminedPublicChannels":
        flags = Int.read(b)

        by_location = bool(flags & 1 << 0)
        check_limit = bool(flags & 1 << 1)
        for_personal = bool(flags & 1 << 2)
        return GetAdminedPublicChannels(
            by_location=by_location,
            check_limit=check_limit,
            for_personal=for_personal,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.by_location else 0
        flags |= (1 << 1) if self.check_limit else 0
        flags |= (1 << 2) if self.for_personal else 0
        b.write(Int(flags))

        return b.getvalue()
