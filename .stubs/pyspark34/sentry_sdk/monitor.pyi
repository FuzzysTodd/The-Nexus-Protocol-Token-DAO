import sentry_sdk
from _typeshed import Incomplete
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.utils import logger as logger

MAX_DOWNSAMPLE_FACTOR: int

class Monitor:
    """
    Performs health checks in a separate thread once every interval seconds
    and updates the internal state. Other parts of the SDK only read this state
    and act accordingly.
    """
    name: str
    transport: Incomplete
    interval: Incomplete
    def __init__(self, transport: sentry_sdk.transport.Transport, interval: float = 10) -> None: ...
    def run(self) -> None: ...
    def set_downsample_factor(self) -> None: ...
    def check_health(self) -> None:
        """
        Perform the actual health checks,
        currently only checks if the transport is rate-limited.
        TODO: augment in the future with more checks.
        """
    def is_healthy(self) -> bool: ...
    @property
    def downsample_factor(self) -> int: ...
    def kill(self) -> None: ...
    def __del__(self) -> None: ...
