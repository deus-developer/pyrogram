# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type ReportReason = (
    raw.types.InputReportReasonChildAbuse
    | raw.types.InputReportReasonCopyright
    | raw.types.InputReportReasonFake
    | raw.types.InputReportReasonGeoIrrelevant
    | raw.types.InputReportReasonIllegalDrugs
    | raw.types.InputReportReasonOther
    | raw.types.InputReportReasonPersonalDetails
    | raw.types.InputReportReasonPornography
    | raw.types.InputReportReasonSpam
    | raw.types.InputReportReasonViolence
)
