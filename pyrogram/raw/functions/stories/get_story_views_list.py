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


class GetStoryViewsList(TLFunction["raw.base.stories.StoryViewsList"]):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7ED23C57``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        just_contacts (``bool``, *optional*):
            N/A

        reactions_first (``bool``, *optional*):
            N/A

        forwards_first (``bool``, *optional*):
            N/A

        q (``str``, *optional*):
            N/A

    Returns:
        :obj:`stories.StoryViewsList <pyrogram.raw.base.stories.StoryViewsList>`
    """

    __slots__: list[str] = [
        "forwards_first",
        "id",
        "just_contacts",
        "limit",
        "offset",
        "peer",
        "q",
        "reactions_first",
    ]

    ID = 0x7ED23C57
    QUALNAME = "functions.stories.GetStoryViewsList"

    def __init__(
        self,
        *,
        peer: "raw.base.InputPeer",
        id: int,
        offset: str,
        limit: int,
        just_contacts: bool | None = None,
        reactions_first: bool | None = None,
        forwards_first: bool | None = None,
        q: str | None = None,
    ) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.offset = offset  # string
        self.limit = limit  # int
        self.just_contacts = just_contacts  # flags.0?true
        self.reactions_first = reactions_first  # flags.2?true
        self.forwards_first = forwards_first  # flags.3?true
        self.q = q  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryViewsList":
        flags = Int.read(b)

        just_contacts = bool(flags & 1 << 0)
        reactions_first = bool(flags & 1 << 2)
        forwards_first = bool(flags & 1 << 3)
        peer = TLObject.read(b)

        q = String.read(b) if flags & (1 << 1) else None
        id = Int.read(b)

        offset = String.read(b)

        limit = Int.read(b)

        return GetStoryViewsList(
            peer=peer,
            id=id,
            offset=offset,
            limit=limit,
            just_contacts=just_contacts,
            reactions_first=reactions_first,
            forwards_first=forwards_first,
            q=q,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.just_contacts else 0
        flags |= (1 << 2) if self.reactions_first else 0
        flags |= (1 << 3) if self.forwards_first else 0
        flags |= (1 << 1) if self.q is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.q is not None:
            b.write(String(self.q))

        b.write(Int(self.id))

        b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
