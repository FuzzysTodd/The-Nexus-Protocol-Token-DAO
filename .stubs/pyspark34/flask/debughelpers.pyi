from .blueprints import Blueprint as Blueprint
from .globals import request_ctx as request_ctx
from .sansio.app import App as App
from _typeshed import Incomplete

class UnexpectedUnicodeError(AssertionError, UnicodeError):
    """Raised in places where we want some better error reporting for
    unexpected unicode or binary data.
    """

class DebugFilesKeyError(KeyError, AssertionError):
    """Raised from request.files during debugging.  The idea is that it can
    provide a better error message than just a generic KeyError/BadRequest.
    """
    msg: Incomplete
    def __init__(self, request, key) -> None: ...

class FormDataRoutingRedirect(AssertionError):
    """This exception is raised in debug mode if a routing redirect
    would cause the browser to drop the method or body. This happens
    when method is not GET, HEAD or OPTIONS and the status code is not
    307 or 308.
    """
    def __init__(self, request) -> None: ...

def attach_enctype_error_multidict(request):
    """Patch ``request.files.__getitem__`` to raise a descriptive error
    about ``enctype=multipart/form-data``.

    :param request: The request to patch.
    :meta private:
    """
def explain_template_loading_attempts(app: App, template, attempts) -> None:
    """This should help developers understand what failed"""
