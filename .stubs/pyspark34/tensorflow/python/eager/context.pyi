import threading
from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.framework import function_pb2 as function_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python import pywrap_tfe as pywrap_tfe, tf2 as tf2
from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.eager import executor as executor, monitoring as monitoring
from tensorflow.python.framework import c_api_util as c_api_util, tfrt_utils as tfrt_utils
from tensorflow.python.util import compat as compat, is_in_graph_mode as is_in_graph_mode, tf_contextlib as tf_contextlib
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tsl.protobuf import coordination_config_pb2 as coordination_config_pb2
from typing import NamedTuple

GRAPH_MODE: int
EAGER_MODE: int
default_execution_mode: Incomplete
DEVICE_PLACEMENT_EXPLICIT: Incomplete
DEVICE_PLACEMENT_WARN: Incomplete
DEVICE_PLACEMENT_SILENT: Incomplete
DEVICE_PLACEMENT_SILENT_FOR_INT32: Incomplete
SYNC: int
ASYNC: int
is_tfrt_enabled = tfrt_utils.enabled

def run_eager_op_as_function_enabled(): ...
def enable_jit_compile_rewrite() -> None:
    """Run jit_compile functions through rewrite pass.

  This runs jit_compile functions through all of the multidevice function
  rewrite passes.
  """
def disable_jit_compile_rewrite() -> None: ...
def jit_compile_rewrite_enabled(): ...

class _EagerTensorCache:
    """Simple cache which evicts items based on length in a FIFO manner."""
    def __init__(self, max_items: int = 256, max_tensor_size: int = 10000) -> None: ...
    def put(self, key, value) -> None: ...
    def get(self, key): ...
    def flush(self) -> None: ...

class FunctionCallOptions:
    """Options applied at call sites of eager functions.

  Eager functions are functions decorated with tf.contrib.eager.defun.
  """
    def __init__(self, executor_type: Incomplete | None = None, config_proto: Incomplete | None = None) -> None:
        """Constructor.

    Args:
      executor_type: (optional) name of the executor to be used to execute the
        eager function. If None or an empty string, the default Tensorflow
        executor will be used.
      config_proto: (optional) a `config_pb2.ConfigProto` proto or a serialized
        string of that proto. The config used by Grappler when optimizing the
        function graph. Each concrete function is optimized the first time is
        called. Changing config_proto after the first call has no effect. If
        config_proto is None, an empty RewriterConfig will be used.
    """
    @property
    def executor_type(self): ...
    @executor_type.setter
    def executor_type(self, executor_type) -> None: ...
    @property
    def config_proto_serialized(self): ...
    @config_proto_serialized.setter
    def config_proto_serialized(self, config) -> None: ...

class _TensorCaches(threading.local):
    """Thread local tensor caches."""
    def __init__(self) -> None: ...
    @property
    def ones_rank_cache(self): ...
    @property
    def zeros_cache(self): ...

class ContextSwitch(NamedTuple):
    is_building_function: Incomplete
    enter_context_fn: Incomplete
    device_stack: Incomplete

class _ContextSwitchStack(threading.local):
    """A thread-local stack of context switches."""
    stack: Incomplete
    def __init__(self, eager) -> None: ...
    def push(self, is_building_function, enter_context_fn, device_stack) -> None:
        """Push metadata about a context switch onto the stack.

    A context switch can take any one of the two forms: installing a graph as
    the default graph, or entering the eager context. For each context switch,
    we record whether or not the entered context is building a function.

    Args:
      is_building_function: (bool.) Whether the context is building a function.
      enter_context_fn: (function.) A callable that executes the context switch.
        For example, `graph.as_default` or `eager_mode`.
      device_stack: If applicable, the device function stack for this graph.
        When breaking out of graphs in init_scope, the innermost nonempty device
        stack is used. Eager contexts put `None` here and the value is never
        used.
    """
    def pop(self) -> None:
        """Pop the stack."""

class LogicalDevice(NamedTuple('LogicalDevice', [('name', Incomplete), ('device_type', Incomplete)])):
    '''Abstraction for a logical device initialized by the runtime.

  A `tf.config.LogicalDevice` corresponds to an initialized logical device on a
  `tf.config.PhysicalDevice` or a remote device visible to the cluster. Tensors
  and operations can be placed on a specific logical device by calling
  `tf.device` with a specified `tf.config.LogicalDevice`.

  Fields:
    name: The fully qualified name of the device. Can be used for Op or function
      placement.
    device_type: String declaring the type of device such as "CPU" or "GPU".
  '''

class LogicalDeviceConfiguration(NamedTuple('LogicalDeviceConfiguration', [('memory_limit', Incomplete), ('experimental_priority', Incomplete), ('experimental_device_ordinal', Incomplete)])):
    """Configuration class for a logical devices.

  The class specifies the parameters to configure a `tf.config.PhysicalDevice`
  as it is initialized to a `tf.config.LogicalDevice` during runtime
  initialization. Not all fields are valid for all device types.

  See `tf.config.get_logical_device_configuration` and
  `tf.config.set_logical_device_configuration` for usage examples.

  Fields:
    memory_limit: (optional) Maximum memory (in MB) to allocate on the virtual
      device. Currently only supported for GPUs.
    experimental_priority: (optional) Priority to assign to a virtual device.
      Lower values have higher priorities and 0 is the default.
      Within a physical GPU, the GPU scheduler will prioritize ops on virtual
      devices with higher priority. Currently only supported for Nvidia GPUs.
    experimental_device_ordinal: (optional) Ordinal number to order the virtual
    device.
      LogicalDevice with lower ordinal number will receive a lower device id.
      Physical device id and location in the list is used to break ties.
      Currently only supported for Nvidia GPUs.
  """
    def __new__(cls, memory_limit: Incomplete | None = None, experimental_priority: Incomplete | None = None, experimental_device_ordinal: Incomplete | None = None): ...

class PhysicalDevice(NamedTuple('PhysicalDevice', [('name', Incomplete), ('device_type', Incomplete)])):
    '''Abstraction for a locally visible physical device.

  TensorFlow can utilize various devices such as the CPU or multiple GPUs
  for computation. Before initializing a local device for use, the user can
  customize certain properties of the device such as it\'s visibility or memory
  configuration.

  Once a visible `tf.config.PhysicalDevice` is initialized one or more
  `tf.config.LogicalDevice` objects are created. Use
  `tf.config.set_visible_devices` to configure the visibility of a physical
  device and `tf.config.set_logical_device_configuration` to configure multiple
  `tf.config.LogicalDevice` objects for a `tf.config.PhysicalDevice`. This is
  useful when separation between models is needed or to simulate a multi-device
  environment.

  Fields:
    name: Unique identifier for device.
    device_type: String declaring the type of device such as "CPU" or "GPU".
  '''

class _AtomicCounter:
    """A simple atomic counter."""
    def __init__(self) -> None: ...
    def increment_and_get(self): ...

class _TensorCacheDeleter:
    """Deletes tensor caches for a given context."""
    def __init__(self, context_id) -> None: ...
    def __del__(self) -> None: ...

class Context:
    """Environment in which eager operations execute."""
    def __init__(self, config: Incomplete | None = None, device_policy: Incomplete | None = None, execution_mode: Incomplete | None = None, server_def: Incomplete | None = None) -> None:
        '''Creates a new Context.

    Args:
      config: (Optional.) A `ConfigProto` protocol buffer with configuration
        options for the Context. Note that a lot of these options may be
        currently unimplemented or irrelevant when eager execution is enabled.
      device_policy: (Optional.) What policy to use when trying to run an
        operation on a device with inputs which are not on that device. When set
        to None, an appropriate value will be picked automatically. The value
        picked may change between TensorFlow releases.  Defaults to
        DEVICE_PLACEMENT_SILENT.
        Valid values:
        - DEVICE_PLACEMENT_EXPLICIT: raises an error if the placement is not
          correct.
        - DEVICE_PLACEMENT_WARN: copies the tensors which are not on the right
          device but raises a warning.
        - DEVICE_PLACEMENT_SILENT: silently copies the tensors. This might hide
          performance problems.
        - DEVICE_PLACEMENT_SILENT_FOR_INT32: silently copies int32 tensors,
          raising errors on the other ones.
      execution_mode: (Optional.) Policy controlling how operations dispatched
        are actually executed. When set to None, an appropriate value will be
        picked automatically. The value picked may change between TensorFlow
        releases.
        Valid values:
        - SYNC: executes each operation synchronously.
        - ASYNC: executes each operation asynchronously. These operations may
          return "non-ready" handles.
      server_def: (Optional.) A tensorflow::ServerDef proto. Enables execution
        on remote devices. GrpcServers need to be started by creating an
        identical server_def to this, and setting the appropriate task_indexes,
        so that the servers can communicate. It will then be possible to execute
        operations on remote devices.

    Raises:
     ValueError: If execution_mode is not valid.
    '''
    def ensure_initialized(self) -> None:
        """Initialize handle and devices if not already done so."""
    def mark_as_global_context(self) -> None: ...
    def get_server_def(self): ...
    def set_server_def(self, server_def, keep_alive_secs=...) -> None:
        """Allow setting a server_def on the context.

    When a server def is replaced, it effectively clears a bunch of caches
    within the context. If you attempt to use a tensor object that was pointing
    to a tensor on the remote device, it will raise an error.

    Args:
      server_def: A tensorflow::ServerDef proto. Enables execution on remote
        devices.
      keep_alive_secs: Num. seconds after which the remote end will hang up. As
        long as the client is still alive, the server state for the context will
        be kept alive. If the client is killed (or there is some failure), the
        server will clean up its context keep_alive_secs after the final RPC it
        receives.

    Raises:
      ValueError: if server_def is None.
    """
    def update_server_def(self, server_def, keep_alive_secs=...) -> None:
        """Update a server_def on the context.

    Args:
      server_def: A tensorflow::ServerDef proto. Enables execution on remote
        devices.
      keep_alive_secs: Num. seconds after which the remote end will hang up. As
        long as the client is still alive, the server state for the context will
        be kept alive. If the client is killed (or there is some failure), the
        server will clean up its context keep_alive_secs after the final RPC it
        receives.

    Raises:
      ValueError: if server_def is None.
    """
    def check_alive(self, worker_name):
        '''Checks whether a remote worker is alive or not.

    Args:
      worker_name: a string representing the remote worker. It must be a fully
      specified name like "/job:worker/replica:0/task:0".

    Returns:
      a boolean indicating whether the remote worker is alive or not.

    Raises:
      ValueError: if context is not initialized.
    '''
    def sync_executors(self) -> None:
        """Sync both local executors and the ones on remote workers.

    In async execution mode, local function calls can return before the
    corresponding remote op/function execution requests are completed. Calling
    this method creates a synchronization barrier for remote executors. It only
    returns when all remote pending nodes are finished, potentially with errors
    if any remote executors are in error state.

    Raises:
      ValueError: if context is not initialized.
    """
    def clear_executor_errors(self) -> None:
        """Clear errors in both local executors and remote workers.

    After receiving errors from remote workers, additional requests on the fly
    could further taint the status on the remote workers due to the async nature
    of remote execution. Calling this method block on waiting for all pending
    nodes in remote executors to finish and clear their error statuses.

    Raises:
      ValueError: if context is not initialized.
    """
    def configure_coordination_service(self, service_type, service_leader: str = '', enable_health_check: bool = True, cluster_register_timeout_in_ms: int = 0, heartbeat_timeout_in_ms: int = 0, shutdown_barrier_timeout_in_ms: int = 0, coordinated_jobs: Incomplete | None = None) -> None:
        """Enable distributed coordination service with specified configs."""
    @property
    def coordination_service(self): ...
    def set_config_key_value(self, key, value) -> None: ...
    def get_config_key_value(self, key): ...
    def delete_config_key_value(self, key) -> None: ...
    def report_error_to_cluster(self, error_code, error_message) -> None:
        """Report error to other members in a multi-client cluster.

    Args:
      error_code: a `tf.errors` error code.
      error_message: a string. The error message.
    """
    def get_task_states(self, job_configs):
        """Get task states from the Coordination Service.

    Args:
      job_configs: A list of tuples of job name and task number.

    Returns:
      A list of TF_Status.
    """
    def wait_at_barrier(self, barrier_id, timeout_in_ms) -> None:
        """Blocks until all coordinated tasks are at the barrier.

    The barrier may fail if it times out or if one of the tasks is unhealthy.

    Args:
      barrier_id: Unique string identifying the barrier.
      timeout_in_ms: Duration before the barrier times out and fails.
    """
    def clear_kernel_cache(self) -> None:
        """Clear kernel cache and reset all stateful kernels."""
    def enable_collective_ops(self, server_def) -> None:
        """Enable distributed collective ops with an appropriate server_def.

    Args:
      server_def: A tensorflow::ServerDef proto. Enables execution on remote
        devices.

    Raises:
      ValueError: if server_def is None.
      RuntimeError: if this method is not called at program startup.
    """
    def configure_collective_ops(self, collective_leader: str = '', scoped_allocator_enabled_ops=('CollectiveReduce',), use_nccl_communication: bool = False, device_filters: Incomplete | None = None) -> None:
        '''Configure collective ops.

      Collective group leader is necessary for collective ops to run, other
      configurations are mainly for the purpose of performance.

    Args:
      collective_leader: a device string for collective leader, e.g.
        "/job:worker/replica:0/task:0"; empty string means local execution of
          collective ops.
      scoped_allocator_enabled_ops: a tuple or a list of op names for scoped
        allocator to run with.
      use_nccl_communication: whether to use nccl communication for collective
        ops.
      device_filters: a tuple or a list of device strings. If set, corresponding
        task can only see the devices filtered by these device filters.

    Raises:
      RuntimeError: if this method is not called at program startup.
    '''
    def abort_collective_ops(self, code, message) -> None:
        """Abort the collective ops.

    This is intended to be used when a peer failure is detected, which allows
    the user to handle the case instead of hanging. This aborts all on-going
    collectives. After all subsequent collectives error immediately, and you
    need to reset_context() to use collectives again.

    Args:
      code: a `tf.errors` error code.
      message: a string. The error message.
    """
    def check_collective_ops_peer_health(self, task, timeout_in_ms) -> None:
        """Check collective peer health.

    This probes each task to see if they're still alive. Note that restarted
    tasks are considered a different one, and they're considered not healthy.

    This should only be used in multi client multi worker training.

    Args:
      task: a task string, must be in the format of /job:xxx/replica:0/task:N.
      timeout_in_ms: an integer, the timeout. If zero, there's no timeout.

    Raises:
      tf.errors.UnavailableError: when a peer is down.
      tf.errors.FailedPreconditionError: when a peer is a different one from the
        one this task has talked to, e.g. the peer has restarted.
      tf.errors.InvalidArgumentError: when the task string is invalid.
    """
    def executing_eagerly(self):
        """Returns True if current thread has eager executing enabled."""
    def ones_rank_cache(self):
        """Per-device cache for scalars."""
    def zeros_cache(self):
        """Per-device cache for scalars."""
    @property
    def scope_name(self):
        """Returns scope name for the current thread."""
    @scope_name.setter
    def scope_name(self, s) -> None:
        """Sets scope name for the current thread."""
    @property
    def device_name(self):
        """Returns the device name for the current thread."""
    @property
    def device_spec(self):
        """Returns the device spec for the current thread."""
    def device(self, name):
        """Context-manager to force placement of operations and Tensors on a device.

    Args:
      name: Name of the device or None to get default placement.

    Returns:
      Context manager that forces device placement.

    Raises:
      ValueError: If name is not a string or is an invalid device name.
      RuntimeError: If device scopes are not properly nested.
    """
    def devices(self):
        """List of the names of devices available to execute operations."""
    def host_address_space(self): ...
    @property
    def execution_mode(self):
        """Gets execution mode for current thread."""
    @execution_mode.setter
    def execution_mode(self, mode) -> None:
        """Sets execution mode for current thread."""
    def is_async(self): ...
    @property
    def executor(self): ...
    @executor.setter
    def executor(self, e) -> None: ...
    @property
    def config(self):
        """Return the ConfigProto with all runtime deltas applied."""
    @property
    def function_call_options(self):
        """Returns function call options for current thread.

    Note that the returned object is still referenced by the eager context.

    Returns: the FunctionCallOptions for current thread.
    """
    @function_call_options.setter
    def function_call_options(self, options) -> None:
        """Returns function call options for current thread."""
    def num_gpus(self):
        """The number of GPUs available to execute operations."""
    def add_function(self, fn) -> None:
        """Add a function definition to the context.

    Once added, the function (identified by its name) can be executed like any
    other operation.

    Args:
      fn: A wrapped TF_Function (returned from TF_GraphToFunction_wrapper).
    """
    def add_function_def(self, fdef) -> None:
        """Add a function definition to the context.

    Once added, the function (identified by its name) can be executed like any
    other operation.

    Args:
      fdef: A FunctionDef protocol buffer message.
    """
    def get_function_def(self, name):
        """Get a function definition from the context.

    Args:
      name: function signature name.

    Returns:
      The requested FunctionDef.

    Raises:
      tf.errors.NotFoundError: if name is not the name of a registered function.
    """
    def is_custom_device(self, device_name):
        """Calls TFE_IsCustomDevice. See the non-member function."""
    def register_custom_device(self, device_capsule, device_name, device_info_capsule) -> None:
        """Calls TFE_RegisterCustomDevice. See the non-member function."""
    def pack_eager_tensors(self, tensors):
        """Pack multiple `EagerTensor`s of the same dtype and shape.

    Args:
      tensors: a list of EagerTensors to pack.

    Returns:
      A packed EagerTensor.
    """
    def list_function_names(self):
        """Get a list of names of registered functions.

    Returns:
      A set of names of all registered functions for the context.
    """
    def remove_function(self, name) -> None:
        """Remove a function from the context.

    Once removed, the function cannot be executed anymore.

    Args:
      name: function signature name.
    """
    def has_function(self, name):
        """Check if a function `name` is registered."""
    def add_op_callback(self, callback) -> None:
        """Add a post-op callback to the context.

    A post-op callback is invoked immediately after an eager operation or
    function has finished execution or after a op has been added to a graph,
    providing access to the op's type, name input and output tensors. Multiple
    op callbacks can be added, in which case the callbacks will be invoked in
    the order in which they are added.

    Args:
      callback: a callable of the signature `f(op_type, inputs, attrs, outputs,
        op_name=None, graph=None)`. See doc strings in `op_callbacks.py` for
        details on the function signature and its semantics.
    """
    def remove_op_callback(self, callback) -> None:
        """Remove an already-registered op callback.

    Args:
      callback: The op callback to be removed.

    Raises:
      KeyError: If `callback` is not already registered.
    """
    @property
    def op_callbacks(self): ...
    @property
    def invoking_op_callbacks(self): ...
    @invoking_op_callbacks.setter
    def invoking_op_callbacks(self, value) -> None: ...
    def reinitialize_physical_devices(self) -> None:
        """Gets local devices visible to the system."""
    def list_physical_devices(self, device_type: Incomplete | None = None):
        """List local devices visible to the system.

    This API allows a client to query the devices before they have been
    initialized by the eager runtime. Additionally a user can filter by device
    type, to get only CPUs or GPUs.

    Args:
      device_type: Optional device type to limit results to

    Returns:
      List of PhysicalDevice objects.
    """
    def get_device_details(self, device):
        """Returns details about a physical devices.

    Args:
      device: A `tf.config.PhysicalDevice` returned by
        `tf.config.list_physical_devices` or `tf.config.get_visible_devices`.

    Returns:
      A dict with string keys.
    """
    def list_logical_devices(self, device_type: Incomplete | None = None):
        """Return logical devices."""
    def get_visible_devices(self, device_type: Incomplete | None = None):
        """Get the list of visible devices."""
    def set_visible_devices(self, devices, device_type: Incomplete | None = None) -> None:
        """Set the list of visible devices."""
    def get_memory_info(self, dev):
        """Returns a dict of memory info for the device."""
    def reset_memory_stats(self, dev) -> None:
        """Resets the tracked memory stats for the device."""
    def get_memory_growth(self, dev):
        """Get if memory growth is enabled for a PhysicalDevice."""
    def set_memory_growth(self, dev, enable) -> None:
        """Set if memory growth should be enabled for a PhysicalDevice."""
    def get_logical_device_configuration(self, dev):
        """Get the virtual device configuration for a PhysicalDevice."""
    def set_logical_device_configuration(self, dev, virtual_devices) -> None:
        """Set the virtual device configuration for a PhysicalDevice."""
    def set_logical_cpu_devices(self, num_cpus, prefix: str = '') -> None:
        """Set virtual CPU devices in context.

    If virtual CPU devices are already configured at context initialization
    by tf.config.set_logical_device_configuration(), this method should not be
    called.

    Args:
      num_cpus: Number of virtual CPUs.
      prefix: Device name prefix.

    Raises:
     RuntimeError: If virtual CPUs are already configured at context
     initialization.
    """
    def get_compiler_ir(self, device_name, function_name, flat_args, captured_inputs, stage: str = 'hlo'): ...
    def enable_xla_devices(self) -> None:
        """Enables XLA:CPU and XLA:GPU devices registration."""
    @property
    def enable_mlir_bridge(self): ...
    @property
    def enable_mlir_graph_optimization(self): ...
    @enable_mlir_bridge.setter
    def enable_mlir_bridge(self, enabled) -> None: ...
    @enable_mlir_graph_optimization.setter
    def enable_mlir_graph_optimization(self, enabled) -> None: ...
    @property
    def optimizer_jit(self): ...
    @optimizer_jit.setter
    def optimizer_jit(self, enabled) -> None: ...
    def get_optimizer_experimental_options(self):
        """Get experimental options for the optimizer.

    Returns:
      Dictionary of current option values
    """
    def set_optimizer_experimental_options(self, options) -> None:
        """Set experimental options for the optimizer.

    Args:
      options: Dictionary of options to modify
    """
    @property
    def intra_op_parallelism_threads(self): ...
    @intra_op_parallelism_threads.setter
    def intra_op_parallelism_threads(self, num_threads) -> None: ...
    @property
    def inter_op_parallelism_threads(self): ...
    @inter_op_parallelism_threads.setter
    def inter_op_parallelism_threads(self, num_threads) -> None: ...
    @property
    def soft_device_placement(self): ...
    @soft_device_placement.setter
    def soft_device_placement(self, enable) -> None: ...
    @property
    def log_device_placement(self): ...
    @log_device_placement.setter
    def log_device_placement(self, enable) -> None: ...
    @property
    def jit_compile_rewrite(self): ...
    @jit_compile_rewrite.setter
    def jit_compile_rewrite(self, enable) -> None: ...
    @property
    def device_policy(self): ...
    @device_policy.setter
    def device_policy(self, policy) -> None: ...
    @property
    def use_tfrt(self): ...
    @use_tfrt.setter
    def use_tfrt(self, tfrt) -> None:
        """Sets whether to use TFRT."""
    @property
    def operation_timeout_in_ms(self): ...
    @operation_timeout_in_ms.setter
    def operation_timeout_in_ms(self, timeout_in_ms) -> None: ...
    def enable_run_metadata(self) -> None:
        """Enables tracing of op execution via RunMetadata.

    To retrieve the accumulated metadata call context.export_run_metadata()
    and to stop tracing call context.disable_run_metadata().
    """
    def disable_run_metadata(self) -> None:
        """Disables tracing of op execution via RunMetadata."""
    def enable_graph_collection(self) -> None:
        """Enables graph collection of executed functions.

    To retrieve the accumulated graphs call context.export_run_metadata()
    and to stop collecting graphs call context.disable_graph_collection().
    """
    def disable_graph_collection(self) -> None:
        """Disables graph collection of executed functions."""
    def export_run_metadata(self):
        """Returns a RunMetadata proto with accumulated information.

    The returned protocol buffer contains information since the most recent call
    to either enable_run_metadata or export_run_metadata.

    Returns:
      A RunMetadata protocol buffer. Or None if not enabled.
    """
    @property
    def context_switches(self):
        """Returns a stack of context switches."""

class _EagerDeviceContext:
    """Context-manager forcing placement of ops and Tensors on a device."""
    def __init__(self, ctx, device_name) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *ex_info) -> None: ...

def context():
    """Returns a singleton context object."""
def context_safe():
    """Returns current context (or None if one hasn't been initialized)."""
def ensure_initialized() -> None:
    """Initialize the context."""
def initialize_logical_devices() -> None:
    """Initialize the virtual devices."""
def set_global_seed(seed) -> None:
    """Sets the eager mode seed."""
def global_seed():
    """Returns the eager mode seed."""
def internal_operation_seed():
    """Returns the operation seed generated based on global seed."""
def executing_eagerly():
    """Checks whether the current thread has eager execution enabled.

  Eager execution is enabled by default and this API returns `True`
  in most of cases. However, this API might return `False` in the following use
  cases.

  *  Executing inside `tf.function`, unless under `tf.init_scope` or
     `tf.config.run_functions_eagerly(True)` is previously called.
  *  Executing inside a transformation function for `tf.dataset`.
  *  `tf.compat.v1.disable_eager_execution()` is called.

  General case:

  >>> print(tf.executing_eagerly())
  True

  Inside `tf.function`:

  >>> @tf.function
  ... def fn():
  ...   with tf.init_scope():
  ...     print(tf.executing_eagerly())
  ...   print(tf.executing_eagerly())
  >>> fn()
  True
  False

  Inside `tf.function` after `tf.config.run_functions_eagerly(True)` is called:

  >>> tf.config.run_functions_eagerly(True)
  >>> @tf.function
  ... def fn():
  ...   with tf.init_scope():
  ...     print(tf.executing_eagerly())
  ...   print(tf.executing_eagerly())
  >>> fn()
  True
  True
  >>> tf.config.run_functions_eagerly(False)

  Inside a transformation function for `tf.dataset`:

  >>> def data_fn(x):
  ...   print(tf.executing_eagerly())
  ...   return x
  >>> dataset = tf.data.Dataset.range(100)
  >>> dataset = dataset.map(data_fn)
  False

  Returns:
    `True` if the current thread has eager execution enabled.
  """
def executing_eagerly_v1():
    """Checks whether the current thread has eager execution enabled.

  Eager execution is typically enabled via
  `tf.compat.v1.enable_eager_execution`, but may also be enabled within the
  context of a Python function via tf.contrib.eager.py_func.

  When eager execution is enabled, returns `True` in most cases. However,
  this API might return `False` in the following use cases.

  *  Executing inside `tf.function`, unless under `tf.init_scope` or
     `tf.config.run_functions_eagerly(True)` is previously called.
  *  Executing inside a transformation function for `tf.dataset`.
  *  `tf.compat.v1.disable_eager_execution()` is called.

  >>> tf.compat.v1.enable_eager_execution()

  General case:

  >>> print(tf.executing_eagerly())
  True

  Inside `tf.function`:

  >>> @tf.function
  ... def fn():
  ...   with tf.init_scope():
  ...     print(tf.executing_eagerly())
  ...   print(tf.executing_eagerly())
  >>> fn()
  True
  False

  Inside `tf.function`
  after  `tf.config.run_functions_eagerly(True)` is called:

  >>> tf.config.run_functions_eagerly(True)
  >>> @tf.function
  ... def fn():
  ...   with tf.init_scope():
  ...     print(tf.executing_eagerly())
  ...   print(tf.executing_eagerly())
  >>> fn()
  True
  True
  >>> tf.config.run_functions_eagerly(False)

  Inside a transformation function for `tf.dataset`:

  >>> def data_fn(x):
  ...   print(tf.executing_eagerly())
  ...   return x
  >>> dataset = tf.data.Dataset.range(100)
  >>> dataset = dataset.map(data_fn)
  False

  Returns:
    `True` if the current thread has eager execution enabled.
  """
def in_eager_mode():
    """Use executing_eagerly() instead. This function will be removed."""
def anonymous_name():
    """Returns the anonymous shared name.

  In eager mode we create anonymous resources to avoid spurious sharing issues.
  The runtime generates a unique name on our behalf when the reserved
  anonymous shared name is used as a shared name.

  Returns:
    The anonymous shared name.
  """
def graph_mode():
    """Context-manager to disable eager execution for the current thread."""
def eager_mode():
    """Context-manager to enable eager execution for the current thread."""
def scope_name():
    """Name of the current scope."""
def device(name):
    """Context-manager to force placement of operations and Tensors on a device.

  Example:
  ```python
  with tf.device('gpu:0'):
    with tf.device('cpu:0'):
      shape = tf.constant([], dtype=tf.int32)
    x = tf.random.truncated_normal(shape, tf.float32)
  ```
  will ensure that the `shape` Tensor is on CPU but the `truncated_normal`
  operation runs on GPU 0.

  Args:
    name: Name of the device (see context().devices()), or None to perform
      automatic placement.

  Returns:
    Context manager for setting the device.
  """
def get_config():
    """Get the ConfigProto of Context.

  Returns:
    The ConfigProto of Context.
  """
def get_device_name():
    """Get the device name for the current thread.

  Returns:
    The device name for the current thread.
  """
def set_soft_device_placement(enabled) -> None:
    """Set if soft device placements should be allowed.

  Args:
    enabled: Whether to enable soft device placement.
  """
def get_executor():
    """Get the Executor of the current thread.

  Returns:
    The Executor of the current thread.
  """
def get_log_device_placement():
    """Get if device placements are logged.

  Returns:
    If device placements are logged.
  """
def set_log_device_placement(enabled) -> None:
    '''Turns logging for device placement decisions on or off.

  Operations execute on a particular device, producing and consuming tensors on
  that device. This may change the performance of the operation or require
  TensorFlow to copy data to or from an accelerator, so knowing where operations
  execute is useful for debugging performance issues.

  For more advanced profiling, use the [TensorFlow
  profiler](https://www.tensorflow.org/guide/profiler).

  Device placement for operations is typically controlled by a `tf.device`
  scope, but there are exceptions, for example operations on a `tf.Variable`
  which follow the initial placement of the variable. Turning off soft device
  placement (with `tf.config.set_soft_device_placement`) provides more explicit
  control.

  >>> tf.debugging.set_log_device_placement(True)
  >>> tf.ones([])
  >>> # [...] op Fill in device /job:localhost/replica:0/task:0/device:GPU:0
  >>> with tf.device("CPU"):
  ...  tf.ones([])
  >>> # [...] op Fill in device /job:localhost/replica:0/task:0/device:CPU:0
  >>> tf.debugging.set_log_device_placement(False)

  Turning on `tf.debugging.set_log_device_placement` also logs the placement of
  ops inside `tf.function` when the function is called.

  Args:
    enabled: Whether to enabled device placement logging.
  '''
def device_policy(policy) -> Generator[None, None, None]:
    """Context manager for setting device placement policy for current thread."""
def set_execution_mode(mode) -> None:
    """Sets execution mode for the current thread."""
def execution_mode(mode) -> Generator[None, None, None]:
    """Context manager for setting execution mode for current thread."""
def executor_scope(e) -> Generator[None, None, None]:
    """Context manager for changing executor for current thread.

  Args:
    e: A Executor to execute eager ops under this scope. Setting it to None will
      switch back to use the default executor for the context.

  Yields:
    Context manager for setting the executor for current thread.
  """
def function_executor_type(executor_type) -> Generator[None, None, None]:
    """Context manager for setting the executor of eager defined functions.

  Eager defined functions are functions decorated by tf.contrib.eager.defun.

  Args:
    executor_type: a string for the name of the executor to be used to execute
      functions defined by tf.contrib.eager.defun.

  Yields:
    Context manager for setting the executor of eager defined functions.
  """
def is_async():
    """Returns true if current thread is in async mode."""
def num_gpus():
    """Get the number of available GPU devices.

  Returns:
    The number of available GPU devices.
  """
def enable_run_metadata() -> None:
    """Enables tracing of op execution via RunMetadata.

  To retrieve the accumulated metadata call context.export_run_metadata()
  and to stop tracing call context.disable_run_metadata().
  """
def disable_run_metadata() -> None:
    """Disables tracing of op execution via RunMetadata."""
def enable_graph_collection() -> None:
    """Enables graph collection of executed functions.

  To retrieve the accumulated graphs call context.export_run_metadata()
  and to stop collecting graphs call context.disable_graph_collection().
  """
def disable_graph_collection() -> None:
    """Disables graph collection of executed functions."""
def export_run_metadata():
    """Returns a RunMetadata proto with accumulated information.

  The returned protocol buffer contains information since the most recent call
  to either enable_run_metadata or export_run_metadata.

  Returns:
    A RunMetadata protocol buffer.
  """
def collect_graphs(optimized: bool = True) -> Generator[Incomplete, None, None]:
    '''Collects a flat list of pre- or post-optimization graphs.

  The collected graphs include device placements, which can be useful for
  testing.

  Usage:

  ```
  @def_function.function
  def f(x):
    return x + constant_op.constant(1.)

  with context.collect_graphs() as graphs:
    with ops.device("CPU:0"):
      f(constant_op.constant(1.))

  graph, = graphs  # `graph` contains a single GraphDef for inspection
  ```

  Args:
    optimized: whether to collect optimized graphs or non-optimized graphs

  Yields:
    A list of GraphDefs, populated when the context manager exits.
  '''
def get_server_def(): ...
def set_server_def(server_def) -> None: ...
def update_server_def(server_def) -> None: ...
def check_alive(worker_name): ...
def async_scope() -> Generator[None, None, None]:
    """Context manager for grouping async operations.

  Ops/function calls inside the scope can return before finishing the actual
  execution. When exiting the async scope, a synchronization barrier will be
  automatically added to ensure the completion of all async op and function
  execution, potentially raising exceptions if async execution results in
  an error state.

  Users may write the following code to asynchronously invoke `train_step_fn`
  and log the `loss` metric for every `num_steps` steps in a training loop.
  `train_step_fn` internally consumes data using `iterator.get_next()`, and may
  throw OutOfRangeError when running out of data. In the case:

  ```
  try:
    with tf.experimental.async_scope():
      for _ in range(num_steps):
        # Step function updates the metric `loss` internally
        train_step_fn()
  except tf.errors.OutOfRangeError:
    tf.experimental.async_clear_error()
  logging.info('loss = %s', loss.numpy())
  ```

  Yields:
    Context manager for grouping async operations.
  """
def async_wait() -> None:
    """Sync all async operations and raise any errors during execution.

  In async execution mode, an op/function call can return before finishing the
  actual execution. Calling this method creates a synchronization barrier for
  all async op and function execution. It only returns when all pending nodes
  are finished, potentially raising exceptions if async execution results in
  an error state. It is a no-op if the context is not initialized.
  """
def async_clear_error() -> None:
    """Clear pending operations and error statuses in async execution.

  In async execution mode, an error in op/function execution can lead to errors
  in subsequent ops/functions that are scheduled but not yet executed. Calling
  this method clears all pending operations and reset the async execution state.

  Example:

  ```
  while True:
    try:
      # Step function updates the metric `loss` internally
      train_step_fn()
    except tf.errors.OutOfRangeError:
      tf.experimental.async_clear_error()
      break
  logging.info('loss = %s', loss.numpy())
  ```
  """
def add_function(fdef) -> None:
    """Add a function definition to the context."""
def remove_function(name) -> None:
    """Remove a function from the context."""
def get_function_def(name): ...
def is_custom_device(device_name):
    """Calls TFE_IsCustomDevice.

  Enables using C extensions specifying a custom device from Python. See the
  experimental eager C API in tensorflow/c/eager/c_api_experimental.h for
  details.

  Args:
    device_name: A string indicating the name to check whether it is a
      registered custom device.

  Returns:
    A boolean.
  """
def register_custom_device(device_capsule, device_name, device_info_capsule) -> None:
    """Calls TFE_RegisterCustomDevice to register a custom device with Python.

  Enables using C extensions specifying a custom device from Python. See the
  experimental eager C API in tensorflow/c/eager/c_api_experimental.h for
  details.

  Note that custom devices are not currently supported inside `tf.function`s.

  Args:
    device_capsule: A PyCapsule with the name set to 'TFE_CustomDevice'
      containing a pointer to a TFE_CustomDevice struct. The capsule retains
      ownership of the memory.
    device_name: A string indicating the name to register the custom device
      under, e.g. '/job:localhost/replica:0/task:0/device:CUSTOM:0'. It may
      subsequently be passed to `with tf.device(...):`.
    device_info_capsule: A PyCapsule with the name set to
      'TFE_CustomDevice_DeviceInfo' containing a pointer to a device-specific
      struct with the initial state of the custom device (the void* device_info
      argument to TFE_RegisterCustomDevice). This method takes ownership of the
      memory and clears the capsule destructor.
  """
