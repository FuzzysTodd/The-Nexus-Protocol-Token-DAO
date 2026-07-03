import threading
from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.eager import context as context, tape as tape
from tensorflow.python.framework import composite_tensor as composite_tensor, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import nest as nest

def regroup(values, wrap_class=..., always_wrap: bool = False):
    """Makes a nest per-replica into a nest of PerReplica/Mirrored values.

  Args:
    values: Values to regroup
    wrap_class: Class that `values` be wrapped in.
    always_wrap: Always wrap the `values` in `wrap_class` even if the values
        are the same except for DistributeVariable.
  Returns:
    Wrapped `values`.
  """
def select_replica(replica_id, structured):
    """Specialize a nest of regular & per-replica values for one replica."""
def select_replica_mirrored(replica_id, structured):
    """Specialize a nest of regular & mirrored values for one replica."""
def assert_mirrored(structured) -> None:
    """Raises if the structured is not composed of mirrored or regular values."""
def update_regroup(extended, updates, group):
    """Regroup for an update, with dependencies to ensure all updates execute."""
def value_container(val):
    """Returns the container that this per-replica `value` belongs to.

  Args:
    val: A value returned by `call_for_each_replica()` or a variable created in
      `scope()`.

  Returns:
    A container that `value` belongs to.
    If value does not belong to any container (including the case of
    container having been destroyed), returns the value itself.
  """
def is_distributed_variable(v):
    """Determine if a variable is ds variable or TPU mirrored variable."""
def is_distributed_table(v):
    """Determine if an object is a DistributedTable."""
def validate_colocate_distributed_variable(v, extended) -> None: ...
def validate_colocate(v, extended) -> None: ...
def create_mirrored_variable(strategy, real_mirrored_creator, class_mapping, policy_mapping, **kwargs):
    """Create distributed variables with given synchronization and aggregation."""
def is_mirrored(val): ...
def is_sync_on_read(val): ...

class CachingScopeLocal(threading.local):
    """Class for maintaining thread local state for caching scope."""
    new_cache_scope_count: int
    cache_scope_exited_count: int
    def __init__(self) -> None: ...
    def enter_scope(self) -> None: ...
    def exit_scope(self) -> None: ...
    def in_caching_scope(self): ...

caching_scope_local: Incomplete

def cache_variable_reads() -> Generator[None, None, None]:
    """Scope for caching variable reads for AggregatingVariable.

  The variable reads for AggregatingVariable inside this scope are cached. i.e.
  the first read of variable reads the value from possibly remote handle, but
  subsequent reads are returned using local cached value.

  For example:
  strategy = ParameterServerStrategy...
  with strategy.scope():
    # Variable v is of AggregatingVariable type with actual variable residing
    # on PS.
    v = tf.Variable(1.0)

  with distribute_utils.cache_variable_reads():
    v.read_value()  # Reads value 1.0
    v.assign(constant_op.constant(5.0))  # v changes to 5.0
    t1 = v.read_value()
    t2 = v.read_value()  # Both t1 & t2 return cached value 1.0 from local CPU.

  Notes about cache_variable_reads scope:
  1. Nesting of scope cache_variable_reads() is not supported
  2. And when caching scope is enabled, the thread enabling the cache and
    mirrored_run._MirroredReplicaThread threads spawned from it will have
    caching enabled.

  Yields:
    A context for caching variables.
  """

VARIABLE_POLICY_MAPPING: Incomplete
VARIABLE_CLASS_MAPPING: Incomplete
TPU_VARIABLE_POLICY_MAPPING: Incomplete
TPU_VARIABLE_CLASS_MAPPING: Incomplete
