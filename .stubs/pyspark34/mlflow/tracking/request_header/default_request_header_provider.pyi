from mlflow import __version__ as __version__
from mlflow.tracking.request_header.abstract_request_header_provider import RequestHeaderProvider as RequestHeaderProvider

class DefaultRequestHeaderProvider(RequestHeaderProvider):
    """
    Provides default request headers for outgoing request.
    """
    def in_context(self): ...
    def request_headers(self): ...
