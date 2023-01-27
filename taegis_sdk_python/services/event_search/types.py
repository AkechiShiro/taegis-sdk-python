"""EventSearch Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuxiliaryEventsSearchInput:
    """AuxiliaryEventsSearchInput."""

    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    limit: Optional[int] = field(default=None, metadata=config(field_name="limit"))
    offset: Optional[int] = field(default=None, metadata=config(field_name="offset"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AsynchronousEventsSearchPrepInput:
    """AsynchronousEventsSearchPrepInput."""

    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    limit: Optional[int] = field(default=None, metadata=config(field_name="limit"))
    job_id: Optional[str] = field(default=None, metadata=config(field_name="jobId"))
    table_name: Optional[str] = field(
        default=None, metadata=config(field_name="tableName")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class GetEventByIDRequestInput:
    """GetEventByIDRequestInput."""

    ids: Optional[List[str]] = field(default=None, metadata=config(field_name="ids"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AsynchronousEventsSearchPrepInputResponse:
    """AsynchronousEventsSearchPrepInputResponse."""

    job_id: Optional[str] = field(default=None, metadata=config(field_name="jobId"))
    successful: Optional[bool] = field(
        default=None, metadata=config(field_name="successful")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Alerts2:
    """Alerts2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Observation:
    """Observation."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Investigation:
    """Investigation."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuxiliaryEvent:
    """AuxiliaryEvent."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    event_data: Optional[dict] = field(
        default=None, metadata=config(field_name="event_data")
    )
    observation_ids: Optional[List[Observation]] = field(
        default=None, metadata=config(field_name="observation_ids")
    )
    investigations_resource_id: Optional[List[Investigation]] = field(
        default=None, metadata=config(field_name="investigations_resource_id")
    )
    alerts_resource_id: Optional[List[Alerts2]] = field(
        default=None, metadata=config(field_name="alerts_resource_id")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuxiliaryEventsSearchResponse:
    """AuxiliaryEventsSearchResponse."""

    total_hits: Optional[int] = field(
        default=None, metadata=config(field_name="total_hits")
    )
    events: Optional[List[AuxiliaryEvent]] = field(
        default=None, metadata=config(field_name="events")
    )
