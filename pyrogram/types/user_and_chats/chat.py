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

from collections.abc import AsyncGenerator
from datetime import datetime
from typing import (
    BinaryIO,
    Optional,
    Union,
    assert_never,
)

import pyrogram
from pyrogram import enums, raw, types, utils

from ...utils import get_channel_id
from ..object import Object


class Chat(Object):
    """A chat.

    Parameters:
        id (``int``):
            Unique identifier for this chat.

        type (:obj:`~pyrogram.enums.ChatType`):
            Type of chat.

        is_forum (``bool``, *optional*):
            True, if the supergroup chat is a forum.

        is_verified (``bool``, *optional*):
            True, if this chat has been verified by Telegram. Supergroups, channels and bots only.

        is_members_hidden (``bool``, *optional*):
            True, if the chat members are hidden.

        is_restricted (``bool``, *optional*):
            True, if this chat has been restricted. Supergroups, channels and bots only.
            See *restriction_reason* for details.

        is_creator (``bool``, *optional*):
            True, if this chat owner is the current user. Supergroups, channels and groups only.

        is_admin (``bool``, *optional*):
            True, if the current user is admin. Supergroups, channels and groups only.

        is_scam (``bool``, *optional*):
            True, if this chat has been flagged for scam.

        is_fake (``bool``, *optional*):
            True, if this chat has been flagged for impersonation.

        is_deactivated (``bool``, *optional*):
            True, if this chat has been flagged for deactivated.

        is_support (``bool``, *optional*):
            True, if this chat is part of the Telegram support team. Users and bots only.

        is_stories_hidden (``bool``, *optional*):
            True, if this chat has hidden stories.

        is_stories_unavailable (``bool``, *optional*):
            True, if this chat stories is unavailable.

        is_business_bot (``bool``, *optional*):
            True, if this bot can connect to business account.

        title (``str``, *optional*):
            Title, for supergroups, channels and basic group chats.

        username (``str``, *optional*):
            Username, for private chats, bots, supergroups and channels if available.

        usernames (List of :obj:`~pyrogram.types.Username`, *optional*):
            The list of chat's collectible (and basic) usernames if available.

        first_name (``str``, *optional*):
            First name of the other party in a private chat, for private chats and bots.

        last_name (``str``, *optional*):
            Last name of the other party in a private chat, for private chats.

        full_name (``str``, *property*):
            Full name of the other party in a private chat, for private chats and bots.

        photo (:obj:`~pyrogram.types.ChatPhoto`, *optional*):
            Chat photo. Suitable for downloads only.

        stories (List of :obj:`~pyrogram.types.Story`, *optional*):
            The list of chat's stories if available.

        wallpaper (:obj:`~pyrogram.types.Document`, *optional*):
            Chat wallpaper.

        bio (``str``, *optional*):
            Bio of the other party in a private chat.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        description (``str``, *optional*):
            Description, for groups, supergroups and channel chats.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        dc_id (``int``, *optional*):
            The chat assigned DC (data center). Available only in case the chat has a photo.
            Note that this information is approximate; it is based on where Telegram stores the current chat photo.
            It is accurate only in case the owner has set the chat photo, otherwise the dc_id will be the one assigned
            to the administrator who set the current chat photo.

        folder_id (``int``, *optional*):
            The folder identifier where the chat is located.

        has_protected_content (``bool``, *optional*):
            True, if messages from the chat can't be forwarded to other chats.

        invite_link (``str``, *optional*):
            Chat invite link, for groups, supergroups and channels.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        pinned_message (:obj:`~pyrogram.types.Message`, *optional*):
            Pinned message, for groups, supergroups channels and own chat.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        sticker_set_name (``str``, *optional*):
            For supergroups, name of group sticker set.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        can_set_sticker_set (``bool``, *optional*):
            True, if the group sticker set can be changed by you.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        members_count (``int``, *optional*):
            Chat members count, for groups, supergroups and channels only.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        restrictions (List of :obj:`~pyrogram.types.Restriction`, *optional*):
            The list of reasons why this chat might be unavailable to some users.
            This field is available only in case *is_restricted* is True.

        permissions (:obj:`~pyrogram.types.ChatPermissions` *optional*):
            Default chat member permissions, for groups and supergroups.

        distance (``int``, *optional*):
            Distance in meters of this group chat from your location.
            Returned only in :meth:`~pyrogram.Client.get_nearby_chats`.

        personal_channel (:obj:`~pyrogram.types.Chat`, *optional*):
            The personal channel linked to this chat.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        personal_channel_message (:obj:`~pyrogram.types.Message`, *optional*):
            The last message in the personal channel of this chat.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        linked_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            The linked discussion group (in case of channels) or the linked channel (in case of supergroups).
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        send_as_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            The default "send_as" chat.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        available_reactions (:obj:`~pyrogram.types.ChatReactions`, *optional*):
            Available reactions in the chat.
            Returned only in :meth:`~pyrogram.Client.get_chat`.

        level (``int``, *optional*):
            Channel boosts level.

        reply_color (:obj:`~pyrogram.types.ChatColor`, *optional*):
            Chat reply color.

        profile_color (:obj:`~pyrogram.types.ChatColor`, *optional*):
            Chat profile color.

        business_info (:obj:`~pyrogram.types.BusinessInfo`, *optional*):
            Business information of a chat.

        business_intro (:obj:`~pyrogram.types.BusinessIntro`, *optional*):
            For private chats with business accounts, the intro of the business.

        birthday (:obj:`~pyrogram.types.Birthday`, *optional*):
            Information about user birthday.

        raw (:obj:`~pyrogram.raw.base.Chat` | :obj:`~pyrogram.raw.base.User` | :obj:`~pyrogram.raw.base.ChatFull` | :obj:`~pyrogram.raw.base.UserFull`, *optional*):
            The raw chat or user object, as received from the Telegram API.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        type: "enums.ChatType",
        is_forum: bool = None,
        is_verified: bool = None,
        is_members_hidden: bool = None,
        is_restricted: bool = None,
        is_creator: bool = None,
        is_admin: bool = None,
        is_scam: bool = None,
        is_fake: bool = None,
        is_deactivated: bool = None,
        is_support: bool = None,
        is_stories_hidden: bool = None,
        is_stories_unavailable: bool = None,
        is_business_bot: bool = None,
        title: str = None,
        username: str = None,
        usernames: list["types.Username"] = None,
        first_name: str = None,
        last_name: str = None,
        photo: "types.ChatPhoto" = None,
        stories: list["types.Story"] = None,
        wallpaper: "types.Document" = None,
        bio: str = None,
        description: str = None,
        dc_id: int = None,
        folder_id: int = None,
        has_protected_content: bool = None,
        invite_link: str = None,
        pinned_message=None,
        sticker_set_name: str = None,
        can_set_sticker_set: bool = None,
        members_count: int = None,
        restrictions: list["types.Restriction"] = None,
        permissions: "types.ChatPermissions" = None,
        distance: int = None,
        personal_channel: "types.Chat" = None,
        personal_channel_message: "types.Message" = None,
        linked_chat: "types.Chat" = None,
        send_as_chat: "types.Chat" = None,
        available_reactions: Optional["types.ChatReactions"] = None,
        level: int = None,
        reply_color: "types.ChatColor" = None,
        profile_color: "types.ChatColor" = None,
        business_info: "types.BusinessInfo" = None,
        business_intro: "types.BusinessIntro" = None,
        birthday: "types.Birthday" = None,
        raw: Union[
            "raw.base.Chat",
            "raw.base.User",
            "raw.base.ChatFull",
            "raw.base.UserFull",
        ] = None,
    ):
        super().__init__(client)

        self.id = id
        self.type = type
        self.is_forum = is_forum
        self.is_verified = is_verified
        self.is_members_hidden = is_members_hidden
        self.is_restricted = is_restricted
        self.is_creator = is_creator
        self.is_admin = is_admin
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_deactivated = is_deactivated
        self.is_support = is_support
        self.is_stories_hidden = is_stories_hidden
        self.is_stories_unavailable = is_stories_unavailable
        self.is_business_bot = is_business_bot
        self.title = title
        self.username = username
        self.usernames = usernames
        self.first_name = first_name
        self.last_name = last_name
        self.photo = photo
        self.stories = stories
        self.wallpaper = wallpaper
        self.bio = bio
        self.description = description
        self.dc_id = dc_id
        self.folder_id = folder_id
        self.has_protected_content = has_protected_content
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.members_count = members_count
        self.restrictions = restrictions
        self.permissions = permissions
        self.distance = distance
        self.personal_channel = personal_channel
        self.personal_channel_message = personal_channel_message
        self.linked_chat = linked_chat
        self.send_as_chat = send_as_chat
        self.available_reactions = available_reactions
        self.level = level
        self.reply_color = reply_color
        self.profile_color = profile_color
        self.business_info = business_info
        self.business_intro = business_intro
        self.birthday = birthday
        self.raw = raw

    @staticmethod
    def _parse_user_chat(
        client, user: raw.types.User | raw.types.UserEmpty | None,
    ) -> "Chat | None":
        if user is None:
            return None
        if isinstance(user, raw.types.UserEmpty):
            return Chat(
                id=user.id,
                type=enums.ChatType.PRIVATE,
                raw=user,
                client=client,
            )
        if isinstance(user, raw.types.User):
            return Chat(
                id=user.id,
                type=enums.ChatType.BOT if user.bot else enums.ChatType.PRIVATE,
                is_verified=user.verified,
                is_restricted=user.restricted,
                is_scam=user.scam,
                is_fake=user.fake,
                is_support=user.support,
                is_stories_hidden=user.stories_hidden,
                is_stories_unavailable=user.stories_unavailable,
                is_business_bot=user.bot_business,
                username=user.username
                or (user.usernames[0].username if user.usernames else None),
                usernames=types.List([types.Username._parse(r) for r in user.usernames])
                or None,
                first_name=user.first_name,
                last_name=user.last_name,
                photo=types.ChatPhoto._parse(
                    client, user.photo, user.id, user.access_hash,
                ),
                restrictions=types.List(
                    [types.Restriction._parse(r) for r in user.restriction_reason],
                )
                or None,
                dc_id=getattr(user.photo, "dc_id", None),
                reply_color=types.ChatColor._parse(user.color),
                profile_color=types.ChatColor._parse_profile_color(
                    user.profile_color,
                ),
                raw=user,
                client=client,
            )
        assert_never(user)

    @staticmethod
    def _parse_chat_chat(
        client, chat: raw.types.Chat | raw.types.ChatEmpty | raw.types.ChatForbidden,
    ) -> "Chat | None":
        if chat is None:
            return None
        if isinstance(chat, raw.types.ChatEmpty):
            return Chat(
                id=-chat.id,
                type=enums.ChatType.GROUP,
                raw=chat,
                client=client,
            )
        if isinstance(chat, raw.types.ChatForbidden):
            return Chat(
                id=-chat.id,
                type=enums.ChatType.GROUP,
                title=chat.title,
                raw=chat,
                client=client,
            )
        if isinstance(chat, raw.types.Chat):
            return Chat(
                id=-chat.id,
                type=enums.ChatType.GROUP,
                title=chat.title,
                is_creator=chat.creator,
                is_admin=True if chat.admin_rights else None,
                is_deactivated=chat.deactivated,
                usernames=None,
                photo=types.ChatPhoto._parse(
                    client,
                    chat.photo,
                    -chat.id,
                    0,
                ),
                permissions=types.ChatPermissions._parse(
                    chat.default_banned_rights,
                ),
                members_count=chat.participants_count,
                dc_id=getattr(chat.photo, "dc_id", None),
                has_protected_content=chat.noforwards,
                raw=chat,
                client=client,
            )
        assert_never(chat)

    @staticmethod
    def _parse_channel_chat(
        client, channel: raw.types.Channel | raw.types.ChannelForbidden | None,
    ) -> "Chat | None":
        if channel is None:
            return None
        if isinstance(channel, raw.types.ChannelForbidden):
            return Chat(
                id=get_channel_id(channel.id),
                type=enums.ChatType.SUPERGROUP
                if channel.megagroup
                else enums.ChatType.CHANNEL,
                title=channel.title,
                raw=channel,
                client=client,
            )
        if isinstance(channel, raw.types.Channel):
            return Chat(
                id=utils.get_channel_id(channel.id),
                type=enums.ChatType.SUPERGROUP
                if channel.megagroup
                else enums.ChatType.CHANNEL,
                is_forum=channel.forum if channel.megagroup else None,
                is_verified=channel.verified,
                is_restricted=channel.restricted,
                is_creator=channel.creator,
                is_admin=True if channel.admin_rights else None,
                is_scam=channel.scam,
                is_fake=channel.fake,
                is_stories_hidden=channel.stories_hidden,
                is_stories_unavailable=channel.stories_unavailable,
                title=channel.title,
                username=channel.username,
                usernames=types.List(
                    [types.Username._parse(r) for r in channel.usernames],
                )
                or None,
                photo=types.ChatPhoto._parse(
                    client,
                    channel.photo,
                    get_channel_id(channel.id),
                    channel.access_hash,
                ),
                restrictions=types.List(
                    [types.Restriction._parse(r) for r in channel.restriction_reason],
                )
                or None,
                permissions=types.ChatPermissions._parse(channel.default_banned_rights),
                members_count=channel.participants_count,
                dc_id=getattr(channel.photo, "dc_id", None),
                has_protected_content=channel.noforwards,
                level=channel.level,
                reply_color=types.ChatColor._parse(channel.color),
                profile_color=types.ChatColor._parse(
                    channel.profile_color,
                ),
                raw=channel,
                client=client,
            )
        assert_never(channel)

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        message: raw.types.Message | raw.types.MessageService | raw.types.MessageEmpty,
        is_chat: bool = True,
    ) -> "Chat | None":
        from_id: raw.base.Peer | None = None
        peer_id: raw.base.Peer | None = None

        if message is None:
            return None
        if isinstance(message, raw.types.MessageEmpty):
            peer_id = message.peer_id
        elif isinstance(message, raw.types.MessageService) or isinstance(
            message, raw.types.Message,
        ):
            peer_id = message.peer_id
            from_id = message.from_id
        else:
            assert_never(message)

        chat_id = (peer_id or from_id) if is_chat else (from_id or peer_id)
        entity = client.entity_cache.get_by_peer_id(peer=chat_id)
        return Chat._parse_chat(client, entity)

    @staticmethod
    def _parse_dialog(client: "pyrogram.Client", peer):
        entity = client.entity_cache.get_by_peer_id(peer=peer)
        return Chat._parse_chat(client, entity)

    @staticmethod
    async def _parse_full(
        client: "pyrogram.Client",
        chat_full: raw.types.messages.ChatFull | raw.types.users.UserFull,
    ) -> "Chat":
        if isinstance(chat_full, raw.types.users.UserFull):
            full_user: raw.types.UserFull = chat_full.full_user

            parsed_chat = Chat._parse_user_chat(
                client,
                client.entity_cache.get_by_user_id(user_id=full_user.id),
            )
            parsed_chat.bio = full_user.about
            parsed_chat.folder_id = getattr(full_user, "folder_id", None)
            parsed_chat.business_info = types.BusinessInfo._parse(
                client,
                full_user,
            )
            parsed_chat.business_intro = await types.BusinessIntro._parse(
                client,
                getattr(full_user, "business_intro", None),
            )
            parsed_chat.birthday = types.Birthday._parse(
                getattr(full_user, "birthday", None),
            )
            parsed_chat.raw = full_user

            if full_user.pinned_msg_id:
                parsed_chat.pinned_message = await client.get_messages(
                    parsed_chat.id,
                    message_ids=full_user.pinned_msg_id,
                )

            if full_user.personal_channel_id:
                parsed_chat.personal_channel = Chat._parse_channel_chat(
                    client,
                    client.entity_cache.get_by_channel_id(
                        channel_id=full_user.personal_channel_id,
                    ),
                )
                parsed_chat.personal_channel_message = await client.get_messages(
                    parsed_chat.personal_channel.id,
                    message_ids=full_user.personal_channel_message,
                )

            if full_user.stories:
                peer_stories: raw.types.PeerStories = full_user.stories
                parsed_chat.stories = (
                    types.List(
                        [
                            await types.Story._parse(client, story, peer_stories.peer)
                            for story in peer_stories.stories
                        ],
                    )
                    or None
                )

            if full_user.wallpaper and isinstance(
                full_user.wallpaper,
                raw.types.WallPaper,
            ):
                parsed_chat.wallpaper = types.Document._parse(
                    client,
                    full_user.wallpaper.document,
                    "wallpaper.jpg",
                )
        else:
            full_chat = chat_full.full_chat

            if isinstance(full_chat, raw.types.ChatFull):
                parsed_chat = Chat._parse_chat_chat(
                    client,
                    client.entity_cache.get_by_chat_id(chat_id=full_chat.id),
                )
                parsed_chat.description = full_chat.about or None

                if isinstance(full_chat.participants, raw.types.ChatParticipants):
                    parsed_chat.members_count = len(full_chat.participants.participants)
            else:
                parsed_chat = Chat._parse_channel_chat(
                    client,
                    client.entity_cache.get_by_channel_id(channel_id=full_chat.id),
                )
                parsed_chat.members_count = full_chat.participants_count
                parsed_chat.description = full_chat.about or None
                # TODO: Add StickerSet type
                parsed_chat.can_set_sticker_set = full_chat.can_set_stickers
                parsed_chat.sticker_set_name = getattr(
                    full_chat.stickerset,
                    "short_name",
                    None,
                )
                parsed_chat.is_members_hidden = full_chat.participants_hidden
                parsed_chat.folder_id = getattr(full_chat, "folder_id", None)

                linked_chat_raw = client.entity_cache.get_by_channel_id(
                    channel_id=full_chat.linked_chat_id,
                )

                if linked_chat_raw:
                    parsed_chat.linked_chat = Chat._parse_channel_chat(
                        client,
                        linked_chat_raw,
                    )

                default_send_as = full_chat.default_send_as

                if default_send_as:
                    parsed_chat.send_as_chat = Chat._parse_chat(
                        client,
                        client.entity_cache.get_by_peer_id(peer=default_send_as),
                    )

                if full_chat.stories:
                    peer_stories: raw.types.PeerStories = full_chat.stories
                    parsed_chat.stories = (
                        types.List(
                            [
                                await types.Story._parse(
                                    client,
                                    story,
                                    peer_stories.peer,
                                )
                                for story in peer_stories.stories
                            ],
                        )
                        or None
                    )

                if full_chat.wallpaper and isinstance(
                    full_chat.wallpaper,
                    raw.types.WallPaper,
                ):
                    parsed_chat.wallpaper = types.Document._parse(
                        client,
                        full_chat.wallpaper.document,
                        "wallpaper.jpg",
                    )

            if full_chat.pinned_msg_id:
                parsed_chat.pinned_message = await client.get_messages(
                    parsed_chat.id,
                    message_ids=full_chat.pinned_msg_id,
                )

            if isinstance(full_chat.exported_invite, raw.types.ChatInviteExported):
                parsed_chat.invite_link = full_chat.exported_invite.link

            parsed_chat.available_reactions = types.ChatReactions._parse(
                client,
                full_chat.available_reactions,
            )
            parsed_chat.raw = full_chat

        return parsed_chat

    @staticmethod
    def _parse_chat(
        client,
        chat: raw.base.Chat | raw.base.User | None,
    ) -> "Chat | None":
        if chat is None:
            return None
        if isinstance(
            chat, raw.types.Chat | raw.types.ChatEmpty | raw.types.ChatForbidden,
        ):
            return Chat._parse_chat_chat(client, chat)
        if isinstance(chat, raw.types.User | raw.types.UserEmpty):
            return Chat._parse_user_chat(client, chat)
        if isinstance(chat, raw.types.Channel | raw.types.ChannelForbidden):
            return Chat._parse_channel_chat(client, chat)
        assert_never(chat)

    @property
    def full_name(self) -> str | None:
        if self.title:
            return self.title

        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"

        if self.first_name:
            return self.first_name

        return None

    async def archive(self):
        """Bound method *archive* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.archive_chats(-100123456789)

        Example:
            .. code-block:: python

                await chat.archive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.archive_chats(self.id)

    async def unarchive(self):
        """Bound method *unarchive* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.unarchive_chats(-100123456789)

        Example:
            .. code-block:: python

                await chat.unarchive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.unarchive_chats(self.id)

    # TODO: Remove notes about "All Members Are Admins" for basic groups, the attribute doesn't exist anymore
    async def set_title(self, title: str) -> bool:
        """Bound method *set_title* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_title(chat_id=chat_id, title=title)

        Example:
            .. code-block:: python

                await chat.set_title("Lounge")

        Note:
            In regular groups (non-supergroups), this method will only work if the "All Members Are Admins"
            setting is off.

        Parameters:
            title (``str``):
                New chat title, 1-255 characters.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of Telegram RPC error.
            ValueError: In case a chat_id belongs to user.
        """
        return await self._client.set_chat_title(chat_id=self.id, title=title)

    async def set_description(self, description: str) -> bool:
        """Bound method *set_description* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_description(chat_id=chat_id, description=description)

        Example:
            .. code-block:: python

                await chat.set_chat_description("Don't spam!")

        Parameters:
            description (``str``):
                New chat description, 0-255 characters.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of Telegram RPC error.
            ValueError: If a chat_id doesn't belong to a supergroup or a channel.
        """
        return await self._client.set_chat_description(
            chat_id=self.id,
            description=description,
        )

    async def set_photo(
        self,
        *,
        photo: str | BinaryIO = None,
        video: str | BinaryIO = None,
        video_start_ts: float = None,
    ) -> bool:
        """Bound method *set_photo* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_photo(chat_id=chat_id, photo=photo)

        Example:
            .. code-block:: python

                # Set chat photo using a local file
                await chat.set_photo(photo="photo.jpg")

                # Set chat photo using an existing Photo file_id
                await chat.set_photo(photo=photo.file_id)


                # Set chat video using a local file
                await chat.set_photo(video="video.mp4")

                # Set chat photo using an existing Video file_id
                await chat.set_photo(video=video.file_id)

        Parameters:
            photo (``str`` | ``BinaryIO``, *optional*):
                New chat photo. You can pass a :obj:`~pyrogram.types.Photo` file_id, a file path to upload a new photo
                from your local machine or a binary file-like object with its attribute
                ".name" set for in-memory uploads.

            video (``str`` | ``BinaryIO``, *optional*):
                New chat video. You can pass a :obj:`~pyrogram.types.Video` file_id, a file path to upload a new video
                from your local machine or a binary file-like object with its attribute
                ".name" set for in-memory uploads.

            video_start_ts (``float``, *optional*):
                The timestamp in seconds of the video frame to use as photo profile preview.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
            ValueError: if a chat_id belongs to user.
        """
        return await self._client.set_chat_photo(
            chat_id=self.id,
            photo=photo,
            video=video,
            video_start_ts=video_start_ts,
        )

    async def set_ttl(self, ttl_seconds: int) -> "types.Message":
        """Bound method *set_ttl* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_ttl(chat_id=chat_id, ttl_seconds=ttl_seconds)

        Example:
            .. code-block:: python

                await chat.set_ttl(86400)

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the generated service message is returned.
        """
        return await self._client.set_chat_ttl(chat_id=self.id, ttl_seconds=ttl_seconds)

    async def ban_member(
        self,
        user_id: int | str,
        until_date: datetime = utils.zero_datetime(),
    ) -> Union["types.Message", bool]:
        """Bound method *ban_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.ban_chat_member(chat_id=chat_id, user_id=user_id)

        Example:
            .. code-block:: python

                await chat.ban_member(123456789)

        Note:
            In regular groups (non-supergroups), this method will only work if the "All Members Are Admins" setting is
            off in the target group. Otherwise members may only be removed by the group's creator or by the member
            that added them.

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unbanned.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to epoch (ban forever).

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: On success, a service message will be returned (when applicable), otherwise, in
            case a message object couldn't be returned, True is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.ban_chat_member(
            chat_id=self.id,
            user_id=user_id,
            until_date=until_date,
        )

    async def unban_member(self, user_id: int | str) -> bool:
        """Bound method *unban_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.unban_chat_member(chat_id=chat_id, user_id=user_id)

        Example:
            .. code-block:: python

                await chat.unban_member(123456789)

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.unban_chat_member(
            chat_id=self.id,
            user_id=user_id,
        )

    async def restrict_member(
        self,
        user_id: int | str,
        permissions: "types.ChatPermissions",
        until_date: datetime = utils.zero_datetime(),
    ) -> "types.Chat":
        """Bound method *unban_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.restrict_chat_member(
                chat_id=chat_id, user_id=user_id, permissions=ChatPermissions()
            )

        Example:
            .. code-block:: python

                await chat.restrict_member(user_id, ChatPermissions())

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            permissions (:obj:`~pyrogram.types.ChatPermissions`):
                New user permissions.

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unbanned.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to epoch (ban forever).

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.restrict_chat_member(
            chat_id=self.id,
            user_id=user_id,
            permissions=permissions,
            until_date=until_date,
        )

    # Set None as privileges default due to issues with partially initialized module, because at the time Chat
    # is being initialized, ChatPrivileges would be required here, but was not initialized yet.
    async def promote_member(
        self,
        user_id: int | str,
        privileges: "types.ChatPrivileges" = None,
    ) -> bool:
        """Bound method *promote_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.promote_chat_member(chat_id=chat_id, user_id=user_id)

        Example:

            .. code-block:: python

                await chat.promote_member(123456789)

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            privileges (:obj:`~pyrogram.types.ChatPrivileges`, *optional*):
                New user privileges.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.promote_chat_member(
            chat_id=self.id,
            user_id=user_id,
            privileges=privileges,
        )

    async def join(self):
        """Bound method *join* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.join_chat(123456789)

        Example:
            .. code-block:: python

                await chat.join()

        Note:
            This only works for public groups, channels that have set a username or linked chats.

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.join_chat(self.username or self.id)

    async def leave(self):
        """Bound method *leave* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.leave_chat(123456789)

        Example:
            .. code-block:: python

                await chat.leave()

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.leave_chat(self.id)

    async def export_invite_link(self):
        """Bound method *export_invite_link* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.export_chat_invite_link(123456789)

        Example:
            .. code-block:: python

                chat.export_invite_link()

        Returns:
            ``str``: On success, the exported invite link is returned.

        Raises:
            ValueError: In case the chat_id belongs to a user.
        """
        return await self._client.export_chat_invite_link(self.id)

    async def get_member(
        self,
        user_id: int | str,
    ) -> "types.ChatMember":
        """Bound method *get_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.get_chat_member(chat_id=chat_id, user_id=user_id)

        Example:
            .. code-block:: python

                await chat.get_member(user_id)

        Returns:
            :obj:`~pyrogram.types.ChatMember`: On success, a chat member is returned.
        """
        return await self._client.get_chat_member(self.id, user_id=user_id)

    def get_members(
        self,
        query: str = "",
        limit: int = 0,
        filter: "enums.ChatMembersFilter" = enums.ChatMembersFilter.SEARCH,
    ) -> AsyncGenerator["types.ChatMember", None]:
        """Bound method *get_members* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            async for member in client.get_chat_members(chat_id):
                print(member)

        Example:
            .. code-block:: python

                async for member in chat.get_members():
                    print(member)

        Parameters:
            query (``str``, *optional*):
                Query string to filter members based on their display names and usernames.
                Only applicable to supergroups and channels. Defaults to "" (empty string).
                A query string is applicable only for :obj:`~pyrogram.enums.ChatMembersFilter.SEARCH`,
                :obj:`~pyrogram.enums.ChatMembersFilter.BANNED` and :obj:`~pyrogram.enums.ChatMembersFilter.RESTRICTED`
                filters only.

            limit (``int``, *optional*):
                Limits the number of members to be retrieved.

            filter (:obj:`~pyrogram.enums.ChatMembersFilter`, *optional*):
                Filter used to select the kind of members you want to retrieve. Only applicable for supergroups
                and channels.

        Returns:
            ``Generator``: On success, a generator yielding :obj:`~pyrogram.types.ChatMember` objects is returned.
        """
        return self._client.get_chat_members(
            self.id,
            query=query,
            limit=limit,
            filter=filter,
        )

    async def add_members(
        self,
        user_ids: int | str | list[int | str],
        forward_limit: int = 100,
    ) -> bool:
        """Bound method *add_members* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.add_chat_members(chat_id, user_id)

        Example:
            .. code-block:: python

                await chat.add_members(user_id)

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self._client.add_chat_members(
            self.id,
            user_ids=user_ids,
            forward_limit=forward_limit,
        )

    async def mark_unread(
        self,
    ) -> bool:
        """Bound method *mark_unread* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.mark_unread(chat_id)

        Example:
            .. code-block:: python

                await chat.mark_unread()

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self._client.mark_chat_unread(self.id)

    async def set_protected_content(self, enabled: bool) -> bool:
        """Bound method *set_protected_content* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_protected_content(chat_id, enabled)

        Parameters:
            enabled (``bool``):
                Pass True to enable the protected content setting, False to disable.

        Example:
            .. code-block:: python

                await chat.set_protected_content(enabled)

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self._client.set_chat_protected_content(self.id, enabled=enabled)

    async def unpin_all_messages(self) -> bool:
        """Bound method *unpin_all_messages* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.unpin_all_chat_messages(chat_id)

        Example:
            .. code-block:: python

                chat.unpin_all_messages()

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self._client.unpin_all_chat_messages(self.id)

    async def mute(self, mute_until: datetime = None) -> bool:
        """Bound method *mute* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.update_chat_notifications(chat_id, mute=True, mute_until=mute_until)

        Parameters:
            mute (``bool``, *optional*):
                Pass True if you want to mute chat.

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unmuted. Defaults to forever.

        Example:
            .. code-block:: python

                chat.mute()

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self._client.update_chat_notifications(
            self.id,
            mute=True,
            mute_until=mute_until,
        )

    async def unmute(self) -> bool:
        """Bound method *unmute* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.update_chat_notifications(chat_id, mute=False)

        Example:
            .. code-block:: python

                chat.unmute()

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self._client.update_chat_notifications(self.id, mute=False)
