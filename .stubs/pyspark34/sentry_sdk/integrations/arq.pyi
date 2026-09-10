from _typeshed import Incomplete
from arq.cron import CronJob as CronJob
from arq.jobs import Job as Job
from arq.typing import WorkerCoroutine as WorkerCoroutine
from arq.worker import Function as Function
from sentry_sdk import Hub as Hub
from sentry_sdk._compat import reraise as reraise
from sentry_sdk._types import Event as Event, EventProcessor as EventProcessor, ExcInfo as ExcInfo, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations.logging import ignore_logger as ignore_logger
from sentry_sdk.tracing import TRANSACTION_SOURCE_TASK as TRANSACTION_SOURCE_TASK, Transaction as Transaction
from sentry_sdk.utils import SENSITIVE_DATA_SUBSTITUTE as SENSITIVE_DATA_SUBSTITUTE, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, parse_version as parse_version

ARQ_CONTROL_FLOW_EXCEPTIONS: Incomplete

class ArqIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...

def patch_enqueue_job() -> None: ...
def patch_run_job() -> None: ...
def patch_create_worker() -> None: ...
