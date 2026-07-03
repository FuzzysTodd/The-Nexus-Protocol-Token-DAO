from _typeshed import Incomplete
from celery import Celery as Celery, Task
from sentry_sdk._compat import reraise as reraise
from sentry_sdk._functools import wraps as wraps
from sentry_sdk._types import Event as Event, EventProcessor as EventProcessor, ExcInfo as ExcInfo, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.api import continue_trace as continue_trace
from sentry_sdk.consts import OP as OP
from sentry_sdk.crons import MonitorStatus as MonitorStatus, capture_checkin as capture_checkin
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations.logging import ignore_logger as ignore_logger
from sentry_sdk.tracing import BAGGAGE_HEADER_NAME as BAGGAGE_HEADER_NAME, TRANSACTION_SOURCE_TASK as TRANSACTION_SOURCE_TASK
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, logger as logger, match_regex_list as match_regex_list
from typing import Any, Callable, Dict, List, TypeVar

F = TypeVar('F', bound=Callable[..., Any])
CELERY_CONTROL_FLOW_EXCEPTIONS: Incomplete

class CeleryIntegration(Integration):
    identifier: str
    propagate_traces: Incomplete
    monitor_beat_tasks: Incomplete
    exclude_beat_tasks: Incomplete
    def __init__(self, propagate_traces: bool = True, monitor_beat_tasks: bool = False, exclude_beat_tasks: List[str] | None = None) -> None: ...
    @staticmethod
    def setup_once() -> None: ...

def crons_task_success(sender: Task, **kwargs: Dict[Any, Any]) -> None: ...
def crons_task_failure(sender: Task, **kwargs: Dict[Any, Any]) -> None: ...
def crons_task_retry(sender: Task, **kwargs: Dict[Any, Any]) -> None: ...
