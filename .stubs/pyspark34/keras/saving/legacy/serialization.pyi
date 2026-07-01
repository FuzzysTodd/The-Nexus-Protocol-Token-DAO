from _typeshed import Incomplete
from collections.abc import Generator
from keras.utils import tf_contextlib as tf_contextlib, tf_inspect as tf_inspect

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

    Created to simplify serialization code that doesn't care about shared
    objects (e.g. when serializing a single object).
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
          object_id: shared object ID to use when attempting to find
            already-loaded object.

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
def skip_failed_serialization() -> Generator[None, None, None]: ...
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
def class_and_config_for_serialized_keras_object(config, module_objects: Incomplete | None = None, custom_objects: Incomplete | None = None, printable_module_name: str = 'object'):
    """Returns the class name and config for a serialized keras object."""
def deserialize_keras_object(identifier, module_objects: Incomplete | None = None, custom_objects: Incomplete | None = None, printable_module_name: str = 'object'):
    '''Turns the serialized form of a Keras object back into an actual object.

    This function is for mid-level library implementers rather than end users.

    Importantly, this utility requires you to provide the dict of
    `module_objects` to use for looking up the object config; this is not
    populated by default. If you need a deserialization utility that has
    preexisting knowledge of built-in Keras objects, use e.g.
    `keras.layers.deserialize(config)`, `keras.metrics.deserialize(config)`,
    etc.

    Calling `deserialize_keras_object` while underneath the
    `SharedObjectLoadingScope` context manager will cause any already-seen
    shared objects to be returned as-is rather than creating a new object.

    Args:
      identifier: the serialized form of the object.
      module_objects: A dictionary of built-in objects to look the name up in.
        Generally, `module_objects` is provided by midlevel library
        implementers.
      custom_objects: A dictionary of custom objects to look the name up in.
        Generally, `custom_objects` is provided by the end user.
      printable_module_name: A human-readable string representing the type of
        the object. Printed in case of exception.

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
def validate_config(config):
    """Determines whether config appears to be a valid layer config."""
def is_default(method):
    """Check if a method is decorated with the `default` wrapper."""
