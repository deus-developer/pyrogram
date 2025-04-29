# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type InputStorePaymentPurpose = (
    raw.types.InputStorePaymentGiftPremium
    | raw.types.InputStorePaymentPremiumGiftCode
    | raw.types.InputStorePaymentPremiumGiveaway
    | raw.types.InputStorePaymentPremiumSubscription
    | raw.types.InputStorePaymentStars
)
