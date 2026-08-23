from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def collective_all_to_all_v3(input, communicator, group_assignment, timeout_seconds: int = 0, name: Incomplete | None = None):
    """Mutually exchanges multiple tensors of identical type and shape.

  Args:
    input: A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `half`, `float64`, `int32`, `int64`.
    communicator: A `Tensor` of type `resource`.
    group_assignment: A `Tensor` of type `int32`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

CollectiveAllToAllV3: Incomplete

def collective_all_to_all_v3_eager_fallback(input, communicator, group_assignment, timeout_seconds, name, ctx): ...

class _CollectiveAssignGroupV2Output(NamedTuple):
    group_size: Incomplete
    group_key: Incomplete

def collective_assign_group_v2(group_assignment, device_index, base_key, name: Incomplete | None = None):
    """Assign group keys based on group assignment.

  Args:
    group_assignment: A `Tensor` of type `int32`.
    device_index: A `Tensor` of type `int32`.
    base_key: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (group_size, group_key).

    group_size: A `Tensor` of type `int32`.
    group_key: A `Tensor` of type `int32`.
  """

CollectiveAssignGroupV2: Incomplete

def collective_assign_group_v2_eager_fallback(group_assignment, device_index, base_key, name, ctx): ...
def collective_bcast_recv(T, group_size, group_key, instance_key, shape, communication_hint: str = 'auto', timeout_seconds: int = 0, name: Incomplete | None = None):
    '''Receives a tensor value broadcast from another device.

  Args:
    T: A `tf.DType` from: `tf.bool, tf.float32, tf.half, tf.float64, tf.int32, tf.int64`.
    group_size: An `int`.
    group_key: An `int`.
    instance_key: An `int`.
    shape: A `tf.TensorShape` or list of `ints`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `T`.
  '''

CollectiveBcastRecv: Incomplete

def collective_bcast_recv_eager_fallback(T, group_size, group_key, instance_key, shape, communication_hint, timeout_seconds, name, ctx): ...
def collective_bcast_recv_v2(group_size, group_key, instance_key, shape, T, communication_hint: str = 'auto', timeout_seconds: int = 0, name: Incomplete | None = None):
    '''Receives a tensor value broadcast from another device.

  Args:
    group_size: A `Tensor` of type `int32`.
    group_key: A `Tensor` of type `int32`.
    instance_key: A `Tensor` of type `int32`.
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    T: A `tf.DType` from: `tf.bool, tf.float32, tf.half, tf.float64, tf.int32, tf.int64`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `T`.
  '''

CollectiveBcastRecvV2: Incomplete

def collective_bcast_recv_v2_eager_fallback(group_size, group_key, instance_key, shape, T, communication_hint, timeout_seconds, name, ctx): ...
def collective_bcast_send(input, group_size, group_key, instance_key, shape, communication_hint: str = 'auto', timeout_seconds: int = 0, name: Incomplete | None = None):
    '''Broadcasts a tensor value to one or more other devices.

  Args:
    input: A `Tensor`. Must be one of the following types: `bool`, `float32`, `half`, `float64`, `int32`, `int64`.
    group_size: An `int`.
    group_key: An `int`.
    instance_key: An `int`.
    shape: A `tf.TensorShape` or list of `ints`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CollectiveBcastSend: Incomplete

def collective_bcast_send_eager_fallback(input, group_size, group_key, instance_key, shape, communication_hint, timeout_seconds, name, ctx): ...
def collective_bcast_send_v2(input, group_size, group_key, instance_key, communication_hint: str = 'auto', timeout_seconds: int = 0, name: Incomplete | None = None):
    '''Broadcasts a tensor value to one or more other devices.

  Args:
    input: A `Tensor`. Must be one of the following types: `bool`, `float32`, `half`, `float64`, `int32`, `int64`.
    group_size: A `Tensor` of type `int32`.
    group_key: A `Tensor` of type `int32`.
    instance_key: A `Tensor` of type `int32`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CollectiveBcastSendV2: Incomplete

def collective_bcast_send_v2_eager_fallback(input, group_size, group_key, instance_key, communication_hint, timeout_seconds, name, ctx): ...
def collective_gather(input, group_size, group_key, instance_key, shape, communication_hint: str = 'auto', timeout_seconds: int = 0, name: Incomplete | None = None):
    '''Mutually accumulates multiple tensors of identical type and shape.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `half`, `float64`, `int32`, `int64`.
    group_size: An `int`.
    group_key: An `int`.
    instance_key: An `int`.
    shape: A `tf.TensorShape` or list of `ints`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CollectiveGather: Incomplete

def collective_gather_eager_fallback(input, group_size, group_key, instance_key, shape, communication_hint, timeout_seconds, name, ctx): ...
def collective_gather_v2(input, group_size, group_key, instance_key, ordering_token, communication_hint: str = 'auto', timeout_seconds: int = 0, name: Incomplete | None = None):
    '''Mutually accumulates multiple tensors of identical type and shape.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `half`, `float64`, `int32`, `int64`.
    group_size: A `Tensor` of type `int32`.
    group_key: A `Tensor` of type `int32`.
    instance_key: A `Tensor` of type `int32`.
    ordering_token: A list of `Tensor` objects with type `resource`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CollectiveGatherV2: Incomplete

def collective_gather_v2_eager_fallback(input, group_size, group_key, instance_key, ordering_token, communication_hint, timeout_seconds, name, ctx): ...
def collective_initialize_communicator(group_key, rank, group_size, communication_hint: str = 'auto', timeout_seconds: int = 0, name: Incomplete | None = None):
    '''Initializes a group for collective operations.

  Args:
    group_key: A `Tensor` of type `int32`.
    rank: A `Tensor` of type `int32`.
    group_size: A `Tensor` of type `int32`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

CollectiveInitializeCommunicator: Incomplete

def collective_initialize_communicator_eager_fallback(group_key, rank, group_size, communication_hint, timeout_seconds, name, ctx): ...
def collective_reduce(input, group_size, group_key, instance_key, merge_op, final_op, subdiv_offsets, wait_for=[], communication_hint: str = 'auto', timeout_seconds: int = 0, name: Incomplete | None = None):
    '''Mutually reduces multiple tensors of identical type and shape.

  Args:
    input: A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `half`, `float64`, `int32`, `int64`.
    group_size: An `int`.
    group_key: An `int`.
    instance_key: An `int`.
    merge_op: A `string` from: `"Min", "Max", "Mul", "Add"`.
    final_op: A `string` from: `"Id", "Div"`.
    subdiv_offsets: A list of `ints`.
    wait_for: An optional list of `ints`. Defaults to `[]`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CollectiveReduce: Incomplete

def collective_reduce_eager_fallback(input, group_size, group_key, instance_key, merge_op, final_op, subdiv_offsets, wait_for, communication_hint, timeout_seconds, name, ctx): ...
def collective_reduce_scatter_v2(input, group_size, group_key, instance_key, ordering_token, merge_op, final_op, communication_hint: str = 'auto', timeout_seconds: int = 0, max_subdivs_per_device: int = -1, name: Incomplete | None = None):
    '''Mutually reduces multiple tensors of identical type and shape and scatters the result.

  Args:
    input: A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `half`, `float64`, `int32`, `int64`.
    group_size: A `Tensor` of type `int32`.
    group_key: A `Tensor` of type `int32`.
    instance_key: A `Tensor` of type `int32`.
    ordering_token: A list of `Tensor` objects with type `resource`.
    merge_op: A `string` from: `"Min", "Max", "Mul", "Add"`.
    final_op: A `string` from: `"Id", "Div"`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    max_subdivs_per_device: An optional `int`. Defaults to `-1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CollectiveReduceScatterV2: Incomplete

def collective_reduce_scatter_v2_eager_fallback(input, group_size, group_key, instance_key, ordering_token, merge_op, final_op, communication_hint, timeout_seconds, max_subdivs_per_device, name, ctx): ...
def collective_reduce_v2(input, group_size, group_key, instance_key, ordering_token, merge_op, final_op, communication_hint: str = 'auto', timeout_seconds: int = 0, max_subdivs_per_device: int = -1, name: Incomplete | None = None):
    '''Mutually reduces multiple tensors of identical type and shape.

  Args:
    input: A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `half`, `float64`, `int32`, `int64`.
    group_size: A `Tensor` of type `int32`.
    group_key: A `Tensor` of type `int32`.
    instance_key: A `Tensor` of type `int32`.
    ordering_token: A list of `Tensor` objects with type `resource`.
    merge_op: A `string` from: `"Min", "Max", "Mul", "Add"`.
    final_op: A `string` from: `"Id", "Div"`.
    communication_hint: An optional `string`. Defaults to `"auto"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    max_subdivs_per_device: An optional `int`. Defaults to `-1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CollectiveReduceV2: Incomplete

def collective_reduce_v2_eager_fallback(input, group_size, group_key, instance_key, ordering_token, merge_op, final_op, communication_hint, timeout_seconds, max_subdivs_per_device, name, ctx): ...
def collective_reduce_v3(input, communicator, group_assignment, reduction, timeout_seconds: int = 0, name: Incomplete | None = None):
    '''Mutually reduces multiple tensors of identical type and shape.

  Args:
    input: A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `half`, `float64`, `int32`, `int64`.
    communicator: A `Tensor` of type `resource`.
    group_assignment: A `Tensor` of type `int32`.
    reduction: A `string` from: `"Min", "Max", "Mul", "Add"`.
    timeout_seconds: An optional `float`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CollectiveReduceV3: Incomplete

def collective_reduce_v3_eager_fallback(input, communicator, group_assignment, reduction, timeout_seconds, name, ctx): ...
