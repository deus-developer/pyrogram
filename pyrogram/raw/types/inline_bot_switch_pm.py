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


class InlineBotSwitchPM(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InlineBotSwitchPM`.

    Details:
        - Layer: ``199``
        - ID: ``3C20629F``

    Parameters:
        text (``str``):
            N/A

        start_param (``str``):
            N/A

    """

    __slots__: list[str] = ["start_param", "text"]

    ID = 0x3C20629F
    QUALNAME = "types.InlineBotSwitchPM"

    def __init__(self, *, text: str, start_param: str) -> None:
        self.text = text  # string
        self.start_param = start_param  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InlineBotSwitchPM":
        # No flags

        text = String.read(b)

        start_param = String.read(b)

        return InlineBotSwitchPM(text=text, start_param=start_param)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.text))

        b.write(String(self.start_param))

        return b.getvalue()
