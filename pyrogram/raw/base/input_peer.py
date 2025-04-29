# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type InputPeer = (
    raw.types.InputPeerChannel
    | raw.types.InputPeerChannelFromMessage
    | raw.types.InputPeerChat
    | raw.types.InputPeerEmpty
    | raw.types.InputPeerSelf
    | raw.types.InputPeerUser
    | raw.types.InputPeerUserFromMessage
)
