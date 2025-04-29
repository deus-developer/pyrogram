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
    Bytes,
    Int,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ReportSponsoredMessage(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``AF8FF6B9``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        random_id (``bytes``):
            N/A

        option (``bytes``):
            N/A

    Returns:
        :obj:`channels.SponsoredMessageReportResult <pyrogram.raw.base.channels.SponsoredMessageReportResult>`
    """

    __slots__: list[str] = ["channel", "option", "random_id"]

    ID = 0xAF8FF6B9
    QUALNAME = "functions.channels.ReportSponsoredMessage"

    def __init__(
        self,
        *,
        channel: "raw.base.InputChannel",
        random_id: bytes,
        option: bytes,
    ) -> None:
        self.channel = channel  # InputChannel
        self.random_id = random_id  # bytes
        self.option = option  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportSponsoredMessage":
        # No flags

        channel = TLObject.read(b)

        random_id = Bytes.read(b)

        option = Bytes.read(b)

        return ReportSponsoredMessage(
            channel=channel,
            random_id=random_id,
            option=option,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Bytes(self.random_id))

        b.write(Bytes(self.option))

        return b.getvalue()
