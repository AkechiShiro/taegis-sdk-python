"""Assets2 Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class AssetState(str, Enum):
    """AssetState."""

    ALL = "All"
    ARCHIVED = "Archived"
    ACTIVE = "Active"
    UNHEALTHY = "Unhealthy"


class EndpointTypeV2(str, Enum):
    """EndpointTypeV2."""

    ENDPOINT_REDCLOAK = "ENDPOINT_REDCLOAK"
    ENDPOINT_TAEGIS = "ENDPOINT_TAEGIS"
    ENDPOINT_CROWD_STRIKE = "ENDPOINT_CROWD_STRIKE"
    ENDPOINT_CARBON_BLACK_PSC = "ENDPOINT_CARBON_BLACK_PSC"
    ENDPOINT_MICROSOFT_ATP = "ENDPOINT_MICROSOFT_ATP"
    ENDPOINT_SENTINELONE = "ENDPOINT_SENTINELONE"


class FacetInfoOrderByInputV2(str, Enum):
    """FacetInfoOrderByInputV2."""

    COUNT_DESC = "count_desc"
    COUNT_ASC = "count_asc"


class AssetSearchOrderByInputV2(str, Enum):
    """AssetSearchOrderByInputV2."""

    OS_VERSION_ASC = "os_version_asc"
    OS_VERSION_DESC = "os_version_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    OS_FAMILY_ASC = "os_family_asc"
    OS_FAMILY_DESC = "os_family_desc"
    OS_DISTRIBUTOR_ASC = "os_distributor_asc"
    OS_DISTRIBUTOR_DESC = "os_distributor_desc"
    SENSOR_VERSION_ASC = "sensor_version_asc"
    SENSOR_VERSION_DESC = "sensor_version_desc"
    HOSTNAME_ASC = "hostname_asc"
    HOSTNAME_DESC = "hostname_desc"
    CONNECTION_STATUS_ASC = "connection_status_asc"
    CONNECTION_STATUS_DESC = "connection_status_desc"
    ISOLATION_STATUS_ASC = "isolation_status_asc"
    ISOLATION_STATUS_DESC = "isolation_status_desc"
    IP_ADDRESS_ASC = "ip_address_asc"
    IP_ADDRESS_DESC = "ip_address_desc"
    ENDPOINT_TYPE_ASC = "endpoint_type_asc"
    ENDPOINT_TYPE_DESC = "endpoint_type_desc"
    LAST_SEEN_ASC = "last_seen_asc"
    LAST_SEEN_DESC = "last_seen_desc"
    ETHERNET_ADDRESSES_ASC = "ethernet_addresses_asc"
    ETHERNET_ADDRESSES_DESC = "ethernet_addresses_desc"
    SYSTEM_TYPE_ASC = "system_type_asc"
    SYSTEM_TYPE_DESC = "system_type_desc"
    GROUP_ASC = "group_asc"
    GROUP_DESC = "group_desc"
    TAG_KEY_ASC = "tag_key_asc"
    TAG_KEY_DESC = "tag_key_desc"
    TAG_VALUE_ASC = "tag_value_asc"
    TAG_VALUE_DESC = "tag_value_desc"


class BulkOpStatusV2(str, Enum):
    """BulkOpStatusV2."""

    TASK_STATE_PENDING = "TASK_STATE_PENDING"
    TASK_STATE_FAILED = "TASK_STATE_FAILED"
    TASK_STATE_COMPLETED = "TASK_STATE_COMPLETED"
    TASK_STATE_IN_PROGRESS = "TASK_STATE_IN_PROGRESS"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EndpointGroupV2:
    """EndpointGroupV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class HostnameV2:
    """HostnameV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))
    hostname: Optional[str] = field(
        default=None, metadata=config(field_name="hostname")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EthernetAddressV2:
    """EthernetAddressV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))
    mac: Optional[str] = field(default=None, metadata=config(field_name="mac"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IpAddressV2:
    """IpAddressV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserV2:
    """UserV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))
    username: Optional[str] = field(
        default=None, metadata=config(field_name="username")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TagV2:
    """TagV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    tag: Optional[str] = field(default=None, metadata=config(field_name="tag"))
    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Investigation:
    """Investigation."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FacetV2:
    """FacetV2."""

    label: Optional[str] = field(default=None, metadata=config(field_name="label"))
    facet: Optional[str] = field(default=None, metadata=config(field_name="facet"))
    search_only: Optional[bool] = field(
        default=None, metadata=config(field_name="searchOnly")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FacetFieldInfoV2:
    """FacetFieldInfoV2."""

    field_: Optional[str] = field(default=None, metadata=config(field_name="field"))
    count: Optional[int] = field(default=None, metadata=config(field_name="count"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TagWhereInputV2:
    """TagWhereInputV2."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    key_contains: Optional[str] = field(
        default=None, metadata=config(field_name="key_contains")
    )
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    value_contains: Optional[str] = field(
        default=None, metadata=config(field_name="value_contains")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PageInfoV2:
    """PageInfoV2."""

    end_cursor: Optional[str] = field(
        default=None, metadata=config(field_name="endCursor")
    )
    start_cursor: Optional[str] = field(
        default=None, metadata=config(field_name="startCursor")
    )
    has_next_page: Optional[bool] = field(
        default=None, metadata=config(field_name="hasNextPage")
    )
    has_previous_page: Optional[bool] = field(
        default=None, metadata=config(field_name="hasPreviousPage")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class KVTagInputV2:
    """KVTagInputV2."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TaskInfoMetadata:
    """TaskInfoMetadata."""

    num_endpoints: Optional[int] = field(
        default=None, metadata=config(field_name="numEndpoints")
    )
    num_succeeded: Optional[int] = field(
        default=None, metadata=config(field_name="numSucceeded")
    )
    num_failed: Optional[int] = field(
        default=None, metadata=config(field_name="numFailed")
    )
    sync_succeeded: Optional[bool] = field(
        default=None, metadata=config(field_name="syncSucceeded")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FacetInfoV2:
    """FacetInfoV2."""

    facet: Optional[str] = field(default=None, metadata=config(field_name="facet"))
    fields: Optional[List[FacetFieldInfoV2]] = field(
        default=None, metadata=config(field_name="fields")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateTagsForEndpointInputV2:
    """UpdateTagsForEndpointInputV2."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointId")
    )
    tags: Optional[List[KVTagInputV2]] = field(
        default=None, metadata=config(field_name="tags")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BulkOpPayloadV2:
    """BulkOpPayloadV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    status: Optional[BulkOpStatusV2] = field(
        default=None, metadata=config(field_name="status")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AssetsExportOutputV2:
    """AssetsExportOutputV2."""

    column_def: Optional[List[str]] = field(
        default=None, metadata=config(field_name="columnDef")
    )
    rows: Optional[List[List[str]]] = field(
        default=None, metadata=config(field_name="rows")
    )
    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    page_info: Optional[PageInfoV2] = field(
        default=None, metadata=config(field_name="pageInfo")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TagFilter:
    """TagFilter."""

    endpoint_types: Optional[List[EndpointTypeV2]] = field(
        default=None, metadata=config(field_name="endpointTypes")
    )
    where: Optional[TagWhereInputV2] = field(
        default=None, metadata=config(field_name="where")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TaskInfoPayload:
    """TaskInfoPayload."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    status: Optional[BulkOpStatusV2] = field(
        default=None, metadata=config(field_name="status")
    )
    metadata: Optional[TaskInfoMetadata] = field(
        default=None, metadata=config(field_name="metadata")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AssetWhereInputV2:
    """AssetWhereInputV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    connection_status: Optional[str] = field(
        default=None, metadata=config(field_name="connectionStatus")
    )
    group_name: Optional[str] = field(
        default=None, metadata=config(field_name="groupName")
    )
    group_name_contains: Optional[str] = field(
        default=None, metadata=config(field_name="groupName_contains")
    )
    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))
    host_id_contains: Optional[str] = field(
        default=None, metadata=config(field_name="hostId_contains")
    )
    hostname: Optional[str] = field(
        default=None, metadata=config(field_name="hostname")
    )
    hostname_contains: Optional[str] = field(
        default=None, metadata=config(field_name="hostname_contains")
    )
    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigationId")
    )
    investigation_id_contains: Optional[str] = field(
        default=None, metadata=config(field_name="investigationId_contains")
    )
    ip_address: Optional[str] = field(
        default=None, metadata=config(field_name="ipAddress")
    )
    ip_address_contains: Optional[str] = field(
        default=None, metadata=config(field_name="ipAddress_contains")
    )
    isolation_status: Optional[str] = field(
        default=None, metadata=config(field_name="isolationStatus")
    )
    mac_address: Optional[str] = field(
        default=None, metadata=config(field_name="macAddress")
    )
    mac_address_contains: Optional[str] = field(
        default=None, metadata=config(field_name="macAddress_contains")
    )
    os_distributor: Optional[str] = field(
        default=None, metadata=config(field_name="osDistributor")
    )
    os_family: Optional[str] = field(
        default=None, metadata=config(field_name="osFamily")
    )
    os_version: Optional[str] = field(
        default=None, metadata=config(field_name="osVersion")
    )
    sensor_version: Optional[str] = field(
        default=None, metadata=config(field_name="sensorVersion")
    )
    system_type: Optional[str] = field(
        default=None, metadata=config(field_name="systemType")
    )
    username: Optional[str] = field(
        default=None, metadata=config(field_name="username")
    )
    username_contains: Optional[str] = field(
        default=None, metadata=config(field_name="username_contains")
    )
    and_: Optional[List["AssetWhereInputV2"]] = field(
        default=None, metadata=config(field_name="and")
    )
    or_: Optional[List["AssetWhereInputV2"]] = field(
        default=None, metadata=config(field_name="or")
    )
    not_: Optional["AssetWhereInputV2"] = field(
        default=None, metadata=config(field_name="not")
    )
    tags: Optional[TagWhereInputV2] = field(
        default=None, metadata=config(field_name="tags")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AssetV2:
    """AssetV2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))
    rn: Optional[str] = field(default=None, metadata=config(field_name="rn"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    sensor_tenant: Optional[str] = field(
        default=None, metadata=config(field_name="sensorTenant")
    )
    sensor_id: Optional[str] = field(
        default=None, metadata=config(field_name="sensorId")
    )
    ingest_time: Optional[str] = field(
        default=None, metadata=config(field_name="ingestTime")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    deleted_at: Optional[str] = field(
        default=None, metadata=config(field_name="deletedAt")
    )
    last_seen_at: Optional[str] = field(
        default=None, metadata=config(field_name="lastSeenAt")
    )
    bios_serial: Optional[str] = field(
        default=None, metadata=config(field_name="biosSerial")
    )
    first_disk_serial: Optional[str] = field(
        default=None, metadata=config(field_name="firstDiskSerial")
    )
    system_volume_serial: Optional[str] = field(
        default=None, metadata=config(field_name="systemVolumeSerial")
    )
    sensor_version: Optional[str] = field(
        default=None, metadata=config(field_name="sensorVersion")
    )
    endpoint_type: Optional[str] = field(
        default=None, metadata=config(field_name="endpointType")
    )
    endpoint_platform: Optional[str] = field(
        default=None, metadata=config(field_name="endpointPlatform")
    )
    architecture: Optional[str] = field(
        default=None, metadata=config(field_name="architecture")
    )
    os_family: Optional[str] = field(
        default=None, metadata=config(field_name="osFamily")
    )
    os_version: Optional[str] = field(
        default=None, metadata=config(field_name="osVersion")
    )
    os_distributor: Optional[str] = field(
        default=None, metadata=config(field_name="osDistributor")
    )
    os_release: Optional[str] = field(
        default=None, metadata=config(field_name="osRelease")
    )
    system_type: Optional[str] = field(
        default=None, metadata=config(field_name="systemType")
    )
    os_codename: Optional[str] = field(
        default=None, metadata=config(field_name="osCodename")
    )
    kernel_release: Optional[str] = field(
        default=None, metadata=config(field_name="kernelRelease")
    )
    kernel_version: Optional[str] = field(
        default=None, metadata=config(field_name="kernelVersion")
    )
    connection_status: Optional[str] = field(
        default=None, metadata=config(field_name="connectionStatus")
    )
    isolation_status: Optional[str] = field(
        default=None, metadata=config(field_name="isolationStatus")
    )
    model: Optional[str] = field(default=None, metadata=config(field_name="model"))
    cloud_provider_name: Optional[str] = field(
        default=None, metadata=config(field_name="cloudProviderName")
    )
    cloud_instance_id: Optional[str] = field(
        default=None, metadata=config(field_name="cloudInstanceId")
    )
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    hostnames: Optional[List[HostnameV2]] = field(
        default=None, metadata=config(field_name="hostnames")
    )
    ethernet_addresses: Optional[List[EthernetAddressV2]] = field(
        default=None, metadata=config(field_name="ethernetAddresses")
    )
    ip_addresses: Optional[List[IpAddressV2]] = field(
        default=None, metadata=config(field_name="ipAddresses")
    )
    users: Optional[List[UserV2]] = field(
        default=None, metadata=config(field_name="users")
    )
    tags: Optional[List[TagV2]] = field(
        default=None, metadata=config(field_name="tags")
    )
    endpoint_group: Optional[EndpointGroupV2] = field(
        default=None, metadata=config(field_name="endpointGroup")
    )
    investigations: Optional[List[Investigation]] = field(
        default=None, metadata=config(field_name="investigations")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AssetsV2:
    """AssetsV2."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    assets: Optional[List[AssetV2]] = field(
        default=None, metadata=config(field_name="assets")
    )
    page_info: Optional[PageInfoV2] = field(
        default=None, metadata=config(field_name="pageInfo")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AssetFilter:
    """AssetFilter."""

    endpoint_types: Optional[List[EndpointTypeV2]] = field(
        default=None, metadata=config(field_name="endpointTypes")
    )
    asset_state: Optional[List[AssetState]] = field(
        default=None, metadata=config(field_name="assetState")
    )
    where: Optional[AssetWhereInputV2] = field(
        default=None, metadata=config(field_name="where")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BulkDeleteTagsForEndpointsInputV2:
    """BulkDeleteTagsForEndpointsInputV2."""

    tag_keys: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tagKeys")
    )
    filter: Optional[AssetFilter] = field(
        default=None, metadata=config(field_name="filter")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DeleteAssetsInputV2:
    """DeleteAssetsInputV2."""

    filter: Optional[AssetFilter] = field(
        default=None, metadata=config(field_name="filter")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RestoreAssetsInputV2:
    """RestoreAssetsInputV2."""

    filter: Optional[AssetFilter] = field(
        default=None, metadata=config(field_name="filter")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AssignBulkAssetsToGroupInput:
    """AssignBulkAssetsToGroupInput."""

    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))
    filter: Optional[AssetFilter] = field(
        default=None, metadata=config(field_name="filter")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AssignBulkAssetsToInvestigationInput:
    """AssignBulkAssetsToInvestigationInput."""

    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigationId")
    )
    filter: Optional[AssetFilter] = field(
        default=None, metadata=config(field_name="filter")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BulkDeleteInvestigationForEndpointsInput:
    """BulkDeleteInvestigationForEndpointsInput."""

    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigationId")
    )
    filter: Optional[AssetFilter] = field(
        default=None, metadata=config(field_name="filter")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BulkUpdateTagsForEndpointsInputV2:
    """BulkUpdateTagsForEndpointsInputV2."""

    filter: Optional[AssetFilter] = field(
        default=None, metadata=config(field_name="filter")
    )
    tags: Optional[List[KVTagInputV2]] = field(
        default=None, metadata=config(field_name="tags")
    )
