"""AccessPoints Query."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import build_output_string, prepare_input
from taegis_sdk_python.services.access_points.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.access_points import AccessPointsService


class TaegisSDKAccessPointsQuery:
    """Teagis Access_points Query operations."""

    def __init__(self, service: AccessPointsService):
        self.service = service

    def get_access_point(self) -> AccessPoint:
        """None."""
        endpoint = "getAccessPoint"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AccessPoint)
        )
        if result.get(endpoint) is not None:
            return AccessPoint.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getAccessPoint")

    def get_access_point_template(self) -> AccessPointCloudFormation:
        """None."""
        endpoint = "getAccessPointTemplate"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(AccessPointCloudFormation),
        )
        if result.get(endpoint) is not None:
            return AccessPointCloudFormation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getAccessPointTemplate")