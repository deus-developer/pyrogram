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


class PeerSettings(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PeerSettings`.

    Details:
        - Layer: ``181``
        - ID: ``ACD66C5E``

    Parameters:
        report_spam (``bool``, *optional*):
            N/A

        add_contact (``bool``, *optional*):
            N/A

        block_contact (``bool``, *optional*):
            N/A

        share_contact (``bool``, *optional*):
            N/A

        need_contacts_exception (``bool``, *optional*):
            N/A

        report_geo (``bool``, *optional*):
            N/A

        autoarchived (``bool``, *optional*):
            N/A

        invite_members (``bool``, *optional*):
            N/A

        request_chat_broadcast (``bool``, *optional*):
            N/A

        business_bot_paused (``bool``, *optional*):
            N/A

        business_bot_can_reply (``bool``, *optional*):
            N/A

        geo_distance (``int`` ``32-bit``, *optional*):
            N/A

        request_chat_title (``str``, *optional*):
            N/A

        request_chat_date (``int`` ``32-bit``, *optional*):
            N/A

        business_bot_id (``int`` ``64-bit``, *optional*):
            N/A

        business_bot_manage_url (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = [
        "add_contact",
        "autoarchived",
        "block_contact",
        "business_bot_can_reply",
        "business_bot_id",
        "business_bot_manage_url",
        "business_bot_paused",
        "geo_distance",
        "invite_members",
        "need_contacts_exception",
        "report_geo",
        "report_spam",
        "request_chat_broadcast",
        "request_chat_date",
        "request_chat_title",
        "share_contact",
    ]

    ID = 0xACD66C5E
    QUALNAME = "types.PeerSettings"

    def __init__(
        self,
        *,
        report_spam: bool | None = None,
        add_contact: bool | None = None,
        block_contact: bool | None = None,
        share_contact: bool | None = None,
        need_contacts_exception: bool | None = None,
        report_geo: bool | None = None,
        autoarchived: bool | None = None,
        invite_members: bool | None = None,
        request_chat_broadcast: bool | None = None,
        business_bot_paused: bool | None = None,
        business_bot_can_reply: bool | None = None,
        geo_distance: int | None = None,
        request_chat_title: str | None = None,
        request_chat_date: int | None = None,
        business_bot_id: int | None = None,
        business_bot_manage_url: str | None = None,
    ) -> None:
        self.report_spam = report_spam  # flags.0?true
        self.add_contact = add_contact  # flags.1?true
        self.block_contact = block_contact  # flags.2?true
        self.share_contact = share_contact  # flags.3?true
        self.need_contacts_exception = need_contacts_exception  # flags.4?true
        self.report_geo = report_geo  # flags.5?true
        self.autoarchived = autoarchived  # flags.7?true
        self.invite_members = invite_members  # flags.8?true
        self.request_chat_broadcast = request_chat_broadcast  # flags.10?true
        self.business_bot_paused = business_bot_paused  # flags.11?true
        self.business_bot_can_reply = business_bot_can_reply  # flags.12?true
        self.geo_distance = geo_distance  # flags.6?int
        self.request_chat_title = request_chat_title  # flags.9?string
        self.request_chat_date = request_chat_date  # flags.9?int
        self.business_bot_id = business_bot_id  # flags.13?long
        self.business_bot_manage_url = business_bot_manage_url  # flags.13?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerSettings":
        flags = Int.read(b)

        report_spam = bool(flags & 1 << 0)
        add_contact = bool(flags & 1 << 1)
        block_contact = bool(flags & 1 << 2)
        share_contact = bool(flags & 1 << 3)
        need_contacts_exception = bool(flags & 1 << 4)
        report_geo = bool(flags & 1 << 5)
        autoarchived = bool(flags & 1 << 7)
        invite_members = bool(flags & 1 << 8)
        request_chat_broadcast = bool(flags & 1 << 10)
        business_bot_paused = bool(flags & 1 << 11)
        business_bot_can_reply = bool(flags & 1 << 12)
        geo_distance = Int.read(b) if flags & (1 << 6) else None
        request_chat_title = String.read(b) if flags & (1 << 9) else None
        request_chat_date = Int.read(b) if flags & (1 << 9) else None
        business_bot_id = Long.read(b) if flags & (1 << 13) else None
        business_bot_manage_url = String.read(b) if flags & (1 << 13) else None
        return PeerSettings(
            report_spam=report_spam,
            add_contact=add_contact,
            block_contact=block_contact,
            share_contact=share_contact,
            need_contacts_exception=need_contacts_exception,
            report_geo=report_geo,
            autoarchived=autoarchived,
            invite_members=invite_members,
            request_chat_broadcast=request_chat_broadcast,
            business_bot_paused=business_bot_paused,
            business_bot_can_reply=business_bot_can_reply,
            geo_distance=geo_distance,
            request_chat_title=request_chat_title,
            request_chat_date=request_chat_date,
            business_bot_id=business_bot_id,
            business_bot_manage_url=business_bot_manage_url,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.report_spam else 0
        flags |= (1 << 1) if self.add_contact else 0
        flags |= (1 << 2) if self.block_contact else 0
        flags |= (1 << 3) if self.share_contact else 0
        flags |= (1 << 4) if self.need_contacts_exception else 0
        flags |= (1 << 5) if self.report_geo else 0
        flags |= (1 << 7) if self.autoarchived else 0
        flags |= (1 << 8) if self.invite_members else 0
        flags |= (1 << 10) if self.request_chat_broadcast else 0
        flags |= (1 << 11) if self.business_bot_paused else 0
        flags |= (1 << 12) if self.business_bot_can_reply else 0
        flags |= (1 << 6) if self.geo_distance is not None else 0
        flags |= (1 << 9) if self.request_chat_title is not None else 0
        flags |= (1 << 9) if self.request_chat_date is not None else 0
        flags |= (1 << 13) if self.business_bot_id is not None else 0
        flags |= (1 << 13) if self.business_bot_manage_url is not None else 0
        b.write(Int(flags))

        if self.geo_distance is not None:
            b.write(Int(self.geo_distance))

        if self.request_chat_title is not None:
            b.write(String(self.request_chat_title))

        if self.request_chat_date is not None:
            b.write(Int(self.request_chat_date))

        if self.business_bot_id is not None:
            b.write(Long(self.business_bot_id))

        if self.business_bot_manage_url is not None:
            b.write(String(self.business_bot_manage_url))

        return b.getvalue()
