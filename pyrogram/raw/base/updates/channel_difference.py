# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type ChannelDifference = (
    raw.types.updates.ChannelDifference
    | raw.types.updates.ChannelDifferenceEmpty
    | raw.types.updates.ChannelDifferenceTooLong
)
