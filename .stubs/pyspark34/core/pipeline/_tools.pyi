from azure.core.rest import AsyncHttpResponse as AsyncHttpResponse, HttpRequest as HttpRequest, HttpResponse as HttpResponse
from typing import Callable, TypeVar
from typing_extensions import ParamSpec, TypeGuard

P = ParamSpec('P')
T = TypeVar('T')

def await_result(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
    """If func returns an awaitable, raise that this runner can't handle it.

    :param func: The function to run.
    :type func: callable
    :param args: The positional arguments to pass to the function.
    :type args: list
    :rtype: any
    :return: The result of the function
    :raises: TypeError
    """
def is_rest(obj: object) -> TypeGuard[HttpRequest | HttpResponse | AsyncHttpResponse]:
    """Return whether a request or a response is a rest request / response.

    Checking whether the response has the object content can sometimes result
    in a ResponseNotRead error if you're checking the value on a response
    that has not been read in yet. To get around this, we also have added
    a check for is_stream_consumed, which is an exclusive property on our new responses.

    :param obj: The object to check.
    :type obj: any
    :rtype: bool
    :return: Whether the object is a rest request / response.
    """
def handle_non_stream_rest_response(response: HttpResponse) -> None:
    """Handle reading and closing of non stream rest responses.
    For our new rest responses, we have to call .read() and .close() for our non-stream
    responses. This way, we load in the body for users to access.

    :param response: The response to read and close.
    :type response: ~azure.core.rest.HttpResponse
    """
