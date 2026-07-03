from _typeshed import Incomplete
from tensorflow.core.framework import versions_pb2 as versions_pb2
from tensorflow.core.protobuf import saved_object_graph_pb2 as saved_object_graph_pb2
from tensorflow.python.util.tf_export import tf_export as tf_export

class VersionedTypeRegistration:
    """Holds information about one version of a revived type."""
    setter: Incomplete
    identifier: Incomplete
    version: Incomplete
    def __init__(self, object_factory, version, min_producer_version, min_consumer_version, bad_consumers: Incomplete | None = None, setter=...) -> None:
        """Identify a revived type version.

    Args:
      object_factory: A callable which takes a SavedUserObject proto and returns
        a trackable object. Dependencies are added later via `setter`.
      version: An integer, the producer version of this wrapper type. When
        making incompatible changes to a wrapper, add a new
        `VersionedTypeRegistration` with an incremented `version`. The most
        recent version will be saved, and all registrations with a matching
        identifier will be searched for the highest compatible version to use
        when loading.
      min_producer_version: The minimum producer version number required to use
        this `VersionedTypeRegistration` when loading a proto.
      min_consumer_version: `VersionedTypeRegistration`s with a version number
        less than `min_consumer_version` will not be used to load a proto saved
        with this object. `min_consumer_version` should be set to the lowest
        version number which can successfully load protos saved by this
        object. If no matching registration is available on load, the object
        will be revived with a generic trackable type.

        `min_consumer_version` and `bad_consumers` are a blunt tool, and using
        them will generally break forward compatibility: previous versions of
        TensorFlow will revive newly saved objects as opaque trackable
        objects rather than wrapped objects. When updating wrappers, prefer
        saving new information but preserving compatibility with previous
        wrapper versions. They are, however, useful for ensuring that
        previously-released buggy wrapper versions degrade gracefully rather
        than throwing exceptions when presented with newly-saved SavedModels.
      bad_consumers: A list of consumer versions which are incompatible (in
        addition to any version less than `min_consumer_version`).
      setter: A callable with the same signature as `setattr` to use when adding
        dependencies to generated objects.
    """
    def to_proto(self):
        """Create a SavedUserObject proto."""
    def from_proto(self, proto):
        """Recreate a trackable object from a SavedUserObject proto."""
    def should_load(self, proto):
        """Checks if this object should load the SavedUserObject `proto`."""

def register_revived_type(identifier, predicate, versions):
    """Register a type for revived objects.

  Args:
    identifier: A unique string identifying this class of objects.
    predicate: A Boolean predicate for this registration. Takes a
      trackable object as an argument. If True, `type_registration` may be
      used to save and restore the object.
    versions: A list of `VersionedTypeRegistration` objects.
  """
def serialize(obj):
    """Create a SavedUserObject from a trackable object."""
def deserialize(proto):
    """Create a trackable object from a SavedUserObject proto.

  Args:
    proto: A SavedUserObject to deserialize.

  Returns:
    A tuple of (trackable, assignment_fn) where assignment_fn has the same
    signature as setattr and should be used to add dependencies to
    `trackable` when they are available.
  """
def registered_identifiers():
    """Return all the current registered revived object identifiers.

  Returns:
    A set of strings.
  """
def get_setter(proto):
    """Gets the registered setter function for the SavedUserObject proto.

  See VersionedTypeRegistration for info about the setter function.

  Args:
    proto: SavedUserObject proto

  Returns:
    setter function
  """
