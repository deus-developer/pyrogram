# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from pyrogram import raw

type SendMessageAction = (
    raw.types.SendMessageCancelAction
    | raw.types.SendMessageChooseContactAction
    | raw.types.SendMessageChooseStickerAction
    | raw.types.SendMessageEmojiInteraction
    | raw.types.SendMessageEmojiInteractionSeen
    | raw.types.SendMessageGamePlayAction
    | raw.types.SendMessageGeoLocationAction
    | raw.types.SendMessageHistoryImportAction
    | raw.types.SendMessageRecordAudioAction
    | raw.types.SendMessageRecordRoundAction
    | raw.types.SendMessageRecordVideoAction
    | raw.types.SendMessageTypingAction
    | raw.types.SendMessageUploadAudioAction
    | raw.types.SendMessageUploadDocumentAction
    | raw.types.SendMessageUploadPhotoAction
    | raw.types.SendMessageUploadRoundAction
    | raw.types.SendMessageUploadVideoAction
    | raw.types.SpeakingInGroupCallAction
)
