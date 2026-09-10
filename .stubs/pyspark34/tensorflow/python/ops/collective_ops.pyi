from _typeshed import Incomplete
from tensorflow.python.ops import gen_collective_ops as gen_collective_ops

def all_reduce(t, group_size, group_key, instance_key, merge_op: str = 'Add', final_op: str = 'Id', subdiv_offsets=(0,), communication_hint: str = 'auto', timeout: int = 0):
    """Reduces tensors collectively, across devices.

  Args:
    t: the tensor to be reduced.
    group_size: the total number of tensors to be collectively reduced.
      Each must reside on a different device.  Should be a positive integer.
    group_key: an integer identifying the group of devices.
    instance_key: an integer identifying the participating group of Ops.
    merge_op: string naming the binary Op to be applied to compute each
      partial reduction.
    final_op: string naming the unary Op to be applied to each fully
      reduced value.  Can be 'Id' for no operation.
    subdiv_offsets: a list of integer offsets into the tensor at which each
      independent subdivision should begin.  Use [0] if no subdivision should
      be done.
    communication_hint: preferred collective communication.  The implementation
      may fall back to another mechanism.  Options include `auto`, `ring`, and
      `nccl`.
    timeout: a float. If set to a non zero, set a completion timeout to detect
      staleness.  If the timer goes off, a DeadlineExceededError is raised.  The
      timeout value in seconds. This feature is experimental.

  Returns:
    An Op implementing the distributed reduction.

  Raises:
    ValueError: if any of the input parameter constraints are not met.
  """
def assign_group_v2(group_assignment, device_index, base_key):
    """Assign group key based on group_assignment.

  Args:
    group_assignment: a 2 dimensional integer Tensor that encodes which devices
      belong to the same group. The values are indices of the devices within 0
      to number of devices.
    device_index: integer for the index of the current device
    base_key: integer to offset the resulted group_key. The base key shall be
      unique for different values of group_assignment in the same tf.function.
  Notes: The device_index argument must be consistent with the index of the
    device of this Op in the device assignment list. The behavior of this Op is
    undefined if they are inconsistent.

  Returns:
    group_size, group_key: The group size and group key for the current device.
  """
def all_reduce_v2(t, group_size, group_key, instance_key, merge_op: str = 'Add', final_op: str = 'Id', communication_hint: str = 'auto', timeout: int = 0, ordering_token: Incomplete | None = None, max_subdivs_per_device: int = -1, name: Incomplete | None = None):
    """Reduces tensors collectively, across devices.

  Args:
    t: the tensor to be reduced.
    group_size: an int32 tensor. The total number of tensors to be collectively
      reduced.  Each must reside on a different device.  Should be a positive
      integer.
    group_key: an int32 tensor identifying the group of devices.
    instance_key: an int32 tensor identifying the participating group of Ops.
    merge_op: string naming the binary Op to be applied to compute each partial
      reduction.
    final_op: string naming the unary Op to be applied to each fully reduced
      value.  Can be 'Id' for no operation.
    communication_hint: preferred collective communication.  The implementation
      may fall back to another mechanism.  Options include `auto`, `ring`, and
      `nccl`.
    timeout: a float. If set to a non zero, set a completion timeout to detect
      staleness.  If the timer goes off, a DeadlineExceededError is raised.  The
      timeout value in seconds. This feature is experimental.
    ordering_token: a resource tensor on the same device as the op to order
      the collectives in a per-device manner by auto control dependency.
      This argument can be omited when there is one collective Op per
      `tf.function`, or when explicit control dependency is used instead of
      auto control dependency.
    max_subdivs_per_device: int specifying the maximum number of subdivisions a
      tensor on a device can be divided into. The runtime uses this contraint to
      parallelize processing of each per-device tensor. Setting to -1 disables
      subdivision and reverts to previous behavior of not sub-dividing tensor.
      Setting to 0 uses sytem defaults.
    name: name of the Op.

  Returns:
    An Op implementing the distributed reduction.
  """
def all_gather(t, group_size, group_key, instance_key, communication_hint: str = 'auto', timeout: int = 0):
    """Accumulates tensors collectively, across devices, along first dimension.

  Args:
    t: the tensor to participate in the accumulation.
    group_size: the total number of tensors to be collectively accumulated.
      Each must reside on a different device. Should be a positive integer.
    group_key: an integer identifying the group of devices.
    instance_key: an integer identifying the participating group of Ops.
    communication_hint: preferred collective communication. The implementation
      may fall back to another mechanism. Options include `auto`, `ring`, and
      `nccl`.
    timeout: a float. If set to a non zero, set a completion timeout to detect
      staleness. If the timer goes off, a DeadlineExceededError is raised. The
      timeout value in seconds. This feature is experimental.

  Returns:
    An Op implementing the distributed operation.

  Raises:
    ValueError: if any of the input parameter constraints are not met.
  """
def all_gather_v2(t, group_size, group_key, instance_key, communication_hint: str = 'auto', timeout: int = 0, ordering_token: Incomplete | None = None, name: Incomplete | None = None):
    """Accumulates tensors collectively, across devices, along first dimension.

  Args:
    t: the tensor to participate in the accumulation.
    group_size: an int32 tensor, the total number of tensors to be collectively
      accumulated. Each must reside on a different device. Should be a positive
      integer.
    group_key: an int32 tensor identifying the group of devices.
    instance_key: an int32 tensor identifying the participating group of Ops.
    communication_hint: preferred collective communication. The implementation
      may fall back to another mechanism. Options include `auto`, `ring`, and
      `nccl`.
    timeout: a float. If set to a non zero, set a completion timeout to detect
      staleness. If the timer goes off, a DeadlineExceededError is raised. The
      timeout value in seconds. This feature is experimental.
    ordering_token: a resource tensor on the same device as the op to order
      the collectives in a per-device manner by auto control dependency.
      This argument can be omited when there is one collective Op per
      `tf.function`, or when explicit control dependency is used instead of
      auto control dependency.
    name: name of the Op.

  Returns:
    An Op implementing the distributed operation.
  """
def broadcast_send(t, shape, dtype, group_size, group_key, instance_key, communication_hint: str = 'auto', timeout: int = 0):
    """Broadcasts one tensor to a group of others, across devices.

  Args:
    t: the tensor to be sent.
    shape: the shape of the tensor being sent, which must agree with t.
    dtype: the type of the tensor being sent, which must agree with t.
    group_size: one plus the number of receiving tensors, i.e. the total
      number of devices participating.  Each tensor must reside on a
      different device.
    group_key: an integer identifying the group of devices.
    instance_key: an integer identifying the participating group of Ops.
    communication_hint: preferred collective communication.  The implementation
      may fall back to another mechanism.  Options include `auto`, `ring`, and
      `nccl`.
    timeout: If set to a non zero, set a completion timeout to detect staleness.
      If the timer goes off, a DeadlineExceededError is raised.
      The timeout value in seconds. This feature is experimental.

  Returns:
    An Op implementing the distributed broadcast send.

  Raises:
    ValueError: if any of the input parameter constraints are not met.

  Note that the shape and dtype arguments appear redundant since they
  should be obtainable from t.  The are two reasons for including
  them.  First, the shape and type of tensors passed via broadcast must
  be known ahead of time in their most specific form so that the receive
  side can allocate memory for the operation and shape/type inference can
  carry forward from there.  Including the same declarations on the
  send side clarifies a commitment already made.  Secondly, having nearly
  identical use syntax for send and receive sides may simplify tool-driven
  generation of broadcast.
  """
def broadcast_send_v2(t, group_size, group_key, instance_key, communication_hint: str = 'auto', timeout: int = 0):
    """Broadcasts one tensor to a group of others, across devices.

  Args:
    t: the tensor to be sent.
    group_size: an int32 tensor.  One plus the number of receiving tensors, i.e.
        the total number of devices participating.  Each tensor must reside on a
        different device.
    group_key: an int32 tensor identifying the group of devices.
    instance_key: an int32 tensor identifying the participating group of Ops.
    communication_hint: preferred collective communication.  The implementation
      may fall back to another mechanism.  Options include `auto`, `ring`, and
      `nccl`.
    timeout: If set to a non zero, set a completion timeout to detect staleness.
      If the timer goes off, a DeadlineExceededError is raised.
      The timeout value in seconds. This feature is experimental.

  Returns:
    An Op implementing the distributed broadcast send.
  """
def broadcast_recv(shape, dtype, group_size, group_key, instance_key, communication_hint: str = 'auto', timeout: int = 0):
    """Receives a broadcasts tensor, across devices.

  Args:
    shape: Shape of the tensor to be received.
    dtype: Type of the tensor to be received.
    group_size: one plus the number of receiving tensors, i.e. the total
      number of devices participating.  Each tensor must reside on a
      different device.
    group_key: an integer identifying the group of devices.
    instance_key: an integer identifying the participating group of Ops.
    communication_hint: preferred collective communication.  The implementation
      may fall back to another mechanism.  Options include `auto`, `ring`, and
      `nccl`.
    timeout: If set to a non zero, set a completion timeout to detect staleness.
      If the timer goes off, a DeadlineExceededError is raised.
      The timeout value in seconds. This feature is experimental.

  Returns:
    An Op implementing the broadcast receive.

  Raises:
    ValueError: if any of the input parameter constraints are not met.
  """
def broadcast_recv_v2(shape, dtype, group_size, group_key, instance_key, communication_hint: str = 'auto', timeout: int = 0):
    """Receives a broadcasts tensor, across devices.

  Args:
    shape: an int tensor.  Shape of the tensor to be received.
    dtype: Type of the tensor to be received.
    group_size: an int32 tensor.  One plus the number of receiving tensors, i.e.
        the total number of devices participating.  Each tensor must reside on a
        different device.
    group_key: an int32 tensor identifying the group of devices.
    instance_key: an int32 tensor identifying the participating group of Ops.
    communication_hint: preferred collective communication.  The implementation
      may fall back to another mechanism.  Options include `auto`, `ring`, and
      `nccl`.
    timeout: If set to a non zero, set a completion timeout to detect staleness.
      If the timer goes off, a DeadlineExceededError is raised.
      The timeout value in seconds. This feature is experimental.

  Returns:
    An Op implementing the broadcast receive.
  """
def initialize_communicator(group_key, rank, group_size, communication_hint: str = 'auto', timeout_seconds: int = 0):
    """Initializes a collective communicator.

  This creates a collective communicator, which represents membership to a
  collective group identified by the group_key. It should be called once per
  member of the group, and each member needs to be on a different device.
  It blocks until all members of the group run this op.

  Communicators of a group can only be initialized once. Trying to initialize
  communicators for an existing group key will result in an error.

  Args:
    group_key: an int32 `tf.Tensor` identifying the group.
    rank: an `tf.Tensor` specifying the rank of this device in the group. If
      specified, the rank is required to be unique in the group.
    group_size: an int32 `tf.Tensor`. The size of the group.
    communication_hint: preferred collective communication.  The implementation
      may fall back to another mechanism.  Options include `auto`, `ring`, and
      `nccl`.
    timeout_seconds: If set to a non zero, set a completion timeout to detect
      staleness. If the timer goes off, a DeadlineExceededError is raised. The
      timeout value in seconds. This feature is experimental.


  Returns:
    A resource `tf.Tensor`.
  """
def all_reduce_v3(communicator, t, reduction: str = 'Add', group_assignment: Incomplete | None = None, timeout_seconds: Incomplete | None = None):
    '''Reduces tensors mutually.

  Args:
    communicator: the resource `tf.Tensor` returned from
      `initialize_communicator`.
    t: the `tf.Tensor` to be reduced.
    reduction: a string. The name of the operation to reduce the values.
      Accpeted values are `"min"`, `"max"`, `"mul"`, `"add"`.
    group_assignment: Optional int32 `tf.Tensor` with shape [num_groups,
      num_ranks_per_group]. `group_assignment[i]` represents the ranks in the
      `ith` subgroup.
    timeout_seconds: If set to a non zero, set a completion timeout to detect
      staleness. If the timer goes off, a DeadlineExceededError is raised. The
      timeout value in seconds. This feature is experimental.

  Returns:
    The reduced `tf.Tensor`.
  '''
def all_to_all_v3(communicator, t, group_assignment: Incomplete | None = None, timeout_seconds: Incomplete | None = None):
    """Exchanges tensors mutually.

  Args:
    communicator: the resource `tf.Tensor` returned from
      `initialize_communicator`.
    t: a `tf.Tensor`. The first dimension should have the length as the size of
      the group. `t[i]` is sent to `rank i` within the group.
    group_assignment: Optional int32 `tf.Tensor` with shape [num_groups,
      num_ranks_per_group]. `group_assignment[i]` represents the ranks in the
      `ith` subgroup.
    timeout_seconds: If set to a non zero, set a completion timeout to detect
      staleness. If the timer goes off, a DeadlineExceededError is raised. The
      timeout value in seconds. This feature is experimental.

  Returns:
    a `tf.Tensor`. `t[i]` is sent from `rank i` within the group.
  """
