""""EventSearch Mutation."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import build_output_string, prepare_input
from taegis_sdk_python.services.event_search.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.event_search import EventSearchService


class TaegisSDKEventSearchMutation:
    """Teagis Event_search Mutation operations."""

    def __init__(self, service: EventSearchService):
        self.service = service

    def asynchronous_events_search_prep(
        self, in_: Optional[AsynchronousEventsSearchPrepInput] = None
    ) -> AsynchronousEventsSearchPrepInputResponse:
        """None."""
        endpoint = "AsynchronousEventsSearchPrep"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AsynchronousEventsSearchPrepInputResponse),
        )
        if result is not None:
            return AsynchronousEventsSearchPrepInputResponse.from_dict(
                result.get(endpoint)
            )
        raise GraphQLNoRowsInResultSetError("for mutation AsynchronousEventsSearchPrep")