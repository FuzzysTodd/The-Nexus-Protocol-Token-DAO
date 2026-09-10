from ._compat import DeprecatedAwaitableList as DeprecatedAwaitableList
from ._eventloop import get_asynclib as get_asynclib
from _typeshed import Incomplete
from typing import Any, Awaitable, Generator

class TaskInfo:
    """
    Represents an asynchronous task.

    :ivar int id: the unique identifier of the task
    :ivar parent_id: the identifier of the parent task, if any
    :vartype parent_id: Optional[int]
    :ivar str name: the description of the task (if any)
    :ivar ~collections.abc.Coroutine coro: the coroutine object of the task
    """
    id: Incomplete
    parent_id: Incomplete
    name: Incomplete
    coro: Incomplete
    def __init__(self, id: int, parent_id: int | None, name: str | None, coro: Generator[Any, Any, Any] | Awaitable[Any]) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __await__(self) -> Generator[None, None, TaskInfo]: ...

def get_current_task() -> TaskInfo:
    """
    Return the current task.

    :return: a representation of the current task

    """
def get_running_tasks() -> DeprecatedAwaitableList[TaskInfo]:
    """
    Return a list of running tasks in the current event loop.

    :return: a list of task info objects

    """
async def wait_all_tasks_blocked() -> None:
    """Wait until all other tasks are waiting for something."""
