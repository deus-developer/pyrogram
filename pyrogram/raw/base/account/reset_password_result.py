# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union, TypeAlias
from pyrogram import raw
from pyrogram.raw.core import TLObject

ResetPasswordResult: TypeAlias = Union["raw.types.account.ResetPasswordFailedWait, raw.types.account.ResetPasswordOk, raw.types.account.ResetPasswordRequestedWait"]