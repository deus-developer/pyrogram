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


class Channel(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Chat`.

    Details:
        - Layer: ``199``
        - ID: ``E00998B7``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        title (``str``):
            N/A

        photo (:obj:`ChatPhoto <pyrogram.raw.base.ChatPhoto>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        creator (``bool``, *optional*):
            N/A

        left (``bool``, *optional*):
            N/A

        broadcast (``bool``, *optional*):
            N/A

        verified (``bool``, *optional*):
            N/A

        megagroup (``bool``, *optional*):
            N/A

        restricted (``bool``, *optional*):
            N/A

        signatures (``bool``, *optional*):
            N/A

        min (``bool``, *optional*):
            N/A

        scam (``bool``, *optional*):
            N/A

        has_link (``bool``, *optional*):
            N/A

        has_geo (``bool``, *optional*):
            N/A

        slowmode_enabled (``bool``, *optional*):
            N/A

        call_active (``bool``, *optional*):
            N/A

        call_not_empty (``bool``, *optional*):
            N/A

        fake (``bool``, *optional*):
            N/A

        gigagroup (``bool``, *optional*):
            N/A

        noforwards (``bool``, *optional*):
            N/A

        join_to_send (``bool``, *optional*):
            N/A

        join_request (``bool``, *optional*):
            N/A

        forum (``bool``, *optional*):
            N/A

        stories_hidden (``bool``, *optional*):
            N/A

        stories_hidden_min (``bool``, *optional*):
            N/A

        stories_unavailable (``bool``, *optional*):
            N/A

        signature_profiles (``bool``, *optional*):
            N/A

        access_hash (``int`` ``64-bit``, *optional*):
            N/A

        username (``str``, *optional*):
            N/A

        restriction_reason (List of :obj:`RestrictionReason <pyrogram.raw.base.RestrictionReason>`, *optional*):
            N/A

        admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            N/A

        banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`, *optional*):
            N/A

        default_banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`, *optional*):
            N/A

        participants_count (``int`` ``32-bit``, *optional*):
            N/A

        usernames (List of :obj:`Username <pyrogram.raw.base.Username>`, *optional*):
            N/A

        stories_max_id (``int`` ``32-bit``, *optional*):
            N/A

        color (:obj:`PeerColor <pyrogram.raw.base.PeerColor>`, *optional*):
            N/A

        profile_color (:obj:`PeerColor <pyrogram.raw.base.PeerColor>`, *optional*):
            N/A

        emoji_status (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`, *optional*):
            N/A

        level (``int`` ``32-bit``, *optional*):
            N/A

        subscription_until_date (``int`` ``32-bit``, *optional*):
            N/A

        bot_verification_icon (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = [
        "access_hash",
        "admin_rights",
        "banned_rights",
        "bot_verification_icon",
        "broadcast",
        "call_active",
        "call_not_empty",
        "color",
        "creator",
        "date",
        "default_banned_rights",
        "emoji_status",
        "fake",
        "forum",
        "gigagroup",
        "has_geo",
        "has_link",
        "id",
        "join_request",
        "join_to_send",
        "left",
        "level",
        "megagroup",
        "min",
        "noforwards",
        "participants_count",
        "photo",
        "profile_color",
        "restricted",
        "restriction_reason",
        "scam",
        "signature_profiles",
        "signatures",
        "slowmode_enabled",
        "stories_hidden",
        "stories_hidden_min",
        "stories_max_id",
        "stories_unavailable",
        "subscription_until_date",
        "title",
        "username",
        "usernames",
        "verified",
    ]

    ID = 0xE00998B7
    QUALNAME = "types.Channel"

    def __init__(
        self,
        *,
        id: int,
        title: str,
        photo: "raw.base.ChatPhoto",
        date: int,
        creator: bool | None = None,
        left: bool | None = None,
        broadcast: bool | None = None,
        verified: bool | None = None,
        megagroup: bool | None = None,
        restricted: bool | None = None,
        signatures: bool | None = None,
        min: bool | None = None,
        scam: bool | None = None,
        has_link: bool | None = None,
        has_geo: bool | None = None,
        slowmode_enabled: bool | None = None,
        call_active: bool | None = None,
        call_not_empty: bool | None = None,
        fake: bool | None = None,
        gigagroup: bool | None = None,
        noforwards: bool | None = None,
        join_to_send: bool | None = None,
        join_request: bool | None = None,
        forum: bool | None = None,
        stories_hidden: bool | None = None,
        stories_hidden_min: bool | None = None,
        stories_unavailable: bool | None = None,
        signature_profiles: bool | None = None,
        access_hash: int | None = None,
        username: str | None = None,
        restriction_reason: list["raw.base.RestrictionReason"] | None = None,
        admin_rights: "raw.base.ChatAdminRights" = None,
        banned_rights: "raw.base.ChatBannedRights" = None,
        default_banned_rights: "raw.base.ChatBannedRights" = None,
        participants_count: int | None = None,
        usernames: list["raw.base.Username"] | None = None,
        stories_max_id: int | None = None,
        color: "raw.base.PeerColor" = None,
        profile_color: "raw.base.PeerColor" = None,
        emoji_status: "raw.base.EmojiStatus" = None,
        level: int | None = None,
        subscription_until_date: int | None = None,
        bot_verification_icon: int | None = None,
    ) -> None:
        self.id = id  # long
        self.title = title  # string
        self.photo = photo  # ChatPhoto
        self.date = date  # int
        self.creator = creator  # flags.0?true
        self.left = left  # flags.2?true
        self.broadcast = broadcast  # flags.5?true
        self.verified = verified  # flags.7?true
        self.megagroup = megagroup  # flags.8?true
        self.restricted = restricted  # flags.9?true
        self.signatures = signatures  # flags.11?true
        self.min = min  # flags.12?true
        self.scam = scam  # flags.19?true
        self.has_link = has_link  # flags.20?true
        self.has_geo = has_geo  # flags.21?true
        self.slowmode_enabled = slowmode_enabled  # flags.22?true
        self.call_active = call_active  # flags.23?true
        self.call_not_empty = call_not_empty  # flags.24?true
        self.fake = fake  # flags.25?true
        self.gigagroup = gigagroup  # flags.26?true
        self.noforwards = noforwards  # flags.27?true
        self.join_to_send = join_to_send  # flags.28?true
        self.join_request = join_request  # flags.29?true
        self.forum = forum  # flags.30?true
        self.stories_hidden = stories_hidden  # flags2.1?true
        self.stories_hidden_min = stories_hidden_min  # flags2.2?true
        self.stories_unavailable = stories_unavailable  # flags2.3?true
        self.signature_profiles = signature_profiles  # flags2.12?true
        self.access_hash = access_hash  # flags.13?long
        self.username = username  # flags.6?string
        self.restriction_reason = (
            restriction_reason  # flags.9?Vector<RestrictionReason>
        )
        self.admin_rights = admin_rights  # flags.14?ChatAdminRights
        self.banned_rights = banned_rights  # flags.15?ChatBannedRights
        self.default_banned_rights = default_banned_rights  # flags.18?ChatBannedRights
        self.participants_count = participants_count  # flags.17?int
        self.usernames = usernames  # flags2.0?Vector<Username>
        self.stories_max_id = stories_max_id  # flags2.4?int
        self.color = color  # flags2.7?PeerColor
        self.profile_color = profile_color  # flags2.8?PeerColor
        self.emoji_status = emoji_status  # flags2.9?EmojiStatus
        self.level = level  # flags2.10?int
        self.subscription_until_date = subscription_until_date  # flags2.11?int
        self.bot_verification_icon = bot_verification_icon  # flags2.13?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Channel":
        flags = Int.read(b)

        creator = True if flags & (1 << 0) else False
        left = True if flags & (1 << 2) else False
        broadcast = True if flags & (1 << 5) else False
        verified = True if flags & (1 << 7) else False
        megagroup = True if flags & (1 << 8) else False
        restricted = True if flags & (1 << 9) else False
        signatures = True if flags & (1 << 11) else False
        min = True if flags & (1 << 12) else False
        scam = True if flags & (1 << 19) else False
        has_link = True if flags & (1 << 20) else False
        has_geo = True if flags & (1 << 21) else False
        slowmode_enabled = True if flags & (1 << 22) else False
        call_active = True if flags & (1 << 23) else False
        call_not_empty = True if flags & (1 << 24) else False
        fake = True if flags & (1 << 25) else False
        gigagroup = True if flags & (1 << 26) else False
        noforwards = True if flags & (1 << 27) else False
        join_to_send = True if flags & (1 << 28) else False
        join_request = True if flags & (1 << 29) else False
        forum = True if flags & (1 << 30) else False
        flags2 = Int.read(b)

        stories_hidden = True if flags2 & (1 << 1) else False
        stories_hidden_min = True if flags2 & (1 << 2) else False
        stories_unavailable = True if flags2 & (1 << 3) else False
        signature_profiles = True if flags2 & (1 << 12) else False
        id = Long.read(b)

        access_hash = Long.read(b) if flags & (1 << 13) else None
        title = String.read(b)

        username = String.read(b) if flags & (1 << 6) else None
        photo = TLObject.read(b)

        date = Int.read(b)

        restriction_reason = TLObject.read(b) if flags & (1 << 9) else []

        admin_rights = TLObject.read(b) if flags & (1 << 14) else None

        banned_rights = TLObject.read(b) if flags & (1 << 15) else None

        default_banned_rights = TLObject.read(b) if flags & (1 << 18) else None

        participants_count = Int.read(b) if flags & (1 << 17) else None
        usernames = TLObject.read(b) if flags2 & (1 << 0) else []

        stories_max_id = Int.read(b) if flags2 & (1 << 4) else None
        color = TLObject.read(b) if flags2 & (1 << 7) else None

        profile_color = TLObject.read(b) if flags2 & (1 << 8) else None

        emoji_status = TLObject.read(b) if flags2 & (1 << 9) else None

        level = Int.read(b) if flags2 & (1 << 10) else None
        subscription_until_date = Int.read(b) if flags2 & (1 << 11) else None
        bot_verification_icon = Long.read(b) if flags2 & (1 << 13) else None
        return Channel(
            id=id,
            title=title,
            photo=photo,
            date=date,
            creator=creator,
            left=left,
            broadcast=broadcast,
            verified=verified,
            megagroup=megagroup,
            restricted=restricted,
            signatures=signatures,
            min=min,
            scam=scam,
            has_link=has_link,
            has_geo=has_geo,
            slowmode_enabled=slowmode_enabled,
            call_active=call_active,
            call_not_empty=call_not_empty,
            fake=fake,
            gigagroup=gigagroup,
            noforwards=noforwards,
            join_to_send=join_to_send,
            join_request=join_request,
            forum=forum,
            stories_hidden=stories_hidden,
            stories_hidden_min=stories_hidden_min,
            stories_unavailable=stories_unavailable,
            signature_profiles=signature_profiles,
            access_hash=access_hash,
            username=username,
            restriction_reason=restriction_reason,
            admin_rights=admin_rights,
            banned_rights=banned_rights,
            default_banned_rights=default_banned_rights,
            participants_count=participants_count,
            usernames=usernames,
            stories_max_id=stories_max_id,
            color=color,
            profile_color=profile_color,
            emoji_status=emoji_status,
            level=level,
            subscription_until_date=subscription_until_date,
            bot_verification_icon=bot_verification_icon,
        )

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 2) if self.left else 0
        flags |= (1 << 5) if self.broadcast else 0
        flags |= (1 << 7) if self.verified else 0
        flags |= (1 << 8) if self.megagroup else 0
        flags |= (1 << 9) if self.restricted else 0
        flags |= (1 << 11) if self.signatures else 0
        flags |= (1 << 12) if self.min else 0
        flags |= (1 << 19) if self.scam else 0
        flags |= (1 << 20) if self.has_link else 0
        flags |= (1 << 21) if self.has_geo else 0
        flags |= (1 << 22) if self.slowmode_enabled else 0
        flags |= (1 << 23) if self.call_active else 0
        flags |= (1 << 24) if self.call_not_empty else 0
        flags |= (1 << 25) if self.fake else 0
        flags |= (1 << 26) if self.gigagroup else 0
        flags |= (1 << 27) if self.noforwards else 0
        flags |= (1 << 28) if self.join_to_send else 0
        flags |= (1 << 29) if self.join_request else 0
        flags |= (1 << 30) if self.forum else 0
        flags |= (1 << 13) if self.access_hash is not None else 0
        flags |= (1 << 6) if self.username is not None else 0
        flags |= (1 << 9) if self.restriction_reason else 0
        flags |= (1 << 14) if self.admin_rights is not None else 0
        flags |= (1 << 15) if self.banned_rights is not None else 0
        flags |= (1 << 18) if self.default_banned_rights is not None else 0
        flags |= (1 << 17) if self.participants_count is not None else 0
        b.write(Int(flags))
        flags2 = 0
        flags2 |= (1 << 1) if self.stories_hidden else 0
        flags2 |= (1 << 2) if self.stories_hidden_min else 0
        flags2 |= (1 << 3) if self.stories_unavailable else 0
        flags2 |= (1 << 12) if self.signature_profiles else 0
        flags2 |= (1 << 0) if self.usernames else 0
        flags2 |= (1 << 4) if self.stories_max_id is not None else 0
        flags2 |= (1 << 7) if self.color is not None else 0
        flags2 |= (1 << 8) if self.profile_color is not None else 0
        flags2 |= (1 << 9) if self.emoji_status is not None else 0
        flags2 |= (1 << 10) if self.level is not None else 0
        flags2 |= (1 << 11) if self.subscription_until_date is not None else 0
        flags2 |= (1 << 13) if self.bot_verification_icon is not None else 0
        b.write(Int(flags2))

        b.write(Long(self.id))

        if self.access_hash is not None:
            b.write(Long(self.access_hash))

        b.write(String(self.title))

        if self.username is not None:
            b.write(String(self.username))

        b.write(self.photo.write())

        b.write(Int(self.date))

        if self.restriction_reason is not None:
            b.write(Vector(self.restriction_reason))

        if self.admin_rights is not None:
            b.write(self.admin_rights.write())

        if self.banned_rights is not None:
            b.write(self.banned_rights.write())

        if self.default_banned_rights is not None:
            b.write(self.default_banned_rights.write())

        if self.participants_count is not None:
            b.write(Int(self.participants_count))

        if self.usernames is not None:
            b.write(Vector(self.usernames))

        if self.stories_max_id is not None:
            b.write(Int(self.stories_max_id))

        if self.color is not None:
            b.write(self.color.write())

        if self.profile_color is not None:
            b.write(self.profile_color.write())

        if self.emoji_status is not None:
            b.write(self.emoji_status.write())

        if self.level is not None:
            b.write(Int(self.level))

        if self.subscription_until_date is not None:
            b.write(Int(self.subscription_until_date))

        if self.bot_verification_icon is not None:
            b.write(Long(self.bot_verification_icon))

        return b.getvalue()
