from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def tpu_partitioned_input(inputs, partition_dim: int = 0, name: Incomplete | None = None):
    """An op that groups a list of partitioned inputs together. This op

  Args:
    inputs: A list of at least 1 `Tensor` objects with the same type.
      A list of partitioned inputs which must have the same shape.
    partition_dim: An optional `int`. Defaults to `0`.
      An integer describles which dimension is partitioned. -1 means
      those inputs are replicated.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `inputs`.
  """

TPUPartitionedInput: Incomplete

def tpu_partitioned_input_eager_fallback(inputs, partition_dim, name, ctx): ...
def tpu_partitioned_input_v2(inputs, partition_dims, is_packed: bool = False, name: Incomplete | None = None):
    """An op that groups a list of partitioned inputs together. Supports ND sharding.

  Args:
    inputs: A list of at least 1 `Tensor` objects with the same type.
      A list of partitioned inputs which must have the same shape.
    partition_dims: A list of `ints`.
      A list of integers describing how each dimension is partitioned. Emptiness
      indicates the inputs are replicated.
    is_packed: An optional `bool`. Defaults to `False`.
      Indicates whether the input is a packed resource.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `inputs`.
  """

TPUPartitionedInputV2: Incomplete

def tpu_partitioned_input_v2_eager_fallback(inputs, partition_dims, is_packed, name, ctx): ...
def tpu_partitioned_output(inputs, num_splits, partition_dim: int = 0, name: Incomplete | None = None):
    """An op that demultiplexes a tensor to be sharded by XLA to a list of partitioned

  outputs outside the XLA computation.

  Args:
    inputs: A `Tensor`.
      A tensor which represents the full shape of partitioned tensors.
    num_splits: An `int` that is `>= 1`.
    partition_dim: An optional `int`. Defaults to `0`.
      An integer describles which dimension is partitioned.
    name: A name for the operation (optional).

  Returns:
    A list of `num_splits` `Tensor` objects with the same type as `inputs`.
  """

TPUPartitionedOutput: Incomplete

def tpu_partitioned_output_eager_fallback(inputs, num_splits, partition_dim, name, ctx): ...
def tpu_partitioned_output_v2(inputs, num_splits, partition_dims, name: Incomplete | None = None):
    """An op that demultiplexes a tensor to be sharded by XLA to a list of partitioned

  outputs outside the XLA computation. Supports ND sharding.

  Args:
    inputs: A `Tensor`.
      A tensor which represents the full shape of partitioned tensors.
    num_splits: An `int` that is `>= 1`.
    partition_dims: A list of `ints`.
      A list of integers describing how each dimension is partitioned. Emptiness
      indicates the inputs are replicated.
    name: A name for the operation (optional).

  Returns:
    A list of `num_splits` `Tensor` objects with the same type as `inputs`.
  """

TPUPartitionedOutputV2: Incomplete

def tpu_partitioned_output_v2_eager_fallback(inputs, num_splits, partition_dims, name, ctx): ...
