# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type RecentMeUrl = (
    raw.types.RecentMeUrlChat
    | raw.types.RecentMeUrlChatInvite
    | raw.types.RecentMeUrlStickerSet
    | raw.types.RecentMeUrlUnknown
    | raw.types.RecentMeUrlUser
)
