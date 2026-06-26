import wandb.sdk
from _typeshed import Incomplete
from typing import Any, Dict, Protocol, Sequence, TypeVar
from wandb.sdk.lib.timer import Timer as Timer

logger: Incomplete
AutologInitArgs = Dict[str, Any] | None
K = TypeVar('K', bound=str)
V = TypeVar('V')

class Response(Protocol[K, V]):
    def __getitem__(self, key: K) -> V: ...
    def get(self, key: K, default: V | None = None) -> V | None: ...

class ArgumentResponseResolver(Protocol):
    def __call__(self, args: Sequence[Any], kwargs: Dict[str, Any], response: Response, start_time: float, time_elapsed: float) -> Dict[str, Any] | None: ...

class PatchAPI:
    name: Incomplete
    original_methods: Incomplete
    symbols: Incomplete
    resolver: Incomplete
    def __init__(self, name: str, symbols: Sequence[str], resolver: ArgumentResponseResolver) -> None:
        """Patches the API to log wandb Media or metrics."""
    @property
    def set_api(self) -> Any:
        """Returns the API module."""
    def patch(self, run: wandb.sdk.wandb_run.Run) -> None:
        """Patches the API to log media or metrics to W&B."""
    def unpatch(self) -> None:
        """Unpatches the API."""

class AutologAPI:
    def __init__(self, name: str, symbols: Sequence[str], resolver: ArgumentResponseResolver, telemetry_feature: str | None = None) -> None:
        """Autolog API calls to W&B."""
    def __call__(self, init: AutologInitArgs = None) -> None:
        """Enable autologging."""
    def enable(self, init: AutologInitArgs = None) -> None:
        """Enable autologging.

        Args:
            init: Optional dictionary of arguments to pass to wandb.init().

        """
    def disable(self) -> None:
        """Disable autologging."""
