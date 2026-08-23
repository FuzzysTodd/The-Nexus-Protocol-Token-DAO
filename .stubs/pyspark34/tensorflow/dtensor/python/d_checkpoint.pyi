from _typeshed import Incomplete
from tensorflow.core.protobuf import trackable_object_graph_pb2 as trackable_object_graph_pb2
from tensorflow.dtensor.python import api as api, d_variable as d_variable, gen_dtensor_ops as gen_dtensor_ops, layout as layout, save_restore as save_restore
from tensorflow.python.checkpoint import checkpoint as util, checkpoint_options as checkpoint_options, restore as restore_lib
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, errors_impl as errors_impl, ops as ops
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.trackable import base as base, data_structures as data_structures
from tensorflow.python.training import py_checkpoint_reader as py_checkpoint_reader
from tensorflow.python.training.saving import saveable_object as saveable_object, saveable_object_util as saveable_object_util
from tensorflow.python.util import deprecation as deprecation, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Dict, List, Optional

class _DSaver:
    """A single device saver that places tensors on DTensor Device."""
    def __init__(self, mesh: layout.Mesh, saveable_objects: List[saveable_object.SaveableObject]) -> None: ...
    def save(self, file_prefix: str, options: Optional[checkpoint_options.CheckpointOptions] = None) -> Optional[ops.Operation]:
        """Saves the saveable objects to a checkpoint with `file_prefix`.

    Also query the generated shards from the distributed DTensor SaveV2 ops and
    do a MergeV2 on those. Each op here is backed by a global_barrier to avoid
    racing from multiple clients.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix to
        save under.
      options: Optional `CheckpointOptions` object. This is unused in DTensor.

    Returns:
      An `Operation`, or None when executing eagerly.
    """
    def restore(self, file_prefix: str, options: Optional[checkpoint_options.CheckpointOptions] = None) -> Dict[str, ops.Operation]:
        """Restore the saveable objects from a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix for
        files to read from.
      options: Optional `CheckpointOptions` object. This is unused in DTensor.

    Returns:
      A dictionary mapping from SaveableObject names to restore operations.
    """

class _DCheckpointRestoreCoordinator(util._CheckpointRestoreCoordinator):
    """Holds the status of an object-based checkpoint load."""
    def __init__(self, mesh: layout.Mesh, **kwargs) -> None: ...
    def restore_saveables(self, tensor_saveables: Dict[str, saveable_object.SaveableObject], python_positions: List[restore_lib.CheckpointPosition], registered_savers: Optional[Dict[str, Dict[str, base.Trackable]]] = None, reader: py_checkpoint_reader.NewCheckpointReader = None) -> Optional[List[ops.Operation]]:
        """Run or build restore operations for SaveableObjects.

    Args:
      tensor_saveables: `SaveableObject`s which correspond to Tensors.
      python_positions: `CheckpointPosition`s which correspond to `PythonState`
        Trackables bound to the checkpoint.
      registered_savers: a dict mapping saver names-> object name -> Trackable.
        This argument is not implemented for DTensorCheckpoint.
      reader: A CheckpointReader. Creates one lazily if None.

    Returns:
      When graph building, a list of restore operations, either cached or newly
      created, to restore `tensor_saveables`.
    """

class DTrackableSaver(util.TrackableSaver):
    """A DTensor trackable saver that uses _SingleDeviceSaver."""
    def __init__(self, mesh: layout.Mesh, graph_view) -> None: ...
    def restore(self, save_path, options: Incomplete | None = None):
        """Restore a training checkpoint with host mesh placement."""

class DTensorCheckpoint(util.Checkpoint):
    """Manages saving/restoring trackable values to disk, for DTensor."""
    def __init__(self, mesh: layout.Mesh, root: Incomplete | None = None, **kwargs) -> None: ...
