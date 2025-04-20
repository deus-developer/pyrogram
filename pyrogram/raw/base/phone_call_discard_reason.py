# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union, TypeAlias
from pyrogram import raw
from pyrogram.raw.core import TLObject

PhoneCallDiscardReason: TypeAlias = Union["raw.types.PhoneCallDiscardReasonBusy, raw.types.PhoneCallDiscardReasonDisconnect, raw.types.PhoneCallDiscardReasonHangup, raw.types.PhoneCallDiscardReasonMissed"]