# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type EmailVerification = (
    raw.types.EmailVerificationApple
    | raw.types.EmailVerificationCode
    | raw.types.EmailVerificationGoogle
)
