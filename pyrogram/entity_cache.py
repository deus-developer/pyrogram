from pyrogram import raw


class EntityCache:
    def __init__(self) -> None:
        self._user_by_id: dict[int, raw.base.User] = {}
        self._chat_by_id: dict[int, raw.base.Chat] = {}
        self._channel_by_id: dict[int, raw.base.Chat] = {}
        self._topic_by_id: dict[int, raw.base.ForumTopic] = {}
        self._message_by_id: dict[int, raw.base.Message] = {}
