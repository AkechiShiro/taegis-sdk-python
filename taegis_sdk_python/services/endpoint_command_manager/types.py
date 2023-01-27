"""EndpointCommandManager Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class FetchRequestPathTypeEnum(str, Enum):
    """FetchRequestPathTypeEnum."""

    FILE = "FILE"


class FetchRequestReasonCodeEnum(str, Enum):
    """FetchRequestReasonCodeEnum."""

    REASONCODE_UNSPECIFIED = "REASONCODE_UNSPECIFIED"
    POSSIBLY_MALICIOUS = "POSSIBLY_MALICIOUS"


class StatusEnum(str, Enum):
    """StatusEnum."""

    ISSUED = "ISSUED"
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    FAILED = "FAILED"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Result:
    """Result."""

    success: Optional[bool] = field(default=None, metadata=config(field_name="Success"))
    reason: Optional[str] = field(default=None, metadata=config(field_name="Reason"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CommandRequestInput:
    """CommandRequestInput."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )
    reason: Optional[str] = field(default=None, metadata=config(field_name="reason"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BlockUserCommandInput:
    """BlockUserCommandInput."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )
    reason: Optional[str] = field(default=None, metadata=config(field_name="reason"))
    user_principal_name: Optional[str] = field(
        default=None, metadata=config(field_name="userPrincipalName")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UninstallStateArguments:
    """UninstallStateArguments."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserInfo:
    """UserInfo."""

    family_name: Optional[str] = field(
        default=None, metadata=config(field_name="FamilyName")
    )
    given_name: Optional[str] = field(
        default=None, metadata=config(field_name="GivenName")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="Email"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CommandHistoryArguments:
    """CommandHistoryArguments."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CreateIsolationExclusionRuleArguments:
    """CreateIsolationExclusionRuleArguments."""

    name: Optional[str] = field(default=None, metadata=config(field_name="Name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="Description")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="Type"))
    values: Optional[List[str]] = field(
        default=None, metadata=config(field_name="Values")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateIsolationExclusionRuleArguments:
    """UpdateIsolationExclusionRuleArguments."""

    rule_id: Optional[str] = field(default=None, metadata=config(field_name="RuleID"))
    name: Optional[str] = field(default=None, metadata=config(field_name="Name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="Description")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="Type"))
    values: Optional[List[str]] = field(
        default=None, metadata=config(field_name="Values")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsolationExclusionRuleResult:
    """IsolationExclusionRuleResult."""

    rule_id: Optional[str] = field(default=None, metadata=config(field_name="RuleID"))
    success: Optional[bool] = field(default=None, metadata=config(field_name="Success"))
    reason: Optional[str] = field(default=None, metadata=config(field_name="Reason"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsolationExclusionRule:
    """IsolationExclusionRule."""

    name: Optional[str] = field(default=None, metadata=config(field_name="Name"))
    rule_id: Optional[str] = field(default=None, metadata=config(field_name="RuleID"))
    create_time: Optional[str] = field(
        default=None, metadata=config(field_name="CreateTime")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="Description")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="Type"))
    values: Optional[List[str]] = field(
        default=None, metadata=config(field_name="Values")
    )
    user_id: Optional[str] = field(default=None, metadata=config(field_name="UserID"))
    user: Optional[UserInfo] = field(default=None, metadata=config(field_name="User"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FetchRequestInput:
    """FetchRequestInput."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )
    reason: Optional[str] = field(default=None, metadata=config(field_name="reason"))
    path: Optional[str] = field(default=None, metadata=config(field_name="path"))
    path_type: Optional[FetchRequestPathTypeEnum] = field(
        default=None, metadata=config(field_name="pathType")
    )
    reason_code: Optional[FetchRequestReasonCodeEnum] = field(
        default=None, metadata=config(field_name="reasonCode")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class HistoryEntry:
    """HistoryEntry."""

    command: Optional[str] = field(default=None, metadata=config(field_name="Command"))
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="UpdatedAt")
    )
    issued_at: Optional[str] = field(
        default=None, metadata=config(field_name="IssuedAt")
    )
    response_at: Optional[str] = field(
        default=None, metadata=config(field_name="ResponseAt")
    )
    success: Optional[bool] = field(default=None, metadata=config(field_name="Success"))
    user_id: Optional[str] = field(default=None, metadata=config(field_name="UserID"))
    request_reason: Optional[str] = field(
        default=None, metadata=config(field_name="RequestReason")
    )
    failure_reason: Optional[str] = field(
        default=None, metadata=config(field_name="FailureReason")
    )
    status: Optional[StatusEnum] = field(
        default=None, metadata=config(field_name="Status")
    )
    user: Optional[UserInfo] = field(default=None, metadata=config(field_name="User"))
