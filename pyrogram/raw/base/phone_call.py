# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type PhoneCall = (
    raw.types.PhoneCall
    | raw.types.PhoneCallAccepted
    | raw.types.PhoneCallDiscarded
    | raw.types.PhoneCallEmpty
    | raw.types.PhoneCallRequested
    | raw.types.PhoneCallWaiting
)
