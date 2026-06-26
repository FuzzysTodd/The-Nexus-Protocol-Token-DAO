import typing as t
from ..exceptions import BadRequest as BadRequest, HTTPException as HTTPException
from ..utils import cached_property as cached_property, redirect as redirect
from ..wrappers.request import Request as Request
from ..wrappers.response import Response as Response
from .map import MapAdapter as MapAdapter
from .rules import Rule as Rule
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIEnvironment as WSGIEnvironment

class RoutingException(Exception):
    """Special exceptions that require the application to redirect, notifying
    about missing urls, etc.

    :internal:
    """

class RequestRedirect(HTTPException, RoutingException):
    """Raise if the map requests a redirect. This is for example the case if
    `strict_slashes` are activated and an url that requires a trailing slash.

    The attribute `new_url` contains the absolute destination url.
    """
    code: int
    new_url: Incomplete
    def __init__(self, new_url: str) -> None: ...
    def get_response(self, environ: WSGIEnvironment | Request | None = None, scope: dict | None = None) -> Response: ...

class RequestPath(RoutingException):
    """Internal exception."""
    path_info: Incomplete
    def __init__(self, path_info: str) -> None: ...

class RequestAliasRedirect(RoutingException):
    """This rule is an alias and wants to redirect to the canonical URL."""
    matched_values: Incomplete
    endpoint: Incomplete
    def __init__(self, matched_values: t.Mapping[str, t.Any], endpoint: str) -> None: ...

class BuildError(RoutingException, LookupError):
    """Raised if the build system cannot find a URL for an endpoint with the
    values provided.
    """
    endpoint: Incomplete
    values: Incomplete
    method: Incomplete
    adapter: Incomplete
    def __init__(self, endpoint: str, values: t.Mapping[str, t.Any], method: str | None, adapter: MapAdapter | None = None) -> None: ...
    def suggested(self) -> Rule | None: ...
    def closest_rule(self, adapter: MapAdapter | None) -> Rule | None: ...

class WebsocketMismatch(BadRequest):
    """The only matched rule is either a WebSocket and the request is
    HTTP, or the rule is HTTP and the request is a WebSocket.
    """

class NoMatch(Exception):
    have_match_for: Incomplete
    websocket_mismatch: Incomplete
    def __init__(self, have_match_for: set[str], websocket_mismatch: bool) -> None: ...
