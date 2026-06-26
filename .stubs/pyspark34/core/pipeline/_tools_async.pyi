from ..rest import AsyncHttpResponse as RestAsyncHttpResponse
from typing import Awaitable, Callable, TypeVar, overload
from typing_extensions import ParamSpec

P = ParamSpec('P')
T = TypeVar('T')

@overload
async def await_result(func: Callable[P, Awaitable[T]], *args: P.args, **kwargs: P.kwargs) -> T: ...
@overload
async def await_result(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T: ...
async def handle_no_stream_rest_response(response: RestAsyncHttpResponse) -> None:
    """Handle reading and closing of non stream rest responses.
    For our new rest responses, we have to call .read() and .close() for our non-stream
    responses. This way, we load in the body for users to access.

    :param response: The response to read and close.
    :type response: ~azure.core.rest.AsyncHttpResponse
    """
