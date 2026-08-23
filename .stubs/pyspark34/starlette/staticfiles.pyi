import os
import typing
from _typeshed import Incomplete
from starlette.datastructures import Headers as Headers, URL as URL
from starlette.exceptions import HTTPException as HTTPException
from starlette.responses import FileResponse as FileResponse, RedirectResponse as RedirectResponse, Response as Response
from starlette.types import Receive as Receive, Scope as Scope, Send as Send

PathLike: Incomplete

class NotModifiedResponse(Response):
    NOT_MODIFIED_HEADERS: Incomplete
    def __init__(self, headers: Headers) -> None: ...

class StaticFiles:
    directory: Incomplete
    packages: Incomplete
    all_directories: Incomplete
    html: Incomplete
    config_checked: bool
    follow_symlink: Incomplete
    def __init__(self, *, directory: PathLike | None = None, packages: typing.List[str | typing.Tuple[str, str]] | None = None, html: bool = False, check_dir: bool = True, follow_symlink: bool = False) -> None: ...
    def get_directories(self, directory: PathLike | None = None, packages: typing.List[str | typing.Tuple[str, str]] | None = None) -> typing.List[PathLike]:
        """
        Given `directory` and `packages` arguments, return a list of all the
        directories that should be used for serving static files from.
        """
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        The ASGI entry point.
        """
    def get_path(self, scope: Scope) -> str:
        """
        Given the ASGI scope, return the `path` string to serve up,
        with OS specific path separators, and any '..', '.' components removed.
        """
    async def get_response(self, path: str, scope: Scope) -> Response:
        """
        Returns an HTTP response, given the incoming path, method and request headers.
        """
    def lookup_path(self, path: str) -> typing.Tuple[str, os.stat_result | None]: ...
    def file_response(self, full_path: PathLike, stat_result: os.stat_result, scope: Scope, status_code: int = 200) -> Response: ...
    async def check_config(self) -> None:
        """
        Perform a one-off configuration check that StaticFiles is actually
        pointed at a directory, so that we can raise loud errors rather than
        just returning 404 responses.
        """
    def is_not_modified(self, response_headers: Headers, request_headers: Headers) -> bool:
        '''
        Given the request and response headers, return `True` if an HTTP
        "Not Modified" response could be returned instead.
        '''
