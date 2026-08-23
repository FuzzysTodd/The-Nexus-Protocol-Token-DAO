import jinja2
import typing
from _typeshed import Incomplete
from os import PathLike
from starlette.background import BackgroundTask as BackgroundTask
from starlette.datastructures import URL as URL
from starlette.requests import Request as Request
from starlette.responses import Response as Response
from starlette.types import Receive as Receive, Scope as Scope, Send as Send

pass_context: Incomplete

class _TemplateResponse(Response):
    media_type: str
    template: Incomplete
    context: Incomplete
    def __init__(self, template: typing.Any, context: dict, status_code: int = 200, headers: typing.Mapping[str, str] | None = None, media_type: str | None = None, background: BackgroundTask | None = None) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...

class Jinja2Templates:
    '''
    templates = Jinja2Templates("templates")

    return templates.TemplateResponse("index.html", {"request": request})
    '''
    env: Incomplete
    context_processors: Incomplete
    def __init__(self, directory: str | PathLike, context_processors: typing.List[typing.Callable[[Request], typing.Dict[str, typing.Any]]] | None = None, **env_options: typing.Any) -> None: ...
    def get_template(self, name: str) -> jinja2.Template: ...
    def TemplateResponse(self, name: str, context: dict, status_code: int = 200, headers: typing.Mapping[str, str] | None = None, media_type: str | None = None, background: BackgroundTask | None = None) -> _TemplateResponse: ...
