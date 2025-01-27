# Taegis SDK for Python

The Taegis SDK is a Python library for interfacing with the GraphQL APIs in Taegis.

## Getting Started

### Installation

```bash
pip install taegis_sdk_python
```

### Example Usage

```python
from taegis_sdk_python import GraphQLService

from pprint import pprint as pp

service = GraphQLService()

results = service.users.query.current_tdruser()

pp(results)
```

## Exploring the SDK

The SDK was built around utilizing the Python built-in: `help`.  You can use help on any object
within the `GraphQLService` object structure to understand what is available and how to call it.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import SearchRequestInput

service = GraphQLService()

# Find available services (Service Endpoints)
help(service)
# Find available service queries (or mutations or subscriptions)
help(service.alerts.query)
help(service.alerts.mutation)
help(service.alerts.subscription)
# Reference documentation on specific endpoint
help(service.alerts.query.alerts_service_search)
# Help on an Input variable
help(SearchRequestInput)
```

```
# service
class GraphQLService(builtins.object)
 |  GraphQLService(*, environment: Optional[str] = None, tenant_id: Optional[str] = None, environments: Optional[Dict[str, str]] = None, gateway: Optional[str] = None)
...
 |  agent
 |      Events Service Endpoint.
 |
 |  alerts
 |      Alerts2 Service Endpoint.
 |
 |  assets
 |      Assets
...
# Alerts Query
class TaegisSDKAlertsQuery(builtins.object)
 |  TaegisS
...
 |  alerts_service_aggregate_alerts_by_severity(self, in_: 'Optional[AggregateAlertsBySeverityInputInput]' = None) -> 'AlertsAggregateResponse'
 |      Pull alert severity aggregates based on `group_by` parameters: domain, watchlist, hostname, detector, user..
 |
 |  alerts_service_alerts_dashboard_triage(self, in_: 'Optional[TriageDashboardInputInput]' = None) -> 'TriageDashboardOutput'
 |      None.
 |
 |  alerts_service_poll(self, in_: 'Optional[PollRequestInput]' = None) -> 'AlertsResponse'
 |      Poll for results for a specific `search
...
# SearchRequestInput
class SearchRequestInput(builtins.object)
 |  SearchRequestInput(cql_query: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None) -> None
...
```

*Note: Output has been truncated for verbosity.*

## Context Manager

The service object is also a context manager to help temporarily override default values when making
an API call.  This can include fields like the `environment`, `tenant_id`, `output`, or `access_token`.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import SearchRequestInput

service = GraphQLService()

with service(
    environment="delta",
    tenant_id="00000",
    output="""
        reason
        alerts {
            total_results
            list {
                id
                tenant_id
                metadata {
                    title
                    severity
                }
                status
            }
        }
    """,
):
    result = service.alerts.query.alerts_service_search(SearchRequestInput(
        offset=0,
        limit=10,
        cql_query="""
        FROM alert
        WHERE
            severity >= 0.6
        EARLIEST=-1d
        """
    ))
```

### Pruning GraphQL Output

One of the benefits of using GraphQL is that you can define which fields that you want returned.
By default we assume little to no knowledge of GraphQL to get you started, so we provide all the fields
in the API call for exploration reasons.  This may be unneeded for specific application or reporting
purposes.

To assist with this, we have a utility called `build_output_string`.  This will return a string
representation of the output object with all possible fields for the return type.  You can use
this as reference to build your own, or modify it to remove fields that are not needed.

```python
from taegis_sdk_python import build_output_string
from taegis_sdk_python.services.alerts.types import AlertsResponse

print(build_output_string(AlertsResponse))
```

```
reason search_id status alerts { previous_offset total_parts list { reference_details { reference {
description url type } } parent_tenant_id entities { entities relationships { relationship to_entity
from_entity type } } sensor_types suppression_rules { id version } resolution_history { timestamp {
nanos seconds } user_id status num_alerts_affected id reason } enrichment_details {
business_email_compromise { user_name source_address_geo_summary { country { confidence iso_code
geoname_id code } city { confidence locale_names { record { value key } } geoname_id name } location {
timezone latitude longitude us_metro_code radius metro_code gmt_offset } asn { autonomous_system_no
autonomous_system_org } continent { code geoname_id } } source_address }
...
```

*Note: Output has been truncated for verbosity.*

The service object can be called as a context manager with `output` assigned with the new GraphQL
output fields.  The same object will be returned, but fields not defined will be assigned a `None`
value.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import SearchRequestInput

from pprint import pprint as pp

service = GraphQLService()
with service(output="search_id alerts { list { id status metadata { title severity confidence } } }")
    results = service.alerts.query.alerts_service_search(
        SearchRequestInput(
            offset=0,
            limit=10,
            cql_query="""
            FROM alert
            WHERE
                severity >= 0.6
            EARLIEST=-1d
            """,
        )
    )
pp(results)
```

## Arbitrary Queries

If would like to run an API call that is different from the provided method or which the SDK
does not support, you can craft your own query/mutation/subscription.  Certain services may be
configured differently; it is recommended to use the service endpoint you want to query against
when available.

* `execute_query`
* `execute_mutation`
* `execute_subscription`

```python
from taegis_sdk_python import GraphQLService

from pprint import pprint as pp

service = GraphQLService()

results = service.alerts.execute_query(
    endpoint="alertsServiceSearch",
    variables={
        "in": {
            "limit": 3,
            "offset": 0,
            "cql_query": """
            FROM alert
            WHERE
                severity >= 0.6
            EARLIEST=-1d
            """
        }
    },
    output="""
        search_id
        alerts {
            list {
                id
                tenant_id
                metadata {
                    title
                    severity
                }
                status
            }
        }
    """
)
pp(results)
```

## Raw Queries

You can also run your own raw GraphQL strings.  This provides the most flexibility
but least amount of guard rails.

* `execute`
* `subscribe`

```python
from taegis_sdk_python import GraphQLService

from pprint import pprint as pp

service = GraphQLService()

results = service.investigations.execute("""
    query investigationsStatusCount
    {
        investigationsStatusCount
        {
            open closed active awaiting_action suspended total
        }
    }
""")
pp(results)
```

## Helpers

### `build_output_string`

There is a utility called `build_output_string`.   This will return a string
representation of the output object with all possible fields for the return type.

```python
from taegis_sdk_python import build_output_string
from taegis_sdk_python.services.alerts.types import AlertsResponse

print(build_output_string(AlertsResponse))
```

### `_build_output_query`

If you want some assistance in building a complete GraphQL query string,
you can call the service endpoint `_build_output_query` to help.  This does build
the query from the schema, so ensure you are pulling the schema from the correct
service endpoint.

```python
from taegis_sdk_python import GraphQLService, build_output_string
from taegis_sdk_python.services.investigations.types import InvestigationStatusCountResponse

service = GraphQLService()
schema = service.alerts.get_sync_schema()

print(service.alerts._build_output_query(
    operation_type="query",
    endpoint="investigationsStatusCount",
    graphql_field=schema.query_type.fields.get("investigationsStatusCount"),
    output=build_output_string(InvestigationStatusCountResponse)
))
```
