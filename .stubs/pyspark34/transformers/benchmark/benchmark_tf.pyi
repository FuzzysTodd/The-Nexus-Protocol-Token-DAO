import tensorflow as tf
from ..configuration_utils import PretrainedConfig as PretrainedConfig
from ..models.auto.modeling_tf_auto import TF_MODEL_MAPPING as TF_MODEL_MAPPING, TF_MODEL_WITH_LM_HEAD_MAPPING as TF_MODEL_WITH_LM_HEAD_MAPPING
from ..utils import is_py3nvml_available as is_py3nvml_available, is_tf_available as is_tf_available, logging as logging
from .benchmark_args_tf import TensorFlowBenchmarkArguments as TensorFlowBenchmarkArguments
from .benchmark_utils import Benchmark as Benchmark, Memory as Memory, MemorySummary as MemorySummary, measure_peak_memory_cpu as measure_peak_memory_cpu, start_memory_tracing as start_memory_tracing, stop_memory_tracing as stop_memory_tracing
from _typeshed import Incomplete

logger: Incomplete

def run_with_tf_optimizations(do_eager_mode: bool, use_xla: bool): ...
def random_input_ids(batch_size: int, sequence_length: int, vocab_size: int) -> [tf.Tensor]: ...

class TensorFlowBenchmark(Benchmark):
    args: TensorFlowBenchmarkArguments
    configs: PretrainedConfig
    framework: str
    @property
    def framework_version(self): ...
