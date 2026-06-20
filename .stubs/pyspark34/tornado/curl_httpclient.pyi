from _typeshed import Incomplete
from tornado import httputil as httputil, ioloop as ioloop
from tornado.escape import native_str as native_str, utf8 as utf8
from tornado.httpclient import AsyncHTTPClient as AsyncHTTPClient, HTTPError as HTTPError, HTTPRequest as HTTPRequest, HTTPResponse as HTTPResponse, main as main
from tornado.log import app_log as app_log
from typing import Any, Callable, Dict

curl_log: Incomplete

class CurlAsyncHTTPClient(AsyncHTTPClient):
    def initialize(self, max_clients: int = 10, defaults: Dict[str, Any] | None = None) -> None: ...
    def close(self) -> None: ...
    def fetch_impl(self, request: HTTPRequest, callback: Callable[[HTTPResponse], None]) -> None: ...
    def handle_callback_exception(self, callback: Any) -> None: ...

class CurlError(HTTPError):
    errno: Incomplete
    def __init__(self, errno: int, message: str) -> None: ...
