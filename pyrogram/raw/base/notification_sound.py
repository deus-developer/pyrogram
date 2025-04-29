# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type NotificationSound = (
    raw.types.NotificationSoundDefault
    | raw.types.NotificationSoundLocal
    | raw.types.NotificationSoundNone
    | raw.types.NotificationSoundRingtone
)
