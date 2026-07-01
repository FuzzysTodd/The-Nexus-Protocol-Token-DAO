from _typeshed import Incomplete
from tensorflow.core.protobuf import trackable_object_graph_pb2 as trackable_object_graph_pb2
from tensorflow.python.checkpoint import graph_view as graph_view_lib, save_util_v1 as save_util_v1, saveable_compat as saveable_compat, util as util
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.saved_model import registration as registration
from tensorflow.python.trackable import base as base, python_state as python_state, trackable_utils as trackable_utils
from tensorflow.python.training.saving import saveable_object_util as saveable_object_util
from tensorflow.python.types import core as core
from tensorflow.python.util import object_identity as object_identity
from typing import Any, Callable, Dict, Mapping, NamedTuple, Optional

class _TrackableData(NamedTuple):
    trackable: Incomplete
    node_id: Incomplete
    object_name: Incomplete
    children_proto: Incomplete
    slot_variable_proto: Incomplete
    object_to_save: Incomplete

def serialize_graph_view(graph_view: graph_view_lib.ObjectGraphView, object_map: Optional[Mapping[base.Trackable, base.Trackable]] = None, call_with_mapped_captures: Optional[Callable[..., Any]] = None, cache: Optional[Dict[base.Trackable, Any]] = None) -> ...:
    """Gathers serialization objects, and creates a TrackableObjectGraph proto."""
