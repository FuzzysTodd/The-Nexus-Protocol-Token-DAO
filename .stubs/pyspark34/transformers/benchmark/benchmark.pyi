from ..configuration_utils import PretrainedConfig as PretrainedConfig
from ..models.auto.modeling_auto import MODEL_MAPPING as MODEL_MAPPING, MODEL_WITH_LM_HEAD_MAPPING as MODEL_WITH_LM_HEAD_MAPPING
from ..utils import is_py3nvml_available as is_py3nvml_available, is_torch_available as is_torch_available, logging as logging
from .benchmark_args import PyTorchBenchmarkArguments as PyTorchBenchmarkArguments
from .benchmark_utils import Benchmark as Benchmark, Memory as Memory, MemorySummary as MemorySummary, measure_peak_memory_cpu as measure_peak_memory_cpu, start_memory_tracing as start_memory_tracing, stop_memory_tracing as stop_memory_tracing
from _typeshed import Incomplete

logger: Incomplete

class PyTorchBenchmark(Benchmark):
    args: PyTorchBenchmarkArguments
    configs: PretrainedConfig
    framework: str
    @property
    def framework_version(self): ...
