from _typeshed import Incomplete
from tensorflow.python.distribute import device_util as device_util
from tensorflow.python.distribute.sharded_variable import ShardedVariable as ShardedVariable
from tensorflow.python.eager import context as context, def_function as def_function, executor as executor
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops.resource_variable_ops import UninitializedVariable as UninitializedVariable
from tensorflow.python.ops.variables import Variable as Variable
from tensorflow.python.saved_model.pywrap_saved_model import metrics as metrics
from tensorflow.python.tpu.tpu_embedding_v2 import TPUEmbedding as TPUEmbedding
from tensorflow.python.util import object_identity as object_identity

class AsyncCheckpointHelper:
    """Helper class for async checkpoint."""
    def __init__(self, checkpointer_impl, root: Incomplete | None = None, **kwargs) -> None:
        """Initialize AsyncCheckpoint.

    Args:
      checkpointer_impl: The Checkpoint class to power the AsyncCheckpoint.
      root: The root object to checkpoint. `root` may be a trackable object or
        `WeakRef` of a trackable object.
      **kwargs: The keyword arguments representing the checkpointed variables.
    """
    @property
    def save_counter(self):
        """An integer variable numbering the checkpoint events.

    This is maintained by the underlying tf.train.Checkpoing object employed by
    AsyncCheckpoint class. The number starts at 0 and gets incremented for each
    checkpoint event.

    Returns:
      The save counter variable.
    """
    def write(self, save_path, options: Incomplete | None = None) -> None:
        """Save the checkpointed variables.

    Args:
      save_path: The file prefix of the checkpoint file.
      options: Optional CheckpointOption instance.

    Returns:
      The full path of the checkpoint file.
    """
    def save(self, save_path, options: Incomplete | None = None):
        """Save the checkpointed variables.

    Args:
      save_path: The file prefix of the checkpoint file.
      options: Optional CheckpointOption instance.

    Returns:
      The full path of the checkpoint file.
    """
    def read(self, save_path, options: Incomplete | None = None):
        """Restore the checkpointed variables.

    This method has exactly the same logic as restore(). This method is
    implemented only to fulfill the duty of subclassing tf.train.Checkpoint.

    Args:
      save_path: The full name of the checkpoint file to be restored.
      options: CheckpointOption instance.

    Returns:
      A load status object, which can be used to make assertions about the
      status of a checkpoint restoration. See tf.train.Checkpoint.restore()
      for more details.
    """
    def restore(self, save_path, options: Incomplete | None = None):
        """Restore the checkpointed variables.

    Args:
      save_path: The full name of the checkpoint file to be restored.
      options: CheckpointOption instance.

    Returns:
      A load status object, which can be used to make assertions about the
      status of a checkpoint restoration. See tf.train.Checkpoint.restore()
      for more details.
    """
    def sync(self) -> None:
        """Sync on any ongoing save or restore events."""
