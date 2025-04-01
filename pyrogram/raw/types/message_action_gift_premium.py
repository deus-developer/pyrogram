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
    Long,
    String,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageActionGiftPremium(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``199``
        - ID: ``6C6274FA``

    Parameters:
        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        months (``int`` ``32-bit``):
            N/A

        crypto_currency (``str``, *optional*):
            N/A

        crypto_amount (``int`` ``64-bit``, *optional*):
            N/A

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: list[str] = [
        "amount",
        "crypto_amount",
        "crypto_currency",
        "currency",
        "message",
        "months",
    ]

    ID = 0x6C6274FA
    QUALNAME = "types.MessageActionGiftPremium"

    def __init__(
        self,
        *,
        currency: str,
        amount: int,
        months: int,
        crypto_currency: str | None = None,
        crypto_amount: int | None = None,
        message: "raw.base.TextWithEntities" = None,
    ) -> None:
        self.currency = currency  # string
        self.amount = amount  # long
        self.months = months  # int
        self.crypto_currency = crypto_currency  # flags.0?string
        self.crypto_amount = crypto_amount  # flags.0?long
        self.message = message  # flags.1?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiftPremium":
        flags = Int.read(b)

        currency = String.read(b)

        amount = Long.read(b)

        months = Int.read(b)

        crypto_currency = String.read(b) if flags & (1 << 0) else None
        crypto_amount = Long.read(b) if flags & (1 << 0) else None
        message = TLObject.read(b) if flags & (1 << 1) else None

        return MessageActionGiftPremium(
            currency=currency,
            amount=amount,
            months=months,
            crypto_currency=crypto_currency,
            crypto_amount=crypto_amount,
            message=message,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.crypto_currency is not None else 0
        flags |= (1 << 0) if self.crypto_amount is not None else 0
        flags |= (1 << 1) if self.message is not None else 0
        b.write(Int(flags))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        b.write(Int(self.months))

        if self.crypto_currency is not None:
            b.write(String(self.crypto_currency))

        if self.crypto_amount is not None:
            b.write(Long(self.crypto_amount))

        if self.message is not None:
            b.write(self.message.write())

        return b.getvalue()
