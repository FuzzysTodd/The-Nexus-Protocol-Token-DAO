import typing
from _typeshed import Incomplete
from starlette._utils import is_async_callable as is_async_callable
from starlette.concurrency import run_in_threadpool as run_in_threadpool
from typing import ParamSpec

P = ParamSpec('P')

class BackgroundTask:
    func: Incomplete
    args: Incomplete
    kwargs: Incomplete
    is_async: Incomplete
    def __init__(self, func: typing.Callable[P, typing.Any], *args: P.args, **kwargs: P.kwargs) -> None: ...
    async def __call__(self) -> None: ...

class BackgroundTasks(BackgroundTask):
    tasks: Incomplete
    def __init__(self, tasks: typing.Sequence[BackgroundTask] | None = None) -> None: ...
    def add_task(self, func: typing.Callable[P, typing.Any], *args: P.args, **kwargs: P.kwargs) -> None: ...
    async def __call__(self) -> None: ...
