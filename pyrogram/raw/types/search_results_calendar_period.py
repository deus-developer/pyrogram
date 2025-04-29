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


class SearchResultsCalendarPeriod(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SearchResultsCalendarPeriod`.

    Details:
        - Layer: ``181``
        - ID: ``C9B0539F``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        min_msg_id (``int`` ``32-bit``):
            N/A

        max_msg_id (``int`` ``32-bit``):
            N/A

        count (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["count", "date", "max_msg_id", "min_msg_id"]

    ID = 0xC9B0539F
    QUALNAME = "types.SearchResultsCalendarPeriod"

    def __init__(
        self,
        *,
        date: int,
        min_msg_id: int,
        max_msg_id: int,
        count: int,
    ) -> None:
        self.date = date  # int
        self.min_msg_id = min_msg_id  # int
        self.max_msg_id = max_msg_id  # int
        self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultsCalendarPeriod":
        # No flags

        date = Int.read(b)

        min_msg_id = Int.read(b)

        max_msg_id = Int.read(b)

        count = Int.read(b)

        return SearchResultsCalendarPeriod(
            date=date,
            min_msg_id=min_msg_id,
            max_msg_id=max_msg_id,
            count=count,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.date))

        b.write(Int(self.min_msg_id))

        b.write(Int(self.max_msg_id))

        b.write(Int(self.count))

        return b.getvalue()
