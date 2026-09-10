import abc
import typing
from _typeshed import Incomplete
from tenacity import RetryCallState as RetryCallState

class retry_base(abc.ABC, metaclass=abc.ABCMeta):
    """Abstract base class for retry strategies."""
    @abc.abstractmethod
    def __call__(self, retry_state: RetryCallState) -> bool: ...
    def __and__(self, other: retry_base) -> retry_all: ...
    def __or__(self, other: retry_base) -> retry_any: ...

RetryBaseT: Incomplete

class _retry_never(retry_base):
    """Retry strategy that never rejects any result."""
    def __call__(self, retry_state: RetryCallState) -> bool: ...

retry_never: Incomplete

class _retry_always(retry_base):
    """Retry strategy that always rejects any result."""
    def __call__(self, retry_state: RetryCallState) -> bool: ...

retry_always: Incomplete

class retry_if_exception(retry_base):
    """Retry strategy that retries if an exception verifies a predicate."""
    predicate: Incomplete
    def __init__(self, predicate: typing.Callable[[BaseException], bool]) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class retry_if_exception_type(retry_if_exception):
    """Retries if an exception has been raised of one or more types."""
    exception_types: Incomplete
    def __init__(self, exception_types: typing.Type[BaseException] | typing.Tuple[typing.Type[BaseException], ...] = ...) -> None: ...

class retry_if_not_exception_type(retry_if_exception):
    """Retries except an exception has been raised of one or more types."""
    exception_types: Incomplete
    def __init__(self, exception_types: typing.Type[BaseException] | typing.Tuple[typing.Type[BaseException], ...] = ...) -> None: ...

class retry_unless_exception_type(retry_if_exception):
    """Retries until an exception is raised of one or more types."""
    exception_types: Incomplete
    def __init__(self, exception_types: typing.Type[BaseException] | typing.Tuple[typing.Type[BaseException], ...] = ...) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class retry_if_exception_cause_type(retry_base):
    """Retries if any of the causes of the raised exception is of one or more types.

    The check on the type of the cause of the exception is done recursively (until finding
    an exception in the chain that has no `__cause__`)
    """
    exception_cause_types: Incomplete
    def __init__(self, exception_types: typing.Type[BaseException] | typing.Tuple[typing.Type[BaseException], ...] = ...) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class retry_if_result(retry_base):
    """Retries if the result verifies a predicate."""
    predicate: Incomplete
    def __init__(self, predicate: typing.Callable[[typing.Any], bool]) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class retry_if_not_result(retry_base):
    """Retries if the result refutes a predicate."""
    predicate: Incomplete
    def __init__(self, predicate: typing.Callable[[typing.Any], bool]) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class retry_if_exception_message(retry_if_exception):
    """Retries if an exception message equals or matches."""
    def __init__(self, message: str | None = None, match: str | None = None) -> None: ...

class retry_if_not_exception_message(retry_if_exception_message):
    """Retries until an exception message equals or matches."""
    predicate: Incomplete
    def __init__(self, message: str | None = None, match: str | None = None) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class retry_any(retry_base):
    """Retries if any of the retries condition is valid."""
    retries: Incomplete
    def __init__(self, *retries: retry_base) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...

class retry_all(retry_base):
    """Retries if all the retries condition are valid."""
    retries: Incomplete
    def __init__(self, *retries: retry_base) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> bool: ...
