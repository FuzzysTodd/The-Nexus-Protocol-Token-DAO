import threading
from .aggregators import aggregate_mean as aggregate_mean
from .asset_registry import asset_registry as asset_registry
from .interfaces import Interface as Interface, Metric as Metric, MetricsMonitor as MetricsMonitor
from _typeshed import Incomplete
from typing import Any, Deque, Dict, Final, List
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic
from wandb.sdk.lib import telemetry as telemetry

logger: Incomplete
ROCM_SMI_CMD: Final[str]

def get_rocm_smi_stats() -> Dict[str, Any]: ...

class GPUAMDStats:
    """Stats for AMD GPU devices."""
    name: str
    samples: Deque[List[_Stats]]
    def __init__(self) -> None: ...
    @staticmethod
    def parse_stats(stats: Dict[str, str]) -> _Stats:
        """Parse stats from rocm-smi output."""
    def sample(self) -> None: ...
    def clear(self) -> None: ...
    def aggregate(self) -> dict: ...

class GPUAMD:
    """GPUAMD is a class for monitoring AMD GPU devices.

    Uses AMD's rocm_smi tool to get GPU stats.
    For the list of supported environments and devices, see
    https://github.com/RadeonOpenCompute/ROCm/blob/develop/docs/deploy/
    """
    name: Incomplete
    metrics: Incomplete
    metrics_monitor: Incomplete
    def __init__(self, interface: Interface, settings: SettingsStatic, shutdown_event: threading.Event) -> None: ...
    @classmethod
    def is_available(cls) -> bool: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...
    def probe(self) -> dict: ...
