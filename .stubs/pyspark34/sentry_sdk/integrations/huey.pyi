from _typeshed import Incomplete
from huey.api import Result as Result, ResultGroup as ResultGroup, Task as Task
from sentry_sdk import Hub as Hub
from sentry_sdk._compat import reraise as reraise
from sentry_sdk._types import Event as Event, EventProcessor as EventProcessor, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.tracing import TRANSACTION_SOURCE_TASK as TRANSACTION_SOURCE_TASK, Transaction as Transaction
from sentry_sdk.utils import ExcInfo as ExcInfo, SENSITIVE_DATA_SUBSTITUTE as SENSITIVE_DATA_SUBSTITUTE, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])
HUEY_CONTROL_FLOW_EXCEPTIONS: Incomplete

class HueyIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...

def patch_enqueue() -> None: ...
def patch_execute() -> None: ...
