# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type InputBotInlineMessage = (
    raw.types.InputBotInlineMessageGame
    | raw.types.InputBotInlineMessageMediaAuto
    | raw.types.InputBotInlineMessageMediaContact
    | raw.types.InputBotInlineMessageMediaGeo
    | raw.types.InputBotInlineMessageMediaInvoice
    | raw.types.InputBotInlineMessageMediaVenue
    | raw.types.InputBotInlineMessageMediaWebPage
    | raw.types.InputBotInlineMessageText
)
