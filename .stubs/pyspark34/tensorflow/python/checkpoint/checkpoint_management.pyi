from _typeshed import Incomplete
from tensorflow.core.protobuf import saver_pb2 as saver_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variable_scope as variable_scope
from tensorflow.python.training import training_util as training_util
from tensorflow.python.training.checkpoint_state_pb2 import CheckpointState as CheckpointState
from tensorflow.python.util import compat as compat, deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def generate_checkpoint_state_proto(save_dir, model_checkpoint_path, all_model_checkpoint_paths: Incomplete | None = None, all_model_checkpoint_timestamps: Incomplete | None = None, last_preserved_timestamp: Incomplete | None = None):
    """Generates a checkpoint state proto.

  Args:
    save_dir: Directory where the model was saved.
    model_checkpoint_path: The checkpoint file.
    all_model_checkpoint_paths: List of strings.  Paths to all not-yet-deleted
      checkpoints, sorted from oldest to newest.  If this is a non-empty list,
      the last element must be equal to model_checkpoint_path.  These paths
      are also saved in the CheckpointState proto.
    all_model_checkpoint_timestamps: A list of floats, indicating the number of
      seconds since the Epoch when each checkpoint was generated.
    last_preserved_timestamp: A float, indicating the number of seconds since
      the Epoch when the last preserved checkpoint was written, e.g. due to a
      `keep_checkpoint_every_n_hours` parameter (see
      `tf.train.CheckpointManager` for an implementation).
  Returns:
    CheckpointState proto with model_checkpoint_path and
    all_model_checkpoint_paths updated to either absolute paths or
    relative paths to the current save_dir.

  Raises:
    ValueError: If `all_model_checkpoint_timestamps` was provided but its length
      does not match `all_model_checkpoint_paths`.
  """
def update_checkpoint_state(save_dir, model_checkpoint_path, all_model_checkpoint_paths: Incomplete | None = None, latest_filename: Incomplete | None = None, all_model_checkpoint_timestamps: Incomplete | None = None, last_preserved_timestamp: Incomplete | None = None) -> None:
    """Updates the content of the 'checkpoint' file.

  This updates the checkpoint file containing a CheckpointState
  proto.

  Args:
    save_dir: Directory where the model was saved.
    model_checkpoint_path: The checkpoint file.
    all_model_checkpoint_paths: List of strings.  Paths to all not-yet-deleted
      checkpoints, sorted from oldest to newest.  If this is a non-empty list,
      the last element must be equal to model_checkpoint_path.  These paths
      are also saved in the CheckpointState proto.
    latest_filename: Optional name of the checkpoint file.  Default to
      'checkpoint'.
    all_model_checkpoint_timestamps: Optional list of timestamps (floats,
      seconds since the Epoch) indicating when the checkpoints in
      `all_model_checkpoint_paths` were created.
    last_preserved_timestamp: A float, indicating the number of seconds since
      the Epoch when the last preserved checkpoint was written, e.g. due to a
      `keep_checkpoint_every_n_hours` parameter (see
      `tf.train.CheckpointManager` for an implementation).
  Raises:
    RuntimeError: If any of the model checkpoint paths conflict with the file
      containing CheckpointSate.
  """
def update_checkpoint_state_internal(save_dir, model_checkpoint_path, all_model_checkpoint_paths: Incomplete | None = None, latest_filename: Incomplete | None = None, save_relative_paths: bool = False, all_model_checkpoint_timestamps: Incomplete | None = None, last_preserved_timestamp: Incomplete | None = None) -> None:
    """Updates the content of the 'checkpoint' file.

  This updates the checkpoint file containing a CheckpointState
  proto.

  Args:
    save_dir: Directory where the model was saved.
    model_checkpoint_path: The checkpoint file.
    all_model_checkpoint_paths: List of strings.  Paths to all not-yet-deleted
      checkpoints, sorted from oldest to newest.  If this is a non-empty list,
      the last element must be equal to model_checkpoint_path.  These paths
      are also saved in the CheckpointState proto.
    latest_filename: Optional name of the checkpoint file.  Default to
      'checkpoint'.
    save_relative_paths: If `True`, will write relative paths to the checkpoint
      state file.
    all_model_checkpoint_timestamps: Optional list of timestamps (floats,
      seconds since the Epoch) indicating when the checkpoints in
      `all_model_checkpoint_paths` were created.
    last_preserved_timestamp: A float, indicating the number of seconds since
      the Epoch when the last preserved checkpoint was written, e.g. due to a
      `keep_checkpoint_every_n_hours` parameter (see
      `tf.train.CheckpointManager` for an implementation).

  Raises:
    RuntimeError: If any of the model checkpoint paths conflict with the file
      containing CheckpointSate.
  """
def get_checkpoint_state(checkpoint_dir, latest_filename: Incomplete | None = None):
    '''Returns CheckpointState proto from the "checkpoint" file.

  If the "checkpoint" file contains a valid CheckpointState
  proto, returns it.

  Args:
    checkpoint_dir: The directory of checkpoints.
    latest_filename: Optional name of the checkpoint file.  Default to
      \'checkpoint\'.

  Returns:
    A CheckpointState if the state was available, None
    otherwise.

  Raises:
    ValueError: if the checkpoint read doesn\'t have model_checkpoint_path set.
  '''
def latest_checkpoint(checkpoint_dir, latest_filename: Incomplete | None = None):
    """Finds the filename of latest saved checkpoint file.

  Gets the checkpoint state given the provided checkpoint_dir and looks for a
  corresponding TensorFlow 2 (preferred) or TensorFlow 1.x checkpoint path.
  The latest_filename argument is only applicable if you are saving checkpoint
  using `v1.train.Saver.save`


  See the [Training Checkpoints
  Guide](https://www.tensorflow.org/guide/checkpoint) for more details and
  examples.`

  Args:
    checkpoint_dir: Directory where the variables were saved.
    latest_filename: Optional name for the protocol buffer file that
      contains the list of most recent checkpoint filenames.
      See the corresponding argument to `v1.train.Saver.save`.

  Returns:
    The full path to the latest checkpoint or `None` if no checkpoint was found.
  """
def checkpoint_exists_internal(checkpoint_prefix):
    """Checks whether a V1 or V2 checkpoint exists with the specified prefix.

  This is an internal function to check if a checkpoint exists,
  since it takes into account the naming difference between V1 and V2 formats.

  Args:
    checkpoint_prefix: the prefix of a V1 or V2 checkpoint, with V2 taking
      priority.  Typically the result of `Saver.save()` or that of
      `tf.train.latest_checkpoint()`, regardless of sharded/non-sharded or
      V1/V2.
  Returns:
    A bool, true if a checkpoint referred to by `checkpoint_prefix` exists.
  """
def checkpoint_exists(checkpoint_prefix):
    """Checks whether a V1 or V2 checkpoint exists with the specified prefix.

  This is the recommended way to check if a checkpoint exists, since it takes
  into account the naming difference between V1 and V2 formats.

  Args:
    checkpoint_prefix: the prefix of a V1 or V2 checkpoint, with V2 taking
      priority.  Typically the result of `Saver.save()` or that of
      `tf.train.latest_checkpoint()`, regardless of sharded/non-sharded or
      V1/V2.

  Returns:
    A bool, true if a checkpoint referred to by `checkpoint_prefix` exists.
  """
def get_checkpoint_mtimes(checkpoint_prefixes):
    """Returns the mtimes (modification timestamps) of the checkpoints.

  Globs for the checkpoints pointed to by `checkpoint_prefixes`.  If the files
  exist, collect their mtime.  Both V2 and V1 checkpoints are considered, in
  that priority.

  This is the recommended way to get the mtimes, since it takes into account
  the naming difference between V1 and V2 formats.

  Note: If not all checkpoints exist, the length of the returned mtimes list
  will be smaller than the length of `checkpoint_prefixes` list, so mapping
  checkpoints to corresponding mtimes will not be possible.

  Args:
    checkpoint_prefixes: a list of checkpoint paths, typically the results of
      `Saver.save()` or those of `tf.train.latest_checkpoint()`, regardless of
      sharded/non-sharded or V1/V2.
  Returns:
    A list of mtimes (in microseconds) of the found checkpoints.
  """
def remove_checkpoint(checkpoint_prefix, checkpoint_format_version=..., meta_graph_suffix: str = 'meta') -> None:
    """Removes a checkpoint given by `checkpoint_prefix`.

  Args:
    checkpoint_prefix: The prefix of a V1 or V2 checkpoint. Typically the result
      of `Saver.save()` or that of `tf.train.latest_checkpoint()`, regardless of
      sharded/non-sharded or V1/V2.
    checkpoint_format_version: `SaverDef.CheckpointFormatVersion`, defaults to
      `SaverDef.V2`.
    meta_graph_suffix: Suffix for `MetaGraphDef` file. Defaults to 'meta'.
  """
def meta_graph_filename(checkpoint_filename, meta_graph_suffix: str = 'meta'):
    """Returns the meta graph filename.

  Args:
    checkpoint_filename: Name of the checkpoint file.
    meta_graph_suffix: Suffix for `MetaGraphDef` file. Defaults to 'meta'.

  Returns:
    MetaGraph file name.
  """

class CheckpointManager:
    '''Manages multiple checkpoints by keeping some and deleting unneeded ones.

  Example usage:

  ```python
  import tensorflow as tf
  checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
  manager = tf.train.CheckpointManager(
      checkpoint, directory="/tmp/model", max_to_keep=5)
  status = checkpoint.restore(manager.latest_checkpoint)
  while True:
    # train
    manager.save()
  ```

  `CheckpointManager` preserves its own state across instantiations (see the
  `__init__` documentation for details). Only one should be active in a
  particular directory at a time.
  '''
    def __init__(self, checkpoint, directory, max_to_keep, keep_checkpoint_every_n_hours: Incomplete | None = None, checkpoint_name: str = 'ckpt', step_counter: Incomplete | None = None, checkpoint_interval: Incomplete | None = None, init_fn: Incomplete | None = None) -> None:
        '''Configure a `CheckpointManager` for use in `directory`.

    If a `CheckpointManager` was previously used in `directory`, its
    state will be restored. This includes the list of managed checkpoints and
    the timestamp bookkeeping necessary to support
    `keep_checkpoint_every_n_hours`. The behavior of the new `CheckpointManager`
    will be the same as the previous `CheckpointManager`, including cleaning up
    existing checkpoints if appropriate.

    Checkpoints are only considered for deletion just after a new checkpoint has
    been added. At that point, `max_to_keep` checkpoints will remain in an
    "active set". Once a checkpoint is preserved by
    `keep_checkpoint_every_n_hours` it will not be deleted by this
    `CheckpointManager` or any future `CheckpointManager` instantiated in
    `directory` (regardless of the new setting of
    `keep_checkpoint_every_n_hours`). The `max_to_keep` checkpoints in the
    active set may be deleted by this `CheckpointManager` or a future
    `CheckpointManager` instantiated in `directory` (subject to its
    `max_to_keep` and `keep_checkpoint_every_n_hours` settings).

    `CheckpointManager` can be also used for initializing the model if
    there is no checkpoints for restoring in `directory`. An example usage is:

    >>> import tempfile

    >>> tmp_dir = tempfile.mkdtemp()
    >>> checkpoint = tf.train.Checkpoint()
    >>> init_path = checkpoint.save(os.path.join(tmp_dir, \'init\'))

    >>> def init_fn():
    ...   # Partially restore the checkpoint from `init_path`.
    ...   checkpoint.restore(init_path)

    >>> manager = tf.train.CheckpointManager(
    ...     checkpoint,
    ...     directory=os.path.join(tmp_dir, \'ckpt\'),
    ...     max_to_keep=None,
    ...     init_fn=init_fn)
    >>> # `restore_or_initialize` will call `init_fn` if there is no existing
    >>> # checkpoint in `directory`.
    >>> manager.restore_or_initialize()

    Args:
      checkpoint: The `tf.train.Checkpoint` instance to save and manage
        checkpoints for.
      directory: The path to a directory in which to write checkpoints. A
        special file named "checkpoint" is also written to this directory (in a
        human-readable text format) which contains the state of the
        `CheckpointManager`.
      max_to_keep: An integer, the number of checkpoints to keep. Unless
        preserved by `keep_checkpoint_every_n_hours`, checkpoints will be
        deleted from the active set, oldest first, until only `max_to_keep`
        checkpoints remain. If `None`, no checkpoints are deleted and everything
        stays in the active set. Note that `max_to_keep=None` will keep all
        checkpoint paths in memory and in the checkpoint state protocol buffer
        on disk.
      keep_checkpoint_every_n_hours: Upon removal from the active set, a
        checkpoint will be preserved if it has been at least
        `keep_checkpoint_every_n_hours` since the last preserved checkpoint. The
        default setting of `None` does not preserve any checkpoints in this way.
      checkpoint_name: Custom name for the checkpoint file.
      step_counter: A `tf.Variable` instance for checking the current step
        counter value, in case users want to save checkpoints every N steps.
      checkpoint_interval: An integer, indicates the minimum step interval
        between two checkpoints.
      init_fn: Callable. A function to do customized intialization if no
        checkpoints are in the directory.

    Raises:
      ValueError: If `max_to_keep` is not a positive integer.
    '''
    @property
    def directory(self): ...
    @property
    def checkpoint_interval(self): ...
    @property
    def latest_checkpoint(self):
        """The prefix of the most recent checkpoint in `directory`.

    Equivalent to `tf.train.latest_checkpoint(directory)` where `directory` is
    the constructor argument to `CheckpointManager`.

    Suitable for passing to `tf.train.Checkpoint.restore` to resume training.

    Returns:
      The checkpoint prefix. If there are no checkpoints, returns `None`.
    """
    @property
    def checkpoints(self):
        """A list of managed checkpoints.

    Note that checkpoints saved due to `keep_checkpoint_every_n_hours` will not
    show up in this list (to avoid ever-growing filename lists).

    Returns:
      A list of filenames, sorted from oldest to newest.
    """
    @property
    def checkpoint(self):
        """Returns the `tf.train.Checkpoint` object."""
    def save(self, checkpoint_number: Incomplete | None = None, check_interval: bool = True, options: Incomplete | None = None):
        """Creates a new checkpoint and manages it.

    Args:
      checkpoint_number: An optional integer, or an integer-dtype `Variable` or
        `Tensor`, used to number the checkpoint. If `None` (default),
        checkpoints are numbered using `checkpoint.save_counter`. Even if
        `checkpoint_number` is provided, `save_counter` is still incremented. A
        user-provided `checkpoint_number` is not incremented even if it is a
        `Variable`.
      check_interval: An optional boolean. The argument is only effective when
        `checkpoint_interval` is passed into the manager. If `True`, the manager
        will only save the checkpoint if the interval between checkpoints is
        larger than `checkpoint_interval`. Otherwise it will always save the
        checkpoint unless a checkpoint has already been saved for the current
        step.
      options: Optional `tf.train.CheckpointOptions` object. This argument only
        works with TF2 checkpoint objects. For example, options =
        tf.saved_model.SaveOptions(experimental_io_device='/job:localhost')

    Returns:
      The path to the new checkpoint. It is also recorded in the `checkpoints`
      and `latest_checkpoint` properties. `None` if no checkpoint is saved.
    """
    def restore_or_initialize(self):
        """Restore items in `checkpoint` from the latest checkpoint file.

    This method will first try to restore from the most recent checkpoint in
    `directory`. If no checkpoints exist in `directory`, and `init_fn` is
    specified, this method will call `init_fn` to do customized
    initialization. This can be used to support initialization from pretrained
    models.

    Note that unlike `tf.train.Checkpoint.restore()`, this method doesn't return
    a load status object that users can run assertions on
    (e.g. assert_consumed()). Thus to run assertions, users should directly use
    `tf.train.Checkpoint.restore()` method.

    Returns:
      The restored checkpoint path if the lastest checkpoint is found and
      restored. Otherwise None.
    """
