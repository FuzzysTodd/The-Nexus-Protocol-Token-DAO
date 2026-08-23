import typing
from _typeshed import Incomplete
from tenacity import BaseRetrying as BaseRetrying, DoAttempt as DoAttempt, DoSleep as DoSleep, RetryCallState as RetryCallState
from tornado.concurrent import Future as Future

class TornadoRetrying(BaseRetrying):
    sleep: Incomplete
    def __init__(self, sleep: typing.Callable[[float], Future[None]] = ..., **kwargs: typing.Any) -> None: ...
    def __call__(self, fn: typing.Callable[..., typing.Generator[typing.Any, typing.Any, _RetValT] | Future[_RetValT]], *args: typing.Any, **kwargs: typing.Any) -> typing.Generator[typing.Any, typing.Any, _RetValT]: ...
