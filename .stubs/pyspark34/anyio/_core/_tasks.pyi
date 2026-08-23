from ..abc._tasks import TaskGroup as TaskGroup, TaskStatus as TaskStatus
from ._compat import DeprecatedAsyncContextManager as DeprecatedAsyncContextManager, DeprecatedAwaitable as DeprecatedAwaitable, DeprecatedAwaitableFloat as DeprecatedAwaitableFloat
from ._eventloop import get_asynclib as get_asynclib
from _typeshed import Incomplete
from types import TracebackType

class _IgnoredTaskStatus(TaskStatus[object]):
    def started(self, value: object = None) -> None: ...

TASK_STATUS_IGNORED: Incomplete

class CancelScope(DeprecatedAsyncContextManager['CancelScope']):
    """
    Wraps a unit of work that can be made separately cancellable.

    :param deadline: The time (clock value) when this scope is cancelled automatically
    :param shield: ``True`` to shield the cancel scope from external cancellation
    """
    def __new__(cls, *, deadline: float = ..., shield: bool = False) -> CancelScope: ...
    def cancel(self) -> DeprecatedAwaitable:
        """Cancel this scope immediately."""
    @property
    def deadline(self) -> float:
        """
        The time (clock value) when this scope is cancelled automatically.

        Will be ``float('inf')`` if no timeout has been set.

        """
    @deadline.setter
    def deadline(self, value: float) -> None: ...
    @property
    def cancel_called(self) -> bool:
        """``True`` if :meth:`cancel` has been called."""
    @property
    def shield(self) -> bool:
        """
        ``True`` if this scope is shielded from external cancellation.

        While a scope is shielded, it will not receive cancellations from outside.

        """
    @shield.setter
    def shield(self, value: bool) -> None: ...
    def __enter__(self) -> CancelScope: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None: ...

def open_cancel_scope(*, shield: bool = False) -> CancelScope:
    """
    Open a cancel scope.

    :param shield: ``True`` to shield the cancel scope from external cancellation
    :return: a cancel scope

    .. deprecated:: 3.0
       Use :class:`~CancelScope` directly.

    """

class FailAfterContextManager(DeprecatedAsyncContextManager[CancelScope]):
    def __init__(self, cancel_scope: CancelScope) -> None: ...
    def __enter__(self) -> CancelScope: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None: ...

def fail_after(delay: float | None, shield: bool = False) -> FailAfterContextManager:
    """
    Create a context manager which raises a :class:`TimeoutError` if does not finish in time.

    :param delay: maximum allowed time (in seconds) before raising the exception, or ``None`` to
        disable the timeout
    :param shield: ``True`` to shield the cancel scope from external cancellation
    :return: a context manager that yields a cancel scope
    :rtype: :class:`~typing.ContextManager`\\[:class:`~anyio.CancelScope`\\]

    """
def move_on_after(delay: float | None, shield: bool = False) -> CancelScope:
    """
    Create a cancel scope with a deadline that expires after the given delay.

    :param delay: maximum allowed time (in seconds) before exiting the context block, or ``None``
        to disable the timeout
    :param shield: ``True`` to shield the cancel scope from external cancellation
    :return: a cancel scope

    """
def current_effective_deadline() -> DeprecatedAwaitableFloat:
    """
    Return the nearest deadline among all the cancel scopes effective for the current task.

    :return: a clock value from the event loop's internal clock (or ``float('inf')`` if
        there is no deadline in effect, or ``float('-inf')`` if the current scope has
        been cancelled)
    :rtype: float

    """
def create_task_group() -> TaskGroup:
    """
    Create a task group.

    :return: a task group

    """
