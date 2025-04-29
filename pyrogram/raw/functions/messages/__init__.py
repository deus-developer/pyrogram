#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from .accept_encryption import AcceptEncryption
from .accept_url_auth import AcceptUrlAuth
from .add_chat_user import AddChatUser
from .check_chat_invite import CheckChatInvite
from .check_history_import import CheckHistoryImport
from .check_history_import_peer import CheckHistoryImportPeer
from .check_quick_reply_shortcut import CheckQuickReplyShortcut
from .clear_all_drafts import ClearAllDrafts
from .clear_recent_reactions import ClearRecentReactions
from .clear_recent_stickers import ClearRecentStickers
from .create_chat import CreateChat
from .delete_chat import DeleteChat
from .delete_chat_user import DeleteChatUser
from .delete_exported_chat_invite import DeleteExportedChatInvite
from .delete_fact_check import DeleteFactCheck
from .delete_history import DeleteHistory
from .delete_messages import DeleteMessages
from .delete_phone_call_history import DeletePhoneCallHistory
from .delete_quick_reply_messages import DeleteQuickReplyMessages
from .delete_quick_reply_shortcut import DeleteQuickReplyShortcut
from .delete_revoked_exported_chat_invites import DeleteRevokedExportedChatInvites
from .delete_saved_history import DeleteSavedHistory
from .delete_scheduled_messages import DeleteScheduledMessages
from .discard_encryption import DiscardEncryption
from .edit_chat_about import EditChatAbout
from .edit_chat_admin import EditChatAdmin
from .edit_chat_default_banned_rights import EditChatDefaultBannedRights
from .edit_chat_photo import EditChatPhoto
from .edit_chat_title import EditChatTitle
from .edit_exported_chat_invite import EditExportedChatInvite
from .edit_fact_check import EditFactCheck
from .edit_inline_bot_message import EditInlineBotMessage
from .edit_message import EditMessage
from .edit_quick_reply_shortcut import EditQuickReplyShortcut
from .export_chat_invite import ExportChatInvite
from .fave_sticker import FaveSticker
from .forward_messages import ForwardMessages
from .get_admins_with_invites import GetAdminsWithInvites
from .get_all_drafts import GetAllDrafts
from .get_all_stickers import GetAllStickers
from .get_archived_stickers import GetArchivedStickers
from .get_attach_menu_bot import GetAttachMenuBot
from .get_attach_menu_bots import GetAttachMenuBots
from .get_attached_stickers import GetAttachedStickers
from .get_available_effects import GetAvailableEffects
from .get_available_reactions import GetAvailableReactions
from .get_bot_app import GetBotApp
from .get_bot_callback_answer import GetBotCallbackAnswer
from .get_chat_invite_importers import GetChatInviteImporters
from .get_chats import GetChats
from .get_common_chats import GetCommonChats
from .get_custom_emoji_documents import GetCustomEmojiDocuments
from .get_default_history_ttl import GetDefaultHistoryTTL
from .get_default_tag_reactions import GetDefaultTagReactions
from .get_dh_config import GetDhConfig
from .get_dialog_filters import GetDialogFilters
from .get_dialog_unread_marks import GetDialogUnreadMarks
from .get_dialogs import GetDialogs
from .get_discussion_message import GetDiscussionMessage
from .get_document_by_hash import GetDocumentByHash
from .get_emoji_groups import GetEmojiGroups
from .get_emoji_keywords import GetEmojiKeywords
from .get_emoji_keywords_difference import GetEmojiKeywordsDifference
from .get_emoji_keywords_languages import GetEmojiKeywordsLanguages
from .get_emoji_profile_photo_groups import GetEmojiProfilePhotoGroups
from .get_emoji_status_groups import GetEmojiStatusGroups
from .get_emoji_sticker_groups import GetEmojiStickerGroups
from .get_emoji_stickers import GetEmojiStickers
from .get_emoji_url import GetEmojiURL
from .get_exported_chat_invite import GetExportedChatInvite
from .get_exported_chat_invites import GetExportedChatInvites
from .get_extended_media import GetExtendedMedia
from .get_fact_check import GetFactCheck
from .get_faved_stickers import GetFavedStickers
from .get_featured_emoji_stickers import GetFeaturedEmojiStickers
from .get_featured_stickers import GetFeaturedStickers
from .get_full_chat import GetFullChat
from .get_game_high_scores import GetGameHighScores
from .get_history import GetHistory
from .get_inline_bot_results import GetInlineBotResults
from .get_inline_game_high_scores import GetInlineGameHighScores
from .get_mask_stickers import GetMaskStickers
from .get_message_edit_data import GetMessageEditData
from .get_message_reactions_list import GetMessageReactionsList
from .get_message_read_participants import GetMessageReadParticipants
from .get_messages import GetMessages
from .get_messages_reactions import GetMessagesReactions
from .get_messages_views import GetMessagesViews
from .get_my_stickers import GetMyStickers
from .get_old_featured_stickers import GetOldFeaturedStickers
from .get_onlines import GetOnlines
from .get_outbox_read_date import GetOutboxReadDate
from .get_peer_dialogs import GetPeerDialogs
from .get_peer_settings import GetPeerSettings
from .get_pinned_dialogs import GetPinnedDialogs
from .get_pinned_saved_dialogs import GetPinnedSavedDialogs
from .get_poll_results import GetPollResults
from .get_poll_votes import GetPollVotes
from .get_quick_replies import GetQuickReplies
from .get_quick_reply_messages import GetQuickReplyMessages
from .get_recent_locations import GetRecentLocations
from .get_recent_reactions import GetRecentReactions
from .get_recent_stickers import GetRecentStickers
from .get_replies import GetReplies
from .get_saved_dialogs import GetSavedDialogs
from .get_saved_gifs import GetSavedGifs
from .get_saved_history import GetSavedHistory
from .get_saved_reaction_tags import GetSavedReactionTags
from .get_scheduled_history import GetScheduledHistory
from .get_scheduled_messages import GetScheduledMessages
from .get_search_counters import GetSearchCounters
from .get_search_results_calendar import GetSearchResultsCalendar
from .get_search_results_positions import GetSearchResultsPositions
from .get_split_ranges import GetSplitRanges
from .get_sticker_set import GetStickerSet
from .get_stickers import GetStickers
from .get_suggested_dialog_filters import GetSuggestedDialogFilters
from .get_top_reactions import GetTopReactions
from .get_unread_mentions import GetUnreadMentions
from .get_unread_reactions import GetUnreadReactions
from .get_web_page import GetWebPage
from .get_web_page_preview import GetWebPagePreview
from .hide_all_chat_join_requests import HideAllChatJoinRequests
from .hide_chat_join_request import HideChatJoinRequest
from .hide_peer_settings_bar import HidePeerSettingsBar
from .import_chat_invite import ImportChatInvite
from .init_history_import import InitHistoryImport
from .install_sticker_set import InstallStickerSet
from .mark_dialog_unread import MarkDialogUnread
from .migrate_chat import MigrateChat
from .prolong_web_view import ProlongWebView
from .rate_transcribed_audio import RateTranscribedAudio
from .read_discussion import ReadDiscussion
from .read_encrypted_history import ReadEncryptedHistory
from .read_featured_stickers import ReadFeaturedStickers
from .read_history import ReadHistory
from .read_mentions import ReadMentions
from .read_message_contents import ReadMessageContents
from .read_reactions import ReadReactions
from .received_messages import ReceivedMessages
from .received_queue import ReceivedQueue
from .reorder_pinned_dialogs import ReorderPinnedDialogs
from .reorder_pinned_saved_dialogs import ReorderPinnedSavedDialogs
from .reorder_quick_replies import ReorderQuickReplies
from .reorder_sticker_sets import ReorderStickerSets
from .report import Report
from .report_encrypted_spam import ReportEncryptedSpam
from .report_reaction import ReportReaction
from .report_spam import ReportSpam
from .request_app_web_view import RequestAppWebView
from .request_encryption import RequestEncryption
from .request_simple_web_view import RequestSimpleWebView
from .request_url_auth import RequestUrlAuth
from .request_web_view import RequestWebView
from .save_default_send_as import SaveDefaultSendAs
from .save_draft import SaveDraft
from .save_gif import SaveGif
from .save_recent_sticker import SaveRecentSticker
from .search import Search
from .search_custom_emoji import SearchCustomEmoji
from .search_emoji_sticker_sets import SearchEmojiStickerSets
from .search_global import SearchGlobal
from .search_sent_media import SearchSentMedia
from .search_sticker_sets import SearchStickerSets
from .send_bot_requested_peer import SendBotRequestedPeer
from .send_encrypted import SendEncrypted
from .send_encrypted_file import SendEncryptedFile
from .send_encrypted_service import SendEncryptedService
from .send_inline_bot_result import SendInlineBotResult
from .send_media import SendMedia
from .send_message import SendMessage
from .send_multi_media import SendMultiMedia
from .send_quick_reply_messages import SendQuickReplyMessages
from .send_reaction import SendReaction
from .send_scheduled_messages import SendScheduledMessages
from .send_screenshot_notification import SendScreenshotNotification
from .send_vote import SendVote
from .send_web_view_data import SendWebViewData
from .send_web_view_result_message import SendWebViewResultMessage
from .set_bot_callback_answer import SetBotCallbackAnswer
from .set_bot_precheckout_results import SetBotPrecheckoutResults
from .set_bot_shipping_results import SetBotShippingResults
from .set_chat_available_reactions import SetChatAvailableReactions
from .set_chat_theme import SetChatTheme
from .set_chat_wall_paper import SetChatWallPaper
from .set_default_history_ttl import SetDefaultHistoryTTL
from .set_default_reaction import SetDefaultReaction
from .set_encrypted_typing import SetEncryptedTyping
from .set_game_score import SetGameScore
from .set_history_ttl import SetHistoryTTL
from .set_inline_bot_results import SetInlineBotResults
from .set_inline_game_score import SetInlineGameScore
from .set_typing import SetTyping
from .start_bot import StartBot
from .start_history_import import StartHistoryImport
from .toggle_bot_in_attach_menu import ToggleBotInAttachMenu
from .toggle_dialog_filter_tags import ToggleDialogFilterTags
from .toggle_dialog_pin import ToggleDialogPin
from .toggle_no_forwards import ToggleNoForwards
from .toggle_peer_translations import TogglePeerTranslations
from .toggle_saved_dialog_pin import ToggleSavedDialogPin
from .toggle_sticker_sets import ToggleStickerSets
from .transcribe_audio import TranscribeAudio
from .translate_text import TranslateText
from .uninstall_sticker_set import UninstallStickerSet
from .unpin_all_messages import UnpinAllMessages
from .update_dialog_filter import UpdateDialogFilter
from .update_dialog_filters_order import UpdateDialogFiltersOrder
from .update_pinned_message import UpdatePinnedMessage
from .update_saved_reaction_tag import UpdateSavedReactionTag
from .upload_encrypted_file import UploadEncryptedFile
from .upload_imported_media import UploadImportedMedia
from .upload_media import UploadMedia
