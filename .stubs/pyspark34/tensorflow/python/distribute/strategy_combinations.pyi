from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.distribute import central_storage_strategy as central_storage_strategy, cluster_resolver as cluster_resolver, collective_all_reduce_strategy as collective_all_reduce_strategy, combinations as combinations, distribution_strategy_context as distribution_strategy_context, multi_process_runner as multi_process_runner, multi_worker_test_base as multi_worker_test_base, parameter_server_strategy_v2 as parameter_server_strategy_v2, sharded_variable as sharded_variable, test_util as test_util
from tensorflow.python.distribute.cluster_resolver import tpu_cluster_resolver as tpu_cluster_resolver
from tensorflow.python.eager import context as context, remote as remote
from tensorflow.python.framework import errors as errors
from tensorflow.python.platform import flags as flags
from tensorflow.python.tpu import tpu_strategy_util as tpu_strategy_util
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.util.tf_export import tf_export as tf_export

CollectiveAllReduceExtended = collective_all_reduce_strategy.CollectiveAllReduceExtended
MirroredStrategy: Incomplete
CentralStorageStrategy: Incomplete
OneDeviceStrategy: Incomplete
CollectiveAllReduceStrategy = collective_all_reduce_strategy.CollectiveAllReduceStrategy
DEFAULT_PARTITIONER: Incomplete
default_strategy: Incomplete
one_device_strategy: Incomplete
one_device_strategy_gpu: Incomplete
one_device_strategy_on_worker_1: Incomplete
one_device_strategy_gpu_on_worker_1: Incomplete
tpu_strategy: Incomplete
tpu_strategy_packed_var: Incomplete
tpu_strategy_spmd: Incomplete
tpu_strategy_one_step: Incomplete
tpu_strategy_one_core: Incomplete
tpu_strategy_one_step_one_core: Incomplete
cloud_tpu_strategy: Incomplete
mirrored_strategy_with_one_cpu: Incomplete
mirrored_strategy_with_one_gpu: Incomplete
mirrored_strategy_with_gpu_and_cpu: Incomplete
mirrored_strategy_with_two_cpus: Incomplete
mirrored_strategy_with_two_gpus: Incomplete
mirrored_strategy_with_two_gpus_no_merge_call: Incomplete
mirrored_strategy_with_cpu_1_and_2: Incomplete
central_storage_strategy_with_two_gpus: Incomplete
central_storage_strategy_with_gpu_and_cpu: Incomplete
multi_worker_mirrored_2x1_cpu: Incomplete
multi_worker_mirrored_2x1_gpu: Incomplete
multi_worker_mirrored_2x1_gpu_noshare: Incomplete
multi_worker_mirrored_2x2_gpu: Incomplete
multi_worker_mirrored_2x2_gpu_no_merge_call: Incomplete
multi_worker_mirrored_4x1_cpu: Incomplete

def parameter_server_strategy_fn(name, num_workers, num_ps, required_gpus: int = 0, variable_partitioner=...): ...

parameter_server_strategy_3worker_2ps_cpu: Incomplete
parameter_server_strategy_1worker_2ps_cpu: Incomplete
parameter_server_strategy_3worker_2ps_1gpu: Incomplete
parameter_server_strategy_1worker_2ps_1gpu: Incomplete
graph_and_eager_modes: Incomplete

def set_virtual_cpus_to_at_least(num_virtual_cpus) -> None: ...

strategies_minus_tpu: Incomplete
strategies_minus_default_and_tpu: Incomplete
tpu_strategies: Incomplete
all_strategies_minus_default: Incomplete
all_strategies: Incomplete
two_replica_strategies: Incomplete
four_replica_strategies: Incomplete
multidevice_strategies: Incomplete
multiworker_strategies: Incomplete

def strategy_minus_tpu_combinations(): ...
def tpu_strategy_combinations(): ...
def all_strategy_combinations(): ...
def all_strategy_minus_default_and_tpu_combinations(): ...
def all_strategy_combinations_minus_default(): ...
