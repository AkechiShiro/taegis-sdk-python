"""EndpointCommandManager Mutation."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import build_output_string, prepare_input
from taegis_sdk_python.services.endpoint_command_manager.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.endpoint_command_manager import (
        EndpointCommandManagerService,
    )


class TaegisSDKEndpointCommandManagerMutation:
    """Teagis Endpoint_command_manager Mutation operations."""

    def __init__(self, service: EndpointCommandManagerService):
        self.service = service

    def create_isolation_exclusion_rule(
        self, input_: CreateIsolationExclusionRuleArguments
    ) -> IsolationExclusionRuleResult:
        """None."""
        endpoint = "createIsolationExclusionRule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(IsolationExclusionRuleResult),
        )
        if result.get(endpoint) is not None:
            return IsolationExclusionRuleResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createIsolationExclusionRule")

    def update_isolation_exclusion_rule(
        self, input_: UpdateIsolationExclusionRuleArguments
    ) -> IsolationExclusionRuleResult:
        """None."""
        endpoint = "updateIsolationExclusionRule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(IsolationExclusionRuleResult),
        )
        if result.get(endpoint) is not None:
            return IsolationExclusionRuleResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateIsolationExclusionRule")

    def delete_isolation_exclusion_rule(self, rule_id: str) -> Result:
        """None."""
        endpoint = "deleteIsolationExclusionRule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "RuleID": prepare_input(rule_id),
            },
            output=build_output_string(Result),
        )
        if result.get(endpoint) is not None:
            return Result.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteIsolationExclusionRule")

    def request_resource_from_endpoint(self, input_: FetchRequestInput) -> Result:
        """Send a request to endpoint of it to upload a resource from the endpoint: currently only a file but could be a
        directory or memory dump or something else."""
        endpoint = "requestResourceFromEndpoint"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Result),
        )
        if result.get(endpoint) is not None:
            return Result.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation requestResourceFromEndpoint")

    def send_reconnect(self, input_: CommandRequestInput) -> Result:
        """None."""
        endpoint = "sendReconnect"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Result),
        )
        if result.get(endpoint) is not None:
            return Result.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation sendReconnect")

    def send_isolate(self, input_: CommandRequestInput) -> Result:
        """None."""
        endpoint = "sendIsolate"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Result),
        )
        if result.get(endpoint) is not None:
            return Result.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation sendIsolate")

    def send_de_isolate(self, input_: CommandRequestInput) -> Result:
        """None."""
        endpoint = "sendDeIsolate"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Result),
        )
        if result.get(endpoint) is not None:
            return Result.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation sendDeIsolate")

    def mark_for_uninstall(self, input_: CommandRequestInput) -> Result:
        """None."""
        endpoint = "markForUninstall"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Result),
        )
        if result.get(endpoint) is not None:
            return Result.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation markForUninstall")

    def send_block_user(self, input_: BlockUserCommandInput) -> Result:
        """None."""
        endpoint = "sendBlockUser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Result),
        )
        if result.get(endpoint) is not None:
            return Result.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation sendBlockUser")

    def send_unblock_user(self, input_: BlockUserCommandInput) -> Result:
        """None."""
        endpoint = "sendUnblockUser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Result),
        )
        if result.get(endpoint) is not None:
            return Result.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation sendUnblockUser")
