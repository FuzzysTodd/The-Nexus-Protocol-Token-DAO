from sentry_sdk import Hub as Hub
from sentry_sdk._types import MYPY as MYPY
from sentry_sdk.consts import OP as OP
from sentry_sdk.integrations.redis import RedisIntegration as RedisIntegration
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions
from typing import Any

def patch_redis_async_pipeline(pipeline_cls: Any) -> None: ...
def patch_redis_async_client(cls) -> None: ...
