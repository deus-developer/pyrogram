# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type UserStatus = (
    raw.types.UserStatusEmpty
    | raw.types.UserStatusLastMonth
    | raw.types.UserStatusLastWeek
    | raw.types.UserStatusOffline
    | raw.types.UserStatusOnline
    | raw.types.UserStatusRecently
)
