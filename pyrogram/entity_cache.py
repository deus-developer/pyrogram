from typing import assert_never

from pyrogram import raw

type UserT = raw.types.User | raw.types.UserEmpty
type ChatT = raw.types.Chat | raw.types.ChatEmpty | raw.types.ChatForbidden
type ChannelT = raw.types.Channel | raw.types.ChannelForbidden
type EntityT = UserT | ChatT | ChannelT


class EntityCache:
    def __init__(self) -> None:
        self._user_by_id: dict[int, UserT] = {}
        self._chat_by_id: dict[int, ChatT] = {}
        self._channel_by_id: dict[int, ChannelT] = {}

    def add_user(self, entity: UserT) -> None:
        if isinstance(entity, raw.types.User):
            self._user_by_id[entity.id] = entity
        elif isinstance(entity, raw.types.UserEmpty):
            return
        else:
            assert_never(entity)

    def add_chat(self, entity: ChatT) -> None:
        if isinstance(entity, raw.types.Chat):
            self._chat_by_id[entity.id] = entity
        elif isinstance(entity, raw.types.ChatEmpty):
            return
        elif isinstance(entity, raw.types.ChatForbidden):
            self._chat_by_id[entity.id] = entity
        else:
            assert_never(entity)

    def add_channel(self, entity: ChannelT) -> None:
        if isinstance(entity, raw.types.Channel) or isinstance(
            entity,
            raw.types.ChannelForbidden,
        ):
            self._channel_by_id[entity.id] = entity
        else:
            assert_never(entity)

    def add(self, entity: EntityT) -> None:
        if isinstance(entity, raw.types.User | raw.types.UserEmpty):
            self.add_user(entity)
        elif isinstance(
            entity,
            raw.types.Chat | raw.types.ChatEmpty | raw.types.ChatForbidden,
        ):
            self.add_chat(entity)
        elif isinstance(entity, raw.types.Channel | raw.types.ChannelForbidden):
            self.add_channel(entity)
        else:
            assert_never(entity)

    def update(self, entities: list[EntityT]) -> None:
        for entity in filter(None, entities):
            self.add(entity)

    def get_by_user_id(self, user_id: int) -> UserT:
        entity = self._user_by_id.get(user_id)
        if entity is None:
            return raw.types.UserEmpty(id=user_id)
        return entity

    def get_by_chat_id(self, chat_id: int) -> ChatT:
        entity = self._chat_by_id.get(chat_id)
        if entity is None:
            return raw.types.ChatEmpty(id=chat_id)
        return entity

    def get_by_channel_id(self, channel_id: int) -> ChannelT | None:
        return self._channel_by_id.get(channel_id)

    def get_by_peer_id(
        self,
        peer: raw.base.Peer | raw.base.InputPeer | None,
    ) -> EntityT | None:
        if peer is None:
            return None
        if isinstance(
            peer,
            raw.types.PeerChannel
            | raw.types.InputPeerChannel
            | raw.types.InputPeerChannelFromMessage,
        ):
            return self.get_by_channel_id(channel_id=peer.channel_id)
        if isinstance(peer, raw.types.PeerChat | raw.types.InputPeerChat):
            return self.get_by_chat_id(chat_id=peer.chat_id)
        if isinstance(
            peer,
            raw.types.PeerUser
            | raw.types.InputPeerUser
            | raw.types.InputPeerUserFromMessage,
        ):
            return self.get_by_user_id(user_id=peer.user_id)
        if isinstance(peer, raw.types.InputPeerSelf):
            raise NotImplementedError
        if isinstance(peer, raw.types.InputPeerEmpty):
            return None
        assert_never(peer)
