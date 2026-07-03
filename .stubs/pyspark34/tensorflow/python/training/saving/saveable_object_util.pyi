from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.checkpoint import saveable_compat as saveable_compat
from tensorflow.python.client import session as session
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, resource_variable_ops as resource_variable_ops, state_ops as state_ops, variables as variables
from tensorflow.python.trackable import base as trackable, python_state as python_state, trackable_utils as trackable_utils
from tensorflow.python.training.saving import saveable_object as saveable_object
from tensorflow.python.types import core as core
from tensorflow.python.util import compat as compat, nest as nest, object_identity as object_identity
from tensorflow.python.util.tf_export import tf_export as tf_export

def set_cpu0(device_string):
    """Creates a new device string based on `device_string` but using /CPU:0.

  If the device is already on /CPU:0 or it is a custom device, this is a no-op.

  Args:
    device_string: A device string.

  Returns:
    A device string.
  """

class ReferenceVariableSaveable(saveable_object.SaveableObject):
    """SaveableObject implementation that handles reference variables."""
    def __init__(self, var, slice_spec, name) -> None: ...
    def restore(self, restored_tensors, restored_shapes): ...

class ResourceVariableSaveable(saveable_object.SaveableObject):
    """SaveableObject implementation that handles ResourceVariables."""
    handle_op: Incomplete
    def __init__(self, var, slice_spec, name) -> None: ...
    def restore(self, restored_tensors, restored_shapes):
        """Restores tensors. Raises ValueError if incompatible shape found."""

def saveable_objects_for_op(op, name) -> Generator[Incomplete, None, None]:
    """Create `SaveableObject`s from an operation.

  Args:
    op: A variable, operation, or SaveableObject to coerce into a
      SaveableObject.
    name: A string name for the SaveableObject.

  Yields:
    `SaveableObject`s which together save/restore `op`.

  Raises:
    TypeError: If `name` is not a string.
    ValueError: For operations with no known conversion to SaveableObject.
  """
def op_list_to_dict(op_list, convert_variable_to_tensor: bool = True):
    """Create a dictionary of names to operation lists.

  This method is only used when the variable name matters (e.g. when saving
  or restoring from a TF1 name-based checkpoint). In TF2, this can be called
  from `tf.train.Checkpoint.restore` when loading from a name-based checkpoint.

  Args:
    op_list: A (nested) list, tuple, or set of Variables or SaveableObjects.
    convert_variable_to_tensor: Whether or not to convert single Variables
      with no slice info into Tensors.

  Returns:
    A dictionary of names to the operations that must be saved under
    that name.  Variables with save_slice_info are grouped together under the
    same key in no particular order.

  Raises:
    TypeError: If the type of op_list or its elements is not supported.
    ValueError: If at least two saveables share the same name.
  """
def validate_and_slice_inputs(names_to_saveables):
    """Returns the variables and names that will be used for a Saver.

  Args:
    names_to_saveables: A dict (k, v) where k is the name of an operation and
       v is an operation to save or a BaseSaverBuilder.Saver.

  Returns:
    A list of SaveableObjects.

  Raises:
    TypeError: If any of the keys are not strings or any of the
      values are not one of Tensor or Variable or a trackable operation.
    ValueError: If the same operation is given in more than one value
      (this also applies to slices of SlicedVariables).
  """
def trace_save_restore_function_map(obj, factory_data_list):
    """Traces all save and restore functions in the provided factory list.

  Args:
    obj: `Trackable` object.
    factory_data_list: List of `_CheckpointFactoryData`.

  Returns:
    Dict mapping atttribute names to tuples of concrete save/restore functions.
  """
def validate_saveables_for_saved_model(saveables, obj):
    """Makes sure SaveableObjects are compatible with SavedModel."""

class RestoredSaveableObject(saveable_object.SaveableObject):
    """SaveableObject restored from SavedModel using the traced save/restore."""
    save_function: Incomplete
    restore_function: Incomplete
    def __init__(self, names_and_slices, save_function, restore_function, name) -> None: ...
    def restore(self, restored_tensors, restored_shapes): ...

def recreate_saveable_objects(saveable_fn_by_name, temp_session):
    """Returns a dict of SaveableObject factories generated from loaded fns."""
def create_saveable_object(name, key, factory, call_with_mapped_captures):
    """Creates a SaveableObject while potentially in a different graph.

  When creating the frozen saver for SavedModel, the save and restore ops are
  placed in a separate graph. Since RestoredSaveableObject uses tf.functions to
  save and restore, the function captures must be mapped to the new graph.

  Args:
    name: Name of SaveableObject factory.
    key: Checkpoint key of this SaveableObject.
    factory: Factory method for creating the SaveableObject.
    call_with_mapped_captures: Helper that calls a tf.function while remapping
      the captures.

  Returns:
    a SaveableObject.
  """
def is_factory_for_restored_saveable_object(factory): ...
def saveable_objects_from_trackable(obj, tf1_saver: bool = False):
    """Returns SaveableObject factory dict from a Trackable.

  Args:
    obj: A `Trackable`
    tf1_saver: Boolean, whether this is being called from a TF1 Saver (
        `tf.compat.v1.train.Saver`). When this is True, the SaveableObject will
        be generated from `obj`'s legacy `_gather_saveables_for_checkpoint` fn.
        When saving with TF2, `Trackable._serialize_from_tensors` is preferred.

  Returns:
    A dict mapping attribute names to SaveableObject factories (callables that
    produce a SaveableObject).
  """

class TrackableSaveable(saveable_object.SaveableObject):
    """A SaveableObject that defines `Trackable` checkpointing steps."""
    def __init__(self, obj, specs, name, local_names, prefix, call_with_mapped_captures: Incomplete | None = None) -> None: ...
    def restore(self, restored_tensors, restored_shapes): ...
    def get_proto_names_and_checkpoint_keys(self): ...

class _PythonStringStateSaveable(saveable_object.SaveableObject):
    """Saves Python state in a checkpoint."""
    def __init__(self, name, state_callback, restore_callback) -> None:
        """Configure saving.

    Args:
      name: The checkpoint key to write to.
      state_callback: A function taking no arguments which returns a string.
        This function is run every time a checkpoint is written.
      restore_callback: A function taking a Python string, used to restore
        state.
    """
    def feed_dict_additions(self):
        """When running a graph, indicates fresh state to feed."""
    def freeze(self):
        """Create a frozen `SaveableObject` which saves the current state."""

def trackable_has_serialize_to_tensor(obj):
    """Returns whether obj's class has `_serialize_to_tensors` defined."""

class SaveableCompatibilityConverter(trackable.Trackable):
    """Converts object's `SaveableObjects` to functions used in TF2 checkpointing.

  A class that converts a Trackable object's `SaveableObjects` to save and
  restore functions with the same signatures as
  `Trackable._serialize_to_tensors` and `Trackable._restore_from_tensors`.
  This class also produces a method for filling the object proto.
  """
    def __init__(self, obj, saveables) -> None:
        """Constructor.

    Args:
      obj: A Trackable object.
      saveables: A list of saveables for `obj`.
    """
    @property
    def obj(self): ...
    @property
    def saveables(self):
        """Returns a list of SaveableObjects generated from the Trackable object."""

def saveable_object_to_tensor_dict(saveables):
    """Converts a list of SaveableObjects to a tensor dictionary."""
def saveable_object_to_restore_fn(saveables):
    """Generates `Trackable._restore_from_tensors` from SaveableObjects."""
def serialized_tensors_to_saveable_cache(serialized_tensors):
    """Converts a tensor dict to a SaveableObject cache.

  Args:
    serialized_tensors: Map from Trackable to a tensor dict. The tensor dict
      maps checkpoint key (-> slice_spec) -> Tensor

  Returns:
    A dict mapping Trackable objects to a map from local savable name to
    SaveableObject.
  """
