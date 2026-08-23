from tensorflow.core.protobuf import saved_object_graph_pb2 as saved_object_graph_pb2
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import nest as nest

def serialize_concrete_function(concrete_function, node_ids):
    """Build a SavedConcreteFunction."""
def serialize_bare_concrete_function(concrete_function):
    """Build a SavedBareConcreteFunction."""
def serialize_function(function, concrete_functions):
    """Build a SavedFunction proto."""
def wrap_cached_variables(concrete_function):
    """Wraps the concrete function if it uses cached read tensors.

  This function creates a new concrete function that captures variables
  instead of the cached read tensors.

  Args:
    concrete_function: A Concrete function that maybe captures cached read
      tensors.

  Returns:
    A concrete function that wraps the original concrete function, which
    captures variables instead. If the original function did not capture any
    cached values, then the function is not wrapped and the original object is
    returned.
  """
