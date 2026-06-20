from _typeshed import Incomplete
from tensorflow.python.compiler.xla.experimental import xla_sharding as xla_sharding
from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, resource_variable_ops as resource_variable_ops, variable_scope as variable_scope, variables as variables

def create_slot(primary, val, name, colocate_with_primary: bool = True, *, copy_xla_sharding: bool = False):
    """Create a slot initialized to the given value.

  The type of the slot is determined by the given value.

  Args:
    primary: The primary `Variable` or `Tensor`.
    val: A `Tensor` specifying the initial value of the slot.
    name: Name to use for the slot variable.
    colocate_with_primary: Boolean.  If True the slot is located
      on the same device as `primary`.
    copy_xla_sharding: Boolean. If True also copies XLA sharding
      from primary.

  Returns:
    A `Variable` object.
  """
def create_slot_with_initializer(primary, initializer, shape, dtype, name, colocate_with_primary: bool = True, *, copy_xla_sharding: bool = False):
    """Creates a slot initialized using an `Initializer`.

  The type of the slot is determined by the given value.

  Args:
    primary: The primary `Variable` or `Tensor`.
    initializer: An `Initializer`.  The initial value of the slot.
    shape: Shape of the initial value of the slot.
    dtype: Type of the value of the slot.
    name: Name to use for the slot variable.
    colocate_with_primary: Boolean.  If True the slot is located
      on the same device as `primary`.
    copy_xla_sharding: Boolean. If True also copies XLA sharding
      from primary.

  Returns:
    A `Variable` object.
  """
def create_zeros_slot(primary, name, dtype: Incomplete | None = None, colocate_with_primary: bool = True, *, copy_xla_sharding: bool = False):
    """Create a slot initialized to 0 with same shape as the primary object.

  Args:
    primary: The primary `Variable` or `Tensor`.
    name: Name to use for the slot variable.
    dtype: Type of the slot variable.  Defaults to the type of `primary`.
    colocate_with_primary: Boolean.  If True the slot is located
      on the same device as `primary`.
    copy_xla_sharding: Boolean. If True also copies XLA sharding
      from primary.

  Returns:
    A `Variable` object.
  """
