from _typeshed import Incomplete
from tensorflow.python.checkpoint import checkpoint_view as checkpoint_view, functional_saver as functional_saver, save_util_v1 as save_util_v1, saveable_compat as saveable_compat
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, io_ops as io_ops
from tensorflow.python.saved_model import registration as registration
from tensorflow.python.trackable import base as base, constants as constants, python_state as python_state, trackable_utils as trackable_utils
from tensorflow.python.util import object_identity as object_identity
from typing import NamedTuple

class CheckpointPosition:
    """Indicates a position within a `_CheckpointRestoreCoordinator`."""
    skip_restore: bool
    def __init__(self, checkpoint, proto_id) -> None:
        """Specify an object within a checkpoint.

    Args:
      checkpoint: A _CheckpointRestoreCoordinator object.
      proto_id: The index of this object in TrackableObjectGraph.nodes.
    """
    def restore(self, trackable, reader: Incomplete | None = None) -> None:
        """Restore this value into `trackable`."""
    def bind_object(self, trackable):
        """Set a checkpoint<->object correspondence.

    Args:
      trackable: The object to record a correspondence for.

    Returns:
      True if this is a new assignment, False if this object has already been
      mapped to a checkpointed `Object` proto.
    Raises:
      AssertionError: If another object is already bound to the `Object` proto.
    """
    def is_simple_variable(self):
        """Determine whether this value is restorable with a Tensor initializer."""
    def value_tensors(self, shape_and_slices: Incomplete | None = None):
        """Create value `Tensor`s for this object's attributes.

    Does not require that the Python object has been created. Used for
    restore-on-create when executing eagerly.

    Args:
      shape_and_slices: A dict mapping from object attribute names to a shape
        and slice string that will be passed to a RestoreV2 op. If the dict is
        None or if an object attribute is not in the dict, the full tensor will
        be restored.

    Returns:
      A dictionary mapping from object attribute names to `Tensor`s.
    """
    def gather_ops_or_named_saveables(self):
        """Looks up or creates SaveableObjects which don't have cached ops.

    Returns:
      A tuple of (
          existing_restore_ops: list,
          named_saveables: dict,
          python_positions: list,
          registered_savers: dict)
    """
    def restore_ops(self, reader: Incomplete | None = None):
        """Create or fetch restore ops for this object's attributes.

    Requires that the `Trackable` Python object has been bound to an object
    ID in the checkpoint.

    Args:
      reader: A `CheckpointReader`. If None, a new instance will be created.

    Returns:
      A list of operations when graph building, or an empty list when executing
      eagerly.
    """
    @property
    def checkpoint(self): ...
    @property
    def trackable(self): ...
    @property
    def object_proto(self): ...
    @property
    def proto_id(self): ...
    @property
    def restore_uid(self): ...
    def value_shape(self):
        """The shape of the VARIABLE_VALUE tensor.

    Returns:
      If found a TensorShape object, otherwise None.
    """
    def get_registered_saver_name(self):
        """Returns the registered saver name defined in the Checkpoint."""
    def create_slot_variable_position(self, optimizer_object, variable, slot_variable_id, slot_name):
        """Generates CheckpointPosition for a slot variable.

    Args:
      optimizer_object: Optimizer that owns the slot variable.
      variable: Variable associated with the slot variable.
      slot_variable_id: ID of the slot variable.
      slot_name: Name of the slot variable.

    Returns:
      If there is a slot variable in the `optimizer_object` that has not been
      bound to the checkpoint, this function returns a tuple of (
        new `CheckpointPosition` for the slot variable,
        the slot variable itself).
    """
    def create_child_position(self, node_id): ...

def restore_nodes(save_path, nodes_to_restore) -> None:
    """Restores nodes from a dict.

  Requires that the `Trackable` Python object has been bound to an object
  ID in the checkpoint.

  Args:
    save_path: a string represents path to the checkpoint.
    nodes_to_restore: a dict maps `node_id` to `trackable` to be restored.
  """

class _DeferredSlotVariableRestoration(NamedTuple):
    original_variable: Incomplete
    slot_variable_id: Incomplete
    slot_name: Incomplete
