import uuid
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    Generic,
    TypeVar,
)

import pyrogram

T = TypeVar("T", bound=pyrogram.raw.base.Update)


@dataclass(
    frozen=True,
    kw_only=True,
    slots=True,
)
class TelegramRawUpdate(Generic[T]):
    update_id: str = field(default_factory=lambda: uuid.uuid4().hex)

    update: T
    users: dict[int, pyrogram.raw.base.User]
    chats: dict[int, pyrogram.raw.base.Chat]


@dataclass(
    frozen=True,
    kw_only=True,
    slots=True,
)
class TelegramUpdate:
    raw: TelegramRawUpdate

    message: pyrogram.types.Message | None = None
    edited_message: pyrogram.types.Message | None = None
    # channel_post
    # edited_channel_post
    # business_connection
    # business_message
    # edited_business_message
    # deleted_business_messages
    message_reaction: pyrogram.types.MessageReactionUpdated | None = None
    message_reaction_count: pyrogram.types.MessageReactionCountUpdated | None = None
    inline_query: pyrogram.types.InlineQuery | None = None
    chosen_inline_result: pyrogram.types.ChosenInlineResult | None = None
    callback_query: pyrogram.types.CallbackQuery | None = None
    shipping_query: pyrogram.types.ShippingQuery | None = None
    pre_checkout_query: pyrogram.types.PreCheckoutQuery | None = None
    purchased_paid_media: pyrogram.types.PurchasedPaidMedia | None = None
    poll: pyrogram.types.Poll | None = None
    # poll_answer
    # my_chat_member
    chat_member: pyrogram.types.ChatMemberUpdated | None = None
    chat_join_request: pyrogram.types.ChatJoinRequest | None = None
    chat_boost: pyrogram.types.ChatBoostUpdated | None = None
    # removed_chat_boost
    story: pyrogram.types.Story | None = None
    user_status: pyrogram.types.User | None = None

    @property
    def update_id(self) -> str:
        return self.raw.update_id

    @property
    def event_type(self) -> str:
        if self.message:
            return "message"
        if self.edited_message:
            return "edited_message"
        if self.message_reaction:
            return "message_reaction"
        if self.message_reaction_count:
            return "message_reaction_count"
        if self.inline_query:
            return "inline_query"
        if self.chosen_inline_result:
            return "chosen_inline_result"
        if self.callback_query:
            return "callback_query"
        if self.shipping_query:
            return "shipping_query"
        if self.pre_checkout_query:
            return "pre_checkout_query"
        if self.purchased_paid_media:
            return "purchased_paid_media"
        if self.poll:
            return "poll"
        if self.chat_member:
            return "chat_member"
        if self.chat_join_request:
            return "chat_join_request"
        if self.chat_boost:
            return "chat_boost"
        if self.story:
            return "story"
        if self.user_status:
            return "user_status"

        return "raw"

    @property
    def event(self) -> Any:
        return getattr(self, self.event_type)


class UpdateTypeLookupError(LookupError):
    """Update does not contain any known event type."""
