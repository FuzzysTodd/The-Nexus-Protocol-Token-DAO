from mlflow.tracking.request_header.abstract_request_header_provider import RequestHeaderProvider as RequestHeaderProvider
from mlflow.utils import databricks_utils as databricks_utils

class DatabricksRequestHeaderProvider(RequestHeaderProvider):
    """
    Provides request headers indicating the type of Databricks environment from which a request
    was made.
    """
    def in_context(self): ...
    def request_headers(self): ...
