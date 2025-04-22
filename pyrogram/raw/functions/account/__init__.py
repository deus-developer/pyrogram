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

from .accept_authorization import AcceptAuthorization
from .cancel_password_email import CancelPasswordEmail
from .change_authorization_settings import ChangeAuthorizationSettings
from .change_phone import ChangePhone
from .check_username import CheckUsername
from .clear_recent_emoji_statuses import ClearRecentEmojiStatuses
from .confirm_password_email import ConfirmPasswordEmail
from .confirm_phone import ConfirmPhone
from .create_business_chat_link import CreateBusinessChatLink
from .create_theme import CreateTheme
from .decline_password_reset import DeclinePasswordReset
from .delete_account import DeleteAccount
from .delete_auto_save_exceptions import DeleteAutoSaveExceptions
from .delete_business_chat_link import DeleteBusinessChatLink
from .delete_secure_value import DeleteSecureValue
from .disable_peer_connected_bot import DisablePeerConnectedBot
from .edit_business_chat_link import EditBusinessChatLink
from .finish_takeout_session import FinishTakeoutSession
from .get_account_ttl import GetAccountTTL
from .get_all_secure_values import GetAllSecureValues
from .get_authorization_form import GetAuthorizationForm
from .get_authorizations import GetAuthorizations
from .get_auto_download_settings import GetAutoDownloadSettings
from .get_auto_save_settings import GetAutoSaveSettings
from .get_bot_business_connection import GetBotBusinessConnection
from .get_business_chat_links import GetBusinessChatLinks
from .get_channel_default_emoji_statuses import GetChannelDefaultEmojiStatuses
from .get_channel_restricted_status_emojis import GetChannelRestrictedStatusEmojis
from .get_chat_themes import GetChatThemes
from .get_connected_bots import GetConnectedBots
from .get_contact_sign_up_notification import GetContactSignUpNotification
from .get_content_settings import GetContentSettings
from .get_default_background_emojis import GetDefaultBackgroundEmojis
from .get_default_emoji_statuses import GetDefaultEmojiStatuses
from .get_default_group_photo_emojis import GetDefaultGroupPhotoEmojis
from .get_default_profile_photo_emojis import GetDefaultProfilePhotoEmojis
from .get_global_privacy_settings import GetGlobalPrivacySettings
from .get_multi_wall_papers import GetMultiWallPapers
from .get_notify_exceptions import GetNotifyExceptions
from .get_notify_settings import GetNotifySettings
from .get_password import GetPassword
from .get_password_settings import GetPasswordSettings
from .get_privacy import GetPrivacy
from .get_reactions_notify_settings import GetReactionsNotifySettings
from .get_recent_emoji_statuses import GetRecentEmojiStatuses
from .get_saved_ringtones import GetSavedRingtones
from .get_secure_value import GetSecureValue
from .get_theme import GetTheme
from .get_themes import GetThemes
from .get_tmp_password import GetTmpPassword
from .get_wall_paper import GetWallPaper
from .get_wall_papers import GetWallPapers
from .get_web_authorizations import GetWebAuthorizations
from .init_takeout_session import InitTakeoutSession
from .install_theme import InstallTheme
from .install_wall_paper import InstallWallPaper
from .invalidate_sign_in_codes import InvalidateSignInCodes
from .register_device import RegisterDevice
from .reorder_usernames import ReorderUsernames
from .report_peer import ReportPeer
from .report_profile_photo import ReportProfilePhoto
from .resend_password_email import ResendPasswordEmail
from .reset_authorization import ResetAuthorization
from .reset_notify_settings import ResetNotifySettings
from .reset_password import ResetPassword
from .reset_wall_papers import ResetWallPapers
from .reset_web_authorization import ResetWebAuthorization
from .reset_web_authorizations import ResetWebAuthorizations
from .resolve_business_chat_link import ResolveBusinessChatLink
from .save_auto_download_settings import SaveAutoDownloadSettings
from .save_auto_save_settings import SaveAutoSaveSettings
from .save_ringtone import SaveRingtone
from .save_secure_value import SaveSecureValue
from .save_theme import SaveTheme
from .save_wall_paper import SaveWallPaper
from .send_change_phone_code import SendChangePhoneCode
from .send_confirm_phone_code import SendConfirmPhoneCode
from .send_verify_email_code import SendVerifyEmailCode
from .send_verify_phone_code import SendVerifyPhoneCode
from .set_account_ttl import SetAccountTTL
from .set_authorization_ttl import SetAuthorizationTTL
from .set_contact_sign_up_notification import SetContactSignUpNotification
from .set_content_settings import SetContentSettings
from .set_global_privacy_settings import SetGlobalPrivacySettings
from .set_privacy import SetPrivacy
from .set_reactions_notify_settings import SetReactionsNotifySettings
from .toggle_connected_bot_paused import ToggleConnectedBotPaused
from .toggle_sponsored_messages import ToggleSponsoredMessages
from .toggle_username import ToggleUsername
from .unregister_device import UnregisterDevice
from .update_birthday import UpdateBirthday
from .update_business_away_message import UpdateBusinessAwayMessage
from .update_business_greeting_message import UpdateBusinessGreetingMessage
from .update_business_intro import UpdateBusinessIntro
from .update_business_location import UpdateBusinessLocation
from .update_business_work_hours import UpdateBusinessWorkHours
from .update_color import UpdateColor
from .update_connected_bot import UpdateConnectedBot
from .update_device_locked import UpdateDeviceLocked
from .update_emoji_status import UpdateEmojiStatus
from .update_notify_settings import UpdateNotifySettings
from .update_password_settings import UpdatePasswordSettings
from .update_personal_channel import UpdatePersonalChannel
from .update_profile import UpdateProfile
from .update_status import UpdateStatus
from .update_theme import UpdateTheme
from .update_username import UpdateUsername
from .upload_ringtone import UploadRingtone
from .upload_theme import UploadTheme
from .upload_wall_paper import UploadWallPaper
from .verify_email import VerifyEmail
from .verify_phone import VerifyPhone

__all__ = [
    "AcceptAuthorization",
    "CancelPasswordEmail",
    "ChangeAuthorizationSettings",
    "ChangePhone",
    "CheckUsername",
    "ClearRecentEmojiStatuses",
    "ConfirmPasswordEmail",
    "ConfirmPhone",
    "CreateBusinessChatLink",
    "CreateTheme",
    "DeclinePasswordReset",
    "DeleteAccount",
    "DeleteAutoSaveExceptions",
    "DeleteBusinessChatLink",
    "DeleteSecureValue",
    "DisablePeerConnectedBot",
    "EditBusinessChatLink",
    "FinishTakeoutSession",
    "GetAccountTTL",
    "GetAllSecureValues",
    "GetAuthorizationForm",
    "GetAuthorizations",
    "GetAutoDownloadSettings",
    "GetAutoSaveSettings",
    "GetBotBusinessConnection",
    "GetBusinessChatLinks",
    "GetChannelDefaultEmojiStatuses",
    "GetChannelRestrictedStatusEmojis",
    "GetChatThemes",
    "GetConnectedBots",
    "GetContactSignUpNotification",
    "GetContentSettings",
    "GetDefaultBackgroundEmojis",
    "GetDefaultEmojiStatuses",
    "GetDefaultGroupPhotoEmojis",
    "GetDefaultProfilePhotoEmojis",
    "GetGlobalPrivacySettings",
    "GetMultiWallPapers",
    "GetNotifyExceptions",
    "GetNotifySettings",
    "GetPassword",
    "GetPasswordSettings",
    "GetPrivacy",
    "GetReactionsNotifySettings",
    "GetRecentEmojiStatuses",
    "GetSavedRingtones",
    "GetSecureValue",
    "GetTheme",
    "GetThemes",
    "GetTmpPassword",
    "GetWallPaper",
    "GetWallPapers",
    "GetWebAuthorizations",
    "InitTakeoutSession",
    "InstallTheme",
    "InstallWallPaper",
    "InvalidateSignInCodes",
    "RegisterDevice",
    "ReorderUsernames",
    "ReportPeer",
    "ReportProfilePhoto",
    "ResendPasswordEmail",
    "ResetAuthorization",
    "ResetNotifySettings",
    "ResetPassword",
    "ResetWallPapers",
    "ResetWebAuthorization",
    "ResetWebAuthorizations",
    "ResolveBusinessChatLink",
    "SaveAutoDownloadSettings",
    "SaveAutoSaveSettings",
    "SaveRingtone",
    "SaveSecureValue",
    "SaveTheme",
    "SaveWallPaper",
    "SendChangePhoneCode",
    "SendConfirmPhoneCode",
    "SendVerifyEmailCode",
    "SendVerifyPhoneCode",
    "SetAccountTTL",
    "SetAuthorizationTTL",
    "SetContactSignUpNotification",
    "SetContentSettings",
    "SetGlobalPrivacySettings",
    "SetPrivacy",
    "SetReactionsNotifySettings",
    "ToggleConnectedBotPaused",
    "ToggleSponsoredMessages",
    "ToggleUsername",
    "UnregisterDevice",
    "UpdateBirthday",
    "UpdateBusinessAwayMessage",
    "UpdateBusinessGreetingMessage",
    "UpdateBusinessIntro",
    "UpdateBusinessLocation",
    "UpdateBusinessWorkHours",
    "UpdateColor",
    "UpdateConnectedBot",
    "UpdateDeviceLocked",
    "UpdateEmojiStatus",
    "UpdateNotifySettings",
    "UpdatePasswordSettings",
    "UpdatePersonalChannel",
    "UpdateProfile",
    "UpdateStatus",
    "UpdateTheme",
    "UpdateUsername",
    "UploadRingtone",
    "UploadTheme",
    "UploadWallPaper",
    "VerifyEmail",
    "VerifyPhone",
]
