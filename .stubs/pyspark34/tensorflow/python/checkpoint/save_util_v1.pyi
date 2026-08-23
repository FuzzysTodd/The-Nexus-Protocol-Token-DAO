from _typeshed import Incomplete
from tensorflow.core.protobuf import trackable_object_graph_pb2 as trackable_object_graph_pb2
from tensorflow.python.checkpoint import saveable_compat as saveable_compat, util as util
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.saved_model import registration as registration
from tensorflow.python.trackable import base as base, python_state as python_state, trackable_utils as trackable_utils
from tensorflow.python.training.saving import saveable_object_util as saveable_object_util
from tensorflow.python.util import object_identity as object_identity
from typing import NamedTuple

class _CheckpointFactoryData(NamedTuple):
    factory: Incomplete
    name: Incomplete
    checkpoint_key: Incomplete

def get_checkpoint_factories_and_keys(object_names, object_map: Incomplete | None = None):
    """Gets a map of saveable factories and corresponding checkpoint keys.

  Args:
    object_names: a dictionary that maps `Trackable` objects to auto-generated
      string names.
    object_map: a dictionary mapping `Trackable` to copied `Trackable` objects.
      The copied objects are generated from `Trackable.
      _export_to_saved_model_graph()` which copies the object into another
      graph. Generally only resource objects (e.g. Variables, Tables) will be
      in this map.

  Returns:
    A tuple of (
      Dictionary mapping trackable -> list of _CheckpointFactoryData,
      Dictionary mapping registered saver name -> {object name -> trackable})
  """
def generate_saveable_objects(checkpoint_factory_map, object_graph_proto: Incomplete | None = None, node_ids: Incomplete | None = None, object_map: Incomplete | None = None, call_with_mapped_captures: Incomplete | None = None, saveables_cache: Incomplete | None = None):
    """Create SaveableObjects and corresponding SerializedTensor protos."""
def serialize_gathered_objects(graph_view, object_map: Incomplete | None = None, call_with_mapped_captures: Incomplete | None = None, saveables_cache: Incomplete | None = None):
    """Create SaveableObjects and protos for gathered objects."""
def serialize_object_graph_with_registered_savers(graph_view, saveables_cache):
    """Determine checkpoint keys for variables and build a serialized graph."""
def frozen_saveables_and_savers(graph_view, object_map: Incomplete | None = None, to_graph: Incomplete | None = None, call_with_mapped_captures: Incomplete | None = None, saveables_cache: Incomplete | None = None):
    """Generates SaveableObjects and registered savers in the frozen graph."""
