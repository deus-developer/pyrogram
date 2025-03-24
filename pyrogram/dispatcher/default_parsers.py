import pyrogram
from pyrogram.dispatcher.parser import TelegramRawUpdateParser
from pyrogram.dispatcher.schemas import TelegramRawUpdate, TelegramUpdate


async def default_message_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[
        pyrogram.raw.types.UpdateNewMessage
        | pyrogram.raw.types.UpdateNewChannelMessage
        | pyrogram.raw.types.UpdateNewScheduledMessage
        | pyrogram.raw.types.UpdateBotNewBusinessMessage
    ],
) -> TelegramUpdate:
    connection_id = getattr(raw.update, "connection_id", None)

    message = await pyrogram.types.Message._parse(
        client=client,
        message=raw.update.message,
        users=raw.users,
        chats=raw.chats,
        is_scheduled=isinstance(
            raw.update,
            pyrogram.raw.types.UpdateNewScheduledMessage,
        ),
        replies=0 if getattr(raw.update, "connection_id", None) else 1,
        business_connection_id=connection_id,
        raw_reply_to_message=getattr(raw.update, "reply_to_message", None),
    )
    return TelegramUpdate(
        raw=raw,
        message=message,
    )


async def default_edited_message_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[
        pyrogram.raw.types.UpdateEditMessage
        | pyrogram.raw.types.UpdateEditChannelMessage
        | pyrogram.raw.types.UpdateBotEditBusinessMessage
    ],
) -> TelegramUpdate:
    connection_id = getattr(raw.update, "connection_id", None)

    message = await pyrogram.types.Message._parse(
        client=client,
        message=raw.update.message,
        users=raw.users,
        chats=raw.chats,
        is_scheduled=isinstance(
            raw.update,
            pyrogram.raw.types.UpdateNewScheduledMessage,
        ),
        replies=0 if getattr(raw.update, "connection_id", None) else 1,
        business_connection_id=connection_id,
        raw_reply_to_message=getattr(raw.update, "reply_to_message", None),
    )
    return TelegramUpdate(
        raw=raw,
        edited_message=message,
    )


async def default_message_reaction_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateBotMessageReaction],
) -> TelegramUpdate:
    message_reaction = pyrogram.types.MessageReactionUpdated._parse(
        client=client,
        update=raw.update,
        users=raw.users,
        chats=raw.chats,
    )
    return TelegramUpdate(
        raw=raw,
        message_reaction=message_reaction,
    )


async def default_message_reaction_count_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateBotMessageReactions],
) -> TelegramUpdate:
    message_reaction_count = pyrogram.types.MessageReactionCountUpdated._parse(
        client=client,
        update=raw.update,
        users=raw.users,
        chats=raw.chats,
    )
    return TelegramUpdate(
        raw=raw,
        message_reaction_count=message_reaction_count,
    )


async def default_inline_query_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateBotInlineQuery],
) -> TelegramUpdate:
    inline_query = pyrogram.types.InlineQuery._parse(
        client=client,
        inline_query=raw.update,
        users=raw.users,
    )
    return TelegramUpdate(
        raw=raw,
        inline_query=inline_query,
    )


async def default_chosen_inline_result_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateBotInlineSend],
) -> TelegramUpdate:
    chosen_inline_result = pyrogram.types.ChosenInlineResult._parse(
        client=client,
        chosen_inline_result=raw.update,
        users=raw.users,
    )
    return TelegramUpdate(
        raw=raw,
        chosen_inline_result=chosen_inline_result,
    )


async def default_callback_query_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[
        pyrogram.raw.types.UpdateBotCallbackQuery
        | pyrogram.raw.types.UpdateInlineBotCallbackQuery
        | pyrogram.raw.types.UpdateBusinessBotCallbackQuery
    ],
) -> TelegramUpdate:
    callback_query = await pyrogram.types.CallbackQuery._parse(
        client=client,
        callback_query=raw.update,
        users=raw.users,
        chats=raw.chats,
    )
    return TelegramUpdate(
        raw=raw,
        callback_query=callback_query,
    )


async def default_shipping_query_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateBotShippingQuery],
) -> TelegramUpdate:
    shipping_query = await pyrogram.types.ShippingQuery._parse(
        client=client,
        shipping_query=raw.update,
        users=raw.users,
    )
    return TelegramUpdate(
        raw=raw,
        shipping_query=shipping_query,
    )


async def default_pre_checkout_query_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateBotPrecheckoutQuery],
) -> TelegramUpdate:
    pre_checkout_query = await pyrogram.types.PreCheckoutQuery._parse(
        client=client,
        pre_checkout_query=raw.update,
        users=raw.users,
    )
    return TelegramUpdate(
        raw=raw,
        pre_checkout_query=pre_checkout_query,
    )


async def default_purchased_paid_media_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateBotPurchasedPaidMedia],
) -> TelegramUpdate:
    purchased_paid_media = pyrogram.types.PurchasedPaidMedia._parse(
        client=client,
        purchased_media=raw.update,
        users=raw.users,
    )
    return TelegramUpdate(
        raw=raw,
        purchased_paid_media=purchased_paid_media,
    )


async def default_poll_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[
        pyrogram.raw.types.UpdateMessagePoll | pyrogram.raw.types.UpdateMessagePollVote
    ],
) -> TelegramUpdate:
    poll = pyrogram.types.Poll._parse_update(
        client=client,
        update=raw.update,
        users=raw.users,
    )
    return TelegramUpdate(
        raw=raw,
        poll=poll,
    )


async def default_chat_member_updated_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[
        pyrogram.raw.types.UpdateChatParticipant
        | pyrogram.raw.types.UpdateChannelParticipant
    ],
) -> TelegramUpdate:
    chat_member = pyrogram.types.ChatMemberUpdated._parse(
        client=client,
        update=raw.update,
        users=raw.users,
        chats=raw.chats,
    )
    return TelegramUpdate(
        raw=raw,
        chat_member=chat_member,
    )


async def default_chat_join_request_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateBotChatInviteRequester],
) -> TelegramUpdate:
    chat_join_request = pyrogram.types.ChatJoinRequest._parse(
        client=client,
        update=raw.update,
        users=raw.users,
        chats=raw.chats,
    )
    return TelegramUpdate(
        raw=raw,
        chat_join_request=chat_join_request,
    )


async def default_chat_boost_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateBotChatBoost],
) -> TelegramUpdate:
    chat_boost = pyrogram.types.ChatBoostUpdated._parse(
        client=client,
        update=raw.update,
        users=raw.users,
        chats=raw.chats,
    )
    return TelegramUpdate(
        raw=raw,
        chat_boost=chat_boost,
    )


async def default_story_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateStory],
) -> TelegramUpdate:
    story = await pyrogram.types.Story._parse(
        client=client,
        story=raw.update.story,
        users=raw.users,
        chats=raw.chats,
        peer=raw.update.peer,
    )
    return TelegramUpdate(
        raw=raw,
        story=story,
    )


async def default_user_status_parser(
    client: pyrogram.Client,
    raw: TelegramRawUpdate[pyrogram.raw.types.UpdateUserStatus],
) -> TelegramUpdate:
    user_status = pyrogram.types.User._parse_user_status(
        client=client,
        user_status=raw.update,
    )
    return TelegramUpdate(
        raw=raw,
        user_status=user_status,
    )


def build_default_parser() -> TelegramRawUpdateParser:
    instance = TelegramRawUpdateParser()

    # Update message
    instance.add_update_parser(
        pyrogram.raw.types.UpdateNewMessage,
        default_message_parser,
    )
    instance.add_update_parser(
        pyrogram.raw.types.UpdateNewChannelMessage,
        default_message_parser,
    )
    instance.add_update_parser(
        pyrogram.raw.types.UpdateNewScheduledMessage,
        default_message_parser,
    )
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotNewBusinessMessage,
        default_message_parser,
    )

    # Update edited_message
    instance.add_update_parser(
        pyrogram.raw.types.UpdateEditMessage,
        default_edited_message_parser,
    )
    instance.add_update_parser(
        pyrogram.raw.types.UpdateEditChannelMessage,
        default_edited_message_parser,
    )
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotEditBusinessMessage,
        default_edited_message_parser,
    )

    # Update message_reaction
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotMessageReaction,
        default_message_reaction_parser,
    )

    # Update message_reaction_count
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotMessageReactions,
        default_message_reaction_count_parser,
    )

    # Update inline_query
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotInlineQuery,
        default_inline_query_parser,
    )

    # Update chosen_inline_result
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotInlineSend,
        default_chosen_inline_result_parser,
    )

    # Update callback_query
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotCallbackQuery,
        default_callback_query_parser,
    )
    instance.add_update_parser(
        pyrogram.raw.types.UpdateInlineBotCallbackQuery,
        default_callback_query_parser,
    )
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBusinessBotCallbackQuery,
        default_callback_query_parser,
    )

    # Update shipping_query
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotShippingQuery,
        default_shipping_query_parser,
    )

    # Update pre_checkout_query
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotPrecheckoutQuery,
        default_pre_checkout_query_parser,
    )

    # Update purchased_paid_media
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotPurchasedPaidMedia,
        default_purchased_paid_media_parser,
    )

    # Update poll
    instance.add_update_parser(
        pyrogram.raw.types.UpdateMessagePoll,
        default_poll_parser,
    )
    instance.add_update_parser(
        pyrogram.raw.types.UpdateMessagePollVote,
        default_poll_parser,
    )

    # Update chat_member
    instance.add_update_parser(
        pyrogram.raw.types.UpdateChatParticipant,
        default_chat_member_updated_parser,
    )
    instance.add_update_parser(
        pyrogram.raw.types.UpdateChannelParticipant,
        default_chat_member_updated_parser,
    )

    # Update chat_join_request
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotChatInviteRequester,
        default_chat_join_request_parser,
    )

    # Update chat_boost
    instance.add_update_parser(
        pyrogram.raw.types.UpdateBotChatBoost,
        default_chat_boost_parser,
    )

    # Update story
    instance.add_update_parser(pyrogram.raw.types.UpdateStory, default_story_parser)

    # Update user_status
    instance.add_update_parser(
        pyrogram.raw.types.UpdateUserStatus,
        default_user_status_parser,
    )

    return instance
