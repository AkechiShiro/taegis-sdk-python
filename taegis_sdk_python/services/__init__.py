"""
This needs to be a generated file.  Need to make jinja template.
"""
from typing import Optional, Dict
from taegis_sdk_python.authentication import get_token

from taegis_sdk_python._consts import TAEGIS_ENVIRONMENT_URLS
from taegis_sdk_python._version import __version__

from taegis_sdk_python.services.access_points import AccessPointsService
from taegis_sdk_python.services.agent import AgentService
from taegis_sdk_python.services.alerts import AlertsService
from taegis_sdk_python.services.assets import AssetsService
from taegis_sdk_python.services.assets2 import Assets2Service
from taegis_sdk_python.services.audits import AuditsService
from taegis_sdk_python.services.clients import ClientsService
from taegis_sdk_python.services.comments import CommentsService
from taegis_sdk_python.services.endpoint_command_manager import (
    EndpointCommandManagerService,
)
from taegis_sdk_python.services.endpoint_management_service import (
    EndpointManagementServiceService,
)
from taegis_sdk_python.services.event_search import EventSearchService
from taegis_sdk_python.services.events import EventsService
from taegis_sdk_python.services.exports import ExportsService
from taegis_sdk_python.services.investigations import InvestigationsService
from taegis_sdk_python.services.mitre_attack_info import MitreAttackInfoService
from taegis_sdk_python.services.notebooks import NotebooksService
from taegis_sdk_python.services.notifications import NotificationsService
from taegis_sdk_python.services.rules import RulesService
from taegis_sdk_python.services.sharelinks import SharelinksService
from taegis_sdk_python.services.tenants import TenantsService
from taegis_sdk_python.services.threat import ThreatService
from taegis_sdk_python.services.users import UsersService


__all__ = ["GraphQLService"]


class GraphQLService:
    """Taegis GraphQL Service manager."""

    def __init__(
        self,
        *,
        environment: Optional[str] = None,
        tenant_id: Optional[str] = None,
        environments: Optional[Dict[str, str]] = None,
        gateway: Optional[str] = None,
    ):
        """
        GraphQLService

        Parameters
        ----------
        environment : Optional[str], optional
            Taegis Cluster environment identifier.
        tenant_id : Optional[str], optional
            Tenant ID, by default None
        environments : Optional[Dict[str, str]], optional
            Environments dictionary {"identifier": "url"}
        gateway : Optional[str], optional
            Default Taegis Gateway, can be overwritten by service

        Raises
        ------
        ValueError
            environment must be charlie, delta, or echo
        """
        self._environments = environments or TAEGIS_ENVIRONMENT_URLS
        self._environment = environment or list(self._environments)[0]

        if self._environment not in self._environments:
            raise ValueError(f"environment must be in {self._environments.keys()}")

        self._tenant_id = tenant_id
        self._gateway = gateway or "/graphql"
        self._context_manager = {}

        self._access_points = None
        self._agent = None
        self._alerts = None
        self._assets = None
        self._assets2 = None
        self._audits = None
        self._clients = None
        self._comments = None
        self._endpoint_command_manager = None
        self._endpoint_management_service = None
        self._event_search = None
        self._events = None
        self._exports = None
        self._investigations = None
        self._mitre_attack_info = None
        self._notebooks = None
        self._notifications = None
        self._rules = None
        self._sharelinks = None
        self._tenants = None
        self._threat = None
        self._users = None

    def __call__(self, **kwargs):
        self._context_manager.update(kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._context_manager.clear()

    @property
    def environment(self):
        """Taegis Environment."""
        return self._context_manager.get("environment", self._environment)

    @property
    def url(self):
        """Taegis Environment URL."""
        return self._context_manager.get("url")

    @property
    def gateway(self):
        """Taegis GraphQL Gateway."""
        return self._context_manager.get("gateway")

    @property
    def tenant_id(self):
        """Taegis Tenant Context."""
        return self._context_manager.get("tenant_id", self._tenant_id)

    @property
    def access_token(self):
        """Taegis Access Token."""
        access_token = self._context_manager.get(
            "access_token",
        )
        if not access_token:
            access_token = get_token(
                environment=self.environment,
                request_url=self._environments.get(self.environment),
            )
        return access_token

    @property
    def output(self):
        """GraphQL Output."""
        return self._context_manager.get("output")

    @property
    def headers(self):
        """Taegis Headers."""
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": f"taegis_sdk_python/{__version__}",
            "apollographql-client-name": "taegis_sdk_python",
            "apollographql-client-version": __version__,
        }

        if self.tenant_id:
            headers["X-Tenant-Context"] = self.tenant_id

        return headers

    @property
    def access_points(self):
        """Access Points Service Endpoint."""
        if not self._access_points:
            self._access_points = AccessPointsService(self)
        return self._access_points

    @property
    def agent(self):
        """Agent Service Endpoint."""
        if not self._agent:
            self._agent = AgentService(self)
        return self._agent

    @property
    def alerts(self):
        """Alerts2 Service Endpoint."""
        if not self._alerts:
            self._alerts = AlertsService(self)
        return self._alerts

    @property
    def assets(self):
        """Assets Service Endpoint."""
        if not self._assets:
            self._assets = AssetsService(self)
        return self._assets

    @property
    def assets2(self):
        """Assets2 Service Endpoint."""
        if not self._assets2:
            self._assets2 = Assets2Service(self)
        return self._assets2

    @property
    def audits(self):
        """Audits Service Endpoint."""
        if not self._audits:
            self._audits = AuditsService(self)
        return self._audits

    @property
    def clients(self):
        """Clients Service Endpoint."""
        if not self._clients:
            self._clients = ClientsService(self)
        return self._clients

    @property
    def comments(self):
        """Comments Service Endpoint."""
        if not self._comments:
            self._comments = CommentsService(self)
        return self._comments

    @property
    def endpoint_command_manager(self):
        """Endpoint Command Manager Service Endpoint."""
        if not self._endpoint_command_manager:
            self._endpoint_command_manager = EndpointCommandManagerService(self)
        return self._endpoint_command_manager

    @property
    def endpoint_management_service(self):
        """Endpoint Management Service Endpoint."""
        if not self._endpoint_management_service:
            self._endpoint_management_service = EndpointManagementServiceService(self)
        return self._endpoint_management_service

    @property
    def event_search(self):
        """Events Search Service Endpoint."""
        if not self._event_search:
            self._event_search = EventSearchService(self)
        return self._event_search

    @property
    def events(self):
        """Events Service Endpoint."""
        if not self._events:
            self._events = EventsService(self)
        return self._events

    @property
    def exports(self):
        """Exports Service Endpoint."""
        if not self._exports:
            self._exports = ExportsService(self)
        return self._exports

    @property
    def investigations(self):
        """Investigations Service Endpoint."""
        if not self._investigations:
            self._investigations = InvestigationsService(self)
        return self._investigations

    @property
    def mitre_attack_info(self):
        """MitreAttackInfo Service Endpoint."""
        if not self._mitre_attack_info:
            self._mitre_attack_info = MitreAttackInfoService(self)
        return self._mitre_attack_info

    @property
    def notebooks(self):
        """Notebooks Service Endpoint."""
        if not self._notebooks:
            self._notebooks = NotebooksService(self)
        return self._notebooks

    @property
    def notifications(self):
        """Notifications Service Endpoint."""
        if not self._notifications:
            self._notifications = NotificationsService(self)
        return self._notifications

    @property
    def rules(self):
        """Rules Service Endpoint."""
        if not self._rules:
            self._rules = RulesService(self)
        return self._rules

    @property
    def sharelinks(self):
        """Sharelinks Service Endpoint."""
        if not self._sharelinks:
            self._sharelinks = SharelinksService(self)
        return self._sharelinks

    @property
    def tenants(self):
        """Tenants Service Endpoint."""
        if not self._tenants:
            self._tenants = TenantsService(self)
        return self._tenants

    @property
    def threat(self):
        """Threat Service Endpoint."""
        if not self._threat:
            self._threat = ThreatService(self)
        return self._threat

    @property
    def users(self):
        """Users Service Endpoint."""
        if not self._users:
            self._users = UsersService(self)
        return self._users
