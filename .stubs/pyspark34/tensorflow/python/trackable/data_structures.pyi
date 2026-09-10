from .....third_party import wrapt
from _typeshed import Incomplete
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.ops import variables as variables
from tensorflow.python.saved_model import revived_types as revived_types
from tensorflow.python.trackable import base as base, layer_utils as layer_utils
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export

class NoDependency:
    '''Allows attribute assignment to `Trackable` objects with no dependency.

  Example usage:
  ```python
  obj = Trackable()
  obj.has_dependency = tf.Variable(0., name="dep")
  obj.no_dependency = NoDependency(tf.Variable(1., name="nodep"))
  assert obj.no_dependency.name == "nodep:0"
  ```

  `obj` in this example has a dependency on the variable "dep", and both
  attributes contain un-wrapped `Variable` objects.

  `NoDependency` also works with `tf.keras.Model`, but only for checkpoint
  dependencies: wrapping a `Layer` in `NoDependency` will assign the (unwrapped)
  `Layer` to the attribute without a checkpoint dependency, but the `Model` will
  still track the `Layer` (so it will appear in `Model.layers`, and its
  variables will appear in `Model.variables`).
  '''
    value: Incomplete
    def __init__(self, value) -> None: ...

def wrap_or_unwrap(value):
    """Wraps input value into trackable data structures.

  This is mostly useful for containers like list, dict, etc, which could contain
  trackable objects in it. Wrapped data structure will be tracked when
  associated with a `tf.Module`, so that save model/checkpoint can properly
  track the dependency.

  It will also unwrap NoDependency objects.

  Args:
    value: the input object to be wrapped.

  Returns:
    Wrapped trackable data structure.
  """
def sticky_attribute_assignment(trackable, name, value):
    """Adds dependencies, generally called from __setattr__.

  This behavior is shared between Trackable and Model.

  Respects NoDependency indicators, but otherwise makes trackable objects
  out of common data structures and tracks objects by their attribute names.

  Args:
    trackable: The object to add dependencies to (generally the one having
      an attribute assigned).
    name: The attribute name being assigned.
    value: The value being assigned. Not necessarily a trackable object.

  Returns:
    The value which should be stored in the attribute (unwrapped from a
    NoDependency object if necessary).
  """

class _UntrackableError(ValueError):
    def __init__(self, value) -> None: ...

class TrackableDataStructure(base.Trackable):
    """Base class for data structures which contain trackable objects."""
    def __init__(self) -> None: ...
    @property
    def trainable(self): ...
    @trainable.setter
    def trainable(self, value) -> None: ...
    @property
    def layers(self): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def weights(self): ...
    @property
    def trainable_variables(self): ...
    @property
    def non_trainable_variables(self): ...
    @property
    def variables(self): ...
    @property
    def updates(self):
        """Aggregate updates from any `Layer` instances."""
    @property
    def losses(self):
        """Aggregate losses from any `Layer` instances."""
    def __hash__(self): ...
    def __eq__(self, other): ...

class List(TrackableDataStructure, collections_abc.Sequence):
    """An append-only sequence type which is trackable.

  Maintains checkpoint dependencies on its contents (which must also be
  trackable), and forwards any `Layer` metadata such as updates and losses.

  Note that `List` is purely a container. It lets a `tf.keras.Model` or
  other trackable object know about its contents, but does not call any
  `Layer` instances which are added to it. To indicate a sequence of `Layer`
  instances which should be called sequentially, use `tf.keras.Sequential`.

  Example usage:
  ```python
  class HasList(tf.keras.Model):

    def __init__(self):
      super().__init__()
      self.layer_list = List([layers.Dense(3)])
      self.layer_list.append(layers.Dense(4))

    def call(self, x):
      aggregation = 0.
      for l in self.layer_list:
        x = l(x)
        aggregation += tf.reduce_sum(x)
      return aggregation
  ```

  This kind of wrapping is necessary because `Trackable` objects do not
  (yet) deeply inspect regular Python data structures, so for example assigning
  a regular list (`self.layer_list = [layers.Dense(3)]`) does not create a
  checkpoint dependency and does not add the `Layer` instance's weights to its
  parent `Model`.
  """
    def __init__(self, *args, **kwargs) -> None:
        """Construct a new sequence. Arguments are passed to `list()`."""
    def copy(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def append(self, value) -> None:
        """Add a new trackable value."""
    def extend(self, values) -> None:
        """Add a sequence of trackable values."""
    def __iadd__(self, values): ...
    def __add__(self, other): ...
    def __imul__(self, y): ...
    def __mul__(self, n): ...
    def __rmul__(self, n): ...
    def __radd__(self, other): ...
    def __getitem__(self, key): ...
    def __getslice__(self, i, j): ...
    def __len__(self) -> int: ...
    def __sizeof__(self) -> int: ...

class ListWrapper(List, collections_abc.MutableSequence, list):
    """Wraps the built-in `list` to support restore-on-create for variables.

  Unlike `List`, this sequence type is mutable in the same ways built-in lists
  are. Instead of throwing an error immediately like `List`, it records
  problematic mutations (e.g. assigning a new element to a position already
  occupied, meaning both elements get the same names at different times) and
  refuses to save.

  On assignment to an attribute of a Model or Trackable object, Python
  lists are replaced with ListWrapper. Wrapping a list in a
  `NoDependency` object prevents this.
  """
    def __init__(self, wrapped_list) -> None:
        """Construct a new list wrapper.

    Args:
      wrapped_list: The initial value of the data structure. A shallow copy may
        be maintained for error checking. `wrapped_list` itself should not be
        modified directly after constructing the `ListWrapper`, and if changes
        are detected the `ListWrapper` will throw an exception on save.
    """
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __reduce_ex__(self, protocol): ...
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def append(self, value) -> None:
        """Add a new trackable value."""
    def extend(self, values) -> None:
        """Add a sequence of trackable values."""
    def __imul__(self, y): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __hash__(self): ...
    def insert(self, index, obj) -> None: ...
    def sort(self) -> None: ...
    def __setslice__(self, i, j, y) -> None: ...
    def __delslice__(self, i, j) -> None: ...

class Mapping(TrackableDataStructure, collections_abc.Mapping):
    """An append-only trackable mapping data structure with string keys.

  Maintains checkpoint dependencies on its contents (which must also be
  trackable), named based on its keys.

  Note that once a key has been added, it may not be deleted or replaced.
  """
    def __init__(self, *args, **kwargs) -> None:
        """Construct a new sequence. Arguments are passed to `dict()`."""
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __setitem__(self, key, value) -> None: ...
    def update(self, *args, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...

class _DictWrapper(TrackableDataStructure, wrapt.ObjectProxy):
    """Wraps built-in dicts to support restore-on-create for variables.

  _DictWrapper is to Mapping as ListWrapper is to List. Unlike Mapping,
  _DictWrapper allows non-string keys and values and arbitrary mutations (delete
  keys, reassign values). Like ListWrapper, these mutations mean that
  _DictWrapper will raise an exception on save.
  """
    def __init__(self, wrapped_dict: Incomplete | None = None) -> None: ...
    def __reduce_ex__(self, protocol): ...
    def __getattribute__(self, name): ...
    def copy(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __setitem__(self, key, value) -> None:
        """Allow any modifications, but possibly mark the wrapper as unsaveable."""
    def __delitem__(self, key) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def update(self, *args, **kwargs) -> None: ...

class _TupleWrapper(TrackableDataStructure, wrapt.ObjectProxy):
    """Trackable wrapper for tuples and namedtuples."""
    def __init__(self, original_wrapped_tuple=()) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __reduce_ex__(self, protocol): ...
    def __imul__(self, y):
        """Avoid running self.__wrapped__ *= y, which mutates `self`."""
    def __iadd__(self, y):
        """Avoid running self.__wrapped__ += y, which mutates `self`."""
    def __getattribute__(self, name): ...
