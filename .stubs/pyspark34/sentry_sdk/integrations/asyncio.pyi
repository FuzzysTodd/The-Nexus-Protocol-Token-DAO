from sentry_sdk._compat import reraise as reraise
from sentry_sdk._types import ExcInfo as ExcInfo, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.utils import event_from_exception as event_from_exception
from typing import Any

def get_name(coro: Any) -> str: ...
def patch_asyncio() -> None: ...

class AsyncioIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
