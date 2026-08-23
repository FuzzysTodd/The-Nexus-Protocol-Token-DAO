from _typeshed import Incomplete

def pretty_print_node_path(path): ...

class CyclicDependencyError(Exception):
    leftover_dependency_map: Incomplete
    def __init__(self, leftover_dependency_map) -> None:
        """Creates a CyclicDependencyException."""

def order_by_dependency(dependency_map):
    """Topologically sorts the keys of a map so that dependencies appear first.

  Uses Kahn's algorithm:
  https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm

  Args:
    dependency_map: a dict mapping values to a list of dependencies (other keys
      in the map). All keys and dependencies must be hashable types.

  Returns:
    A sorted array of keys from dependency_map.

  Raises:
    CyclicDependencyError: if there is a cycle in the graph.
    ValueError: If there are values in the dependency map that are not keys in
      the map.
  """

OBJECT_ATTRIBUTES_NAME: Incomplete
SERIALIZE_TO_TENSORS_NAME: Incomplete

def escape_local_name(name): ...
def object_path_to_string(node_path_arr):
    """Converts a list of nodes to a string."""
def checkpoint_key(object_path, local_name):
    """Returns the checkpoint key for a local attribute of an object."""
def extract_object_name(key):
    '''Substrings the checkpoint key to the start of "/.ATTRIBUTES".'''
def extract_local_name(key, prefix: Incomplete | None = None):
    '''Returns the substring after the "/.ATTIBUTES/" in the checkpoint key.'''
def slot_variable_key(variable_path, optimizer_path, slot_name):
    """Returns checkpoint key for a slot variable."""
