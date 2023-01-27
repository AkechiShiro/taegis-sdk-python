""""MitreAttackInfo Query."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import build_output_string, prepare_input
from taegis_sdk_python.services.mitre_attack_info.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.mitre_attack_info import MitreAttackInfoService


class TaegisSDKMitreAttackInfoQuery:
    """Teagis Mitre_attack_info Query operations."""

    def __init__(self, service: MitreAttackInfoService):
        self.service = service

    def get_mitre_attack_info_by_technique_name(
        self, in_: Optional[str] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByTechniqueName"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError(
            "for query getMitreAttackInfoByTechniqueName"
        )

    def get_mitre_attack_info_by_technique_names(
        self, in_: Optional[Ids] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByTechniqueNames"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError(
            "for query getMitreAttackInfoByTechniqueNames"
        )

    def get_mitre_attack_info_by_technique_id(
        self, in_: Optional[str] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByTechniqueId"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query getMitreAttackInfoByTechniqueId")

    def get_mitre_attack_info_by_technique_ids(
        self, in_: Optional[Ids] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByTechniqueIds"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError(
            "for query getMitreAttackInfoByTechniqueIds"
        )

    def get_mitre_attack_info_by_data_source(
        self, in_: Optional[str] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByDataSource"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query getMitreAttackInfoByDataSource")

    def get_mitre_attack_info_by_data_sources(
        self, in_: Optional[Ids] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByDataSources"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query getMitreAttackInfoByDataSources")

    def get_mitre_attack_info_by_type(
        self, in_: Optional[str] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByType"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query getMitreAttackInfoByType")

    def get_mitre_attack_info_by_types(
        self, in_: Optional[Ids] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByTypes"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query getMitreAttackInfoByTypes")

    def get_mitre_attack_info_by_contributor(
        self, in_: Optional[str] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByContributor"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query getMitreAttackInfoByContributor")

    def get_mitre_attack_info_by_contributors(
        self, in_: Optional[Ids] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getMitreAttackInfoByContributors"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError(
            "for query getMitreAttackInfoByContributors"
        )

    def get_all_mitre_attack_info(self) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "getAllMitreAttackInfo"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query getAllMitreAttackInfo")

    def search_mitre_info_by_regex_pattern(
        self, in_: Optional[SearchMitreAttackInput] = None
    ) -> List[MitreAttackInformation]:
        """None."""
        endpoint = "searchMitreInfoByRegexPattern"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(MitreAttackInformation),
        )
        if result is not None:
            return MitreAttackInformation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query searchMitreInfoByRegexPattern")
