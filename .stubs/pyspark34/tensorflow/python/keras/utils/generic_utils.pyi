import types as python_types
from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.keras.utils import tf_contextlib as tf_contextlib, tf_inspect as tf_inspect
from tensorflow.python.util import nest as nest, tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import keras_export as keras_export

class CustomObjectScope:
    """Exposes custom classes/functions to Keras deserialization internals.

  Under a scope `with custom_object_scope(objects_dict)`, Keras methods such
  as `tf.keras.models.load_model` or `tf.keras.models.model_from_config`
  will be able to deserialize any custom object referenced by a
  saved config (e.g. a custom layer or metric).

  Example:

  Consider a custom regularizer `my_regularizer`:

  ```python
  layer = Dense(3, kernel_regularizer=my_regularizer)
  config = layer.get_config()  # Config contains a reference to `my_regularizer`
  ...
  # Later:
  with custom_object_scope({'my_regularizer': my_regularizer}):
    layer = Dense.from_config(config)
  ```

  Args:
      *args: Dictionary or dictionaries of `{name: object}` pairs.
  """
    custom_objects: Incomplete
    backup: Incomplete
    def __init__(self, *args) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args, **kwargs) -> None: ...

def get_custom_objects():
    """Retrieves a live reference to the global dictionary of custom objects.

  Updating and clearing custom objects using `custom_object_scope`
  is preferred, but `get_custom_objects` can
  be used to directly access the current collection of custom objects.

  Example:

  ```python
  get_custom_objects().clear()
  get_custom_objects()['MyObject'] = MyObject
  ```

  Returns:
      Global dictionary of names to classes (`_GLOBAL_CUSTOM_OBJECTS`).
  """

SHARED_OBJECT_KEY: str
SHARED_OBJECT_DISABLED: Incomplete
SHARED_OBJECT_LOADING: Incomplete
SHARED_OBJECT_SAVING: Incomplete

class DisableSharedObjectScope:
    """A context manager for disabling handling of shared objects.

  Disables shared object handling for both saving and loading.

  Created primarily for use with `clone_model`, which does extra surgery that
  is incompatible with shared objects.
  """
    def __enter__(self) -> None: ...
    def __exit__(self, *args, **kwargs) -> None: ...

class NoopLoadingScope:
    """The default shared object loading scope. It does nothing.

  Created to simplify serialization code that doesn't care about shared objects
  (e.g. when serializing a single object).
  """
    def get(self, unused_object_id) -> None: ...
    def set(self, object_id, obj) -> None: ...

class SharedObjectLoadingScope:
    """A context manager for keeping track of loaded objects.

  During the deserialization process, we may come across objects that are
  shared across multiple layers. In order to accurately restore the network
  structure to its original state, `SharedObjectLoadingScope` allows us to
  re-use shared objects rather than cloning them.
  """
    def __enter__(self): ...
    def get(self, object_id):
        """Given a shared object ID, returns a previously instantiated object.

    Args:
      object_id: shared object ID to use when attempting to find already-loaded
        object.

    Returns:
      The object, if we've seen this ID before. Else, `None`.
    """
    def set(self, object_id, obj) -> None:
        """Stores an instantiated object for future lookup and sharing."""
    def __exit__(self, *args, **kwargs) -> None: ...

class SharedObjectConfig(dict):
    """A configuration container that keeps track of references.

  `SharedObjectConfig` will automatically attach a shared object ID to any
  configs which are referenced more than once, allowing for proper shared
  object reconstruction at load time.

  In most cases, it would be more proper to subclass something like
  `collections.UserDict` or `collections.Mapping` rather than `dict` directly.
  Unfortunately, python's json encoder does not support `Mapping`s. This is
  important functionality to retain, since we are dealing with serialization.

  We should be safe to subclass `dict` here, since we aren't actually
  overriding any core methods, only augmenting with a new one for reference
  counting.
  """
    ref_count: int
    object_id: Incomplete
    def __init__(self, base_config, object_id, **kwargs) -> None: ...
    def increment_ref_count(self) -> None: ...

class SharedObjectSavingScope:
    """Keeps track of shared object configs when serializing."""
    def __enter__(self): ...
    def get_config(self, obj):
        """Gets a `SharedObjectConfig` if one has already been seen for `obj`.

    Args:
      obj: The object for which to retrieve the `SharedObjectConfig`.

    Returns:
      The SharedObjectConfig for a given object, if already seen. Else,
        `None`.
    """
    def create_config(self, base_config, obj):
        """Create a new SharedObjectConfig for a given object."""
    def __exit__(self, *args, **kwargs) -> None: ...

def serialize_keras_class_and_config(cls_name, cls_config, obj: Incomplete | None = None, shared_object_id: Incomplete | None = None):
    """Returns the serialization of the class with the given config."""
def register_keras_serializable(package: str = 'Custom', name: Incomplete | None = None):
    """Registers an object with the Keras serialization framework.

  This decorator injects the decorated class or function into the Keras custom
  object dictionary, so that it can be serialized and deserialized without
  needing an entry in the user-provided custom object dict. It also injects a
  function that Keras will call to get the object's serializable string key.

  Note that to be serialized and deserialized, classes must implement the
  `get_config()` method. Functions do not have this requirement.

  The object will be registered under the key 'package>name' where `name`,
  defaults to the object name if not passed.

  Args:
    package: The package that this class belongs to.
    name: The name to serialize this class under in this package. If None, the
      class' name will be used.

  Returns:
    A decorator that registers the decorated class with the passed names.
  """
def get_registered_name(obj):
    """Returns the name registered to an object within the Keras framework.

  This function is part of the Keras serialization and deserialization
  framework. It maps objects to the string names associated with those objects
  for serialization/deserialization.

  Args:
    obj: The object to look up.

  Returns:
    The name associated with the object, or the default Python name if the
      object is not registered.
  """
def skip_failed_serialization() -> Generator[None, None, None]: ...
def get_registered_object(name, custom_objects: Incomplete | None = None, module_objects: Incomplete | None = None):
    """Returns the class associated with `name` if it is registered with Keras.

  This function is part of the Keras serialization and deserialization
  framework. It maps strings to the objects associated with them for
  serialization/deserialization.

  Example:
  ```
  def from_config(cls, config, custom_objects=None):
    if 'my_custom_object_name' in config:
      config['hidden_cls'] = tf.keras.utils.get_registered_object(
          config['my_custom_object_name'], custom_objects=custom_objects)
  ```

  Args:
    name: The name to look up.
    custom_objects: A dictionary of custom objects to look the name up in.
      Generally, custom_objects is provided by the user.
    module_objects: A dictionary of custom objects to look the name up in.
      Generally, module_objects is provided by midlevel library implementers.

  Returns:
    An instantiable class associated with 'name', or None if no such class
      exists.
  """

class CustomMaskWarning(Warning): ...

def serialize_keras_object(instance):
    """Serialize a Keras object into a JSON-compatible representation.

  Calls to `serialize_keras_object` while underneath the
  `SharedObjectSavingScope` context manager will cause any objects re-used
  across multiple layers to be saved with a special shared object ID. This
  allows the network to be re-created properly during deserialization.

  Args:
    instance: The object to serialize.

  Returns:
    A dict-like, JSON-compatible representation of the object's config.
  """
def get_custom_objects_by_name(item, custom_objects: Incomplete | None = None):
    """Returns the item if it is in either local or global custom objects."""
def class_and_config_for_serialized_keras_object(config, module_objects: Incomplete | None = None, custom_objects: Incomplete | None = None, printable_module_name: str = 'object'):
    """Returns the class name and config for a serialized keras object."""
def deserialize_keras_object(identifier, module_objects: Incomplete | None = None, custom_objects: Incomplete | None = None, printable_module_name: str = 'object'):
    '''Turns the serialized form of a Keras object back into an actual object.

  This function is for mid-level library implementers rather than end users.

  Importantly, this utility requires you to provide the dict of `module_objects`
  to use for looking up the object config; this is not populated by default.
  If you need a deserialization utility that has preexisting knowledge of
  built-in Keras objects, use e.g. `keras.layers.deserialize(config)`,
  `keras.metrics.deserialize(config)`, etc.

  Calling `deserialize_keras_object` while underneath the
  `SharedObjectLoadingScope` context manager will cause any already-seen shared
  objects to be returned as-is rather than creating a new object.

  Args:
    identifier: the serialized form of the object.
    module_objects: A dictionary of built-in objects to look the name up in.
      Generally, `module_objects` is provided by midlevel library implementers.
    custom_objects: A dictionary of custom objects to look the name up in.
      Generally, `custom_objects` is provided by the end user.
    printable_module_name: A human-readable string representing the type of the
      object. Printed in case of exception.

  Returns:
    The deserialized object.

  Example:

  A mid-level library implementer might want to implement a utility for
  retrieving an object from its config, as such:

  ```python
  def deserialize(config, custom_objects=None):
     return deserialize_keras_object(
       identifier,
       module_objects=globals(),
       custom_objects=custom_objects,
       name="MyObjectType",
     )
  ```

  This is how e.g. `keras.layers.deserialize()` is implemented.
  '''
def func_dump(func):
    """Serializes a user defined function.

  Args:
      func: the function to serialize.

  Returns:
      A tuple `(code, defaults, closure)`.
  """
def func_load(code, defaults: Incomplete | None = None, closure: Incomplete | None = None, globs: Incomplete | None = None):
    """Deserializes a user defined function.

  Args:
      code: bytecode of the function.
      defaults: defaults of the function.
      closure: closure of the function.
      globs: dictionary of global objects.

  Returns:
      A function object.
  """
def has_arg(fn, name, accept_all: bool = False):
    """Checks if a callable accepts a given keyword argument.

  Args:
      fn: Callable to inspect.
      name: Check if `fn` can be called with `name` as a keyword argument.
      accept_all: What to return if there is no parameter called `name` but the
        function accepts a `**kwargs` argument.

  Returns:
      bool, whether `fn` accepts a `name` keyword argument.
  """

class Progbar:
    '''Displays a progress bar.

  Args:
      target: Total number of steps expected, None if unknown.
      width: Progress bar width on screen.
      verbose: Verbosity mode, 0 (silent), 1 (verbose), 2 (semi-verbose)
      stateful_metrics: Iterable of string names of metrics that should *not* be
        averaged over time. Metrics in this list will be displayed as-is. All
        others will be averaged by the progbar before display.
      interval: Minimum visual progress update interval (in seconds).
      unit_name: Display name for step counts (usually "step" or "sample").
  '''
    target: Incomplete
    width: Incomplete
    verbose: Incomplete
    interval: Incomplete
    unit_name: Incomplete
    stateful_metrics: Incomplete
    def __init__(self, target, width: int = 30, verbose: int = 1, interval: float = 0.05, stateful_metrics: Incomplete | None = None, unit_name: str = 'step') -> None: ...
    def update(self, current, values: Incomplete | None = None, finalize: Incomplete | None = None) -> None:
        """Updates the progress bar.

    Args:
        current: Index of current step.
        values: List of tuples: `(name, value_for_last_step)`. If `name` is in
          `stateful_metrics`, `value_for_last_step` will be displayed as-is.
          Else, an average of the metric over time will be displayed.
        finalize: Whether this is the last update for the progress bar. If
          `None`, defaults to `current >= self.target`.
    """
    def add(self, n, values: Incomplete | None = None) -> None: ...

def make_batches(size, batch_size):
    """Returns a list of batch indices (tuples of indices).

  Args:
      size: Integer, total size of the data to slice into batches.
      batch_size: Integer, batch size.

  Returns:
      A list of tuples of array indices.
  """
def slice_arrays(arrays, start: Incomplete | None = None, stop: Incomplete | None = None):
    """Slice an array or list of arrays.

  This takes an array-like, or a list of
  array-likes, and outputs:
      - arrays[start:stop] if `arrays` is an array-like
      - [x[start:stop] for x in arrays] if `arrays` is a list

  Can also work on list/array of indices: `slice_arrays(x, indices)`

  Args:
      arrays: Single array or list of arrays.
      start: can be an integer index (start index) or a list/array of indices
      stop: integer (stop index); should be None if `start` was a list.

  Returns:
      A slice of the array(s).

  Raises:
      ValueError: If the value of start is a list and stop is not None.
  """
def to_list(x):
    """Normalizes a list/tensor into a list.

  If a tensor is passed, we return
  a list of size 1 containing the tensor.

  Args:
      x: target object to be normalized.

  Returns:
      A list.
  """
def to_snake_case(name): ...
def is_all_none(structure): ...
def check_for_unexpected_keys(name, input_dict, expected_values) -> None: ...
def validate_kwargs(kwargs, allowed_kwargs, error_message: str = 'Keyword argument not understood:') -> None:
    """Checks that all keyword arguments are in the set of allowed keys."""
def validate_config(config):
    """Determines whether config appears to be a valid layer config."""
def default(method):
    """Decorates a method to detect overrides in subclasses."""
def is_default(method):
    """Check if a method is decorated with the `default` wrapper."""
def populate_dict_with_module_objects(target_dict, modules, obj_filter) -> None: ...

class LazyLoader(python_types.ModuleType):
    """Lazily import a module, mainly to avoid pulling in large dependencies."""
    def __init__(self, local_name, parent_module_globals, name) -> None: ...
    def __getattr__(self, item): ...
custom_object_scope = CustomObjectScope
