from typing import Sequence
from wandb.errors import UnsupportedError as UnsupportedError
from wandb.sdk import wandb_run as wandb_run
from wandb.sdk.lib.wburls import wburls as wburls

class _Requires:
    """Internal feature class."""
    def __init__(self, features: str | Sequence[str]) -> None: ...
    def require_require(self) -> None: ...
    def require_service(self) -> None: ...
    def require_nexus(self) -> None: ...
    def apply(self) -> None:
        """Call require_* method for supported features."""

def require(requirement: str | Sequence[str] | None = None, experiment: str | Sequence[str] | None = None) -> None:
    """Indicate which experimental features are used by the script.

    Args:
        requirement: (str or list) Features to require
        experiment: (str or list) Features to require

    Raises:
        wandb.errors.UnsupportedError: if not supported
    """
