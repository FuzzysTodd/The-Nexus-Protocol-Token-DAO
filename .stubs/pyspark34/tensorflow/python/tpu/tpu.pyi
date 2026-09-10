import enum
from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.core.protobuf.tpu import tpu_embedding_configuration_pb2 as embedding_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.compiler.xla import xla as xla
from tensorflow.python.distribute import device_util as device_util, distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import auto_control_deps as auto_control_deps, c_api_util as c_api_util, composite_tensor as composite_tensor, config as config, constant_op as constant_op, dtypes as dtypes, errors as errors, func_graph as func_graph, function as function, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.tpu import device_assignment as device_assignment_lib, tpu_feed as tpu_feed, tpu_function as tpu_function, tpu_name_util as tpu_name_util
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.types import core as core_types
from tensorflow.python.util import compat as compat, nest as nest, object_identity as object_identity, traceback_utils as traceback_utils, variable_utils as variable_utils
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Callable, List, NamedTuple, Optional, Text, Tuple, Union

core = tpu_name_util.core

def initialize_system(embedding_config: Optional[embedding_pb2.TPUEmbeddingConfiguration] = None, job: Optional[Text] = None, compilation_failure_closes_chips: bool = True, tpu_cancellation_closes_chips: Optional[bool] = None) -> core_types.Tensor:
    """Initializes a distributed TPU system for use with TensorFlow.

  Args:
    embedding_config: If not None, a `TPUEmbeddingConfiguration` proto
      describing the desired configuration of the hardware embedding lookup
      tables. If embedding_config is None, no hardware embeddings can be used.
    job: The job (the XXX in TensorFlow device specification /job:XXX) that
      contains the TPU devices that will be initialized. If job=None it is
      assumed there is only one job in the TensorFlow flock, and an error will
      be returned if this assumption does not hold.
    compilation_failure_closes_chips: Set the configuration whether
      we want to close TPU chips when there is a compilation failure.
    tpu_cancellation_closes_chips: Set the configuration whether
      we want to close TPU chips when a TPU execution is cancelled. If the value
      is None, the behavior will be determined by the command line flag
      `tpu_cancellation_closes_chips` for the TPU worker. WARNING: this argument
      only applies to TFRT TPU runtime.
  Returns:
    A serialized `TopologyProto` that describes the TPU system. Note:
      the topology must be evaluated using `Session.run` before it can be used.
  """
def initialize_system_for_tpu_embedding(embedding_config: embedding_pb2.TPUEmbeddingConfiguration, job: Optional[Text] = None) -> ops.Operation:
    """Initializes a distributed TPU Embedding system for use with TensorFlow.

  The following two are equivalent:
  1. initialize_system() with embedding_config.
  2. initialize_system() without embedding_config, then
     initialize_system_for_tpu_embedding().
  initialize_system() should not be called with embedding_config if
  initialize_system_for_tpu_embedding() is meant to be called later.

  Args:
    embedding_config: a `TPUEmbeddingConfiguration` proto describing the desired
      configuration of the hardware embedding lookup tables.
    job: The job (the XXX in TensorFlow device specification /job:XXX) that
      contains the TPU devices that will be initialized. If job=None it is
      assumed there is only one job in the TensorFlow flock, and an error will
      be returned if this assumption does not hold.

  Returns:
    A no-op.
  """
def shutdown_system(job: Optional[Text] = None) -> ops.Operation:
    """Shuts down a running a distributed TPU system.

  Args:
    job: The job (the XXX in TensorFlow device specification /job:XXX) that
      contains the TPU devices that will be shutdown. If job=None it is
      assumed there is only one job in the TensorFlow flock, and an error will
      be returned if this assumption does not hold.
  """
def is_tpu_strategy(strategy: Any) -> bool: ...
def tpu_replicated_input_resolver(op: ops.Operation, resource_reads: object_identity.ObjectIdentitySet, resource_writes: object_identity.ObjectIdentitySet) -> bool:
    """Replaces TPUReplicatedInput outputs with its inputs in resource_inputs."""

class TPUReplicateContext(control_flow_ops.XLAControlFlowContext):
    '''A `ControlFlowContext` for nodes inside a TPU computation.

  The primary role of `TPUReplicateContext` is to mark operators inside a
  tpu.replicate() computation with the attribute "_tpu_replicate=XYZ", where XYZ
  is a unique name.

  We use a `ControlFlowContext` to perform the annotation since it integrates
  with Tensorflow constructs like ResourceVariables. For example, if a
  `ResourceVariable` is constructed inside a tpu.replicate() block, the
  `ResourceVariable` implementation can use
  `with ops.control_dependencies(None)` to build the variable\'s definition
  outside the replicated computation.
  '''
    def __init__(self, name: Text, num_replicas: int, pivot: ops.Operation) -> None:
        """Builds a new TPUReplicateContext.

    Args:
      name: a unique name for the context, used to populate the `_tpu_replicate`
        attribute.
      num_replicas: an integer that gives the number of replicas for the
        computation.
      pivot: a pivot node. Nodes in the TPUReplicateContext that do not have any
        inputs will have a control dependency on the pivot node. This ensures
        that nodes are correctly included in any enclosing control flow
        contexts.
    """
    def get_replicated_var_handle(self, name: Text, handle_id: Text, vars_: Union[List[core_types.Tensor], List[variables.Variable]], is_mirrored: bool = False, is_packed: bool = False) -> core_types.Tensor:
        """Returns a variable handle for replicated TPU variable 'var'.

    This is a method used by an experimental replicated variable implementation
    and is not intended as a public API.

    Args:
      name: The common name of the variable.
      handle_id: Unique ID of the variable handle, used as the cache key.
      vars_: The replicated TPU variables or handles.
      is_mirrored: Whether the variables are mirrored, which guarantees the
        values in each replica are always the same.
      is_packed: Whether the replicated variables are packed into one variable.

    Returns:
      The handle of the TPU replicated input node.
    """
    def report_unsupported_operations(self) -> None: ...
    def EnterGradientColocation(self, op: ops.Operation, gradient_uid: Text): ...
    def ExitGradientColocation(self, op: ops.Operation, gradient_uid: Text): ...
    def Enter(self) -> None: ...
    def HostComputeCore(self) -> List[Text]: ...
    def AddOp(self, op: ops.Operation) -> None: ...
    def AddValue(self, val: core_types.Tensor) -> core_types.Tensor:
        """Add `val` to the current context and its outer context recursively."""
    def AddInnerOp(self, op: ops.Operation): ...
    @property
    def grad_state(self) -> None: ...
    @property
    def back_prop(self):
        """Forwards to the enclosing while context, if any."""
    def GetControlPivot(self) -> ops.Operation: ...
    def RequiresUniqueFunctionRetracing(self): ...

class OutsideCompilationV2Context(control_flow_ops.ControlFlowContext):
    """The context for outside compilation in Tensorflow 2.0.

  Every op added in this context will be assigned an _xla_outside_compilation
  attribute.
  """
    def __init__(self, name: Text) -> None: ...
    def AddOp(self, op: ops.Operation) -> None: ...
    def AddInnerOp(self, op: ops.Operation) -> None: ...
    def to_control_flow_context_def(self, context_def, export_scope: Incomplete | None = None) -> None: ...

def outside_compilation(computation: Callable[..., Any], *args, **kwargs) -> Any:
    """Builds part of a computation outside any current TPU replicate scope.

  `tf.tpu.outside_compilation()` is used to run ops in `computation` on CPU
  instead of running on TPU. For example, users can run ops that are not
  supported on TPU's (e.g. tf.summary.write()) by explicitly placing those
  ops on CPU's. Below usage of outside compilation will place ops in
  `computation_with_string_ops` on CPU.

  Example usage:

  ```python
  def computation_with_string_ops(x):
    # strings types are not supported on TPU's and below ops must
    # run on CPU instead.
    output = tf.strings.format('1{}', x)
    return tf.strings.to_number(output)

  def tpu_computation():
    # Expected output is 11.
    output = tf.tpu.outside_compilation(computation_with_string_ops, 1)
  ```

  Outside compilation should be called inside TPUReplicateContext. That is,
  `tf.tpu.outside_compilation()` should be called inside a function that is
  passed to `tpu.split_compile_and_replicate()` -- this is implied when
  outside compilation is invoked inside a function passed to TPUStrategy
  `run()`. If invoked outside of TPUReplicateContext,
  then this simply returns the result of `computation`, and therefore,
  would be a no-op. Note that outside compilation is different from
  `tf.distribute.experimental.TPUStrategy.merge_call()` as logic in
  outside compilation is replicated and executed separately for each
  replica. On the other hand, `merge_call()` requires a `merge_fn`
  to aggregate the inputs from different replicas and is executed only
  once.

  For variables placed in TPU device, which includes variables created inside
  TPUStrategy scope, outside compilation logic must not include variable
  read/write. For variables placed on host, which is the case when variables
  created via TPUEstimator, variable read/write is only allowed if the variable
  is not accessed by any other ops in the TPU computation. Variable read/write
  from outside compilation cluster is not visible from TPU computation and
  vice versa. Therefore, if outside compilation logic contains such host
  variables read/write ops and if the variables are accessed by TPU
  computation as well, then this may lead to deadlock.

  Internally, `tf.tpu.outside_compilation()` adds outside compilation
  attributes to all ops in `computation`. During later graph pass, these
  ops with outside compilation attribute is extracted out and replicated
  into a host-side graph. Inputs to this extract host-side graph is sent
  from TPU computation graph to host graph via a pair of XlaSendToHost and
  XlaRecvFromHost ops. Note that using `tf.tpu.outside_compilation()`
  may result in tensor transfer between TPU and CPU, leading to non-trivial
  performance impact.

  Args:
    computation: A Python function that builds the computation to
      place on the host.
    *args: the positional arguments for the computation.
    **kwargs: the keyword arguments for the computation.

  Returns:
    The Tensors returned by computation.
  """

class PaddingSpec(enum.IntEnum):
    """Represents the type of padding policies for tpu.replicate."""
    AUTO: int
    POWER_OF_TWO: int

class XLAOptions(NamedTuple('XLAOptions', [('use_spmd_for_xla_partitioning', Incomplete), ('enable_xla_dynamic_padder', Incomplete)])):
    """XLA compilation options.

  Attributes:
    use_spmd_for_xla_partitioning: Boolean. Whether to use XLA's SPMD
      partitioner instead of MPMD partitioner when compiler partitioning is
      requested.
    enable_xla_dynamic_padder: Boolean. Whether to enable XLA dynamic padder
      infrastructure to handle dynamic shapes inputs inside XLA. True by
      default. Disabling this may cause correctness issues with dynamic shapes
      inputs, as XLA will just assume the inputs are with padded shapes. However
      users can optionally set it to False to improve device time if masking is
      already handled in the user side.
  """
    def __new__(cls, use_spmd_for_xla_partitioning: bool = True, enable_xla_dynamic_padder: bool = True): ...

def replicate(computation: Callable[..., Any], inputs: Optional[List[List[core_types.Tensor]]] = None, infeed_queue: Optional[tpu_feed.InfeedQueue] = None, device_assignment: Optional[device_assignment_lib.DeviceAssignment] = None, name: Optional[Text] = None, maximum_shapes: Optional[Any] = None, padding_spec: Optional[PaddingSpec] = None, xla_options: Optional[XLAOptions] = None) -> List[Any]:
    """Builds a graph operator that runs a replicated TPU computation.

  Example for the basic usage that `inputs` has static shape:

  ```python

  def computation(x):
    x = x + 1
    return tf.math.reduce_mean(x)

  x = tf.convert_to_tensor([1., 2., 3.])
  y = tf.convert_to_tensor([4., 5., 6.])
  tf.compat.v1.tpu.replicate(computation, inputs=[[x], [y]])
  ```

  If the `inputs` has dynamic shapes and you would like to automatically
  bucketize the inputs to avoid XLA recompilation. See the advanced example
  below:

  ```python

  def computation(x):
    x = x + 1
    return tf.math.reduce_mean(x)

  # Assume input tensors in two replicas `x` and `y` both have dynamic shape
  # ([None, 2]).
  tf.compat.v1.tpu.replicate(
    computation,
    inputs=[x, y],
    maximum_shapes=[tf.TensorShape([None, None])],
    padding_spec=tf.compat.v1.tpu.PaddingSpec.POWER_OF_TWO)
  ```

  Args:
    computation: A Python function that builds the computation to replicate.
    inputs: A list of lists of input tensors or `None` (equivalent to
      `[[]]`), indexed by `[replica_num][input_num]`. All replicas must
      have the same number of inputs. Each input can be a nested structure
      containing values that are convertible to tensors. Note that passing an
      N-dimension list of compatible values will result in a N-dimension list of
      scalar tensors rather than a single Rank-N tensors. If you need different
      behavior, convert part of inputs to tensors with `tf.convert_to_tensor`.
    infeed_queue: If not `None`, the `InfeedQueue` from which to append a tuple
      of arguments as inputs to computation.
    device_assignment: If not `None`, a `DeviceAssignment` describing the
      mapping between logical cores in the computation with physical cores in
      the TPU topology. Uses a default device assignment if `None`. The
      `DeviceAssignment` may be omitted if each replica of the computation uses
      only one core, and there is either only one replica, or the number of
      replicas is equal to the number of cores in the TPU system.
    name: (Deprecated) Does nothing.
    maximum_shapes: A nested structure of tf.TensorShape representing the shape
      to which the respective component of each input element in each replica
      should be padded. Any unknown dimensions (e.g.
      tf.compat.v1.Dimension(None) in a tf.TensorShape or -1 in a tensor-like
      object) will be padded to the maximum size of that dimension over all
      replicas. The structure of `maximum_shapes` needs to be the same as
      `inputs[0]`.
    padding_spec: An enum specified by `tpu.PaddingSpec`. This describes the
      padding policy when the `inputs` to `tpu.replicate` is dynamic.
      One usage is to enable automatic bucketizing on the inputs by setting the
      value to `tpu.PaddingSpec.POWER_OF_TWO`, which can help to reduce the
      recompilation in the XLA side.
    xla_options: An instance of `tpu.XLAOptions` which indicates the options
      passed to XLA compiler. Use `None` for default options.
  Returns:
    A list of outputs, indexed by `[replica_num]` each output can be a nested
    structure same as what computation() returns with a few exceptions.

    Exceptions include:
      1) None output: a NoOp would be returned which control-depends on
         computation.
      2) Single value output: A tuple containing the value would be returned.
      3) Operation-only outputs: a NoOp would be returned which
         control-depends on computation.
      TODO(b/121383831): Investigate into removing these special cases.

  Raises:
    ValueError: If all replicas do not have equal numbers of input tensors.
    ValueError: If the number of inputs per replica does not match
      the number of formal parameters to `computation`.
    ValueError: If the static `inputs` dimensions don't match with the values
      given in `maximum_shapes`.
    ValueError: If the structure of inputs per replica does not match
      the structure of `maximum_shapes`.
  """
def split_compile_and_replicate(computation: Callable[..., Any], inputs: Optional[List[List[core_types.Tensor]]] = None, infeed_queue: Optional[tpu_feed.InfeedQueue] = None, device_assignment: Optional[device_assignment_lib.DeviceAssignment] = None, name: Optional[Text] = None, use_tpu: bool = True, maximum_shapes: Optional[Any] = None, padding_spec: Optional[PaddingSpec] = None, xla_options: Optional[XLAOptions] = None) -> List[List[core_types.Tensor]]:
    """Builds graph operators that runs compilation and replicated computation.

  This is a lower level interface than replicate that returns a separate compile
  and execute output tensor. In the generated graph the compile op feeds into
  the execute op and no additional compilation is incurred when running the
  compile op before the execute op. The compile op returns additional
  information about the compilation but does not return the compiled program.

  Args:
    computation: A Python function that builds the computation to replicate.
    inputs: A list of lists of input tensors or `None` (equivalent to
      `[[]]`), indexed by `[replica_num][input_num]`. All replicas must
      have the same number of inputs. Each input can be a nested structure
      containing values that are convertible to tensors. Note that passing an
      N-dimension list of compatible values will result in a N-dimension list of
      scalar tensors rather than a single Rank-N tensors. If you need different
      behavior, convert part of inputs to tensors with `tf.convert_to_tensor`.
    infeed_queue: If not `None`, the `InfeedQueue` from which to append a tuple
      of arguments as inputs to computation.
    device_assignment: If not `None`, a `DeviceAssignment` describing the
      mapping between logical cores in the computation with physical cores in
      the TPU topology. Uses a default device assignment if `None`. The
      `DeviceAssignment` may be omitted if each replica of the computation uses
      only one core, and there is either only one replica, or the number of
      replicas is equal to the number of cores in the TPU system.
    name: (Deprecated) Does nothing.
    use_tpu: When false, the input `computation` is executed on the XLA CPU/GPU
      backends. Currently, only supports a default placement (computation is
      placed on GPU if one is available, and on CPU if not).
    maximum_shapes: A nested structure of tf.TensorShape representing the shape
      to which the respective component of each input element in each replica
      should be padded. Any unknown dimensions (e.g.
      tf.compat.v1.Dimension(None) in a tf.TensorShape or -1 in a tensor-like
      object) will be padded to the maximum size of that dimension over all
      replicas. The structure of `maximum_shapes` needs to be the same as
      `inputs[0]`.
    padding_spec: An enum specified by `tf.tpu.PaddingSpec`. This describes the
      padding policy when the `inputs` to `tf.tpu.replicate` is dynamic.
      One usage is to enable automatic bucketizing on the inputs by setting the
      value to `tpu.PaddingSpec.POWER_OF_TWO`, which can help to reduce the
      recompilation in the XLA side.
    xla_options: An instance of `tpu.XLAOptions` which indicates the options
      passed to XLA compiler. Use `None` for default options.

  Returns:
    A list of lists with the first list corresponding to the compile op and the
    second a list of output tensors, indexed by `[replica_num][output_num]`.
  Raises:
    ValueError: If all replicas do not have equal numbers of input tensors.
    ValueError: If the number of inputs per replica does not match
      the number of formal parameters to `computation`.
    ValueError: If the static `inputs` dimensions don't match with the values
      given in `maximum_shapes`.
    ValueError: If the structure of inputs per replica does not match
      the structure of `maximum_shapes`.
  """
def split_compile_and_shard(computation: Callable[..., Any], inputs: Optional[List[List[Optional[core_types.Tensor]]]] = None, num_shards: int = 1, input_shard_axes: Optional[List[int]] = None, outputs_from_all_shards: Union[bool, List[bool]] = True, output_shard_axes: Optional[List[int]] = None, infeed_queue: Optional[tpu_feed.InfeedQueue] = None, device_assignment: Optional[device_assignment_lib.DeviceAssignment] = None, name: Optional[Text] = None, xla_options: Optional[XLAOptions] = None) -> Tuple[ops.Operation, List[core_types.Tensor]]:
    '''Shards `computation` for parallel execution.

  `inputs` must be a list of Tensors or None (equivalent to an empty list), each
  of which has a corresponding split axis (from `input_shard_axes`). Each input
  is split into `num_shards` pieces along the corresponding axis, and
  computation is applied to each shard in parallel.

  Tensors are broadcast to all shards if they are lexically captured by
  `computation`. e.g.,

  x = tf.constant(7)
  def computation():
    return x + 3
  ... = shard(computation, ...)

  If `outputs_from_all_shards` is true, the outputs from all shards of
  `computation` are concatenated back together along their `output_shard_axes`.
  Otherwise, each output is taken from an arbitrary shard.

  Inputs and outputs of the computation must be at least rank-1 Tensors.

  Args:
    computation: A Python function that builds a computation to apply to each
      shard of the input.
    inputs: A list of input tensors or None (equivalent to an empty list). Each
      input tensor has a corresponding shard axes, given by `input_shard_axes`,
      which must have size divisible by `num_shards`.
    num_shards: The number of shards.
    input_shard_axes: A list of dimensions along which to shard `inputs`, or
      `None`. `None` means "shard all inputs along dimension 0". If not `None`,
      there must be one dimension per input.
    outputs_from_all_shards: Boolean or list of boolean. For each output, if
      `True`, outputs from all shards are concatenated along the corresponding
      `output_shard_axes` entry. Otherwise, each output is taken
      from an arbitrary shard. If the argument is a boolean, the argument\'s
      value is used for each output.
    output_shard_axes: A list of dimensions along which to concatenate the
      outputs of `computation`, or `None`. `None` means "concatenate all outputs
      along dimension 0". If not `None`, there must be one dimension per output.
      Ignored if `outputs_from_all_shards` is False.
    infeed_queue: If not `None`, the `InfeedQueue` to use to augment the inputs
      of `computation`.
    device_assignment: If not `None`, a `DeviceAssignment` describing the
      mapping between logical cores in the computation with physical cores in
      the TPU topology. Uses a default device assignment if `None`. The
      `DeviceAssignment` may be omitted if each shard of the computation uses
      only one core, and there is either only one shard, or the number of shards
      is equal to the number of cores in the TPU system.
    name: (Deprecated) Does nothing.
    xla_options: An instance of `tpu.XLAOptions` which indicates the options
      passed to XLA compiler. Use `None` for default options.
  Returns:
    A tuple of (compile op, [output tensors]).
  Raises:
    ValueError: If num_shards <= 0
    ValueError: If len(input_shard_axes) != len(inputs)
    ValueError: If len(output_shard_axes) != len(outputs from `computation`)
  '''
def shard(computation: Callable[..., Any], inputs: Optional[List[core_types.Tensor]] = None, num_shards: int = 1, input_shard_axes: Optional[List[int]] = None, outputs_from_all_shards: Union[bool, List[bool]] = True, output_shard_axes: Optional[List[int]] = None, infeed_queue: Optional[tpu_feed.InfeedQueue] = None, device_assignment: Optional[device_assignment_lib.DeviceAssignment] = None, name: Optional[Text] = None, xla_options: Optional[XLAOptions] = None) -> List[core_types.Tensor]:
    '''Shards `computation` for parallel execution.

  `inputs` must be a list of Tensors or None (equivalent to an empty list), each
  of which has a corresponding split axis (from `input_shard_axes`). Each input
  is split into `num_shards` pieces along the corresponding axis, and
  computation is applied to each shard in parallel.

  Tensors are broadcast to all shards if they are lexically captured by
  `computation`. e.g.,

  x = tf.constant(7)
  def computation():
    return x + 3
  ... = shard(computation, ...)

  TODO(phawkins): consider adding support for broadcasting Tensors passed
  as inputs.

  If `outputs_from_all_shards` is true, the outputs from all shards of
  `computation` are concatenated back together along their `output_shard_axes`.
  Otherwise, each output is taken from an arbitrary shard.

  Inputs and outputs of the computation must be at least rank-1 Tensors.

  Args:
    computation: A Python function that builds a computation to apply to each
      shard of the input.
    inputs: A list of input tensors or None (equivalent to an empty list). Each
      input tensor has a corresponding shard axes, given by `input_shard_axes`,
      which must have size divisible by `num_shards`.
    num_shards: The number of shards.
    input_shard_axes: A list of dimensions along which to shard `inputs`, or
      `None`. `None` means "shard all inputs along dimension 0". If not `None`,
      there must be one dimension per input.
    outputs_from_all_shards: Boolean or list of boolean. For each output, if
      `True`, outputs from all shards are concatenated along the corresponding
      `output_shard_axes` entry. Otherwise, each output is taken
      from an arbitrary shard. If the argument is a boolean, the argument\'s
      value is used for each output.
    output_shard_axes: A list of dimensions along which to concatenate the
      outputs of `computation`, or `None`. `None` means "concatenate all outputs
      along dimension 0". If not `None`, there must be one dimension per output.
      Ignored if `outputs_from_all_shards` is False.
    infeed_queue: If not `None`, the `InfeedQueue` to use to augment the inputs
      of `computation`.
    device_assignment: If not `None`, a `DeviceAssignment` describing the
      mapping between logical cores in the computation with physical cores in
      the TPU topology. Uses a default device assignment if `None`. The
      `DeviceAssignment` may be omitted if each shard of the computation uses
      only one core, and there is either only one shard, or the number of shards
      is equal to the number of cores in the TPU system.
    name: (Deprecated) Does nothing.
    xla_options: An instance of `tpu.XLAOptions` which indicates the options
      passed to XLA compiler. Use `None` for default options.
  Returns:
    A list of output tensors.
  Raises:
    ValueError: If num_shards <= 0
    ValueError: If len(input_shard_axes) != len(inputs)
    ValueError: If len(output_shard_axes) != len(outputs from `computation`)
  '''
def batch_parallel(computation: Callable[..., Any], inputs: Optional[List[List[Optional[core_types.Tensor]]]] = None, num_shards: int = 1, infeed_queue: Optional[tpu_feed.InfeedQueue] = None, device_assignment: Optional[device_assignment_lib.DeviceAssignment] = None, name: Optional[Text] = None, xla_options: Optional[XLAOptions] = None):
    """Shards `computation` along the batch dimension for parallel execution.

  Convenience wrapper around shard().

  `inputs` must be a list of Tensors or None (equivalent to an empty list).
  Each input is split into `num_shards` pieces along the 0-th dimension, and
  computation is applied to each shard in parallel.

  Tensors are broadcast to all shards if they are lexically captured by
  `computation`. e.g.,

  x = tf.constant(7)
  def computation():
    return x + 3
  ... = shard(computation, ...)

  The outputs from all shards are concatenated back together along their 0-th
  dimension.

  Inputs and outputs of the computation must be at least rank-1 Tensors.

  Args:
    computation: A Python function that builds a computation to apply to each
      shard of the input.
    inputs: A list of input tensors or None (equivalent to an empty list). The
      0-th dimension of each Tensor must have size divisible by `num_shards`.
    num_shards: The number of shards.
    infeed_queue: If not `None`, the `InfeedQueue` from which to append a tuple
      of arguments as inputs to `computation`.
    device_assignment: If not `None`, a `DeviceAssignment` describing the
      mapping between logical cores in the computation with physical cores in
      the TPU topology. Uses a default device assignment if `None`. The
      `DeviceAssignment` may be omitted if each shard of the computation uses
      only one core, and there is either only one shard, or the number of shards
      is equal to the number of cores in the TPU system.
    name: (Deprecated) Does nothing.
    xla_options: An instance of `tpu.XLAOptions` which indicates the options
      passed to XLA compiler. Use `None` for default options.
  Returns:
    A list of output tensors.
  Raises:
    ValueError: If `num_shards <= 0`
  """
def rewrite(computation: Callable[..., Any], inputs: Optional[List[List[Optional[core_types.Tensor]]]] = None, infeed_queue: Optional[tpu_feed.InfeedQueue] = None, device_assignment: Optional[device_assignment_lib.DeviceAssignment] = None, name: Optional[Text] = None, xla_options: Optional[XLAOptions] = None) -> Any:
    """Rewrites `computation` for execution on a TPU system.

  Args:
    computation: A Python function that builds a computation to apply to the
      input. If the function takes n inputs, 'inputs' should be a list of n
      tensors.

      `computation` may return a list of operations and tensors. Tensors must
      come before operations in the returned list.  The return value of
      `rewrite` is a list of tensors corresponding to the tensors from the
      output of `computation`.

      All `Operation`s constructed during `computation` will be executed when
      evaluating any of the returned output tensors, not just the ones returned.
    inputs: A list of input tensors or `None` (equivalent to an empty list).
      Each input can be a nested structure containing values that are
      convertible to tensors. Note that passing an N-dimension list of
      compatible values will result in a N-dimension list of scalar tensors
      rather than a single Rank-N tensors. If you need different behavior,
      convert part of inputs to tensors with `tf.convert_to_tensor`.
    infeed_queue: If not `None`, the `InfeedQueue` from which to append a tuple
      of arguments as inputs to `computation`.
    device_assignment: if not `None`, a `DeviceAssignment` describing the
      mapping between logical cores in the computation with physical cores in
      the TPU topology. May be omitted for a single-core computation, in which
      case the core attached to task 0, TPU device 0 is used.
    name: (Deprecated) Does nothing.
    xla_options: An instance of `tpu.XLAOptions` which indicates the options
      passed to XLA compiler. Use `None` for default options.
  Returns:
    Same data structure as if computation(*inputs) is called directly with some
    exceptions for correctness. Exceptions include:
      1) None output: a NoOp would be returned which control-depends on
         computation.
      2) Single value output: A tuple containing the value would be returned.
      3) Operation-only outputs: a NoOp would be returned which
         control-depends on computation.
      TODO(b/121383831): Investigate into removing these special cases.
  """
def under_tpu_inference_context() -> bool:
    """Check if it is currently under `_TPUInferenceContext`."""

class _TPUInferenceContext(control_flow_ops.XLAControlFlowContext):
    """A `ControlFlowContext` for nodes inside a TPU inference computation.

  The primary role of `_TPUInferenceContext` is to indicate the mode of
  operation and possibly sanity check operators inside a
  tpu.rewrite_for_inference() computation.
  """
    def __init__(self, name: Text, check_ops: bool = True) -> None: ...
    def AddOp(self, op) -> None: ...
    def AddValue(self, val): ...
    def AddInnerOp(self, op) -> None: ...
    @property
    def grad_state(self) -> None: ...

def validate_inference_rewrite_for_variables(graph: ops.Graph):
    """Validates whether rewrite_for_inference() 'worked' for variables.

     The rewrite_for_inference() method is supposed to append GuaranteeConstOps
     after ReadVariableOps, but this mechanism works only if you are using
     tf.compat.v1.get_variable() to create and access variables in your tpu
     computation. This validation method can be called immediately after calling
     tpu.rewrite_for_inference() to check whether GuaranteeConstOps where added
     to the graph.

     Typical usages:
       tpu.validate_inference_rewrite_for_variables(
           tf.compat.v1.get_default_graph())

       tpu.validate_inference_rewrite_for_variables(sess.graph)

  Args:
    graph: The graph which needs to be validated.
  Raises:
    RuntimeError: if validation failed.
  """
def rewrite_for_inference(computation: Callable[..., Any], inputs: Optional[List[core_types.Tensor]] = None, infeed_queue: Optional[tpu_feed.InfeedQueue] = None, device_assignment: Optional[device_assignment_lib.DeviceAssignment] = None, name: Optional[Text] = None) -> List[core_types.Tensor]:
    """Rewrites `computation` for inference on a TPU system.

     Other than 'rewriting' the computation to run on a TPU, if using variables
     in your computation, it moves the ReadVariableOps outside the TPU
     computation, and adds GuaranteeConst ops just after the ReadVariableOps.
     This mechanism works only if you are using tf.compat.v1.get_variable() to
     create and access variables in your tpu computation. You can validate
     whether this worked, by calling validate_inference_rewrite_for_variables()
     method immediately after this method to check whether GuaranteeConstOps
     where added to the graph.

  Args:
    computation: A Python function that builds a computation to apply to the
      input. If the function takes n inputs, 'inputs' should be a list of n
      tensors. If the function returns m outputs, rewrite will return a list of
      m tensors.
    inputs: A list of input tensors or `None` (equivalent to an empty list).
    infeed_queue: If not `None`, the `InfeedQueue` from which to append a tuple
      of arguments as inputs to `computation`.
    device_assignment: if not `None`, a `DeviceAssignment` describing the
      mapping between logical cores in the computation with physical cores in
      the TPU topology. May be omitted for a single-core computation, in which
      case the core attached to task 0, TPU device 0 is used.
    name: The name of the operator.
  Returns:
    A list of output tensors.
  """
def prune_unconnected_ops_from_xla(prune_graph: ops.Graph):
    """Prunes unconnected ops as listed in _UNCONNECTED_OPS_TO_PRUNE.

  Args:
    prune_graph: A tensorflow graph from which we wish to prune unconnected ops
      as listed in _UNCONNECTED_OPS_TO_PRUNE.  In general, these ops should have
      no inputs and no consumers. These can often be left behind due to graph
      construction rewiring (for instance TF-Hub). While they never execute,
      they will cause XLA compile to fail so we strip them from XLA compile by
      removing the tpu_replicate attribute.
  """
