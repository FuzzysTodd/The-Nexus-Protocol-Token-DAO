import os
from _typeshed import Incomplete
from requests import PreparedRequest, models
from requests.adapters import HTTPAdapter
from responses.registries import FirstMatchRegistry
from typing import Any, Callable, Iterator, List, Literal, Mapping, NamedTuple, Protocol, Sequence, Sized, Tuple, Type, overload
from urllib3.response import HTTPHeaderDict, HTTPResponse

__all__ = ['CallbackResponse', 'Response', 'RequestsMock', 'activate', 'add', '_add_from_file', 'add_callback', 'add_passthru', '_deprecated_assert_all_requests_are_fired', 'assert_call_count', 'calls', 'delete', 'DELETE', 'get', 'GET', 'head', 'HEAD', 'options', 'OPTIONS', '_deprecated_passthru_prefixes', 'patch', 'PATCH', 'post', 'POST', 'put', 'PUT', 'registered', 'remove', 'replace', 'reset', 'response_callback', 'start', 'stop', '_deprecated_target', 'upsert']

class UnboundSend(Protocol):
    def __call__(self, adapter: HTTPAdapter, request: PreparedRequest, *args: Any, **kwargs: Any) -> models.Response: ...

class Call(NamedTuple):
    request: Incomplete
    response: Incomplete

class FalseBool:
    """Class to mock up built-in False boolean.

    Used for backwards compatibility, see
    https://github.com/getsentry/responses/issues/464
    """
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__

class CallList(Sequence[Any], Sized):
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[Call]: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, idx: int) -> Call:
        """Overload when get a single item."""
    @overload
    def __getitem__(self, idx: slice) -> List[Call]:
        """Overload when a slice is requested."""
    def add(self, request: PreparedRequest, response: _Body) -> None: ...
    def reset(self) -> None: ...

class BaseResponse:
    passthrough: bool
    content_type: str | None
    headers: Mapping[str, str] | None
    stream: bool | None
    method: Incomplete
    url: Incomplete
    match: Incomplete
    call_count: int
    def __init__(self, method: str, url: _URLPatternType, match_querystring: bool | object = None, match: _MatcherIterable = (), *, passthrough: bool = False) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def get_headers(self) -> HTTPHeaderDict: ...
    def get_response(self, request: PreparedRequest) -> HTTPResponse: ...
    def matches(self, request: PreparedRequest) -> Tuple[bool, str]: ...

class Response(BaseResponse):
    body: Incomplete
    status: Incomplete
    headers: Incomplete
    stream: Incomplete
    content_type: Incomplete
    auto_calculate_content_length: Incomplete
    def __init__(self, method: str, url: _URLPatternType, body: _Body = '', json: Any | None = None, status: int = 200, headers: Mapping[str, str] | None = None, stream: bool | None = None, content_type: str | object = ..., auto_calculate_content_length: bool = False, **kwargs: Any) -> None: ...
    def get_response(self, request: PreparedRequest) -> HTTPResponse: ...

class CallbackResponse(BaseResponse):
    callback: Incomplete
    stream: Incomplete
    content_type: Incomplete
    def __init__(self, method: str, url: _URLPatternType, callback: Callable[[Any], Any], stream: bool | None = None, content_type: str | None = 'text/plain', **kwargs: Any) -> None: ...
    def get_response(self, request: PreparedRequest) -> HTTPResponse: ...

class PassthroughResponse(BaseResponse):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class RequestsMock:
    DELETE: Literal['DELETE']
    GET: Literal['GET']
    HEAD: Literal['HEAD']
    OPTIONS: Literal['OPTIONS']
    PATCH: Literal['PATCH']
    POST: Literal['POST']
    PUT: Literal['PUT']
    response_callback: Callable[[Any], Any] | None
    assert_all_requests_are_fired: Incomplete
    passthru_prefixes: Incomplete
    target: Incomplete
    def __init__(self, assert_all_requests_are_fired: bool = True, response_callback: Callable[[Any], Any] | None = None, passthru_prefixes: Tuple[str, ...] = (), target: str = 'requests.adapters.HTTPAdapter.send', registry: Type[FirstMatchRegistry] = ...) -> None: ...
    def get_registry(self) -> FirstMatchRegistry:
        """Returns current registry instance with responses.

        Returns
        -------
        FirstMatchRegistry
            Current registry instance with responses.

        """
    def reset(self) -> None:
        """Resets registry (including type), calls, passthru_prefixes to default values."""
    def add(self, method: _HTTPMethodOrResponse = None, url: _URLPatternType | None = None, body: _Body = '', adding_headers: _HeaderSet = None, *args: Any, **kwargs: Any) -> BaseResponse:
        """
        >>> import responses

        A basic request:
        >>> responses.add(responses.GET, 'http://example.com')

        You can also directly pass an object which implements the
        ``BaseResponse`` interface:

        >>> responses.add(Response(...))

        A JSON payload:

        >>> responses.add(
        >>>     method='GET',
        >>>     url='http://example.com',
        >>>     json={'foo': 'bar'},
        >>> )

        Custom headers:

        >>> responses.add(
        >>>     method='GET',
        >>>     url='http://example.com',
        >>>     headers={'X-Header': 'foo'},
        >>> )

        """
    delete: Incomplete
    get: Incomplete
    head: Incomplete
    options: Incomplete
    patch: Incomplete
    post: Incomplete
    put: Incomplete
    def _add_from_file(self, file_path: str | bytes | os.PathLike[Any]) -> None: ...
    def add_passthru(self, prefix: _URLPatternType) -> None:
        """
        Register a URL prefix or regex to passthru any non-matching mock requests to.

        For example, to allow any request to 'https://example.com', but require
        mocks for the remainder, you would add the prefix as so:

        >>> import responses
        >>> responses.add_passthru('https://example.com')

        Regex can be used like:

        >>> import re
        >>> responses.add_passthru(re.compile('https://example.com/\\w+'))
        """
    def remove(self, method_or_response: _HTTPMethodOrResponse = None, url: _URLPatternType | None = None) -> List[BaseResponse]:
        """
        Removes a response previously added using ``add()``, identified
        either by a response object inheriting ``BaseResponse`` or
        ``method`` and ``url``. Removes all matching responses.

        >>> import responses
        >>> responses.add(responses.GET, 'http://example.org')
        >>> responses.remove(responses.GET, 'http://example.org')
        """
    def replace(self, method_or_response: _HTTPMethodOrResponse = None, url: _URLPatternType | None = None, body: _Body = '', *args: Any, **kwargs: Any) -> BaseResponse:
        """
        Replaces a response previously added using ``add()``. The signature
        is identical to ``add()``. The response is identified using ``method``
        and ``url``, and the first matching response is replaced.

        >>> import responses
        >>> responses.add(responses.GET, 'http://example.org', json={'data': 1})
        >>> responses.replace(responses.GET, 'http://example.org', json={'data': 2})
        """
    def upsert(self, method_or_response: _HTTPMethodOrResponse = None, url: _URLPatternType | None = None, body: _Body = '', *args: Any, **kwargs: Any) -> BaseResponse:
        """
        Replaces a response previously added using ``add()``, or adds the response
        if no response exists.  Responses are matched using ``method``and ``url``.
        The first matching response is replaced.

        >>> import responses
        >>> responses.add(responses.GET, 'http://example.org', json={'data': 1})
        >>> responses.upsert(responses.GET, 'http://example.org', json={'data': 2})
        """
    def add_callback(self, method: str, url: _URLPatternType, callback: Callable[[PreparedRequest], Exception | Tuple[int, Mapping[str, str], _Body]], match_querystring: bool | FalseBool = ..., content_type: str | None = 'text/plain', match: _MatcherIterable = ()) -> None: ...
    def registered(self) -> List['BaseResponse']: ...
    @property
    def calls(self) -> CallList: ...
    def __enter__(self) -> RequestsMock: ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> bool: ...
    @overload
    def activate(self, func: _F = ...) -> _F:
        """Overload for scenario when 'responses.activate' is used."""
    @overload
    def activate(self, *, registry: Type[Any] = ..., assert_all_requests_are_fired: bool = ...) -> Callable[[_F], '_F']:
        """Overload for scenario when
        'responses.activate(registry=, assert_all_requests_are_fired=True)' is used.

        See https://github.com/getsentry/responses/pull/469 for more details
        """
    def unbound_on_send(self) -> UnboundSend: ...
    def start(self) -> None: ...
    def stop(self, allow_assert: bool = True) -> None: ...
    def assert_call_count(self, url: str, count: int) -> bool: ...

activate: Incomplete
add: Incomplete
_add_from_file: Incomplete
add_callback: Incomplete
add_passthru: Incomplete
_deprecated_assert_all_requests_are_fired: Incomplete
assert_call_count: Incomplete
calls: Incomplete
delete: Incomplete
DELETE: Incomplete
get: Incomplete
GET: Incomplete
head: Incomplete
HEAD: Incomplete
options: Incomplete
OPTIONS: Incomplete
_deprecated_passthru_prefixes: Incomplete
patch: Incomplete
PATCH: Incomplete
post: Incomplete
POST: Incomplete
put: Incomplete
PUT: Incomplete
registered: Incomplete
remove: Incomplete
replace: Incomplete
reset: Incomplete
response_callback: Incomplete
start: Incomplete
stop: Incomplete
_deprecated_target: Incomplete
upsert: Incomplete
