import typing as t
from _typeshed import Incomplete
from _typeshed.wsgi import StartResponse, WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment

class DispatcherMiddleware:
    """Combine multiple applications as a single WSGI application.
    Requests are dispatched to an application based on the path it is
    mounted under.

    :param app: The WSGI application to dispatch to if the request
        doesn't match a mounted path.
    :param mounts: Maps path prefixes to applications for dispatching.
    """
    app: Incomplete
    mounts: Incomplete
    def __init__(self, app: WSGIApplication, mounts: dict[str, WSGIApplication] | None = None) -> None: ...
    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> t.Iterable[bytes]: ...
