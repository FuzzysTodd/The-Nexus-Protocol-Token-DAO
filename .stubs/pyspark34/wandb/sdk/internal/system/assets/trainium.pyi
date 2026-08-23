import dataclasses
import threading
from .aggregators import aggregate_mean as aggregate_mean
from .asset_registry import asset_registry as asset_registry
from .interfaces import Interface as Interface, Metric as Metric, MetricsMonitor as MetricsMonitor
from _typeshed import Incomplete
from typing import Deque, Dict, Final, Tuple
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic
from wandb.sdk.lib import telemetry as telemetry

logger: Incomplete
NEURON_MONITOR_DEFAULT_CONFIG: Final[dict]
NEURON_LS_COMMAND: Final[Tuple[str, str]]
NEURON_MONITOR_PATH: Final[str]

@dataclasses.dataclass
class _NeuronCoreMemoryUsage:
    constants: int
    model_code: int
    model_shared_scratchpad: int
    runtime_memory: int
    tensors: int
    def __init__(self, constants, model_code, model_shared_scratchpad, runtime_memory, tensors) -> None: ...

@dataclasses.dataclass
class _HostMemoryUsage:
    application_memory: int
    constants: int
    dma_buffers: int
    tensors: int
    def __init__(self, application_memory, constants, dma_buffers, tensors) -> None: ...

@dataclasses.dataclass
class _Stats:
    neuroncore_utilization: Dict[int, float]
    host_total_memory_usage: int
    neuron_device_total_memory_usage: int
    host_memory_usage: _HostMemoryUsage
    neuroncore_memory_usage: Dict[int, _NeuronCoreMemoryUsage]
    def __init__(self, neuroncore_utilization, host_total_memory_usage, neuron_device_total_memory_usage, host_memory_usage, neuroncore_memory_usage) -> None: ...

class NeuronCoreStats:
    """AWS Trainium stats."""
    name: str
    samples: Deque[_Stats]
    def write_neuron_monitor_config(self) -> None:
        """Write neuron monitor config file."""
    def neuron_monitor(self) -> None:
        """Run neuron-monitor in a separate process to collect raw data."""
    pid: Incomplete
    neuron_monitor_config_path: Incomplete
    raw_samples: Incomplete
    shutdown_event: Incomplete
    neuron_monitor_thread: Incomplete
    def __init__(self, pid: int, neuron_monitor_config_path: str | None) -> None: ...
    def setup(self) -> None:
        """Start the neuron-monitor thread for collecting raw data."""
    def teardown(self) -> None:
        """Stop the neuron-monitor thread."""
    def sample(self) -> None: ...
    def clear(self) -> None: ...
    @staticmethod
    def flatten_stats(sample: _Stats) -> dict:
        """Flatten _Stats object into a flat dict of numbers."""
    def aggregate(self) -> dict: ...

class Trainium:
    name: Incomplete
    metrics: Incomplete
    metrics_monitor: Incomplete
    def __init__(self, interface: Interface, settings: SettingsStatic, shutdown_event: threading.Event) -> None: ...
    @classmethod
    def is_available(cls) -> bool: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...
    def probe(self) -> dict: ...
