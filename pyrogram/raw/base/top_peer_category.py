# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type TopPeerCategory = (
    raw.types.TopPeerCategoryBotsInline
    | raw.types.TopPeerCategoryBotsPM
    | raw.types.TopPeerCategoryChannels
    | raw.types.TopPeerCategoryCorrespondents
    | raw.types.TopPeerCategoryForwardChats
    | raw.types.TopPeerCategoryForwardUsers
    | raw.types.TopPeerCategoryGroups
    | raw.types.TopPeerCategoryPhoneCalls
)
