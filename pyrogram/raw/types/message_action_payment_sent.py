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
    Long,
    String,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageActionPaymentSent(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``96163F56``

    Parameters:
        currency (``str``):
            N/A

        total_amount (``int`` ``64-bit``):
            N/A

        recurring_init (``bool``, *optional*):
            N/A

        recurring_used (``bool``, *optional*):
            N/A

        invoice_slug (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = [
        "currency",
        "invoice_slug",
        "recurring_init",
        "recurring_used",
        "total_amount",
    ]

    ID = 0x96163F56
    QUALNAME = "types.MessageActionPaymentSent"

    def __init__(
        self,
        *,
        currency: str,
        total_amount: int,
        recurring_init: bool | None = None,
        recurring_used: bool | None = None,
        invoice_slug: str | None = None,
    ) -> None:
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.recurring_init = recurring_init  # flags.2?true
        self.recurring_used = recurring_used  # flags.3?true
        self.invoice_slug = invoice_slug  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPaymentSent":
        flags = Int.read(b)

        recurring_init = bool(flags & 1 << 2)
        recurring_used = bool(flags & 1 << 3)
        currency = String.read(b)

        total_amount = Long.read(b)

        invoice_slug = String.read(b) if flags & (1 << 0) else None
        return MessageActionPaymentSent(
            currency=currency,
            total_amount=total_amount,
            recurring_init=recurring_init,
            recurring_used=recurring_used,
            invoice_slug=invoice_slug,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.recurring_init else 0
        flags |= (1 << 3) if self.recurring_used else 0
        flags |= (1 << 0) if self.invoice_slug is not None else 0
        b.write(Int(flags))

        b.write(String(self.currency))

        b.write(Long(self.total_amount))

        if self.invoice_slug is not None:
            b.write(String(self.invoice_slug))

        return b.getvalue()
