import abc
from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.protobuf import trackable_object_graph_pb2 as trackable_object_graph_pb2
from tensorflow.python.checkpoint import checkpoint_management as checkpoint_management, checkpoint_options as checkpoint_options, functional_saver as functional_saver, save_util as save_util, save_util_v1 as save_util_v1, util as util
from tensorflow.python.client import session as session_lib
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors_impl as errors_impl, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.saved_model import path_helpers as path_helpers
from tensorflow.python.saved_model.pywrap_saved_model import metrics as metrics
from tensorflow.python.trackable import autotrackable as autotrackable, base as base, data_structures as data_structures
from tensorflow.python.training import py_checkpoint_reader as py_checkpoint_reader
from tensorflow.python.training.saving import saveable_object_util as saveable_object_util
from tensorflow.python.util import compat as compat, deprecation as deprecation, object_identity as object_identity, tf_contextlib as tf_contextlib, tf_inspect as tf_inspect
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export

def register_session_provider(session_provider) -> None: ...
def get_session(): ...

class ObjectGraphProtoPrettyPrinter:
    """Lazily traverses an object graph proto to pretty print names.

  If no calls to `node_names` are made this object has no performance
  overhead. On the other hand, it will only traverse the object graph once, so
  repeated naming is cheap after the first.
  """
    def __init__(self, object_graph_proto) -> None: ...
    @property
    def node_names(self):
        '''Lazily creates a mapping from node id to ("path", "to", "root").'''

class _CheckpointRestoreCoordinatorDeleter:
    """Deleter to avoid overriding _CheckpointRestoreCoordinator.__del__()."""
    expect_partial: Incomplete
    object_graph_proto: Incomplete
    matched_proto_ids: Incomplete
    unused_attributes: Incomplete
    def __init__(self, expect_partial, object_graph_proto, matched_proto_ids, unused_attributes) -> None: ...
    def set_expect_partial(self, expect_partial) -> None: ...
    def __del__(self) -> None: ...

class _CheckpointRestoreCoordinator:
    """Holds the status of an object-based checkpoint load."""
    options: Incomplete
    object_graph_proto: Incomplete
    restore_uid: Incomplete
    unused_attributes: Incomplete
    object_by_proto_id: Incomplete
    matched_proto_ids: Incomplete
    all_python_objects: Incomplete
    save_path_tensor: Incomplete
    save_path_string: Incomplete
    dtype_map: Incomplete
    shape_map: Incomplete
    restore_ops: Incomplete
    restore_ops_by_name: Incomplete
    graph_view: Incomplete
    new_restore_ops_callback: Incomplete
    deferred_slot_restorations: Incomplete
    slot_restorations: Incomplete
    expect_partial_attr: bool
    saveables_cache: Incomplete
    def __init__(self, object_graph_proto, save_path, save_path_tensor, reader, restore_op_cache, graph_view, options, saveables_cache) -> None:
        """Specify the checkpoint being loaded.

    Args:
      object_graph_proto: The TrackableObjectGraph protocol buffer associated
        with this checkpoint.
      save_path: A string, the path to the checkpoint, as returned by
        `tf.train.latest_checkpoint`.
      save_path_tensor: A string `Tensor` which contains or will be fed the save
        path.
      reader: A `CheckpointReader` for `save_path`. If None,
        `_CheckpointRestoreCoordinator` will initialize one itself.
      restore_op_cache: A dictionary shared between
        `_CheckpointRestoreCoordinator`s for the same Python objects, used to
        look up restore ops by name to avoid re-creating them across multiple
        `restore()` calls.
      graph_view: A graph_view_lib.ObjectGraphView object for the restored
        objects.
      options: A CheckpointOptions object.
      saveables_cache: An optional cache storing previously created
        SaveableObjects created for each Trackable. Maps Trackables to a
        dictionary of attribute names to Trackable.
    """
    @property
    def expect_partial(self): ...
    @expect_partial.setter
    def expect_partial(self, expect_partial) -> None: ...
    def new_restore_ops(self, new_ops) -> None: ...
    def restore_saveables(self, tensor_saveables, python_positions, registered_savers: Incomplete | None = None, reader: Incomplete | None = None):
        """Run or build restore operations for SaveableObjects.

    Args:
      tensor_saveables: `SaveableObject`s which correspond to Tensors.
      python_positions: List of CheckpointPositions bound to `PythonState`
        objects which must be restored eagerly.
      registered_savers: a dict mapping saver names-> object name -> Trackable.
      reader: A `CheckpointReader`. If None, a new instance will be created.

    Returns:
      When graph building, a list of restore operations, either cached or newly
      created, to restore `tensor_saveables`.
    """

class _NameBasedRestoreCoordinator:
    """Keeps the status of a name-based checkpoint restore."""
    save_path: Incomplete
    dtype_map: Incomplete
    unused_attributes: Incomplete
    restore_uid: Incomplete
    def __init__(self, save_path, dtype_map: Incomplete | None = None) -> None: ...
    def globally_named_object_attributes(self, trackable) -> Generator[Incomplete, None, None]:
        """Create globally named SaveableObjects from attributes.

    If an object's attribute has no global name specified (default construction
    for the SaveableObject factory), records the failure in
    `self.unused_attributes` (which can then be used to make status assertions
    fail; see `NameBasedSaverStatus`).

    Args:
      trackable: An object to save.

    Yields:
      SaveableObjects for `trackable`'s attributes.
    """
    def eager_restore(self, trackable) -> None:
        """Runs restore ops for `trackable`'s attributes."""

def add_variable(trackable, name, shape: Incomplete | None = None, dtype=..., initializer: Incomplete | None = None, trainable: bool = True):
    """Add a variable to a Trackable with no scope influence."""
def object_metadata(save_path):
    """Retrieves information about the objects in a checkpoint.

  Example usage:

  ```python
  object_graph = tf.contrib.checkpoint.object_metadata(
      tf.train.latest_checkpoint(checkpoint_directory))
  ckpt_variable_names = set()
  for node in object_graph.nodes:
    for attribute in node.attributes:
      ckpt_variable_names.add(attribute.full_name)
  ```

  Args:
    save_path: The path to the checkpoint, as returned by `save` or
      `tf.train.latest_checkpoint`.

  Returns:
    A parsed `tf.contrib.checkpoint.TrackableObjectGraph` protocol buffer.
  Raises:
    ValueError: If an object graph was not found in the checkpoint.
  """
def list_objects(root_trackable):
    """Traverse the object graph and list all accessible objects.

  Looks for `Trackable` objects which are dependencies of
  `root_trackable`. Includes slot variables only if the variable they are
  slotting for and the optimizer are dependencies of `root_trackable`
  (i.e. if they would be saved with a checkpoint).

  Args:
    root_trackable: A `Trackable` object whose dependencies should be flattened.

  Returns:
    A flat list of objects.
  """
def gather_initializers(root_trackable):
    """Traverse the object graph and find initialization ops.

  Looks for `Trackable` objects which are dependencies of
  `root_trackable` and which have an `initializer` property. Includes
  initializers for slot variables only if the variable they are slotting for and
  the optimizer are dependencies of `root_trackable` (i.e. if they would be
  saved with a checkpoint).

  Args:
    root_trackable: A `Trackable` object to gather initializers for.

  Returns:
    A list of initialization ops.
  """
def capture_dependencies(template) -> Generator[None, None, Incomplete]:
    """Capture variables created within this scope as `Template` dependencies.

  Requires that `template.variable_scope` is active.

  This scope is intended as a compatibility measure, allowing a trackable
  object to add dependencies on variables created in a block of code which is
  not aware of object-based saving (and instead uses variable names
  heavily). This is how `Template` objects add dependencies on variables and
  sub-`Template`s. Where possible, use `tf.compat.v1.make_template` directly.

  Args:
    template: The `Template` object to register dependencies with.

  Yields:
    None (when used as a context manager).
  """

class _LoadStatus(metaclass=abc.ABCMeta):
    """Abstract base for load status callbacks."""
    @abc.abstractmethod
    def assert_consumed(self):
        """Raises an exception unless a non-trivial restoration has completed."""
    @abc.abstractmethod
    def assert_existing_objects_matched(self):
        """Raises an exception unless existing Python objects have been matched."""
    @abc.abstractmethod
    def assert_nontrivial_match(self):
        """Raises an exception if only the root object matched."""
    @abc.abstractmethod
    def run_restore_ops(self, session: Incomplete | None = None):
        """Runs restore ops from the checkpoint. Requires a valid checkpoint."""
    @abc.abstractmethod
    def initialize_or_restore(self, session: Incomplete | None = None):
        """Runs restore ops from the checkpoint, or initializes variables."""
    def expect_partial(self):
        """Silence warnings about incomplete checkpoint restores."""

def streaming_restore(status, session: Incomplete | None = None):
    """When graph building, runs restore ops as soon as they come in.

  Args:
    status: A _LoadStatus objects from an object-based saver's restore().
      Streaming restore from name-based checkpoints is not currently supported.
    session: A session to run new restore ops in.
  """

class CheckpointLoadStatus(_LoadStatus):
    """Checks the status of checkpoint loading and manages restore ops.

  Returned from `Saver.restore`. Since `restore` may defer the loading of values
  in the checkpoint which don't yet have corresponding Python objects,
  `CheckpointLoadStatus` provides a callback to verify that checkpoint loading
  is complete (`assert_consumed`).

  When graph building, `restore` does not run restore ops itself since their
  creation may be deferred. The `run_restore_ops` method must be called once all
  Python objects with values to restore have been created and added to the
  dependency graph (this does not necessarily have to be the whole checkpoint;
  calling `run_restore_ops` while `assert_consumed` fails is supported and will
  partially restore the checkpoint).

  See `Saver.restore` for usage examples.
  """
    def __init__(self, checkpoint, feed_dict, graph_view) -> None: ...
    def assert_consumed(self):
        """Asserts that all objects in the checkpoint have been created/matched.

    Returns:
      `self` for chaining.
    Raises:
      AssertionError: If there are any Python objects in the dependency graph
        which have not been restored from this checkpoint or a later `restore`,
        or if there are any checkpointed values which have not been matched to
        Python objects.
    """
    def assert_existing_objects_matched(self):
        """Asserts that trackable Python objects have been matched.

    Note that this is a weaker assertion than `assert_consumed`. It will only
    fail for existing Python objects which are (transitive) dependencies of the
    root object and which do not have an entry in the checkpoint.

    It will not fail, for example, if a `tf.keras.Layer` object has not yet been
    built and so has not created any `tf.Variable` objects.

    Returns:
      `self` for chaining.

    Raises:
      AssertionError: If a Python object exists in the transitive dependencies
        of the root object but does not have a value in the checkpoint.
    """
    def assert_nontrivial_match(self):
        """Raises an exception if only the root object matched."""
    def run_restore_ops(self, session: Incomplete | None = None) -> None:
        """Run operations to restore objects in the dependency graph."""
    def initialize_or_restore(self, session: Incomplete | None = None) -> None:
        """Run operations to initialize or restore objects in the dependency graph.

    Any objects in the dependency graph which have initializers but are not in
    the checkpoint will have those initializers run, unless those variables are
    being restored by a later call to `tf.train.Checkpoint.restore()`.

    This method has a sibling in `InitializationOnlyStatus` which instead
    initializes variables. That type is returned if no checkpoint is specified
    in `Saver.restore`.

    Args:
      session: The session to run init/restore ops in. If `None`, uses the
        default session.
    """
    def expect_partial(self):
        """Silence warnings about incomplete checkpoint restores."""

class InitializationOnlyStatus(_LoadStatus):
    """Returned from `Saver.restore` when no checkpoint has been specified.

  Objects of this type have the same `assert_consumed` method as
  `CheckpointLoadStatus`, but it always fails. However,
  `initialize_or_restore` works on objects of both types, and will
  initialize variables in `InitializationOnlyStatus` objects or restore them
  otherwise.
  """
    def __init__(self, object_graph_view, restore_uid) -> None: ...
    def assert_consumed(self) -> None:
        """Assertion for consistency with `CheckpointLoadStatus`. Always fails."""
    def assert_existing_objects_matched(self) -> None:
        """Assertion for consistency with `CheckpointLoadStatus`. Always fails."""
    def assert_nontrivial_match(self) -> None:
        """Assertion for consistency with `CheckpointLoadStatus`. Always fails."""
    def run_restore_ops(self, session: Incomplete | None = None) -> None:
        """For consistency with `CheckpointLoadStatus`.

    Use `initialize_or_restore` for initializing if no checkpoint was passed
    to `Saver.restore` and restoring otherwise.

    Args:
      session: Not used.
    """
    def initialize_or_restore(self, session: Incomplete | None = None) -> None:
        """Runs initialization ops for variables.

    Objects which would be saved by `Saver.save` will be initialized, unless
    those variables are being restored by a later call to
    `tf.train.Checkpoint.restore()`.

    This method does nothing when executing eagerly (initializers get run
    eagerly).

    Args:
      session: The session to run initialization ops in. If `None`, uses the
        default session.
    """

class NameBasedSaverStatus(_LoadStatus):
    """Status for loading a name-based training checkpoint."""
    def __init__(self, checkpoint, object_graph_view) -> None: ...
    def add_to_optionally_restored(self, var) -> None:
        """Add a variable to the list of optionally restored variables.

    There are situations where certain variables should be ignored in assertions
    such as assert_existing_objects_matched(). One example is that of a
    checkpoint saved with train.Saver(), and restored with train.Checkpoint():
    it is possible for the train.Saver() checkpoint to be missing the internal
    `save_counter` variable, which we want to ignore on restore.

    Args:
      var: The variable to treat as optionally restored.
    """
    def assert_consumed(self):
        """Raises an exception if any variables are unmatched."""
    def assert_existing_objects_matched(self):
        """Raises an exception if currently created objects are unmatched."""
    def assert_nontrivial_match(self):
        """Raises an exception if currently created objects are unmatched."""
    def run_restore_ops(self, session: Incomplete | None = None) -> None:
        """Load the name-based checkpoint using a new `tf.compat.v1.train.Saver`."""
    def initialize_or_restore(self, session: Incomplete | None = None) -> None:
        """Alias for `run_restore_ops`."""

class _SessionWithFeedDictAdditions(session_lib.SessionInterface):
    """Pretends to be a session, inserts extra feeds on run()."""
    def __init__(self, session, feed_additions) -> None: ...
    def run(self, fetches, feed_dict: Incomplete | None = None, **kwargs): ...

class TrackableSaver:
    """Saves and restores a `Trackable` object and its dependencies.

  See `Trackable` for details of dependency management. `Saver` wraps
  `tf.compat.v1.train.Saver` for saving, including extra information about the
  graph of
  dependencies between Python objects. When restoring, it uses this information
  about the save-time dependency graph to more robustly match objects with their
  checkpointed values. When executing eagerly, it supports restoring variables
  on object creation (see `Saver.restore`).

  Values in a checkpoint are mapped to `Trackable` Python objects
  (`Variable`s, `Optimizer`s, `Layer`s) based on the names provided when the
  checkpoint was written. To avoid breaking existing checkpoints when modifying
  a class, dependency names (the names of attributes to which `Trackable`
  objects are assigned) may not change. These names are local to objects, in
  contrast to the `Variable.name`-based save/restore from
  `tf.compat.v1.train.Saver`, and
  so allow additional program transformations.
  """
    def __init__(self, graph_view) -> None:
        """Configure saving.

    Args:
      graph_view: An `ObjectGraphView` object containing a description of the
        object graph to save.
    """
    def save(self, file_prefix, checkpoint_number: Incomplete | None = None, session: Incomplete | None = None, options: Incomplete | None = None):
        """Save a training checkpoint.

    The saved checkpoint includes variables created by this object and any
    Trackable objects it depends on at the time `Saver.save()` is called.

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix). Names are generated based on this
        prefix and `checkpoint_number`, if provided.
      checkpoint_number: An integer variable or Tensor, used to number
        checkpoints. Typically this value is saved along with other variables in
        training checkpoints, which will happen automatically if it was created
        by `root_trackable` or one of its dependencies (via
        `Trackable._add_variable`).
      session: The session to evaluate variables in. Ignored when executing
        eagerly. If not provided when graph building, the default session is
        used.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      The full path to the checkpoint.

    Raises:
      RuntimeError: if called in V1 Graph mode without a default session.
    """
    def restore(self, save_path, options: Incomplete | None = None):
        """Restore a training checkpoint.

    Restores `root_trackable` and any objects that it tracks
    (transitive). Either assigns values immediately if variables to restore have
    been created already, or defers restoration until the variables are
    created. Dependencies added to the `root_trackable` passed to the
    constructor after this call will be matched if they have a corresponding
    object in the checkpoint.

    When building a graph, restorations are added to the graph but not run.

    ```python
    saver = Saver(root)
    saver.restore(path)
    ```

    To ensure that loading is complete and no more deferred restorations will
    take place, you can use the `assert_consumed()` method of the status object
    returned by the `restore` call.

    The assert will raise an exception unless every object was matched and all
    checkpointed values have a matching variable object.

    ```python
    saver = Saver(root)
    saver.restore(path).assert_consumed()
    ```

    When graph building, `assert_consumed()` indicates that all of the restore
    ops which will be created for this checkpoint have been created. They can be
    run via the `run_restore_ops()` function of the status object:

    ```python
    saver.restore(path).assert_consumed().run_restore_ops()
    ```

    If the checkpoint has not been consumed completely, then the list of restore
    ops will grow as more objects are added to the dependency graph.

    Name-based `tf.compat.v1.train.Saver` checkpoints can be loaded using this
    method. There is no deferred loading, and names are used to match
    variables. No restore ops are created/run until `run_restore_ops()` or
    `initialize_or_restore()` are called on the returned status object, even
    when executing eagerly. Re-encode name-based checkpoints using this
    object-based `Saver.save` as soon as possible.

    Args:
      save_path: The path to the checkpoint, as returned by `save` or
        `tf.train.latest_checkpoint`. If None (as when there is no latest
        checkpoint for `tf.train.latest_checkpoint` to return), returns an
        object which may run initializers for objects in the dependency graph.
        If the checkpoint was written by the name-based
        `tf.compat.v1.train.Saver`, names are used to match variables.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      A load status object, which can be used to make assertions about the
      status of checkpoint restoration and run initialization/restore ops
      (of type `CheckpointLoadStatus`, or `InitializationOnlyStatus` if
      `save_path` is `None`).

      If `save_path` points to a name-based checkpoint, a `NameBasedSaverStatus`
      object is returned which runs restore ops from a name-based saver.

    Raises:
      RuntimeError: When a checkpoint file saved by async checkpoint is not
        available upon restore().
    """

def frozen_saver(root_trackable):
    """Creates a static `tf.compat.v1.train.Saver` from a trackable object.

  The returned `Saver` saves object-based checkpoints, but these checkpoints
  will no longer reflect structural changes to the object graph, only changes to
  the values of `Variable`s added as dependencies of the root object before
  `freeze` was called.

  `restore` works on the returned `Saver`, but requires that the object graph of
  the checkpoint being loaded exactly matches the object graph when `freeze` was
  called. This is in contrast the object-based restore performed by
  `tf.train.Checkpoint` which attempts a fuzzy matching between a checkpoint's
  object graph and the current Python object graph.

  Args:
    root_trackable: A trackable object to save.

  Returns:
    A saver which saves object-based checkpoints for the object graph frozen at
    the time `frozen_saver` was called.
  """

class CheckpointV1(autotrackable.AutoTrackable):
    '''Groups trackable objects, saving and restoring them.

  `Checkpoint`\'s constructor accepts keyword arguments whose values are types
  that contain trackable state, such as `tf.compat.v1.train.Optimizer`
  implementations, `tf.Variable`, `tf.keras.Layer` implementations, or
  `tf.keras.Model` implementations. It saves these values with a checkpoint, and
  maintains a `save_counter` for numbering checkpoints.

  Example usage when graph building:

  ```python
  import tensorflow as tf
  import os

  checkpoint_directory = "/tmp/training_checkpoints"
  checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

  checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
  status = checkpoint.restore(tf.train.latest_checkpoint(checkpoint_directory))
  train_op = optimizer.minimize( ... )
  status.assert_consumed()  # Optional sanity checks.
  with tf.compat.v1.Session() as session:
    # Use the Session to restore variables, or initialize them if
    # tf.train.latest_checkpoint returned None.
    status.initialize_or_restore(session)
    for _ in range(num_training_steps):
      session.run(train_op)
    checkpoint.save(file_prefix=checkpoint_prefix)
  ```

  Example usage with eager execution enabled:

  ```python
  import tensorflow as tf
  import os

  tf.compat.v1.enable_eager_execution()

  checkpoint_directory = "/tmp/training_checkpoints"
  checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

  checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
  status = checkpoint.restore(tf.train.latest_checkpoint(checkpoint_directory))
  for _ in range(num_training_steps):
    optimizer.minimize( ... )  # Variables will be restored on creation.
  status.assert_consumed()  # Optional sanity checks.
  checkpoint.save(file_prefix=checkpoint_prefix)
  ```

  `Checkpoint.save` and `Checkpoint.restore` write and read object-based
  checkpoints, in contrast to `tf.compat.v1.train.Saver` which writes and reads
  `variable.name` based checkpoints. Object-based checkpointing saves a graph of
  dependencies between Python objects (`Layer`s, `Optimizer`s, `Variable`s,
  etc.) with named edges, and this graph is used to match variables when
  restoring a checkpoint. It can be more robust to changes in the Python
  program, and helps to support restore-on-create for variables when executing
  eagerly. Prefer `tf.train.Checkpoint` over `tf.compat.v1.train.Saver` for new
  code.

  `Checkpoint` objects have dependencies on the objects passed as keyword
  arguments to their constructors, and each dependency is given a name that is
  identical to the name of the keyword argument for which it was created.
  TensorFlow classes like `Layer`s and `Optimizer`s will automatically add
  dependencies on their variables (e.g. "kernel" and "bias" for
  `tf.keras.layers.Dense`). Inheriting from `tf.keras.Model` makes managing
  dependencies easy in user-defined classes, since `Model` hooks into attribute
  assignment. For example:

  ```python
  class Regress(tf.keras.Model):

    def __init__(self):
      super().__init__()
      self.input_transform = tf.keras.layers.Dense(10)
      # ...

    def call(self, inputs):
      x = self.input_transform(inputs)
      # ...
  ```

  This `Model` has a dependency named "input_transform" on its `Dense` layer,
  which in turn depends on its variables. As a result, saving an instance of
  `Regress` using `tf.train.Checkpoint` will also save all the variables created
  by the `Dense` layer.

  When variables are assigned to multiple workers, each worker writes its own
  section of the checkpoint. These sections are then merged/re-indexed to behave
  as a single checkpoint. This avoids copying all variables to one worker, but
  does require that all workers see a common filesystem.

  While `tf.keras.Model.save_weights` and `tf.train.Checkpoint.save` save in the
  same format, note that the root of the resulting checkpoint is the object the
  save method is attached to. This means saving a `tf.keras.Model` using
  `save_weights` and loading into a `tf.train.Checkpoint` with a `Model`
  attached (or vice versa) will not match the `Model`\'s variables. See the
  [guide to training
  checkpoints](https://www.tensorflow.org/guide/checkpoint) for
  details. Prefer `tf.train.Checkpoint` over `tf.keras.Model.save_weights` for
  training checkpoints.

  Attributes:
    save_counter: Incremented when `save()` is called. Used to number
      checkpoints.
  '''
    def __init__(self, **kwargs) -> None:
        """Group objects into a training checkpoint.

    Args:
      **kwargs: Keyword arguments are set as attributes of this object, and are
        saved with the checkpoint. Values must be trackable objects.

    Raises:
      ValueError: If objects in `kwargs` are not trackable.
    """
    def write(self, file_prefix, session: Incomplete | None = None):
        """Writes a training checkpoint.

    The checkpoint includes variables created by this object and any
    trackable objects it depends on at the time `Checkpoint.write()` is
    called.

    `write` does not number checkpoints, increment `save_counter`, or update the
    metadata used by `tf.train.latest_checkpoint`. It is primarily intended for
    use by higher level checkpoint management utilities. `save` provides a very
    basic implementation of these features.

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix).
      session: The session to evaluate variables in. Ignored when executing
        eagerly. If not provided when graph building, the default session is
        used.

    Returns:
      The full path to the checkpoint (i.e. `file_prefix`).
    """
    @property
    def save_counter(self):
        """An integer variable which starts at zero and is incremented on save.

    Used to number checkpoints.

    Returns:
      The save counter variable.
    """
    def save(self, file_prefix, session: Incomplete | None = None):
        """Saves a training checkpoint and provides basic checkpoint management.

    The saved checkpoint includes variables created by this object and any
    trackable objects it depends on at the time `Checkpoint.save()` is
    called.

    `save` is a basic convenience wrapper around the `write` method,
    sequentially numbering checkpoints using `save_counter` and updating the
    metadata used by `tf.train.latest_checkpoint`. More advanced checkpoint
    management, for example garbage collection and custom numbering, may be
    provided by other utilities which also wrap `write`
    (`tf.train.CheckpointManager` for example).

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix). Names are generated based on this
        prefix and `Checkpoint.save_counter`.
      session: The session to evaluate variables in. Ignored when executing
        eagerly. If not provided when graph building, the default session is
        used.

    Returns:
      The full path to the checkpoint.
    """
    def restore(self, save_path):
        """Restore a training checkpoint.

    Restores this `Checkpoint` and any objects it depends on.

    When executing eagerly, either assigns values immediately if variables to
    restore have been created already, or defers restoration until the variables
    are created. Dependencies added after this call will be matched if they have
    a corresponding object in the checkpoint (the restore request will queue in
    any trackable object waiting for the expected dependency to be added).

    When graph building, restoration ops are added to the graph but not run
    immediately.

    ```python
    checkpoint = tf.train.Checkpoint( ... )
    checkpoint.restore(path)
    ```

    To ensure that loading is complete and no more deferred restorations will
    take place, you can use the `assert_consumed()` method of the status object
    returned by `restore`.
    The assert will raise an exception if any Python objects in the dependency
    graph were not found in the checkpoint, or if any checkpointed values do not
    have a matching Python object:

    ```python
    checkpoint = tf.train.Checkpoint( ... )
    checkpoint.restore(path).assert_consumed()
    ```

    When graph building, `assert_consumed()` indicates that all of the restore
    ops that will be created for this checkpoint have been created. They can be
    run via the `run_restore_ops()` method of the status object:

    ```python
    checkpoint.restore(path).assert_consumed().run_restore_ops()
    ```

    If the checkpoint has not been consumed completely, then the list of restore
    ops will grow as more objects are added to the dependency graph.

    To check that all variables in the Python object have restored values from
    checkpoint, use `assert_existing_objects_matched()`. This assertion is
    useful when called after the variables in your graph have been created.

    Name-based `tf.compat.v1.train.Saver` checkpoints can be loaded using this
    method. Names are used to match variables. No restore ops are created/run
    until `run_restore_ops()` or `initialize_or_restore()` are called on the
    returned status object when graph building, but there is restore-on-creation
    when executing eagerly. Re-encode name-based checkpoints using
    `tf.train.Checkpoint.save` as soon as possible.

    Args:
      save_path: The path to the checkpoint, as returned by `save` or
        `tf.train.latest_checkpoint`. If None (as when there is no latest
        checkpoint for `tf.train.latest_checkpoint` to return), returns an
        object which may run initializers for objects in the dependency graph.
        If the checkpoint was written by the name-based
        `tf.compat.v1.train.Saver`, names are used to match variables.

    Returns:
      A load status object, which can be used to make assertions about the
      status of a checkpoint restoration and run initialization/restore ops.

      The returned status object has the following methods:

      * `assert_consumed()`:
          Raises an exception if any variables are unmatched: either
          checkpointed values which don't have a matching Python object or
          Python objects in the dependency graph with no values in the
          checkpoint. This method returns the status object, and so may be
          chained with `initialize_or_restore` or `run_restore_ops`.

      * `assert_existing_objects_matched()`:
          Raises an exception if any existing Python objects in the dependency
          graph are unmatched. Unlike `assert_consumed`, this assertion will
          pass if values in the checkpoint have no corresponding Python
          objects. For example a `tf.keras.Layer` object which has not yet been
          built, and so has not created any variables, will pass this assertion
          but will fail `assert_consumed`. Useful when loading part of a larger
          checkpoint into a new Python program, e.g. a training checkpoint with
          a `tf.compat.v1.train.Optimizer` was saved but only the state required
          for inference is being loaded. This method returns the status object,
          and so may be chained with `initialize_or_restore` or
          `run_restore_ops`.

      * `assert_nontrivial_match()`: Asserts that something aside from the root
          object was matched. This is a very weak assertion, but is useful for
          sanity checking in library code where objects may exist in the
          checkpoint which haven't been created in Python and some Python
          objects may not have a checkpointed value.

      * `expect_partial()`: Silence warnings about incomplete checkpoint
          restores. Warnings are otherwise printed for unused parts of the
          checkpoint file or object when the `Checkpoint` object is deleted
          (often at program shutdown).

      * `initialize_or_restore(session=None)`:
          When graph building, runs variable initializers if `save_path` is
          `None`, but otherwise runs restore operations. If no `session` is
          explicitly specified, the default session is used. No effect when
          executing eagerly (variables are initialized or restored eagerly).

      * `run_restore_ops(session=None)`:
          When graph building, runs restore operations. If no `session` is
          explicitly specified, the default session is used. No effect when
          executing eagerly (restore operations are run eagerly). May only be
          called when `save_path` is not `None`.
    """

class Checkpoint(autotrackable.AutoTrackable):
    '''Manages saving/restoring trackable values to disk.

  TensorFlow objects may contain trackable state, such as `tf.Variable`s,
  `tf.keras.optimizers.Optimizer` implementations, `tf.data.Dataset` iterators,
  `tf.keras.Layer` implementations, or  `tf.keras.Model` implementations.
  These are called **trackable objects**.

  A `Checkpoint` object can be constructed to save either a single or group of
  trackable objects to a checkpoint file. It maintains a `save_counter` for
  numbering checkpoints.

  Example:

  ```python
  model = tf.keras.Model(...)
  checkpoint = tf.train.Checkpoint(model)

  # Save a checkpoint to /tmp/training_checkpoints-{save_counter}. Every time
  # checkpoint.save is called, the save counter is increased.
  save_path = checkpoint.save(\'/tmp/training_checkpoints\')

  # Restore the checkpointed values to the `model` object.
  checkpoint.restore(save_path)
  ```

  Example 2:

  ```python
  import tensorflow as tf
  import os

  checkpoint_directory = "/tmp/training_checkpoints"
  checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

  # Create a Checkpoint that will manage two objects with trackable state,
  # one we name "optimizer" and the other we name "model".
  checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
  status = checkpoint.restore(tf.train.latest_checkpoint(checkpoint_directory))
  for _ in range(num_training_steps):
    optimizer.minimize( ... )  # Variables will be restored on creation.
  status.assert_consumed()  # Optional sanity checks.
  checkpoint.save(file_prefix=checkpoint_prefix)
  ```

  `Checkpoint.save()` and `Checkpoint.restore()` write and read object-based
  checkpoints, in contrast to TensorFlow 1.x\'s `tf.compat.v1.train.Saver` which
  writes and
  reads `variable.name` based checkpoints. Object-based checkpointing saves a
  graph of dependencies between Python objects (`Layer`s, `Optimizer`s,
  `Variable`s, etc.) with named edges, and this graph is used to match variables
  when restoring a checkpoint. It can be more robust to changes in the Python
  program, and helps to support restore-on-create for variables.

  `Checkpoint` objects have dependencies on the objects passed as keyword
  arguments to their constructors, and each dependency is given a name that is
  identical to the name of the keyword argument for which it was created.
  TensorFlow classes like `Layer`s and `Optimizer`s will automatically add
  dependencies on their own variables (e.g. "kernel" and "bias" for
  `tf.keras.layers.Dense`). Inheriting from `tf.keras.Model` makes managing
  dependencies easy in user-defined classes, since `Model` hooks into attribute
  assignment. For example:

  ```python
  class Regress(tf.keras.Model):

    def __init__(self):
      super().__init__()
      self.input_transform = tf.keras.layers.Dense(10)
      # ...

    def call(self, inputs):
      x = self.input_transform(inputs)
      # ...
  ```

  This `Model` has a dependency named "input_transform" on its `Dense` layer,
  which in turn depends on its variables. As a result, saving an instance of
  `Regress` using `tf.train.Checkpoint` will also save all the variables created
  by the `Dense` layer.

  When variables are assigned to multiple workers, each worker writes its own
  section of the checkpoint. These sections are then merged/re-indexed to behave
  as a single checkpoint. This avoids copying all variables to one worker, but
  does require that all workers see a common filesystem.

  This function differs slightly from the Keras Model `save_weights` function.
  `tf.keras.Model.save_weights` creates a checkpoint file with the name
  specified in `filepath`, while `tf.train.Checkpoint` numbers the checkpoints,
  using `filepath` as the prefix for the checkpoint file names. Aside from this,
  `model.save_weights()` and `tf.train.Checkpoint(model).save()` are equivalent.

  See the [guide to training
  checkpoints](https://www.tensorflow.org/guide/checkpoint) for
  details.

  Attributes:
    save_counter: Incremented when `save()` is called. Used to number
      checkpoints.
  '''
    def __init__(self, root: Incomplete | None = None, **kwargs) -> None:
        """Creates a training checkpoint for a single or group of objects.

    Args:
      root: The root object to checkpoint. `root` may be a trackable object or
        `WeakRef` of a trackable object.
      **kwargs: Keyword arguments are set as attributes of this object, and are
        saved with the checkpoint. All `kwargs` must be trackable objects, or a
        nested structure of trackable objects (`list`, `dict`, or `tuple`).

    Raises:
      ValueError: If `root` or the objects in `kwargs` are not trackable. A
        `ValueError` is also raised if the `root` object tracks different
        objects from the ones listed in attributes in kwargs (e.g.
        `root.child = A` and `tf.train.Checkpoint(root, child=B)` are
        incompatible).

    """
    def write(self, file_prefix, options: Incomplete | None = None):
        '''Writes a training checkpoint.

    The checkpoint includes variables created by this object and any
    trackable objects it depends on at the time `Checkpoint.write()` is
    called.

    `write` does not number checkpoints, increment `save_counter`, or update the
    metadata used by `tf.train.latest_checkpoint`. It is primarily intended for
    use by higher level checkpoint management utilities. `save` provides a very
    basic implementation of these features.

    Checkpoints written with `write` must be read with `read`.

    Example usage:

    ```
    step = tf.Variable(0, name="step")
    checkpoint = tf.Checkpoint(step=step)
    checkpoint.write("/tmp/ckpt")

    # Later, read the checkpoint with read()
    checkpoint.read("/tmp/ckpt")

    # You can also pass options to write() and read(). For example this
    # runs the IO ops on the localhost:
    options = tf.CheckpointOptions(experimental_io_device="/job:localhost")
    checkpoint.write("/tmp/ckpt", options=options)

    # Later, read the checkpoint with read()
    checkpoint.read("/tmp/ckpt", options=options)
    ```

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix).
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      The full path to the checkpoint (i.e. `file_prefix`).
    '''
    @property
    def save_counter(self):
        """An integer variable which starts at zero and is incremented on save.

    Used to number checkpoints.

    Returns:
      The save counter variable.
    """
    def save(self, file_prefix, options: Incomplete | None = None):
        '''Saves a training checkpoint and provides basic checkpoint management.

    The saved checkpoint includes variables created by this object and any
    trackable objects it depends on at the time `Checkpoint.save()` is
    called.

    `save` is a basic convenience wrapper around the `write` method,
    sequentially numbering checkpoints using `save_counter` and updating the
    metadata used by `tf.train.latest_checkpoint`. More advanced checkpoint
    management, for example garbage collection and custom numbering, may be
    provided by other utilities which also wrap `write` and `read`.
    (`tf.train.CheckpointManager` for example).

    ```
    step = tf.Variable(0, name="step")
    checkpoint = tf.train.Checkpoint(step=step)
    checkpoint.save("/tmp/ckpt")

    # Later, read the checkpoint with restore()
    checkpoint.restore("/tmp/ckpt-1")

    # You can also pass options to save() and restore(). For example this
    # runs the IO ops on the localhost:
    options = tf.train.CheckpointOptions(experimental_io_device="/job:localhost")
    checkpoint.save("/tmp/ckpt", options=options)

    # Later, read the checkpoint with restore()
    checkpoint.restore("/tmp/ckpt-1", options=options)
    ```

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix). Names are generated based on this
        prefix and `Checkpoint.save_counter`.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      The full path to the checkpoint.
    '''
    def read(self, save_path, options: Incomplete | None = None):
        '''Reads a training checkpoint written with `write`.

    Reads this `Checkpoint` and any objects it depends on.

    This method is just like `restore()` but does not expect the `save_counter`
    variable in the checkpoint. It only restores the objects that the checkpoint
    already depends on.

    The method is primarily intended for use by higher level checkpoint
    management utilities that use `write()` instead of `save()` and have their
    own mechanisms to number and track checkpoints.

    Example usage:

    ```python
    # Create a checkpoint with write()
    ckpt = tf.train.Checkpoint(v=tf.Variable(1.))
    path = ckpt.write(\'/tmp/my_checkpoint\')

    # Later, load the checkpoint with read()
    # With restore() assert_consumed() would have failed.
    checkpoint.read(path).assert_consumed()

    # You can also pass options to read(). For example this
    # runs the IO ops on the localhost:
    options = tf.train.CheckpointOptions(
        experimental_io_device="/job:localhost")
    checkpoint.read(path, options=options)
    ```

    Args:
      save_path: The path to the checkpoint as returned by `write`.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      A load status object, which can be used to make assertions about the
      status of a checkpoint restoration.  See `restore` for details.
    '''
    def restore(self, save_path, options: Incomplete | None = None):
        '''Restores a training checkpoint.

    Restores this `Checkpoint` and any objects it depends on.

    This method is intended to be used to load checkpoints created by `save()`.
    For checkpoints created by `write()` use the `read()` method which does not
    expect the `save_counter` variable added by `save()`.

    `restore()` either assigns values immediately if variables to restore have
    been created already, or defers restoration until the variables are
    created. Dependencies added after this call will be matched if they have a
    corresponding object in the checkpoint (the restore request will queue in
    any trackable object waiting for the expected dependency to be added).

    ```python
    checkpoint = tf.train.Checkpoint( ... )
    checkpoint.restore(path)

    # You can additionally pass options to restore():
    options = tf.CheckpointOptions(experimental_io_device="/job:localhost")
    checkpoint.restore(path, options=options)
    ```

    To ensure that loading is complete and no more deferred restorations will
    take place, use the `assert_consumed()` method of the status object returned
    by `restore()`:

    ```python
    checkpoint.restore(path, options=options).assert_consumed()
    ```

    The assert will raise an error if any Python objects in the dependency graph
    were not found in the checkpoint, or if any checkpointed values do not have
    a matching Python object.

    Name-based `tf.compat.v1.train.Saver` checkpoints from TensorFlow 1.x can be
    loaded using this method. Names are used to match variables. Re-encode
    name-based checkpoints using `tf.train.Checkpoint.save` as soon as possible.

    **Loading from SavedModel checkpoints**

    To load values from a SavedModel, just pass the SavedModel directory
    to checkpoint.restore:

    ```python
    model = tf.keras.Model(...)
    tf.saved_model.save(model, path)  # or model.save(path, save_format=\'tf\')

    checkpoint = tf.train.Checkpoint(model)
    checkpoint.restore(path).expect_partial()
    ```

    This example calls `expect_partial()` on the loaded status, since
    SavedModels saved from Keras often generates extra keys in the checkpoint.
    Otherwise, the program prints a lot of warnings about unused keys at exit
    time.

    Args:
      save_path: The path to the checkpoint, as returned by `save` or
        `tf.train.latest_checkpoint`. If the checkpoint was written by the
        name-based `tf.compat.v1.train.Saver`, names are used to match
        variables. This path may also be a SavedModel directory.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      A load status object, which can be used to make assertions about the
      status of a checkpoint restoration.

      The returned status object has the following methods:

      * `assert_consumed()`:
          Raises an exception if any variables are unmatched: either
          checkpointed values which don\'t have a matching Python object or
          Python objects in the dependency graph with no values in the
          checkpoint. This method returns the status object, and so may be
          chained with other assertions.

      * `assert_existing_objects_matched()`:
          Raises an exception if any existing Python objects in the dependency
          graph are unmatched. Unlike `assert_consumed`, this assertion will
          pass if values in the checkpoint have no corresponding Python
          objects. For example a `tf.keras.Layer` object which has not yet been
          built, and so has not created any variables, will pass this assertion
          but fail `assert_consumed`. Useful when loading part of a larger
          checkpoint into a new Python program, e.g. a training checkpoint with
          a `tf.compat.v1.train.Optimizer` was saved but only the state required
          for
          inference is being loaded. This method returns the status object, and
          so may be chained with other assertions.

      * `assert_nontrivial_match()`: Asserts that something aside from the root
          object was matched. This is a very weak assertion, but is useful for
          sanity checking in library code where objects may exist in the
          checkpoint which haven\'t been created in Python and some Python
          objects may not have a checkpointed value.

      * `expect_partial()`: Silence warnings about incomplete checkpoint
          restores. Warnings are otherwise printed for unused parts of the
          checkpoint file or object when the `Checkpoint` object is deleted
          (often at program shutdown).

    Raises:
      NotFoundError: if the a checkpoint or SavedModel cannot be found at
        `save_path`.
    '''
