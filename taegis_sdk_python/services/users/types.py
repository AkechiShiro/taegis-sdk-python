"""Users Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class UsersAuthzObject(str, Enum):
    """UsersAuthzObject."""

    USER = "User"
    ROLE = "Role"


class UsersAuthzAction(str, Enum):
    """UsersAuthzAction."""

    CREATE = "create"
    READ = "read"
    SEARCH = "search"
    UPDATE = "update"
    UPDATE_SCWX = "updateScwx"
    DEACTIVATE = "deactivate"
    ASSIGN_INTERNAL = "assignInternal"
    VALIDATE_PIN = "validatePin"
    READ_AUTH0_LOG_ENTRIES = "readAuth0LogEntries"
    FORGOT_PASSWORD = "forgotPassword"
    SET_PASSWORD = "setPassword"
    NEED_NEW_MFA = "needNewMFA"
    SET_MFA = "setMFA"
    REGISTER_USER = "registerUser"


class GraphQLQueryType(str, Enum):
    """GraphQLQueryType."""

    TDRUSER = "TDRUser"
    TDRUSERS = "TDRUsers"
    TDRUSERS_SEARCH = "TDRUsersSearch"
    TDRUSERS_BY_IDS = "TDRUsersByIDs"
    ROLE_ASSIGNMENTS = "RoleAssignments"
    TDRUSER_SUPPORT_PIN = "TDRUserSupportPin"
    AUTH0_LOG_ENTRIES = "Auth0LogEntries"


class TDRUsersSearchSortBy(str, Enum):
    """TDRUsersSearchSortBy."""

    EMAIL = "email"
    FIRSTNAME = "firstname"
    LASTNAME = "lastname"
    STATUS = "status"
    TENANT_STATUS = "tenantStatus"
    PHONE = "phone"
    TIMEZONE = "timezone"


class TDRUsersSearchSortOrder(str, Enum):
    """TDRUsersSearchSortOrder."""

    ASC = "asc"
    DESC = "desc"


class TDRUsersLanguage(str, Enum):
    """TDRUsersLanguage."""

    NONE = "none"
    EN = "en"
    JA = "ja"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserTenant:
    """TDRUserTenant."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserTenantV2:
    """TDRUserTenantV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    role: Optional[str] = field(default=None, metadata=config(field_name="role"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserTenantEnvironment:
    """TDRUserTenantEnvironment."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserTenantLabel:
    """TDRUserTenantLabel."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_id")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserTenantService:
    """TDRUserTenantService."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserRoleAssignment:
    """TDRUserRoleAssignment."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_id")
    )
    role_id: Optional[str] = field(default=None, metadata=config(field_name="role_id"))
    deactivated: Optional[bool] = field(
        default=None, metadata=config(field_name="deactivated")
    )
    role_name: Optional[str] = field(
        default=None, metadata=config(field_name="role_name")
    )
    role_display_name: Optional[str] = field(
        default=None, metadata=config(field_name="role_display_name")
    )
    expires_at: Optional[str] = field(
        default=None, metadata=config(field_name="expires_at")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    allowed_environments: Optional[List[str]] = field(
        default=None, metadata=config(field_name="allowed_environments")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserLicense:
    """TDRUserLicense."""

    date: Optional[str] = field(default=None, metadata=config(field_name="date"))
    version: Optional[str] = field(default=None, metadata=config(field_name="version"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserTenantV2Input:
    """TDRUserTenantV2Input."""

    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    role: Optional[str] = field(default=None, metadata=config(field_name="role"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserRoleAssignmentInput:
    """TDRUserRoleAssignmentInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_id")
    )
    role_id: Optional[str] = field(default=None, metadata=config(field_name="role_id"))
    expires_at: Optional[str] = field(
        default=None, metadata=config(field_name="expires_at")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ForgotPasswordResponse:
    """ForgotPasswordResponse."""

    message: Optional[str] = field(default=None, metadata=config(field_name="message"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PasswordResetInput:
    """PasswordResetInput."""

    ticket_id: Optional[str] = field(
        default=None, metadata=config(field_name="ticket_id")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    password: Optional[str] = field(
        default=None, metadata=config(field_name="password")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MFAResetInput:
    """MFAResetInput."""

    ticket_id: Optional[str] = field(
        default=None, metadata=config(field_name="ticket_id")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    password: Optional[str] = field(
        default=None, metadata=config(field_name="password")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MFAResetResponse:
    """MFAResetResponse."""

    barcode_uri: Optional[str] = field(
        default=None, metadata=config(field_name="barcode_uri")
    )
    secret: Optional[str] = field(default=None, metadata=config(field_name="secret"))
    mfa_token: Optional[str] = field(
        default=None, metadata=config(field_name="mfa_token")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Auth0LogEntry:
    """Auth0LogEntry."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    date: Optional[str] = field(default=None, metadata=config(field_name="date"))
    auth0_event_type: Optional[str] = field(
        default=None, metadata=config(field_name="auth0_event_type")
    )
    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EULAAcceptance:
    """EULAAcceptance."""

    version: Optional[str] = field(default=None, metadata=config(field_name="version"))
    machine: Optional[str] = field(default=None, metadata=config(field_name="machine"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthorizeCheckConnection:
    """AuthorizeCheckConnection."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    external_id: Optional[str] = field(
        default=None, metadata=config(field_name="external_id")
    )
    external_name: Optional[str] = field(
        default=None, metadata=config(field_name="external_name")
    )
    testers: Optional[List[str]] = field(
        default=None, metadata=config(field_name="testers")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserInviteInput:
    """TDRUserInviteInput."""

    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    role_id: Optional[str] = field(default=None, metadata=config(field_name="role_id"))
    role_expires_at: Optional[str] = field(
        default=None, metadata=config(field_name="role_expires_at")
    )
    language: Optional[TDRUsersLanguage] = field(
        default=None, metadata=config(field_name="language")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserTrialInviteInput:
    """TDRUserTrialInviteInput."""

    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_id")
    )
    language: Optional[TDRUsersLanguage] = field(
        default=None, metadata=config(field_name="language")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUsersSearchInput:
    """TDRUsersSearchInput."""

    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    emails: Optional[List[str]] = field(
        default=None, metadata=config(field_name="emails")
    )
    role_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="role_IDs")
    )
    tenant_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tenant_IDs")
    )
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    tenant_status: Optional[str] = field(
        default=None, metadata=config(field_name="tenantStatus")
    )
    per_page: Optional[int] = field(default=None, metadata=config(field_name="perPage"))
    cursor_pos: Optional[str] = field(
        default=None, metadata=config(field_name="cursorPos")
    )
    page_offset: Optional[int] = field(
        default=None, metadata=config(field_name="pageOffset")
    )
    exclude_deactivated_role_assignments: Optional[bool] = field(
        default=None, metadata=config(field_name="excludeDeactivatedRoleAssignments")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    quick_lookup: Optional[str] = field(
        default=None, metadata=config(field_name="quickLookup")
    )
    omit_role_assignments: Optional[bool] = field(
        default=None, metadata=config(field_name="omitRoleAssignments")
    )
    sort_by: Optional[TDRUsersSearchSortBy] = field(
        default=None, metadata=config(field_name="sortBy")
    )
    sort_order: Optional[TDRUsersSearchSortOrder] = field(
        default=None, metadata=config(field_name="sortOrder")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserRegistrationInput:
    """UserRegistrationInput."""

    ticket_id: Optional[str] = field(
        default=None, metadata=config(field_name="ticket_id")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    password: Optional[str] = field(
        default=None, metadata=config(field_name="password")
    )
    given_name: Optional[str] = field(
        default=None, metadata=config(field_name="given_name")
    )
    family_name: Optional[str] = field(
        default=None, metadata=config(field_name="family_name")
    )
    phone_number: Optional[str] = field(
        default=None, metadata=config(field_name="phone_number")
    )
    phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="phone_extension")
    )
    timezone: Optional[str] = field(
        default=None, metadata=config(field_name="timezone")
    )
    is_sso_user: Optional[bool] = field(
        default=None, metadata=config(field_name="is_sso_user")
    )
    eula: Optional[EULAAcceptance] = field(
        default=None, metadata=config(field_name="eula")
    )
    preferred_language: Optional[TDRUsersLanguage] = field(
        default=None, metadata=config(field_name="preferred_language")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserInfoInput:
    """TDRUserInfoInput."""

    given_name: Optional[str] = field(
        default=None, metadata=config(field_name="given_name")
    )
    family_name: Optional[str] = field(
        default=None, metadata=config(field_name="family_name")
    )
    timezone: Optional[str] = field(
        default=None, metadata=config(field_name="timezone")
    )
    phone_number: Optional[str] = field(
        default=None, metadata=config(field_name="phone_number")
    )
    phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="phone_extension")
    )
    secondary_phone_number: Optional[str] = field(
        default=None, metadata=config(field_name="secondary_phone_number")
    )
    secondary_phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="secondary_phone_extension")
    )
    entitlement_channel: Optional[str] = field(
        default=None, metadata=config(field_name="entitlement_channel")
    )
    eula: Optional[EULAAcceptance] = field(
        default=None, metadata=config(field_name="eula")
    )
    preferred_language: Optional[TDRUsersLanguage] = field(
        default=None, metadata=config(field_name="preferred_language")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthorizeCheckResponse:
    """AuthorizeCheckResponse."""

    connection: Optional[AuthorizeCheckConnection] = field(
        default=None, metadata=config(field_name="connection")
    )
    role_assignments: Optional[List[TDRUserRoleAssignment]] = field(
        default=None, metadata=config(field_name="role_assignments")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserAccessibleTenant:
    """TDRUserAccessibleTenant."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    name_normalized: Optional[str] = field(
        default=None, metadata=config(field_name="name_normalized")
    )
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    allow_response_actions: Optional[bool] = field(
        default=None, metadata=config(field_name="allow_response_actions")
    )
    actions_approver: Optional[str] = field(
        default=None, metadata=config(field_name="actions_approver")
    )
    expires_at: Optional[str] = field(
        default=None, metadata=config(field_name="expires_at")
    )
    is_partner: Optional[bool] = field(
        default=None, metadata=config(field_name="is_partner")
    )
    parent: Optional[str] = field(default=None, metadata=config(field_name="parent"))
    environments: Optional[List[TDRUserTenantEnvironment]] = field(
        default=None, metadata=config(field_name="environments")
    )
    labels: Optional[List[TDRUserTenantLabel]] = field(
        default=None, metadata=config(field_name="labels")
    )
    services: Optional[List[TDRUserTenantService]] = field(
        default=None, metadata=config(field_name="services")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserUpdateInput:
    """TDRUserUpdateInput."""

    given_name: Optional[str] = field(
        default=None, metadata=config(field_name="given_name")
    )
    family_name: Optional[str] = field(
        default=None, metadata=config(field_name="family_name")
    )
    phone_number: Optional[str] = field(
        default=None, metadata=config(field_name="phone_number")
    )
    phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="phone_extension")
    )
    secondary_phone_number: Optional[str] = field(
        default=None, metadata=config(field_name="secondary_phone_number")
    )
    secondary_phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="secondary_phone_extension")
    )
    timezone: Optional[str] = field(
        default=None, metadata=config(field_name="timezone")
    )
    entitlement_channel: Optional[str] = field(
        default=None, metadata=config(field_name="entitlement_channel")
    )
    tenants: Optional[List[TDRUserTenantV2Input]] = field(
        default=None, metadata=config(field_name="tenants")
    )
    role_assignments: Optional[List[TDRUserRoleAssignmentInput]] = field(
        default=None, metadata=config(field_name="role_assignments")
    )
    eula: Optional[EULAAcceptance] = field(
        default=None, metadata=config(field_name="eula")
    )
    preferred_language: Optional[TDRUsersLanguage] = field(
        default=None, metadata=config(field_name="preferred_language")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUser:
    """TDRUser."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    id_uuid: Optional[str] = field(default=None, metadata=config(field_name="id_uuid"))
    user_id: Optional[str] = field(default=None, metadata=config(field_name="user_id"))
    user_id_v1: Optional[str] = field(
        default=None, metadata=config(field_name="user_id_v1")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    created_by: Optional[str] = field(
        default=None, metadata=config(field_name="created_by")
    )
    updated_by: Optional[str] = field(
        default=None, metadata=config(field_name="updated_by")
    )
    last_login: Optional[str] = field(
        default=None, metadata=config(field_name="last_login")
    )
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    status_localized: Optional[str] = field(
        default=None, metadata=config(field_name="status_localized")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    email_normalized: Optional[str] = field(
        default=None, metadata=config(field_name="email_normalized")
    )
    family_name: Optional[str] = field(
        default=None, metadata=config(field_name="family_name")
    )
    given_name: Optional[str] = field(
        default=None, metadata=config(field_name="given_name")
    )
    phone_number: Optional[str] = field(
        default=None, metadata=config(field_name="phone_number")
    )
    phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="phone_extension")
    )
    secondary_phone_number: Optional[str] = field(
        default=None, metadata=config(field_name="secondary_phone_number")
    )
    secondary_phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="secondary_phone_extension")
    )
    roles: Optional[List[str]] = field(
        default=None, metadata=config(field_name="roles")
    )
    environments: Optional[List[str]] = field(
        default=None, metadata=config(field_name="environments")
    )
    timezone: Optional[str] = field(
        default=None, metadata=config(field_name="timezone")
    )
    tenant_status: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_status")
    )
    tenant_status_localized: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_status_localized")
    )
    entitlement_channel: Optional[str] = field(
        default=None, metadata=config(field_name="entitlement_channel")
    )
    allowed_entitlement_channels: Optional[List[str]] = field(
        default=None, metadata=config(field_name="allowed_entitlement_channels")
    )
    masked: Optional[bool] = field(default=None, metadata=config(field_name="masked"))
    community_role: Optional[str] = field(
        default=None, metadata=config(field_name="community_role")
    )
    is_scwx: Optional[bool] = field(default=None, metadata=config(field_name="is_scwx"))
    is_partner: Optional[bool] = field(
        default=None, metadata=config(field_name="is_partner")
    )
    tenants: Optional[List[TDRUserTenant]] = field(
        default=None, metadata=config(field_name="tenants")
    )
    tenants_v2: Optional[List[TDRUserTenantV2]] = field(
        default=None, metadata=config(field_name="tenants_v2")
    )
    accessible_tenants: Optional[List[TDRUserAccessibleTenant]] = field(
        default=None, metadata=config(field_name="accessible_tenants")
    )
    role_assignments: Optional[List[TDRUserRoleAssignment]] = field(
        default=None, metadata=config(field_name="role_assignments")
    )
    eula: Optional[TDRUserLicense] = field(
        default=None, metadata=config(field_name="eula")
    )
    preferred_language: Optional[TDRUsersLanguage] = field(
        default=None, metadata=config(field_name="preferred_language")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUsersSearchResults:
    """TDRUsersSearchResults."""

    result_count: Optional[int] = field(
        default=None, metadata=config(field_name="result_count")
    )
    cursor_pos: Optional[str] = field(
        default=None, metadata=config(field_name="cursor_pos")
    )
    page_offset: Optional[int] = field(
        default=None, metadata=config(field_name="pageOffset")
    )
    has_next_page: Optional[bool] = field(
        default=None, metadata=config(field_name="has_next_page")
    )
    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="total_count")
    )
    results: Optional[List[TDRUser]] = field(
        default=None, metadata=config(field_name="results")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InviteUsersResponse:
    """InviteUsersResponse."""

    error: Optional[str] = field(default=None, metadata=config(field_name="error"))
    user: Optional[TDRUser] = field(default=None, metadata=config(field_name="user"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SearchByIDsResponse:
    """SearchByIDsResponse."""

    error: Optional[str] = field(default=None, metadata=config(field_name="error"))
    user: Optional[TDRUser] = field(default=None, metadata=config(field_name="user"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUserSupportPin:
    """TDRUserSupportPin."""

    code: Optional[str] = field(default=None, metadata=config(field_name="code"))
    user: Optional[TDRUser] = field(default=None, metadata=config(field_name="user"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PinValidation:
    """PinValidation."""

    successful: Optional[bool] = field(
        default=None, metadata=config(field_name="successful")
    )
    user: Optional[TDRUser] = field(default=None, metadata=config(field_name="user"))
