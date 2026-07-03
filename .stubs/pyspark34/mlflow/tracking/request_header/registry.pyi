from _typeshed import Incomplete
from mlflow.tracking.request_header.databricks_request_header_provider import DatabricksRequestHeaderProvider as DatabricksRequestHeaderProvider
from mlflow.tracking.request_header.default_request_header_provider import DefaultRequestHeaderProvider as DefaultRequestHeaderProvider

class RequestHeaderProviderRegistry:
    def __init__(self) -> None: ...
    def register(self, request_header_provider) -> None: ...
    def register_entrypoints(self) -> None:
        """Register tracking stores provided by other packages"""
    def __iter__(self): ...

def resolve_request_headers(request_headers: Incomplete | None = None):
    """Generate a set of request headers from registered providers. Request headers are resolved in
    the order that providers are registered. Argument headers are applied last.

    This function iterates through all request header providers in the registry. Additional context
    providers can be registered as described in
    :py:class:`mlflow.tracking.request_header.RequestHeaderProvider`.

    :param tags: A dictionary of request headers to override. If specified, headers passed in this
        argument will override those inferred from the context.
    :return: A dictionary of resolved headers.
    """
