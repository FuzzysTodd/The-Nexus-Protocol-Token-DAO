from _typeshed import Incomplete
from tensorflow.python.compiler.xla.experimental import xla_sharding as xla_sharding
from tensorflow.python.distribute import tpu_util as tpu_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops, tensor_conversion_registry as tensor_conversion_registry
from tensorflow.python.ops import control_flow_ops as control_flow_ops, gen_resource_variable_ops as gen_resource_variable_ops, variable_scope as variable_scope, variables as variables_lib
from tensorflow.python.saved_model import save_context as save_context

class TPUReplicatedVariable(variables_lib.Variable):
    """Container for replicated `Variables` that are treated as a single variable.

  This class maintains a list of replicated variables that are stored on
  separate logic TPU devices. TF2XLA bridge accesses these variables as
  if they were a single variable.
  """
    def __init__(self, variables, name: str = 'TPUReplicatedVariable') -> None:
        '''Treats `variables` as a replicated list of `tf.Variable`s.

    Example:

    ```
    variables = [
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
    ]
    replicated_variable = TPUReplicatedVariable(variables)
    assert replicated_variable.shape.as_list() == [10, 100]
    ```

    Args:
      variables: A list of `ResourceVariable`s that comprise this replicated
        variable. Variables should not be shared between different
        `TPUReplicatedVariable` objects.
      name: String. Name of this container. Defaults to "TPUReplicatedVariable".
    '''
    def __iter__(self):
        """Return an iterable for accessing the underlying sharded variables."""
    @property
    def name(self):
        """The name of this object. Used for checkpointing."""
    @property
    def dtype(self):
        """The dtype of all `Variable`s in this object."""
    @property
    def is_initialized(self): ...
    @property
    def trainable(self): ...
    @property
    def device(self):
        """The device this variable is on."""
    @property
    def constraint(self): ...
    @property
    def graph(self): ...
    @property
    def synchronization(self): ...
    @property
    def aggregation(self): ...
    @property
    def variables(self):
        """The list of `Variables`."""
    @property
    def shape(self): ...
    @property
    def handle(self): ...
    def read_value(self): ...
    def assign(self, value, use_locking: bool = False, name: Incomplete | None = None, read_value: bool = True): ...
    def assign_sub(self, value, use_locking: bool = False, name: Incomplete | None = None, read_value: bool = True): ...
    def assign_add(self, value, use_locking: bool = False, name: Incomplete | None = None, read_value: bool = True): ...
