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


class StoryViewPublicForward(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StoryView`.

    Details:
        - Layer: ``181``
        - ID: ``9083670B``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        blocked (``bool``, *optional*):
            N/A

        blocked_my_stories_from (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["blocked", "blocked_my_stories_from", "message"]

    ID = 0x9083670B
    QUALNAME = "types.StoryViewPublicForward"

    def __init__(
        self,
        *,
        message: "raw.base.Message",
        blocked: bool | None = None,
        blocked_my_stories_from: bool | None = None,
    ) -> None:
        self.message = message  # Message
        self.blocked = blocked  # flags.0?true
        self.blocked_my_stories_from = blocked_my_stories_from  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViewPublicForward":
        flags = Int.read(b)

        blocked = bool(flags & 1 << 0)
        blocked_my_stories_from = bool(flags & 1 << 1)
        message = TLObject.read(b)

        return StoryViewPublicForward(
            message=message,
            blocked=blocked,
            blocked_my_stories_from=blocked_my_stories_from,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 1) if self.blocked_my_stories_from else 0
        b.write(Int(flags))

        b.write(self.message.write())

        return b.getvalue()
