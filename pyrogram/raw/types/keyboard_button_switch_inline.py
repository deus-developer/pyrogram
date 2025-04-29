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


class KeyboardButtonSwitchInline(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``181``
        - ID: ``93B9FBB5``

    Parameters:
        text (``str``):
            N/A

        query (``str``):
            N/A

        same_peer (``bool``, *optional*):
            N/A

        peer_types (List of :obj:`InlineQueryPeerType <pyrogram.raw.base.InlineQueryPeerType>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["peer_types", "query", "same_peer", "text"]

    ID = 0x93B9FBB5
    QUALNAME = "types.KeyboardButtonSwitchInline"

    def __init__(
        self,
        *,
        text: str,
        query: str,
        same_peer: bool | None = None,
        peer_types: list["raw.base.InlineQueryPeerType"] | None = None,
    ) -> None:
        self.text = text  # string
        self.query = query  # string
        self.same_peer = same_peer  # flags.0?true
        self.peer_types = peer_types  # flags.1?Vector<InlineQueryPeerType>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonSwitchInline":
        flags = Int.read(b)

        same_peer = True if flags & (1 << 0) else False
        text = String.read(b)

        query = String.read(b)

        peer_types = TLObject.read(b) if flags & (1 << 1) else []

        return KeyboardButtonSwitchInline(
            text=text,
            query=query,
            same_peer=same_peer,
            peer_types=peer_types,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.same_peer else 0
        flags |= (1 << 1) if self.peer_types else 0
        b.write(Int(flags))

        b.write(String(self.text))

        b.write(String(self.query))

        if self.peer_types is not None:
            b.write(Vector(self.peer_types))

        return b.getvalue()
