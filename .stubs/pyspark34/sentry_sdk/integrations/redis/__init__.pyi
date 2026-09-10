from _typeshed import Incomplete
from sentry_sdk import Hub as Hub
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP, SPANDATA as SPANDATA
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.tracing import Span as Span
from sentry_sdk.utils import SENSITIVE_DATA_SUBSTITUTE as SENSITIVE_DATA_SUBSTITUTE, capture_internal_exceptions as capture_internal_exceptions, logger as logger
from typing import Any

def patch_redis_pipeline(pipeline_cls: Any, is_cluster: bool, get_command_args_fn: Any) -> None: ...

class RedisIntegration(Integration):
    identifier: str
    max_data_size: Incomplete
    def __init__(self, max_data_size: int = ...) -> None: ...
    @staticmethod
    def setup_once() -> None: ...

def patch_redis_client(cls, is_cluster: bool) -> None:
    """
    This function can be used to instrument custom redis client classes or
    subclasses.
    """
