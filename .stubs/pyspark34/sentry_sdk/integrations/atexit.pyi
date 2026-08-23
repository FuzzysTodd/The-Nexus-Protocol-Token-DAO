from _typeshed import Incomplete
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.utils import logger as logger
from typing import Any

def default_callback(pending: int, timeout: int) -> None:
    """This is the default shutdown callback that is set on the options.
    It prints out a message to stderr that informs the user that some events
    are still pending and the process is waiting for them to flush out.
    """

class AtexitIntegration(Integration):
    identifier: str
    callback: Incomplete
    def __init__(self, callback: Any | None = None) -> None: ...
    @staticmethod
    def setup_once() -> None: ...
