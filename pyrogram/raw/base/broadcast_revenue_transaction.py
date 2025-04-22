# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type BroadcastRevenueTransaction = (
    raw.types.BroadcastRevenueTransactionProceeds
    | raw.types.BroadcastRevenueTransactionRefund
    | raw.types.BroadcastRevenueTransactionWithdrawal
)
