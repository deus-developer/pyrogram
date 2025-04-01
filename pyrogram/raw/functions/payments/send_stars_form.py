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
)

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class SendStarsForm(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``199``
        - ID: ``7998C914``

    Parameters:
        form_id (``int`` ``64-bit``):
            N/A

        invoice (:obj:`InputInvoice <pyrogram.raw.base.InputInvoice>`):
            N/A

    Returns:
        :obj:`payments.PaymentResult <pyrogram.raw.base.payments.PaymentResult>`
    """

    __slots__: list[str] = ["form_id", "invoice"]

    ID = 0x7998C914
    QUALNAME = "functions.payments.SendStarsForm"

    def __init__(self, *, form_id: int, invoice: "raw.base.InputInvoice") -> None:
        self.form_id = form_id  # long
        self.invoice = invoice  # InputInvoice

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendStarsForm":
        # No flags

        form_id = Long.read(b)

        invoice = TLObject.read(b)

        return SendStarsForm(form_id=form_id, invoice=invoice)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.form_id))

        b.write(self.invoice.write())

        return b.getvalue()
