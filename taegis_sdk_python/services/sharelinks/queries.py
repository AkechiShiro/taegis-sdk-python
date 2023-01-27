""""Sharelinks Query."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import build_output_string, prepare_input
from taegis_sdk_python.services.sharelinks.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.sharelinks import SharelinksService


class TaegisSDKSharelinksQuery:
    """Teagis Sharelinks Query operations."""

    def __init__(self, service: SharelinksService):
        self.service = service

    def share_link_by_id(self, id_: str) -> ShareLink:
        """Fetch a ShareLink by ID."""
        endpoint = "shareLinkById"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(ShareLink),
        )
        if result is not None:
            return ShareLink.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query shareLinkById")
