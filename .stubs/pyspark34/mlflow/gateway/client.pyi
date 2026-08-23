from mlflow import MlflowException as MlflowException
from mlflow.gateway.config import Route as Route
from mlflow.gateway.constants import MLFLOW_GATEWAY_CLIENT_QUERY_RETRY_CODES as MLFLOW_GATEWAY_CLIENT_QUERY_RETRY_CODES, MLFLOW_GATEWAY_CLIENT_QUERY_TIMEOUT_SECONDS as MLFLOW_GATEWAY_CLIENT_QUERY_TIMEOUT_SECONDS, MLFLOW_GATEWAY_CRUD_ROUTE_BASE as MLFLOW_GATEWAY_CRUD_ROUTE_BASE, MLFLOW_GATEWAY_ROUTE_BASE as MLFLOW_GATEWAY_ROUTE_BASE, MLFLOW_QUERY_SUFFIX as MLFLOW_QUERY_SUFFIX
from mlflow.gateway.utils import assemble_uri_path as assemble_uri_path, get_gateway_uri as get_gateway_uri, resolve_route_url as resolve_route_url
from mlflow.protos.databricks_pb2 import BAD_REQUEST as BAD_REQUEST
from mlflow.store.entities.paged_list import PagedList as PagedList
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.databricks_utils import get_databricks_host_creds as get_databricks_host_creds
from mlflow.utils.rest_utils import MlflowHostCreds as MlflowHostCreds, augmented_raise_for_status as augmented_raise_for_status, http_request as http_request
from mlflow.utils.uri import get_uri_scheme as get_uri_scheme
from typing import Any, Dict

class MlflowGatewayClient:
    """
    Client for interacting with the MLflow Gateway API.

    :param gateway_uri: Optional URI of the gateway. If not provided, attempts to resolve from
        first the stored result of `set_gateway_uri()`, then the  environment variable
        `MLFLOW_GATEWAY_URI`.
    """
    def __init__(self, gateway_uri: str | None = None) -> None: ...
    @property
    def gateway_uri(self):
        """
        Get the current value for the URI of the MLflow Gateway.

        :return: The gateway URI.
        """
    def get_route(self, name: str):
        """
        Get a specific query route from the gateway. The routes that are available to retrieve
        are only those that have been configured through the MLflow Gateway Server configuration
        file (set during server start or through server update commands).

        :param name: The name of the route.
        :return: The returned data structure is a serialized representation of the `Route` data
            structure, giving information about the name, type, and model details (model name
            and provider) for the requested route endpoint.
        """
    def search_routes(self, page_token: str | None = None) -> PagedList[Route]:
        """
        Search for routes in the Gateway.

        :param page_token: Token specifying the next page of results. It should be obtained from
                           a prior ``search_routes()`` call.
        :return: Returns a list of all configured and initialized `Route` data for the MLflow
            Gateway Server. The return will be a list of dictionaries that detail the name, type,
            and model details of each active route endpoint.
        """
    def create_route(self, name: str, route_type: str, model: Dict[str, Any]) -> Route:
        '''
        Create a new route in the Gateway.

        .. warning::

            This API is **only available** when running within Databricks. When running elsewhere,
            route configuration is handled via updates to the route configuration YAML file that
            is specified during Gateway server start.

        :param name: The name of the route.
        :param route_type: The type of the route (e.g., \'llm/v1/chat\', \'llm/v1/completions\',
                           \'llm/v1/embeddings\').
        :param model: A dictionary representing the model details to be associated with the route.
                      This dictionary should define:

                      - The model name (e.g., "gpt-3.5-turbo")
                      - The provider (e.g., "openai", "anthropic")
                      - The configuration for the model used in the route

        :return: A serialized representation of the `Route` data structure,
                 providing information about the name, type, and model details for the
                 newly created route endpoint.

        :raises mlflow.MlflowException: If the function is not running within Databricks.

        .. note::

            See the official Databricks documentation for MLflow Gateway for examples of supported
            model configurations and how to dynamically create new routes within Databricks.


        Example usage from within Databricks:

        .. code-block:: python

            from mlflow.gateway import MlflowGatewayClient

            gateway_client = MlflowGatewayClient("databricks")

            openai_api_key = ...

            new_route = gateway_client.create_route(
                "my-new-route",
                "llm/v1/completions",
                {
                    "name": "question-answering-bot-1",
                    "provider": "openai",
                    "config": {
                        "openai_api_key": openai_api_key,
                        "openai_api_version": "2023-05-10",
                        "openai_api_type": "openai/v1/chat/completions",
                    },
                },
            )

        '''
    def delete_route(self, name: str) -> None:
        '''
        Delete an existing route in the Gateway.

        .. warning::

            This API is **only available** when running within Databricks. When running elsewhere,
            route deletion is handled by removing the corresponding entry from the route
            configuration YAML file that is specified during Gateway server start.

        :param name: The name of the route to delete.

        :raises mlflow.MlflowException: If the function is not running within Databricks.

        Example usage from within Databricks:

        .. code-block:: python

            from mlflow.gateway import MlflowGatewayClient

            gateway_client = MlflowGatewayClient("databricks")
            gateway_client.delete_route("my-existing-route")

        '''
    def query(self, route: str, data: Dict[str, Any]):
        '''
        Submit a query to a configured provider route.

        :param route: The name of the route to submit the query to.
        :param data: The data to send in the query. A dictionary representing the per-route
            specific structure required for a given provider.
        :return: The route\'s response as a dictionary, standardized to the route type.

        For chat, the structure should be:

        .. code-block:: python

            from mlflow.gateway import MlflowGatewayClient

            gateway_client = MlflowGatewayClient("http://my.gateway:8888")

            response = gateway_client.query(
                "my-chat-route",
                {"messages": [{"role": "user", "content": "Tell me a joke about rabbits"}, ...]},
            )

        For completions, the structure should be:

        .. code-block:: python

            from mlflow.gateway import MlflowGatewayClient

            gateway_client = MlflowGatewayClient("http://my.gateway:8888")

            response = gateway_client.query(
                "my-completions-route", {"prompt": "It\'s one small step for"}
            )

        For embeddings, the structure should be:

        .. code-block:: python

            from mlflow.gateway import MlflowGatewayClient

            gateway_client = MlflowGatewayClient("http://my.gateway:8888")

            response = gateway_client.query(
                "my-embeddings-route",
                {"text": ["It was the best of times", "It was the worst of times"]},
            )

        '''
