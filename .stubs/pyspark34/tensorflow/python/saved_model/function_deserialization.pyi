from _typeshed import Incomplete
from tensorflow.core.protobuf import saved_object_graph_pb2 as saved_object_graph_pb2
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.framework import op_def_registry as op_def_registry, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import custom_gradient as custom_gradient, default_gradient as default_gradient, resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import compat as compat, nest as nest, tf_decorator as tf_decorator, tf_inspect as tf_inspect

def setup_bare_concrete_function(saved_bare_concrete_function, concrete_functions):
    """Makes a restored bare concrete function callable."""

class RestoredFunction(def_function.Function):
    """Wrapper class for a function that has been restored from saved state.

  See `def_function.Function`.
  """
    concrete_functions: Incomplete
    def __init__(self, python_function, name, function_spec, concrete_functions) -> None: ...

def recreate_function(saved_function, concrete_functions):
    """Creates a `Function` from a `SavedFunction`.

  Args:
    saved_function: `SavedFunction` proto.
    concrete_functions: map from function name to `ConcreteFunction`. As a side
      effect of this function, the `FunctionSpec` from `saved_function` is added
      to each `ConcreteFunction` in this map.

  Returns:
    A `Function`.
  """
def load_function_def_library(library, saved_object_graph: Incomplete | None = None, load_shared_name_suffix: Incomplete | None = None, wrapper_function: Incomplete | None = None):
    """Load a set of functions as concrete functions without captured inputs.

  Functions names are manipulated during load such that they do not overlap
  with previously created ones.

  Gradients are re-registered under new names. Ops that reference the gradients
  are updated to reflect the new registered names.

  Args:
    library: FunctionDefLibrary proto message.
    saved_object_graph: SavedObjectGraph proto message. If not passed in,
      concrete function structured signatures and outputs will not be set.
    load_shared_name_suffix: If specified, used to uniquify shared names.
      Otherwise, a unique name is generated.
    wrapper_function: An object that will be wrapped on newly created functions.

  Returns:
    Map of original function names in the library to instances of
    `ConcreteFunction` without captured inputs.

  Raises:
    ValueError: if functions dependencies have a cycle.
  """
def fix_node_def(node_def, functions, shared_name_suffix) -> None:
    """Replace functions calls and shared names in `node_def`."""
