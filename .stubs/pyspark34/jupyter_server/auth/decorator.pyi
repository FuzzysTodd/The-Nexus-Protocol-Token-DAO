from .utils import HTTP_METHOD_TO_AUTH_ACTION as HTTP_METHOD_TO_AUTH_ACTION
from typing import Callable

def authorized(action: str | Callable | None = None, resource: str | None = None, message: str | None = None) -> Callable:
    """A decorator for tornado.web.RequestHandler methods
    that verifies whether the current user is authorized
    to make the following request.

    Helpful for adding an 'authorization' layer to
    a REST API.

    .. versionadded:: 2.0

    Parameters
    ----------
    action : str
        the type of permission or action to check.

    resource: str or None
        the name of the resource the action is being authorized
        to access.

    message : str or none
        a message for the unauthorized action.
    """
