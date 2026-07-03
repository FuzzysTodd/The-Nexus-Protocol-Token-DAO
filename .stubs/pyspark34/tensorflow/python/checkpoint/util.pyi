from tensorflow.core.protobuf import trackable_object_graph_pb2 as trackable_object_graph_pb2
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops, variables as variables
from tensorflow.python.trackable import trackable_utils as trackable_utils
from tensorflow.python.util import object_identity as object_identity

def serialize_slot_variables(trackable_objects, node_ids, object_names):
    """Gather and name slot variables."""
def get_mapped_trackable(trackable, object_map):
    """Returns the mapped trackable if possible, otherwise returns trackable."""
def get_full_name(var):
    """Gets the full name of variable for name-based checkpoint compatiblity."""
def add_checkpoint_values_check(object_graph_proto) -> None:
    """Determines which objects have checkpoint values and save this to the proto.

  Args:
    object_graph_proto: A `TrackableObjectGraph` proto.
  """
def objects_ids_and_slot_variables_and_paths(graph_view):
    """Traverse the object graph and list all accessible objects.

  Looks for `Trackable` objects which are dependencies of
  `root_trackable`. Includes slot variables only if the variable they are
  slotting for and the optimizer are dependencies of `root_trackable`
  (i.e. if they would be saved with a checkpoint).

  Args:
    graph_view: A GraphView object.

  Returns:
    A tuple of (trackable objects, paths from root for each object,
                object -> node id, slot variables, object_names)
  """
def list_objects(graph_view):
    """Traverse the object graph and list all accessible objects."""
