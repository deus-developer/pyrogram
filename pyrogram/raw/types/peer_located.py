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


class PeerLocated(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PeerLocated`.

    Details:
        - Layer: ``199``
        - ID: ``CA461B5D``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        expires (``int`` ``32-bit``):
            N/A

        distance (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["distance", "expires", "peer"]

    ID = 0xCA461B5D
    QUALNAME = "types.PeerLocated"

    def __init__(self, *, peer: "raw.base.Peer", expires: int, distance: int) -> None:
        self.peer = peer  # Peer
        self.expires = expires  # int
        self.distance = distance  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerLocated":
        # No flags

        peer = TLObject.read(b)

        expires = Int.read(b)

        distance = Int.read(b)

        return PeerLocated(peer=peer, expires=expires, distance=distance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.expires))

        b.write(Int(self.distance))

        return b.getvalue()
