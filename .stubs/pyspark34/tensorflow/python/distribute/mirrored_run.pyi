import threading
from _typeshed import Incomplete
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.distribute import distribute_lib as distribute_lib, distribute_utils as distribute_utils, shared_variable_creator as shared_variable_creator
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import summary_ops_v2 as summary_ops_v2, variable_scope as variable_scope
from tensorflow.python.training import coordinator as coordinator
from tensorflow.python.util import traceback_utils as traceback_utils

def call_for_each_replica(strategy, fn, args: Incomplete | None = None, kwargs: Incomplete | None = None):
    """Call `fn` on each worker devices(replica).

  It's highly recommended to wrap the call to this function inside a
  `tf.function`, otherwise the performance is poor.

  Args:
    strategy: `tf.distribute.Strategy`.
    fn: function to call on each worker devices.
    args: positional arguments to `fn`.
    kwargs: keyword arguments to `fn`.

  Returns:
    Wrapped returned value of `fn` from all replicas.
  """

class _RequestedStop(Exception): ...

class _MirroredReplicaThread(threading.Thread):
    """A thread that runs() a function on a device."""
    coord: Incomplete
    distribution: Incomplete
    devices: Incomplete
    replica_id: Incomplete
    replica_id_in_sync_group: Incomplete
    variable_creator_fn: Incomplete
    main_fn: Incomplete
    main_args: Incomplete
    main_kwargs: Incomplete
    main_result: Incomplete
    done: bool
    merge_fn: Incomplete
    merge_args: Incomplete
    merge_kwargs: Incomplete
    merge_result: Incomplete
    captured_name_scope: Incomplete
    captured_var_scope: Incomplete
    caching_scope_entered: Incomplete
    caching_scope_exited: Incomplete
    should_run: Incomplete
    has_paused: Incomplete
    in_eager: Incomplete
    context_device_policy: Incomplete
    graph: Incomplete
    def __init__(self, dist, coord, replica_id, devices, variable_creator_fn, fn, caching_scope, args, kwargs, thread_local_callables: Incomplete | None = None) -> None: ...
    def run(self) -> None: ...
    def record_thread_local_summary_state(self) -> None:
        """Record the thread local summary state in self."""
    def restore_thread_local_summary_state(self) -> None:
        """Restore thread local summary state from self."""
    def record_thread_local_eager_context_state(self) -> None: ...
    def restore_thread_local_eager_context_state(self) -> None: ...
    def restore_thread_local_callable(self) -> None: ...

class _MirroredReplicaContext(distribute_lib.ReplicaContext):
    """ReplicaContext for synchronized replica."""
    @property
    def devices(self): ...
