from _typeshed import Incomplete
from tensorflow.core.protobuf import saver_pb2 as saver_pb2
from tensorflow.python.checkpoint import checkpoint_options as checkpoint_options
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, gen_io_ops as gen_io_ops, io_ops as io_ops, string_ops as string_ops
from tensorflow.python.saved_model import registration as registration
from tensorflow.python.trackable import trackable_utils as trackable_utils
from tensorflow.python.training.saving import saveable_object as saveable_object, saveable_object_util as saveable_object_util
from tensorflow.python.util import nest as nest, object_identity as object_identity

class _SingleDeviceSaver:
    """Saves and restores checkpoints from the current device."""
    def __init__(self, tensor_slice_dict) -> None:
        """Specify a list of `SaveableObject`s to save and restore.

    Args:
      tensor_slice_dict: A dict mapping checkpoint key -> slice_spec -> tensor.
    """
    def save(self, file_prefix, options: Incomplete | None = None):
        """Save the saveable objects to a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix to
        save under.
      options: Optional `CheckpointOptions` object.
    Returns:
      An `Operation`, or None when executing eagerly.
    """
    def restore(self, file_prefix, options: Incomplete | None = None):
        """Restore the saveable objects from a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix for
        files to read from.
      options: Optional `CheckpointOptions` object.

    Returns:
      A restored tensor dict (maps checkpoint_key -> slice_spec -> tensor).
    """

def sharded_filename(filename_tensor, shard, num_shards):
    """Append sharding information to a filename.

  Args:
    filename_tensor: A string tensor.
    shard: Integer.  The shard for the filename.
    num_shards: An int Tensor for the number of shards.

  Returns:
    A string tensor.
  """
def registered_saver_filename(filename_tensor, saver_name): ...

class MultiDeviceSaver:
    """Saves checkpoints directly from multiple devices.

  Note that this is a low-level utility which stores Tensors in the keys
  specified by `SaveableObject`s. Higher-level utilities for object-based
  checkpointing are built on top of it.
  """
    def __init__(self, serialized_tensors, registered_savers: Incomplete | None = None, call_with_mapped_captures: Incomplete | None = None) -> None:
        """Specify a list of `SaveableObject`s to save and restore.

    Args:
      serialized_tensors: A dictionary mapping `Trackable` to a tensor dict,
        which maps checkpoint_key -> (slice_spec ->) -> Tensor/SaveSpec. The
        `Trackable` key is used to get the `restore_from_tensors` function,
        and may be `None` if the tensor is not meant to be restored.
      registered_savers: A dictionary mapping `registration.RegisteredSaver`
        namedtuples to a dictionary of named Trackables. The keys of the
        Trackable dictionary are string names that uniquely identify the
        Trackable in the checkpoint.
      call_with_mapped_captures: TODO
    """
    @classmethod
    def from_saveables(cls, saveables, registered_savers: Incomplete | None = None, call_with_mapped_captures: Incomplete | None = None): ...
    def to_proto(self):
        """Serializes to a SaverDef referencing the current graph."""
    def save(self, file_prefix, options: Incomplete | None = None):
        """Save the saveable objects to a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix to
        save under.
      options: Optional `CheckpointOptions` object.
    Returns:
      An `Operation`, or None when executing eagerly.
    """
    def restore(self, file_prefix, options: Incomplete | None = None):
        """Restore the saveable objects from a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix for
        files to read from.
      options: Optional `CheckpointOptions` object.

    Returns:
      When not run eagerly or when saving on a single device, returns a
      dictionary mapping from SaveableObject names to restore operations;
      otherwise, returns an empty dict.
    """
