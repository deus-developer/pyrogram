# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type InputPrivacyRule = (
    raw.types.InputPrivacyValueAllowAll
    | raw.types.InputPrivacyValueAllowChatParticipants
    | raw.types.InputPrivacyValueAllowCloseFriends
    | raw.types.InputPrivacyValueAllowContacts
    | raw.types.InputPrivacyValueAllowPremium
    | raw.types.InputPrivacyValueAllowUsers
    | raw.types.InputPrivacyValueDisallowAll
    | raw.types.InputPrivacyValueDisallowChatParticipants
    | raw.types.InputPrivacyValueDisallowContacts
    | raw.types.InputPrivacyValueDisallowUsers
)
