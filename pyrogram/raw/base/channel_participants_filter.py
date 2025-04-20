# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union, TypeAlias
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelParticipantsFilter: TypeAlias = Union["raw.types.ChannelParticipantsAdmins, raw.types.ChannelParticipantsBanned, raw.types.ChannelParticipantsBots, raw.types.ChannelParticipantsContacts, raw.types.ChannelParticipantsKicked, raw.types.ChannelParticipantsMentions, raw.types.ChannelParticipantsRecent, raw.types.ChannelParticipantsSearch"]