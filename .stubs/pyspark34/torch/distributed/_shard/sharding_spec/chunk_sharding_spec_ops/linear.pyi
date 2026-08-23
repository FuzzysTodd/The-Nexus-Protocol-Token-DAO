from torch.autograd import Function as Function
from torch.distributed._shard.sharded_tensor import ShardedTensor as ShardedTensor
from torch.distributed._shard.sharding_spec import ChunkShardingSpec as ChunkShardingSpec
from torch.distributed._shard.sharding_spec._internals import get_chunk_sharding_params as get_chunk_sharding_params, get_chunked_dim_size as get_chunked_dim_size, get_split_size as get_split_size
from torch.distributed._shard.sharding_spec.api import custom_sharding_spec_op as custom_sharding_spec_op
from torch.distributed.nn.functional import all_to_all_single as all_to_all_single

def sharded_linear(types, args, kwargs, pg):
    """
    Handles ``__torch_function__`` dispatch for ``torch.nn.functional.linear``.
    This method computes a sharded linear and has the following limitations:

    1. Supports only sharding of ``weight``.
    2. Supports only ``ChunkShardingSpec``.
    3. Supports only a single local shard per rank.
    4. Tailored for Megatron-LM style model(tensor) parallelism. Further API
       calls are needed if a fully synced local tensor is needed.
       Megatron-LM paper link: https://arxiv.org/abs/1909.08053

    Based on the dimension that the weight is sharded on, there are two
    algorithms:

    ROWWISE SHARDING
    ================
    For row-wise sharding the weight is sharded on dimension 1, but this is
    row-wise since the actual computation for the linear layer involves
    transposing the weight: :math:`y = xA^T + b`

    The overall algorithm can be best explained with an example. Let's assume
    the dims for x are (13 x 16) and A are (17 x 16) and A is sharded across
    4 GPUs creating shards of (17 x 4). The algorithm is as follows:

    1. First the input is split on the column dimension to create shards of
       (13 x 4) and communicated to all other ranks. Since we are running in
       an SPMD mode with each rank having distinct input, this is done via
       an all2all run on all ranks.
    2. Now each (13 x 4) shard on each GPU is multiplied with the local shard
       (4 x 17) (transposed) resulting in a (13 x 17) matrix which is the same
       size that we need for the global result which would be (13 x 16)
       multiplied by (16 x 17). But the final result needs to be aggregated
       across the rest of the ranks.
    3. Here we just return the partial result here. One can call API
       aggregate_partial_tensor_list to get the aggregated final result.
       The API uses a reduce_scatter operation ensuring each rank
       aggregates its own result. This is essentially a sum operation across
       all the (13 x 17) local computations we did for each rank.
    4. For partial result, we only add 1 / n of the bias term to the partial
       result. n is # of all GPUs.

    COLWISE SHARDING
    ================
    For col-wise sharding the weight is sharded on dimension 0, but this is
    col-wise since the actual computation for the linear layer involves
    transposing the weight: :math:`y = xA^T + b`

    The overall algorithm can be best explained with an example. Let's assume
    the dims for x are (13 x 17) and A are (16 x 17) and A is sharded across
    4 GPUs creating shards of (4 x 17). The algorithm is as follows:

    1. First the input is broadcasted to all ranks, since this is SPMD we
       actually do an all_gather for all the inputs resulting in 4 (13 x 17)
       inputs on each rank.
    2. Next we perform local matmuls by multiplying each input (13 x 17)
       with the local shard (17 x 4) (transposed). This results in 4 (13 x 4)
       matrices on each rank.
    3. Next, we stack them into a (4 x 13 x 4) tensor and build a sharded
       tensor across 4 ranks.
    4. To merge them into a fully-sync local tensor, one can call API
       merge_sharded_local_results.
       This API concat these 4 matrices and perform an all2all to share the
       appropriate (13 x 4) matrices to each rank. Specifically, each rank
       receives a (13 x 16) matrix which is basically the size of the result.
    5. If placements are not in order any appropriate rearrangement of rows
       are done for the (13 x 16) matrix and finally the bias term is added.
    """

class _BiasTensorNarrow(Function):
    """
    Since we now return the intermediate results in a col-wise sharding. We
    need to narrow the bias term in the forward while doing backward, we need
    to gather all gradients of narrowed bias across all ranks.
    """
    @staticmethod
    def forward(ctx, world_size, start_pos, chunk_size, weight, pg, bias): ...
    @staticmethod
    def backward(ctx, grad_output): ...

class _BiasTensorPartial(Function):
    """
    Since we now only return partial results in a row-wise sharding. We need to
    divide the bias term by the world size in the forward while doing backward,
    we need to skip this division op.
    """
    @staticmethod
    def forward(ctx, world_size, bias): ...
    @staticmethod
    def backward(ctx, grad_output): ...
