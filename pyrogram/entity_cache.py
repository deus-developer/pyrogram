from collections.abc import Iterable
from typing import (
    assert_never,
)

from pyrogram import raw

type UserT = raw.types.User | raw.types.UserEmpty
type ChatT = raw.types.Chat | raw.types.ChatEmpty | raw.types.ChatForbidden
type ChannelT = raw.types.Channel | raw.types.ChannelForbidden
type EntityT = UserT | ChatT | ChannelT
type PeerT = raw.base.Peer | raw.base.InputPeer | raw.base.ChatFull

MAX_CHANNEL_ID = -1000000000000


def get_channel_id(peer_id: int) -> int:
    return MAX_CHANNEL_ID - peer_id


def get_entity_index(entity: EntityT) -> int:
    if isinstance(
        entity,
        (
            raw.types.User,
            raw.types.UserEmpty,
        ),
    ):
        return entity.id
    if isinstance(
        entity,
        (
            raw.types.Chat,
            raw.types.ChatEmpty,
            raw.types.ChatForbidden,
        ),
    ):
        return -entity.id
    if isinstance(
        entity,
        (
            raw.types.Channel,
            raw.types.ChannelForbidden,
        ),
    ):
        return get_channel_id(entity.id)
    assert_never(entity)


class EntityCache:
    def __init__(
        self,
        time_to_live: float = 60.0,
        garbage_collection_interval: float = 30.0,
    ) -> None:
        self._time_to_live = time_to_live
        self._garbage_collection_interval = garbage_collection_interval

        self._entity_by_index: dict[int, EntityT] = {}
        self._timestamp_by_index: dict[int, float] = {}

        self._next_garbage_collection = 0.0
        self._timestamp = 0.0

        self._self_user_id = 0

    def set_timestamp(self, *, timestamp: float) -> None:
        self._timestamp = timestamp

    def set_self_user_id(self, *, self_user_id: int) -> None:
        self._self_user_id = self_user_id

    def gc(self) -> None:
        if self._timestamp < self._next_garbage_collection:
            return

        self._next_garbage_collection = (
            self._timestamp + self._garbage_collection_interval
        )

        dead_line = self._timestamp - self._time_to_live

        drop: list[int] = [
            index
            for index, value in self._timestamp_by_index.items()
            if value <= dead_line
        ]

        for index in drop:
            self._entity_by_index.pop(index, None)
            self._timestamp_by_index.pop(index, None)

    def set(self, *, entity: EntityT) -> None:
        index = get_entity_index(entity)
        self._entity_by_index[index] = entity
        self._timestamp_by_index[index] = self._timestamp

        self.gc()

    def setdefault(self, *, entity: EntityT) -> None:
        index = get_entity_index(entity)
        self._entity_by_index.setdefault(index, entity)
        self._timestamp_by_index[index] = self._timestamp

        self.gc()

    def add(self, *, entity: EntityT | None) -> None:
        if entity is None:
            return
        if isinstance(
            entity,
            (
                raw.types.User,
                raw.types.Channel,
                raw.types.ChannelForbidden,
                raw.types.Chat,
                raw.types.ChatForbidden,
            ),
        ):
            self.set(entity=entity)
        elif isinstance(
            entity,
            (
                raw.types.UserEmpty,
                raw.types.ChatEmpty,
            ),
        ):
            self.setdefault(entity=entity)
        else:
            assert_never(entity)

    def update(self, *, entities: Iterable[EntityT]) -> None:
        for entity in entities:
            self.add(entity=entity)

    def get_user(self, *, user_id: int) -> UserT:
        index = user_id
        self._timestamp_by_index[index] = self._timestamp
        return self._entity_by_index.setdefault(index, raw.types.UserEmpty(id=user_id))

    def get_chat(self, *, chat_id: int) -> ChatT:
        index = -chat_id
        self._timestamp_by_index[index] = self._timestamp
        return self._entity_by_index.setdefault(index, raw.types.ChatEmpty(id=chat_id))

    def get_channel(self, *, channel_id: int) -> ChannelT | None:
        index = get_channel_id(channel_id)
        self._timestamp_by_index[index] = self._timestamp
        return self._entity_by_index.get(index)

    def get_peer(self, *, peer: PeerT) -> EntityT | None:
        if isinstance(peer, raw.types.InputPeerEmpty):
            return None
        if isinstance(peer, raw.types.InputPeerSelf):
            return self.get_user(user_id=self._self_user_id)
        if isinstance(
            peer,
            (
                raw.types.PeerUser,
                raw.types.InputPeerUser,
                raw.types.InputPeerUserFromMessage,
            ),
        ):
            return self.get_user(user_id=peer.user_id)
        if isinstance(
            peer,
            (
                raw.types.PeerChat,
                raw.types.InputPeerChat,
            ),
        ):
            return self.get_chat(chat_id=peer.chat_id)
        if isinstance(
            peer,
            (
                raw.types.PeerChannel,
                raw.types.InputPeerChannel,
                raw.types.InputPeerChannelFromMessage,
            ),
        ):
            return self.get_channel(channel_id=peer.channel_id)
        if isinstance(peer, raw.types.ChannelFull):
            return self.get_channel(channel_id=peer.id)
        if isinstance(peer, raw.types.ChatFull):
            return self.get_chat(chat_id=peer.id)
        assert_never(peer)

    def get_signed_chat(self, *, signed_chat_id: int) -> EntityT | None:
        if signed_chat_id >= 0:
            return self.get_user(user_id=signed_chat_id)
        if signed_chat_id < MAX_CHANNEL_ID:
            return self.get_channel(channel_id=get_channel_id(signed_chat_id))
        if signed_chat_id < 0:
            return self.get_chat(chat_id=-signed_chat_id)
        return None

    def get(
        self,
        *,
        user_id: int | None = None,
        chat_id: int | None = None,
        channel_id: int | None = None,
        signed_chat_id: int | None = None,
        peer: PeerT | None = None,
    ) -> UserT | ChatT | ChannelT | None:
        if user_id:
            return self.get_user(user_id=user_id)
        if chat_id:
            return self.get_chat(chat_id=chat_id)
        if channel_id:
            return self.get_channel(channel_id=channel_id)
        if signed_chat_id:
            return self.get_signed_chat(signed_chat_id=signed_chat_id)
        if peer:
            return self.get_peer(peer=peer)
        raise ValueError("No arguments provided")
