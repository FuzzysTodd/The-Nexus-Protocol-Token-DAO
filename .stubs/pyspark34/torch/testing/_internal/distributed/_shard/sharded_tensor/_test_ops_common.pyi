from torch.distributed._shard.sharding_spec import ChunkShardingSpec as ChunkShardingSpec, EnumerableShardingSpec as EnumerableShardingSpec, ShardMetadata as ShardMetadata
from torch.distributed._shard.sharding_spec._internals import get_chunked_dim_size as get_chunked_dim_size, get_split_size as get_split_size

def generate_chunk_sharding_specs_for_test(sharding_dim): ...
def generate_enumerable_sharding_specs_for_test(): ...
def generate_local_weight_sharding_params_for_test(local_weight, sharded_dim, gpu_num, spec, rank):
    """
    Shard the local weight based the given spec, so we can compare against
    the one from sharded tensor.

    Args:
        local_weight: weight matrix to be sharded.
        sharded_dim: The dimension which we shard on.
        gpu_num: number of ranks.
        spec: shareding spec.
        rank: # of cuda process.

    Returns:
        start_pos: start position of sharded weight on the given rank.
        chunk_size: chunk size of sharded weight on the given rank.
    """
def clone_module_parameter(module, param_name):
    """
    Clone a parameter from a given existing module.

    Args:
        module (:class:`torch.nn.Module`): Module whose parameter needs to be cloned.
        param_name (str): Name of the parameter of ``module`` that needs to be cloned.

    Returns: cloned tensor as :class:`torch.nn.Parameter`.
    """
def gen_binary_op_func(python_op, inplace: bool = False): ...
