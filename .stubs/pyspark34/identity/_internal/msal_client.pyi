from .pipeline import build_pipeline as build_pipeline
from azure.core.pipeline import PipelineResponse as PipelineResponse
from azure.core.pipeline.transport import HttpResponse as HttpResponse
from typing import Any, Dict

RequestData = Dict[str, str] | str

class MsalResponse:
    """Wraps HttpResponse according to msal.oauth2cli.http.

    :param response: The response to wrap.
    :type response: ~azure.core.pipeline.transport.HttpResponse
    """
    def __init__(self, response: PipelineResponse) -> None: ...
    @property
    def status_code(self) -> int: ...
    @property
    def text(self) -> str: ...
    def raise_for_status(self) -> None: ...

class MsalClient:
    """Wraps Pipeline according to msal.oauth2cli.http"""
    def __init__(self, **kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None: ...
    def post(self, url: str, params: Dict[str, str] | None = None, data: RequestData | None = None, headers: Dict[str, str] | None = None, **kwargs: Any) -> MsalResponse: ...
    def get(self, url: str, params: Dict[str, str] | None = None, headers: Dict[str, str] | None = None, **kwargs: Any) -> MsalResponse: ...
    def get_error_response(self, msal_result: Dict) -> HttpResponse | None:
        """Get the HTTP response associated with an MSAL error.

        :param msal_result: The result of an MSAL request.
        :type msal_result: dict
        :return: The HTTP response associated with the error, if any.
        :rtype: ~azure.core.pipeline.transport.HttpResponse or None
        """
