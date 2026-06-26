import types
from typing import Any, Awaitable, Callable, Dict, Iterable, Literal, MutableMapping, Protocol, Tuple, Type, TypedDict
from typing_extensions import NotRequired

Environ = MutableMapping[str, Any]
ExcInfo = Tuple[Type[BaseException], BaseException, types.TracebackType | None]
StartResponse = Callable[[str, Iterable[Tuple[str, str]], ExcInfo | None], None]
WSGIApp = Callable[[Environ, StartResponse], Iterable[bytes] | BaseException]

class ASGIVersions(TypedDict):
    spec_version: str
    version: Literal['2.0'] | Literal['3.0']

class HTTPScope(TypedDict):
    type: Literal['http']
    asgi: ASGIVersions
    http_version: str
    method: str
    scheme: str
    path: str
    raw_path: bytes
    query_string: bytes
    root_path: str
    headers: Iterable[Tuple[bytes, bytes]]
    client: Tuple[str, int] | None
    server: Tuple[str, int | None] | None
    state: NotRequired[Dict[str, Any]]
    extensions: NotRequired[Dict[str, Dict[object, object]]]

class WebSocketScope(TypedDict):
    type: Literal['websocket']
    asgi: ASGIVersions
    http_version: str
    scheme: str
    path: str
    raw_path: bytes
    query_string: bytes
    root_path: str
    headers: Iterable[Tuple[bytes, bytes]]
    client: Tuple[str, int] | None
    server: Tuple[str, int | None] | None
    subprotocols: Iterable[str]
    state: NotRequired[Dict[str, Any]]
    extensions: NotRequired[Dict[str, Dict[object, object]]]

class LifespanScope(TypedDict):
    type: Literal['lifespan']
    asgi: ASGIVersions
    state: NotRequired[Dict[str, Any]]
WWWScope = HTTPScope | WebSocketScope
Scope = HTTPScope | WebSocketScope | LifespanScope

class HTTPRequestEvent(TypedDict):
    type: Literal['http.request']
    body: bytes
    more_body: bool

class HTTPResponseDebugEvent(TypedDict):
    type: Literal['http.response.debug']
    info: Dict[str, object]

class HTTPResponseStartEvent(TypedDict):
    type: Literal['http.response.start']
    status: int
    headers: Iterable[Tuple[bytes, bytes]]
    trailers: NotRequired[bool]

class HTTPResponseBodyEvent(TypedDict):
    type: Literal['http.response.body']
    body: bytes
    more_body: bool

class HTTPResponseTrailersEvent(TypedDict):
    type: Literal['http.response.trailers']
    headers: Iterable[Tuple[bytes, bytes]]
    more_trailers: bool

class HTTPServerPushEvent(TypedDict):
    type: Literal['http.response.push']
    path: str
    headers: Iterable[Tuple[bytes, bytes]]

class HTTPDisconnectEvent(TypedDict):
    type: Literal['http.disconnect']

class WebSocketConnectEvent(TypedDict):
    type: Literal['websocket.connect']

class WebSocketAcceptEvent(TypedDict):
    type: Literal['websocket.accept']
    subprotocol: str | None
    headers: Iterable[Tuple[bytes, bytes]]

class WebSocketReceiveEvent(TypedDict):
    type: Literal['websocket.receive']
    bytes: bytes | None
    text: str | None

class WebSocketSendEvent(TypedDict):
    type: Literal['websocket.send']
    bytes: bytes | None
    text: str | None

class WebSocketResponseStartEvent(TypedDict):
    type: Literal['websocket.http.response.start']
    status: int
    headers: Iterable[Tuple[bytes, bytes]]

class WebSocketResponseBodyEvent(TypedDict):
    type: Literal['websocket.http.response.body']
    body: bytes
    more_body: bool

class WebSocketDisconnectEvent(TypedDict):
    type: Literal['websocket.disconnect']
    code: int

class WebSocketCloseEvent(TypedDict):
    type: Literal['websocket.close']
    code: int
    reason: str | None

class LifespanStartupEvent(TypedDict):
    type: Literal['lifespan.startup']

class LifespanShutdownEvent(TypedDict):
    type: Literal['lifespan.shutdown']

class LifespanStartupCompleteEvent(TypedDict):
    type: Literal['lifespan.startup.complete']

class LifespanStartupFailedEvent(TypedDict):
    type: Literal['lifespan.startup.failed']
    message: str

class LifespanShutdownCompleteEvent(TypedDict):
    type: Literal['lifespan.shutdown.complete']

class LifespanShutdownFailedEvent(TypedDict):
    type: Literal['lifespan.shutdown.failed']
    message: str
WebSocketEvent = WebSocketReceiveEvent | WebSocketDisconnectEvent | WebSocketConnectEvent
ASGIReceiveEvent = HTTPRequestEvent | HTTPDisconnectEvent | WebSocketConnectEvent | WebSocketReceiveEvent | WebSocketDisconnectEvent | LifespanStartupEvent | LifespanShutdownEvent
ASGISendEvent = HTTPResponseStartEvent | HTTPResponseBodyEvent | HTTPResponseTrailersEvent | HTTPServerPushEvent | HTTPDisconnectEvent | WebSocketAcceptEvent | WebSocketSendEvent | WebSocketResponseStartEvent | WebSocketResponseBodyEvent | WebSocketCloseEvent | LifespanStartupCompleteEvent | LifespanStartupFailedEvent | LifespanShutdownCompleteEvent | LifespanShutdownFailedEvent
ASGIReceiveCallable = Callable[[], Awaitable[ASGIReceiveEvent]]
ASGISendCallable = Callable[[ASGISendEvent], Awaitable[None]]

class ASGI2Protocol(Protocol):
    def __init__(self, scope: Scope) -> None: ...
    async def __call__(self, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None: ...
ASGI2Application = Type[ASGI2Protocol]
ASGI3Application = Callable[[Scope, ASGIReceiveCallable, ASGISendCallable], Awaitable[None]]
ASGIApplication = ASGI2Application | ASGI3Application
