import abc
import threading
from _typeshed import Incomplete
from tenacity import RetryCallState as RetryCallState, _utils

class stop_base(abc.ABC, metaclass=abc.ABCMeta):
    """Abstract base class for stop strategies."""
    @abc.abstractmethod
    def __call__(self, retry_state: RetryCallState) -> bool: ...
    def __and__(self, other: stop_base) -> stop_all: ...
    def __or__(self, other: stop_base) -> stop_any: ...

StopBaseT: Incomplete

class stop_any(stop_base):
    """Stop if any of the stop condition is valid."""
    stops: Incomplete
    def __init__(self, *stops: stop_base) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class stop_all(stop_base):
    """Stop if all the stop conditions are valid."""
    stops: Incomplete
    def __init__(self, *stops: stop_base) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class _stop_never(stop_base):
    """Never stop."""
    def __call__(self, retry_state: RetryCallState) -> bool: ...

stop_never: Incomplete

class stop_when_event_set(stop_base):
    """Stop when the given event is set."""
    event: Incomplete
    def __init__(self, event: threading.Event) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class stop_after_attempt(stop_base):
    """Stop when the previous attempt >= max_attempt."""
    max_attempt_number: Incomplete
    def __init__(self, max_attempt_number: int) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class stop_after_delay(stop_base):
    """Stop when the time from the first attempt >= limit."""
    max_delay: Incomplete
    def __init__(self, max_delay: _utils.time_unit_type) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...
