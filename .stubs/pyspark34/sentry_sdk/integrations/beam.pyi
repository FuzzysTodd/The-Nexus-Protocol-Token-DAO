from sentry_sdk._compat import reraise as reraise
from sentry_sdk._functools import wraps as wraps
from sentry_sdk._types import ExcInfo as ExcInfo, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.client import Client as Client
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.integrations.logging import ignore_logger as ignore_logger
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception
from typing import Any, Callable, TypeVar

T = TypeVar('T')
F = TypeVar('F', bound=Callable[..., Any])
WRAPPED_FUNC: str
INSPECT_FUNC: str
USED_FUNC: str

class BeamIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...

def raise_exception(client: Client | None) -> None:
    """
    Raise an exception. If the client is not in the hub, rebind it.
    """
