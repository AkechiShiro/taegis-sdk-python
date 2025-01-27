"""Events Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class SearchTarget(str, Enum):
    """SearchTarget."""

    ATHENA = "Athena"
    PRESTO = "Presto"
    ATHENA_HUDI = "AthenaHudi"


class BaseType(str, Enum):
    """BaseType."""

    STRING = "String"
    NUMBER = "Number"
    BOOL = "Bool"
    TIMESTAMP_SECONDS = "TimestampSeconds"
    TIMESTAMP_MILLISECONDS = "TimestampMilliseconds"
    TIMESTAMP_MICROSECONDS = "TimestampMicroseconds"
    TIMESTAMP_ISO8601 = "TimestampIso8601"
    BYTES = "Bytes"
    STRUCT = "Struct"
    ENUM = "Enum"
    STRING_LIST = "StringList"
    NUMBER_LIST = "NumberList"
    BOOL_LIST = "BoolList"
    TIMESTAMP_SECONDS_LIST = "TimestampSecondsList"
    TIMESTAMP_MILLISECONDS_LIST = "TimestampMillisecondsList"
    TIMESTAMP_MICROSECONDS_LIST = "TimestampMicrosecondsList"
    TIMESTAMP_ISO8601_LIST = "TimestampIso8601List"
    BYTES_LIST = "BytesList"
    STRUCT_LIST = "StructList"
    ENUM_LIST = "EnumList"
    STRING_MAP = "StringMap"
    NUMBER_MAP = "NumberMap"
    BOOL_MAP = "BoolMap"
    TIMESTAMP_SECONDS_MAP = "TimestampSecondsMap"
    TIMESTAMP_MILLISECONDS_MAP = "TimestampMillisecondsMap"
    TIMESTAMP_MICROSECONDS_MAP = "TimestampMicrosecondsMap"
    TIMESTAMP_ISO8601_MAP = "TimestampIso8601Map"
    BYTES_MAP = "BytesMap"
    STRUCT_MAP = "StructMap"
    ENUM_MAP = "EnumMap"


class LogicalType(str, Enum):
    """LogicalType."""

    COMMAND = "Command"
    HASH = "Hash"
    DOMAIN = "Domain"
    HOST = "Host"
    IP = "IP"
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"
    MAC = "MAC"
    PATH = "Path"
    PORT = "Port"
    RAW = "Raw"
    USER = "User"
    URL = "URL"
    UUID = "UUID"
    SENSOR_ID = "SensorId"
    TIMESTAMP = "Timestamp"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Event:
    """Event."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    values: Optional[dict] = field(default=None, metadata=config(field_name="values"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventUser:
    """EventUser."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    role: Optional[str] = field(default=None, metadata=config(field_name="role"))
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    user_id: Optional[str] = field(default=None, metadata=config(field_name="userID"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventQueryProgress:
    """EventQueryProgress."""

    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    total_rows: Optional[int] = field(
        default=None, metadata=config(field_name="totalRows")
    )
    total_rows_is_lower_bound: Optional[bool] = field(
        default=None, metadata=config(field_name="totalRowsIsLowerBound")
    )
    rows_removed: Optional[int] = field(
        default=None, metadata=config(field_name="rowsRemoved")
    )
    rows_filtered: Optional[int] = field(
        default=None, metadata=config(field_name="rowsFiltered")
    )
    results_truncated: Optional[bool] = field(
        default=None, metadata=config(field_name="resultsTruncated")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventFetchOptions:
    """EventFetchOptions."""

    include_alerts_data: Optional[bool] = field(
        default=None, metadata=config(field_name="includeAlertsData")
    )
    include_mitre_attack_info_data: Optional[bool] = field(
        default=None, metadata=config(field_name="includeMitreAttackInfoData")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventQueryOptions:
    """EventQueryOptions."""

    timestamp_ascending: Optional[bool] = field(
        default=None, metadata=config(field_name="timestampAscending")
    )
    page_size: Optional[int] = field(
        default=None, metadata=config(field_name="pageSize")
    )
    max_rows: Optional[int] = field(default=None, metadata=config(field_name="maxRows"))
    skip_cache: Optional[bool] = field(
        default=None, metadata=config(field_name="skipCache")
    )
    aggregation_off: Optional[bool] = field(
        default=None, metadata=config(field_name="aggregationOff")
    )
    include_alerts_data: Optional[bool] = field(
        default=None, metadata=config(field_name="includeAlertsData")
    )
    include_mitre_attack_info_data: Optional[bool] = field(
        default=None, metadata=config(field_name="includeMitreAttackInfoData")
    )
    save_to_cache: Optional[bool] = field(
        default=None, metadata=config(field_name="saveToCache")
    )
    search_target: Optional[SearchTarget] = field(
        default=None, metadata=config(field_name="searchTarget")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Field:
    """Field."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    searchable: Optional[bool] = field(
        default=None, metadata=config(field_name="searchable")
    )
    debug: Optional[bool] = field(default=None, metadata=config(field_name="debug"))
    base_type: Optional[BaseType] = field(
        default=None, metadata=config(field_name="baseType")
    )
    logical_type: Optional[LogicalType] = field(
        default=None, metadata=config(field_name="logicalType")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventQueryResult:
    """EventQueryResult."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    reason: Optional[str] = field(default=None, metadata=config(field_name="reason"))
    submitted: Optional[str] = field(
        default=None, metadata=config(field_name="submitted")
    )
    completed: Optional[str] = field(
        default=None, metadata=config(field_name="completed")
    )
    expires: Optional[str] = field(default=None, metadata=config(field_name="expires"))
    backend: Optional[str] = field(default=None, metadata=config(field_name="backend"))
    facets: Optional[dict] = field(default=None, metadata=config(field_name="facets"))
    rows: Optional[List[dict]] = field(default=None, metadata=config(field_name="rows"))
    progress: Optional[EventQueryProgress] = field(
        default=None, metadata=config(field_name="progress")
    )
    fields: Optional[List[Field]] = field(
        default=None, metadata=config(field_name="fields")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventQuery:
    """EventQuery."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    types: Optional[List[str]] = field(
        default=None, metadata=config(field_name="types")
    )
    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    submitted: Optional[str] = field(
        default=None, metadata=config(field_name="submitted")
    )
    expires: Optional[str] = field(default=None, metadata=config(field_name="expires"))
    completed: Optional[str] = field(
        default=None, metadata=config(field_name="completed")
    )
    earliest: Optional[str] = field(
        default=None, metadata=config(field_name="earliest")
    )
    latest: Optional[str] = field(default=None, metadata=config(field_name="latest"))
    aggregated: Optional[bool] = field(
        default=None, metadata=config(field_name="aggregated")
    )
    metadata: Optional[dict] = field(
        default=None, metadata=config(field_name="metadata")
    )
    reasons: Optional[List[EventQueryResult]] = field(
        default=None, metadata=config(field_name="reasons")
    )
    progress: Optional[List[EventQueryProgress]] = field(
        default=None, metadata=config(field_name="progress")
    )
    user: Optional[EventUser] = field(default=None, metadata=config(field_name="user"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventQueryResults:
    """EventQueryResults."""

    next: Optional[str] = field(default=None, metadata=config(field_name="next"))
    prev: Optional[str] = field(default=None, metadata=config(field_name="prev"))
    query: Optional[EventQuery] = field(
        default=None, metadata=config(field_name="query")
    )
    result: Optional[EventQueryResult] = field(
        default=None, metadata=config(field_name="result")
    )
