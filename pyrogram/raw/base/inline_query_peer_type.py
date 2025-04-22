# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type InlineQueryPeerType = (
    raw.types.InlineQueryPeerTypeBotPM
    | raw.types.InlineQueryPeerTypeBroadcast
    | raw.types.InlineQueryPeerTypeChat
    | raw.types.InlineQueryPeerTypeMegagroup
    | raw.types.InlineQueryPeerTypePM
    | raw.types.InlineQueryPeerTypeSameBotPM
)
