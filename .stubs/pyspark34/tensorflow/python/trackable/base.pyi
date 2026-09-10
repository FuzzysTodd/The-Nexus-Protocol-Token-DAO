from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops
from tensorflow.python.trackable import constants as constants
from tensorflow.python.training.saving import saveable_object as saveable_object
from tensorflow.python.util import tf_contextlib as tf_contextlib, tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

OBJECT_GRAPH_PROTO_KEY: Incomplete
VARIABLE_VALUE_KEY: Incomplete
OBJECT_CONFIG_JSON_KEY: Incomplete
SaveType = constants.SaveType

class TrackableReference:
    """A named reference to a trackable object for use with the `Trackable` class.

  These references mark named `Trackable` dependencies of a `Trackable` object
  and should be created when overriding `Trackable._checkpoint_dependencies`.

  Attributes:
    name: The local name for this dependency.
    ref: The `Trackable` object being referenced.
  """
    def __init__(self, name, ref) -> None: ...
    @property
    def name(self): ...
    @property
    def ref(self): ...
    def __iter__(self): ...
    def __eq__(self, o): ...

class WeakTrackableReference(TrackableReference):
    """TrackableReference that stores weak references."""
    def __init__(self, name, ref) -> None: ...
    @property
    def ref(self): ...

class ShardInfo(NamedTuple):
    shape: Incomplete
    offset: Incomplete

class CheckpointInitialValueCallable:
    """A callable object that returns a CheckpointInitialValue.

  See CheckpointInitialValue for more information.
  """
    def __init__(self, checkpoint_position) -> None: ...
    @property
    def checkpoint_position(self): ...
    def __call__(self, shape: Incomplete | None = None, dtype: Incomplete | None = None, shard_info: Incomplete | None = None): ...
    @property
    def restore_uid(self): ...

class CheckpointInitialValue(ops.Tensor):
    """Tensor wrapper for managing update UIDs in `Variables`.

  When supplied as an initial value, objects of this type let a `Variable`
  (`Variable`, `ResourceVariable`, etc.) know the UID of the restore the initial
  value came from. This allows deferred restorations to be sequenced in the
  order the user specified them, and lets us fall back on assignment if an
  initial value is not set (e.g. due to a custom getter interfering).

  See comments in _add_variable_with_custom_getter for more information about
  how `CheckpointInitialValue` is used.
  """
    wrapped_value: Incomplete
    def __init__(self, checkpoint_position, shape: Incomplete | None = None, shard_info: Incomplete | None = None) -> None: ...
    def __getattr__(self, attr): ...
    @property
    def checkpoint_position(self): ...

class NoRestoreSaveable(saveable_object.SaveableObject):
    """Embeds a tensor in a checkpoint with no restore ops."""
    def __init__(self, tensor, name, dtype: Incomplete | None = None, device: Incomplete | None = None) -> None: ...
    def restore(self, restored_tensors, restored_shapes): ...

class _SlotVariableRestoration(NamedTuple):
    optimizer_id: Incomplete
    slot_variable_id: Incomplete
    slot_name: Incomplete

def no_automatic_dependency_tracking(method):
    """Disables automatic dependency tracking on attribute assignment.

  Use to decorate any method of a Trackable object. Attribute assignment in
  that method will not add dependencies (also respected in Model). Harmless if
  used in a class which does not do automatic dependency tracking (which means
  it's safe to use in base classes which may have subclasses which also inherit
  from Trackable).

  Args:
    method: The method to decorate.

  Returns:
    A decorated method which sets and un-sets automatic dependency tracking for
    the object the method is called on (not thread safe).
  """
def no_manual_dependency_tracking_scope(obj) -> Generator[None, None, None]:
    '''A context that disables manual dependency tracking for the given `obj`.

  Sometimes library methods might track objects on their own and we might want
  to disable that and do the tracking on our own. One can then use this context
  manager to disable the tracking the library method does and do your own
  tracking.

  For example:

  class TestLayer(tf.keras.Layer):
    def build():
      with no_manual_dependency_tracking_scope(self):
        var = self.add_variable("name1")  # Creates a var and doesn\'t track it
      self._track_trackable("name2", var)  # We track variable with name `name2`

  Args:
    obj: A trackable object.

  Yields:
    a scope in which the object doesn\'t track dependencies manually.
  '''
def no_automatic_dependency_tracking_scope(obj) -> Generator[None, None, None]:
    """A context that disables automatic dependency tracking when assigning attrs.

  Objects that inherit from Autotrackable automatically creates dependencies
  to trackable objects through attribute assignments, and wraps data structures
  (lists or dicts) with trackable classes. This scope may be used to temporarily
  disable this behavior. This works similar to the decorator
  `no_automatic_dependency_tracking`.

  Example usage:
  ```
  model = tf.keras.Model()
  model.arr1 = []  # Creates a ListWrapper object
  with no_automatic_dependency_tracking_scope(model):
    model.arr2 = []  # Creates a regular, untracked python list
  ```

  Args:
    obj: A trackable object.

  Yields:
    a scope in which the object doesn't track dependencies.
  """

class Trackable:
    """Base class for `Trackable` objects without automatic dependencies.

  This class has no __setattr__ override for performance reasons. Dependencies
  must be added explicitly. Unless attribute assignment is performance-critical,
  use `AutoTrackable` instead. Use `Trackable` for `isinstance`
  checks.
  """
