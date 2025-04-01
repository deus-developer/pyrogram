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
    String,
    Vector,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class DeepLinkInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.DeepLinkInfo`.

    Details:
        - Layer: ``199``
        - ID: ``6A4EE832``

    Parameters:
        message (``str``):
            N/A

        update_app (``bool``, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetDeepLinkInfo
    """

    __slots__: list[str] = ["entities", "message", "update_app"]

    ID = 0x6A4EE832
    QUALNAME = "types.help.DeepLinkInfo"

    def __init__(
        self,
        *,
        message: str,
        update_app: bool | None = None,
        entities: list["raw.base.MessageEntity"] | None = None,
    ) -> None:
        self.message = message  # string
        self.update_app = update_app  # flags.0?true
        self.entities = entities  # flags.1?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeepLinkInfo":
        flags = Int.read(b)

        update_app = True if flags & (1 << 0) else False
        message = String.read(b)

        entities = TLObject.read(b) if flags & (1 << 1) else []

        return DeepLinkInfo(message=message, update_app=update_app, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.update_app else 0
        flags |= (1 << 1) if self.entities else 0
        b.write(Int(flags))

        b.write(String(self.message))

        if self.entities is not None:
            b.write(Vector(self.entities))

        return b.getvalue()
