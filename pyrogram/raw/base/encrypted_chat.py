# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type EncryptedChat = (
    raw.types.EncryptedChat
    | raw.types.EncryptedChatDiscarded
    | raw.types.EncryptedChatEmpty
    | raw.types.EncryptedChatRequested
    | raw.types.EncryptedChatWaiting
)
