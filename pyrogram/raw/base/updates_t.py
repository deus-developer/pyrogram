# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type Updates = (
    raw.types.UpdateShort
    | raw.types.UpdateShortChatMessage
    | raw.types.UpdateShortMessage
    | raw.types.UpdateShortSentMessage
    | raw.types.Updates
    | raw.types.UpdatesCombined
    | raw.types.UpdatesTooLong
)
