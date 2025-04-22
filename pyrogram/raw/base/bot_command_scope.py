# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type BotCommandScope = (
    raw.types.BotCommandScopeChatAdmins
    | raw.types.BotCommandScopeChats
    | raw.types.BotCommandScopeDefault
    | raw.types.BotCommandScopePeer
    | raw.types.BotCommandScopePeerAdmins
    | raw.types.BotCommandScopePeerUser
    | raw.types.BotCommandScopeUsers
)
