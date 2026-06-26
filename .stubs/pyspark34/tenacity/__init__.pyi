import abc
import types
import typing as t
from .after import after_log as after_log, after_nothing as after_nothing
from .before import before_log as before_log, before_nothing as before_nothing
from .before_sleep import before_sleep_log as before_sleep_log, before_sleep_nothing as before_sleep_nothing
from .nap import sleep as sleep, sleep_using_event as sleep_using_event
from .retry import RetryBaseT, retry_all as retry_all, retry_always as retry_always, retry_any as retry_any, retry_base as retry_base, retry_if_exception as retry_if_exception, retry_if_exception_cause_type as retry_if_exception_cause_type, retry_if_exception_message as retry_if_exception_message, retry_if_exception_type as retry_if_exception_type, retry_if_not_exception_message as retry_if_not_exception_message, retry_if_not_exception_type as retry_if_not_exception_type, retry_if_not_result as retry_if_not_result, retry_if_result as retry_if_result, retry_never as retry_never, retry_unless_exception_type as retry_unless_exception_type
from .stop import StopBaseT, stop_after_attempt as stop_after_attempt, stop_after_delay as stop_after_delay, stop_all as stop_all, stop_any as stop_any, stop_never as stop_never, stop_when_event_set as stop_when_event_set
from .wait import WaitBaseT, wait_chain as wait_chain, wait_combine as wait_combine, wait_exponential as wait_exponential, wait_exponential_jitter as wait_exponential_jitter, wait_fixed as wait_fixed, wait_incrementing as wait_incrementing, wait_none as wait_none, wait_random as wait_random, wait_random_exponential as wait_full_jitter, wait_random_exponential as wait_random_exponential
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from tenacity._asyncio import AsyncRetrying as AsyncRetrying

__all__ = ['retry_base', 'retry_all', 'retry_always', 'retry_any', 'retry_if_exception', 'retry_if_exception_type', 'retry_if_exception_cause_type', 'retry_if_not_exception_type', 'retry_if_not_result', 'retry_if_result', 'retry_never', 'retry_unless_exception_type', 'retry_if_exception_message', 'retry_if_not_exception_message', 'sleep', 'sleep_using_event', 'stop_after_attempt', 'stop_after_delay', 'stop_all', 'stop_any', 'stop_never', 'stop_when_event_set', 'wait_chain', 'wait_combine', 'wait_exponential', 'wait_fixed', 'wait_incrementing', 'wait_none', 'wait_random', 'wait_random_exponential', 'wait_full_jitter', 'wait_exponential_jitter', 'before_log', 'before_nothing', 'after_log', 'after_nothing', 'before_sleep_log', 'before_sleep_nothing', 'retry', 'WrappedFn', 'TryAgain', 'NO_RESULT', 'DoAttempt', 'DoSleep', 'BaseAction', 'RetryAction', 'RetryError', 'AttemptManager', 'BaseRetrying', 'Retrying', 'Future', 'RetryCallState', 'AsyncRetrying']

WrappedFnReturnT = t.TypeVar('WrappedFnReturnT')
WrappedFn = t.TypeVar('WrappedFn', bound=t.Callable[..., t.Any])

class TryAgain(Exception):
    """Always retry the executed function when raised."""

NO_RESULT: Incomplete

class DoAttempt: ...
class DoSleep(float): ...

class BaseAction:
    """Base class for representing actions to take by retry object.

    Concrete implementations must define:
    - __init__: to initialize all necessary fields
    - REPR_FIELDS: class variable specifying attributes to include in repr(self)
    - NAME: for identification in retry object methods and callbacks
    """
    REPR_FIELDS: t.Sequence[str]
    NAME: str | None

class RetryAction(BaseAction):
    REPR_FIELDS: Incomplete
    NAME: str
    sleep: Incomplete
    def __init__(self, sleep: t.SupportsFloat) -> None: ...

class RetryError(Exception):
    """Encapsulates the last attempt instance right before giving up."""
    last_attempt: Incomplete
    def __init__(self, last_attempt: Future) -> None: ...
    def reraise(self) -> t.NoReturn: ...

class AttemptManager:
    """Manage attempt context."""
    retry_state: Incomplete
    def __init__(self, retry_state: RetryCallState) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: t.Type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> bool | None: ...

class BaseRetrying(ABC, metaclass=abc.ABCMeta):
    sleep: Incomplete
    stop: Incomplete
    wait: Incomplete
    retry: Incomplete
    before: Incomplete
    after: Incomplete
    before_sleep: Incomplete
    reraise: Incomplete
    retry_error_cls: Incomplete
    retry_error_callback: Incomplete
    def __init__(self, sleep: t.Callable[[int | float], None] = ..., stop: StopBaseT = ..., wait: WaitBaseT = ..., retry: RetryBaseT = ..., before: t.Callable[[RetryCallState], None] = ..., after: t.Callable[[RetryCallState], None] = ..., before_sleep: t.Callable[[RetryCallState], None] | None = None, reraise: bool = False, retry_error_cls: t.Type[RetryError] = ..., retry_error_callback: t.Callable[[RetryCallState], t.Any] | None = None) -> None: ...
    def copy(self, sleep: t.Callable[[int | float], None] | object = ..., stop: StopBaseT | object = ..., wait: WaitBaseT | object = ..., retry: retry_base | object = ..., before: t.Callable[[RetryCallState], None] | object = ..., after: t.Callable[[RetryCallState], None] | object = ..., before_sleep: t.Callable[[RetryCallState], None] | None | object = ..., reraise: bool | object = ..., retry_error_cls: t.Type[RetryError] | object = ..., retry_error_callback: t.Callable[[RetryCallState], t.Any] | None | object = ...) -> BaseRetrying:
        """Copy this object with some parameters changed if needed."""
    @property
    def statistics(self) -> t.Dict[str, t.Any]:
        """Return a dictionary of runtime statistics.

        This dictionary will be empty when the controller has never been
        ran. When it is running or has ran previously it should have (but
        may not) have useful and/or informational keys and values when
        running is underway and/or completed.

        .. warning:: The keys in this dictionary **should** be some what
                     stable (not changing), but there existence **may**
                     change between major releases as new statistics are
                     gathered or removed so before accessing keys ensure that
                     they actually exist and handle when they do not.

        .. note:: The values in this dictionary are local to the thread
                  running call (so if multiple threads share the same retrying
                  object - either directly or indirectly) they will each have
                  there own view of statistics they have collected (in the
                  future we may provide a way to aggregate the various
                  statistics from each thread).
        """
    def wraps(self, f: WrappedFn) -> WrappedFn:
        """Wrap a function for retrying.

        :param f: A function to wraps for retrying.
        """
    def begin(self) -> None: ...
    def iter(self, retry_state: RetryCallState) -> DoAttempt | DoSleep | t.Any: ...
    def __iter__(self) -> t.Generator[AttemptManager, None, None]: ...
    @abstractmethod
    def __call__(self, fn: t.Callable[..., WrappedFnReturnT], *args: t.Any, **kwargs: t.Any) -> WrappedFnReturnT: ...

class Retrying(BaseRetrying):
    """Retrying controller."""
    def __call__(self, fn: t.Callable[..., WrappedFnReturnT], *args: t.Any, **kwargs: t.Any) -> WrappedFnReturnT: ...

class Future(FutureGenericT):
    """Encapsulates a (future or past) attempted call to a target function."""
    attempt_number: Incomplete
    def __init__(self, attempt_number: int) -> None: ...
    @property
    def failed(self) -> bool:
        """Return whether a exception is being held in this future."""
    @classmethod
    def construct(cls, attempt_number: int, value: t.Any, has_exception: bool) -> Future:
        """Construct a new Future object."""

class RetryCallState:
    """State related to a single call wrapped with Retrying."""
    start_time: Incomplete
    retry_object: Incomplete
    fn: Incomplete
    args: Incomplete
    kwargs: Incomplete
    attempt_number: int
    outcome: Incomplete
    outcome_timestamp: Incomplete
    idle_for: float
    next_action: Incomplete
    def __init__(self, retry_object: BaseRetrying, fn: WrappedFn | None, args: t.Any, kwargs: t.Any) -> None: ...
    @property
    def seconds_since_start(self) -> float | None: ...
    def prepare_for_next_attempt(self) -> None: ...
    def set_result(self, val: t.Any) -> None: ...
    def set_exception(self, exc_info: t.Tuple[t.Type[BaseException], BaseException, types.TracebackType | None]) -> None: ...

@t.overload
def retry(func: WrappedFn) -> WrappedFn: ...
@t.overload
def retry(sleep: t.Callable[[int | float], t.Awaitable[None] | None] = ..., stop: StopBaseT = ..., wait: WaitBaseT = ..., retry: RetryBaseT = ..., before: t.Callable[[RetryCallState], None] = ..., after: t.Callable[[RetryCallState], None] = ..., before_sleep: t.Callable[[RetryCallState], None] | None = None, reraise: bool = False, retry_error_cls: t.Type['RetryError'] = ..., retry_error_callback: t.Callable[[RetryCallState], t.Any] | None = None) -> t.Callable[[WrappedFn], WrappedFn]: ...
