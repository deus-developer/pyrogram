from enum import StrEnum


class EventType(StrEnum):
    MESSAGE = "message"
    EDITED_MESSAGE = "edited_message"
    MESSAGE_REACTION = "message_reaction"
    MESSAGE_REACTION_COUNT = "message_reaction_count"
    INLINE_QUERY = "inline_query"
    CHOSEN_INLINE_RESULT = "chosen_inline_result"
    CALLBACK_QUERY = "callback_query"
    SHIPPING_QUERY = "shipping_query"
    PRE_CHECKOUT_QUERY = "pre_checkout_query"
    PURCHASED_PAID_MEDIA = "purchased_paid_media"
    POLL = "poll"
    CHAT_MEMBER = "chat_member"
    CHAT_JOIN_REQUEST = "chat_join_request"
    CHAT_BOOST = "chat_boost"
    STORY = "story"
    USER_STATUS = "user_status"
    RAW = "raw"
    UNKNOWN = "any"
