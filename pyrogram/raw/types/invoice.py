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
    Vector,
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class Invoice(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Invoice`.

    Details:
        - Layer: ``181``
        - ID: ``5DB95A15``

    Parameters:
        currency (``str``):
            N/A

        prices (List of :obj:`LabeledPrice <pyrogram.raw.base.LabeledPrice>`):
            N/A

        test (``bool``, *optional*):
            N/A

        name_requested (``bool``, *optional*):
            N/A

        phone_requested (``bool``, *optional*):
            N/A

        email_requested (``bool``, *optional*):
            N/A

        shipping_address_requested (``bool``, *optional*):
            N/A

        flexible (``bool``, *optional*):
            N/A

        phone_to_provider (``bool``, *optional*):
            N/A

        email_to_provider (``bool``, *optional*):
            N/A

        recurring (``bool``, *optional*):
            N/A

        max_tip_amount (``int`` ``64-bit``, *optional*):
            N/A

        suggested_tip_amounts (List of ``int`` ``64-bit``, *optional*):
            N/A

        terms_url (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = [
        "currency",
        "email_requested",
        "email_to_provider",
        "flexible",
        "max_tip_amount",
        "name_requested",
        "phone_requested",
        "phone_to_provider",
        "prices",
        "recurring",
        "shipping_address_requested",
        "suggested_tip_amounts",
        "terms_url",
        "test",
    ]

    ID = 0x5DB95A15
    QUALNAME = "types.Invoice"

    def __init__(
        self,
        *,
        currency: str,
        prices: list["raw.base.LabeledPrice"],
        test: bool | None = None,
        name_requested: bool | None = None,
        phone_requested: bool | None = None,
        email_requested: bool | None = None,
        shipping_address_requested: bool | None = None,
        flexible: bool | None = None,
        phone_to_provider: bool | None = None,
        email_to_provider: bool | None = None,
        recurring: bool | None = None,
        max_tip_amount: int | None = None,
        suggested_tip_amounts: list[int] | None = None,
        terms_url: str | None = None,
    ) -> None:
        self.currency = currency  # string
        self.prices = prices  # Vector<LabeledPrice>
        self.test = test  # flags.0?true
        self.name_requested = name_requested  # flags.1?true
        self.phone_requested = phone_requested  # flags.2?true
        self.email_requested = email_requested  # flags.3?true
        self.shipping_address_requested = shipping_address_requested  # flags.4?true
        self.flexible = flexible  # flags.5?true
        self.phone_to_provider = phone_to_provider  # flags.6?true
        self.email_to_provider = email_to_provider  # flags.7?true
        self.recurring = recurring  # flags.9?true
        self.max_tip_amount = max_tip_amount  # flags.8?long
        self.suggested_tip_amounts = suggested_tip_amounts  # flags.8?Vector<long>
        self.terms_url = terms_url  # flags.10?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Invoice":
        flags = Int.read(b)

        test = bool(flags & 1 << 0)
        name_requested = bool(flags & 1 << 1)
        phone_requested = bool(flags & 1 << 2)
        email_requested = bool(flags & 1 << 3)
        shipping_address_requested = bool(flags & 1 << 4)
        flexible = bool(flags & 1 << 5)
        phone_to_provider = bool(flags & 1 << 6)
        email_to_provider = bool(flags & 1 << 7)
        recurring = bool(flags & 1 << 9)
        currency = String.read(b)

        prices = TLObject.read(b)

        max_tip_amount = Long.read(b) if flags & (1 << 8) else None
        suggested_tip_amounts = TLObject.read(b, Long) if flags & (1 << 8) else []

        terms_url = String.read(b) if flags & (1 << 10) else None
        return Invoice(
            currency=currency,
            prices=prices,
            test=test,
            name_requested=name_requested,
            phone_requested=phone_requested,
            email_requested=email_requested,
            shipping_address_requested=shipping_address_requested,
            flexible=flexible,
            phone_to_provider=phone_to_provider,
            email_to_provider=email_to_provider,
            recurring=recurring,
            max_tip_amount=max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts,
            terms_url=terms_url,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.test else 0
        flags |= (1 << 1) if self.name_requested else 0
        flags |= (1 << 2) if self.phone_requested else 0
        flags |= (1 << 3) if self.email_requested else 0
        flags |= (1 << 4) if self.shipping_address_requested else 0
        flags |= (1 << 5) if self.flexible else 0
        flags |= (1 << 6) if self.phone_to_provider else 0
        flags |= (1 << 7) if self.email_to_provider else 0
        flags |= (1 << 9) if self.recurring else 0
        flags |= (1 << 8) if self.max_tip_amount is not None else 0
        flags |= (1 << 8) if self.suggested_tip_amounts else 0
        flags |= (1 << 10) if self.terms_url is not None else 0
        b.write(Int(flags))

        b.write(String(self.currency))

        b.write(Vector(self.prices))

        if self.max_tip_amount is not None:
            b.write(Long(self.max_tip_amount))

        if self.suggested_tip_amounts is not None:
            b.write(Vector(self.suggested_tip_amounts, Long))

        if self.terms_url is not None:
            b.write(String(self.terms_url))

        return b.getvalue()
