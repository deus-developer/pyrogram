# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type Difference = (
    raw.types.updates.Difference
    | raw.types.updates.DifferenceEmpty
    | raw.types.updates.DifferenceSlice
    | raw.types.updates.DifferenceTooLong
)
