import abc
from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.checkpoint import graph_view as graph_view
from tensorflow.python.distribute import distribute_coordinator_context as distribute_coordinator_context
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, lookup_ops as lookup_ops, resources as resources, variables as variables
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import basic_session_run_hooks as basic_session_run_hooks, coordinator as coordinator, queue_runner as queue_runner, session_run_hook as session_run_hook
from tensorflow.python.util import function_utils as function_utils
from tensorflow.python.util.tf_export import tf_export as tf_export

USE_DEFAULT: Incomplete

class Scaffold:
    """Structure to create or gather pieces commonly needed to train a model.

  When you build a model for training you usually need ops to initialize
  variables, a `Saver` to checkpoint them, an op to collect summaries for
  the visualizer, and so on.

  Various libraries built on top of the core TensorFlow library take care of
  creating some or all of these pieces and storing them in well known
  collections in the graph.  The `Scaffold` class helps pick these pieces from
  the graph collections, creating and adding them to the collections if needed.

  If you call the scaffold constructor without any arguments, it will pick
  pieces from the collections, creating default ones if needed when
  `scaffold.finalize()` is called.  You can pass arguments to the constructor to
  provide your own pieces.  Pieces that you pass to the constructor are not
  added to the graph collections.

  The following pieces are directly accessible as attributes of the `Scaffold`
  object:

  * `saver`: A `tf.compat.v1.train.Saver` object taking care of saving the
  variables.
    Picked from and stored into the `SAVERS` collection in the graph by default.
  * `init_op`: An op to run to initialize the variables.  Picked from and
    stored into the `INIT_OP` collection in the graph by default.
  * `ready_op`: An op to verify that the variables are initialized.  Picked
    from and stored into the `READY_OP` collection in the graph by default.
  * `ready_for_local_init_op`: An op to verify that global state has been
    initialized and it is alright to run `local_init_op`.  Picked from and
    stored into the `READY_FOR_LOCAL_INIT_OP` collection in the graph by
    default. This is needed when the initialization of local variables depends
    on the values of global variables.
  * `local_init_op`: An op to initialize the local variables.  Picked
    from and stored into the `LOCAL_INIT_OP` collection in the graph by default.
  * `summary_op`: An op to run and merge the summaries in the graph.  Picked
    from and stored into the `SUMMARY_OP` collection in the graph by default.

  You can also pass the following additional pieces to the constructor:

  * `init_feed_dict`: A session feed dictionary that should be used when
     running the init op.
  * `init_fn`: A callable to run after the init op to perform additional
    initializations.  The callable will be called as
    `init_fn(scaffold, session)`.

  """
    def __init__(self, init_op: Incomplete | None = None, init_feed_dict: Incomplete | None = None, init_fn: Incomplete | None = None, ready_op: Incomplete | None = None, ready_for_local_init_op: Incomplete | None = None, local_init_op: Incomplete | None = None, summary_op: Incomplete | None = None, saver: Incomplete | None = None, copy_from_scaffold: Incomplete | None = None, local_init_feed_dict: Incomplete | None = None) -> None:
        """Create a scaffold.

    Args:
      init_op: Optional op for initializing variables.
      init_feed_dict: Optional session feed dictionary to use when running the
        init_op.
      init_fn: Optional function to use to initialize the model after running
        the init_op.  Will be called as `init_fn(scaffold, session)`.
      ready_op: Optional op to verify that the variables are initialized.  Must
        return an empty 1D string tensor when the variables are initialized, or
        a non-empty 1D string tensor listing the names of the non-initialized
        variables.
      ready_for_local_init_op: Optional op to verify that the global variables
        are initialized and `local_init_op` can be run. Must return an empty 1D
        string tensor when the global variables are initialized, or a non-empty
        1D string tensor listing the names of the non-initialized global
        variables.
      local_init_op: Optional op to initialize local variables.
      summary_op: Optional op to gather all summaries.  Must return a scalar
        string tensor containing a serialized `Summary` proto.
      saver: Optional `tf.compat.v1.train.Saver` object to use to save and
        restore variables.  May also be a `tf.train.Checkpoint` object, in which
        case object-based checkpoints are saved. This will also load some
        object-based checkpoints saved from elsewhere, but that loading may be
        fragile since it uses fixed keys rather than performing a full
        graph-based match. For example if a variable has two paths from the
        `Checkpoint` object because two `Model` objects share the `Layer` object
        that owns it, removing one `Model` may change the keys and break
        checkpoint loading through this API, whereas a graph-based match would
        match the variable through the other `Model`.
      copy_from_scaffold: Optional scaffold object to copy fields from. Its
        fields will be overwritten by the provided fields in this function.
      local_init_feed_dict: Optional session feed dictionary to use when running
        the local_init_op.
    """
    def finalize(self):
        """Creates operations if needed and finalizes the graph."""
    @property
    def init_fn(self): ...
    @property
    def init_op(self): ...
    @property
    def ready_op(self): ...
    @property
    def ready_for_local_init_op(self): ...
    @property
    def local_init_op(self): ...
    @property
    def local_init_feed_dict(self): ...
    @property
    def summary_op(self): ...
    @property
    def saver(self): ...
    @property
    def init_feed_dict(self): ...
    @staticmethod
    def get_or_default(arg_name, collection_key, default_constructor):
        """Get from cache or create a default operation."""
    @staticmethod
    def default_local_init_op():
        """Returns an op that groups the default local init ops.

    This op is used during session initialization when a Scaffold is
    initialized without specifying the local_init_op arg. It includes
    `tf.compat.v1.local_variables_initializer`,
    `tf.compat.v1.tables_initializer`, and also
    initializes local session resources.

    Returns:
      The default Scaffold local init op.
    """

def MonitoredTrainingSession(master: str = '', is_chief: bool = True, checkpoint_dir: Incomplete | None = None, scaffold: Incomplete | None = None, hooks: Incomplete | None = None, chief_only_hooks: Incomplete | None = None, save_checkpoint_secs=..., save_summaries_steps=..., save_summaries_secs=..., config: Incomplete | None = None, stop_grace_period_secs: int = 120, log_step_count_steps: int = 100, max_wait_secs: int = 7200, save_checkpoint_steps=..., summary_dir: Incomplete | None = None, save_graph_def: bool = True):
    """Creates a `MonitoredSession` for training.

  For a chief, this utility sets proper session initializer/restorer. It also
  creates hooks related to checkpoint and summary saving. For workers, this
  utility sets proper session creator which waits for the chief to
  initialize/restore. Please check `tf.compat.v1.train.MonitoredSession` for
  more
  information.

  @compatibility(TF2)
  This API is not compatible with eager execution and `tf.function`. To migrate
  to TF2, rewrite the code to be compatible with eager execution. Check the
  [migration
  guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
  on replacing `Session.run` calls. In Keras, session hooks can be replaced by
  Callbacks e.g. [logging hook notebook](
  https://github.com/tensorflow/docs/blob/master/site/en/guide/migrate/logging_stop_hook.ipynb)
  For more details please read [Better
  performance with tf.function](https://www.tensorflow.org/guide/function).
  @end_compatibility

  Args:
    master: `String` the TensorFlow master to use.
    is_chief: If `True`, it will take care of initialization and recovery the
      underlying TensorFlow session. If `False`, it will wait on a chief to
      initialize or recover the TensorFlow session.
    checkpoint_dir: A string.  Optional path to a directory where to restore
      variables.
    scaffold: A `Scaffold` used for gathering or building supportive ops. If not
      specified, a default one is created. It's used to finalize the graph.
    hooks: Optional list of `SessionRunHook` objects.
    chief_only_hooks: list of `SessionRunHook` objects. Activate these hooks if
      `is_chief==True`, ignore otherwise.
    save_checkpoint_secs: The frequency, in seconds, that a checkpoint is saved
      using a default checkpoint saver. If both `save_checkpoint_steps` and
      `save_checkpoint_secs` are set to `None`, then the default checkpoint
      saver isn't used. If both are provided, then only `save_checkpoint_secs`
      is used. Default 600.
    save_summaries_steps: The frequency, in number of global steps, that the
      summaries are written to disk using a default summary saver. If both
      `save_summaries_steps` and `save_summaries_secs` are set to `None`, then
      the default summary saver isn't used. Default 100.
    save_summaries_secs: The frequency, in secs, that the summaries are written
      to disk using a default summary saver.  If both `save_summaries_steps` and
      `save_summaries_secs` are set to `None`, then the default summary saver
      isn't used. Default not enabled.
    config: an instance of `tf.compat.v1.ConfigProto` proto used to configure
      the session. It's the `config` argument of constructor of
      `tf.compat.v1.Session`.
    stop_grace_period_secs: Number of seconds given to threads to stop after
      `close()` has been called.
    log_step_count_steps: The frequency, in number of global steps, that the
      global step/sec is logged.
    max_wait_secs: Maximum time workers should wait for the session to become
      available. This should be kept relatively short to help detect incorrect
      code, but sometimes may need to be increased if the chief takes a while to
      start up.
    save_checkpoint_steps: The frequency, in number of global steps, that a
      checkpoint is saved using a default checkpoint saver. If both
      `save_checkpoint_steps` and `save_checkpoint_secs` are set to `None`, then
      the default checkpoint saver isn't used. If both are provided, then only
      `save_checkpoint_secs` is used. Default not enabled.
    summary_dir: A string.  Optional path to a directory where to save
      summaries. If None, checkpoint_dir is used instead.
    save_graph_def: Whether to save the GraphDef and MetaGraphDef to
      `checkpoint_dir`. The GraphDef is saved after the session is created as
      `graph.pbtxt`. MetaGraphDefs are saved out for every checkpoint as
      `model.ckpt-*.meta`.

  Returns:
    A `MonitoredSession` object.
  """

class SessionCreator(metaclass=abc.ABCMeta):
    """A factory for tf.Session."""
    @abc.abstractmethod
    def create_session(self): ...

class ChiefSessionCreator(SessionCreator):
    """Creates a tf.compat.v1.Session for a chief."""
    def __init__(self, scaffold: Incomplete | None = None, master: str = '', config: Incomplete | None = None, checkpoint_dir: Incomplete | None = None, checkpoint_filename_with_path: Incomplete | None = None) -> None:
        """Initializes a chief session creator.

    Args:
      scaffold: A `Scaffold` used for gathering or building supportive ops. If
        not specified a default one is created. It's used to finalize the graph.
      master: `String` representation of the TensorFlow master to use.
      config: `ConfigProto` proto used to configure the session.
      checkpoint_dir: A string.  Optional path to a directory where to restore
        variables.
      checkpoint_filename_with_path: Full file name path to the checkpoint file.
    """
    def create_session(self): ...

class WorkerSessionCreator(SessionCreator):
    """Creates a tf.compat.v1.Session for a worker."""
    def __init__(self, scaffold: Incomplete | None = None, master: str = '', config: Incomplete | None = None, max_wait_secs=...) -> None:
        """Initializes a worker session creator.

    Args:
      scaffold: A `Scaffold` used for gathering or building supportive ops. If
        not specified a default one is created. It's used to finalize the graph.
      master: `String` representation of the TensorFlow master to use.
      config: `ConfigProto` proto used to configure the session.
      max_wait_secs: Maximum time to wait for the session to become available.
    """
    def create_session(self): ...

class _MonitoredSession:
    """See `MonitoredSession` or `SingularMonitoredSession`."""
    def __init__(self, session_creator, hooks, should_recover, stop_grace_period_secs: int = 120) -> None:
        """Sets up a Monitored or Hooked Session.

    Args:
      session_creator: A factory object to create session. Typically a
        `ChiefSessionCreator` or a `WorkerSessionCreator`.
      hooks: An iterable of `SessionRunHook' objects.
      should_recover: A bool. Indicates whether to recover from `AbortedError`
        and `UnavailableError` or not.
      stop_grace_period_secs: Number of seconds given to threads to stop after
        `close()` has been called.
    """
    @property
    def graph(self):
        """The graph that was launched in this session."""
    def run(self, fetches, feed_dict: Incomplete | None = None, options: Incomplete | None = None, run_metadata: Incomplete | None = None):
        """Run ops in the monitored session.

    This method is completely compatible with the `tf.Session.run()` method.

    Args:
      fetches: Same as `tf.Session.run()`.
      feed_dict: Same as `tf.Session.run()`.
      options: Same as `tf.Session.run()`.
      run_metadata: Same as `tf.Session.run()`.

    Returns:
      Same as `tf.Session.run()`.
    """
    def run_step_fn(self, step_fn):
        """Run ops using a step function.

    Args:
      step_fn: A function or a method with a single argument of type
        `StepContext`.  The function may use methods of the argument to perform
        computations with access to a raw session.  The returned value of the
        `step_fn` will be returned from `run_step_fn`, unless a stop is
        requested.  In that case, the next `should_stop` call will return True.
        Example usage:
            ```python
            with tf.Graph().as_default():
              c = tf.compat.v1.placeholder(dtypes.float32)
              v = tf.add(c, 4.0)
              w = tf.add(c, 0.5)
              def step_fn(step_context):
                a = step_context.session.run(fetches=v, feed_dict={c: 0.5})
                if a <= 4.5:
                  step_context.request_stop()
                  return step_context.run_with_hooks(fetches=w,
                                                     feed_dict={c: 0.1})

              with tf.MonitoredSession() as session:
                while not session.should_stop():
                  a = session.run_step_fn(step_fn)
            ```
            Hooks interact with the `run_with_hooks()` call inside the
                 `step_fn` as they do with a `MonitoredSession.run` call.

    Returns:
      Returns the returned value of `step_fn`.

    Raises:
      StopIteration: if `step_fn` has called `request_stop()`.  It may be
        caught by `with tf.MonitoredSession()` to close the session.
      ValueError: if `step_fn` doesn't have a single argument called
        `step_context`. It may also optionally have `self` for cases when it
        belongs to an object.
    """
    class StepContext:
        """Control flow instrument for the `step_fn` from `run_step_fn()`.

       Users of `step_fn` may perform `run()` calls without running hooks
       by accessing the `session`.  A `run()` call with hooks may be performed
       using `run_with_hooks()`.  Computation flow can be interrupted using
       `request_stop()`.
    """
        def __init__(self, session, run_with_hooks_fn) -> None:
            """Initializes the `step_context` argument for a `step_fn` invocation.

      Args:
        session: An instance of `tf.compat.v1.Session`.
        run_with_hooks_fn: A function for running fetches and hooks.
      """
        @property
        def session(self): ...
        def run_with_hooks(self, *args, **kwargs):
            """Same as `MonitoredSession.run`. Accepts the same arguments."""
        def request_stop(self) -> None:
            """Exit the training loop by causing `should_stop()` to return `True`.

         Causes `step_fn` to exit by raising an exception.

      Raises:
        StopIteration
      """
    def should_stop(self): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exception_type, exception_value, traceback): ...
    class _CoordinatedSessionCreator(SessionCreator):
        """Factory for _CoordinatedSession."""
        coord: Incomplete
        tf_sess: Incomplete
        def __init__(self, session_creator, hooks, stop_grace_period_secs) -> None: ...
        def create_session(self):
            """Creates a coordinated session."""

class MonitoredSession(_MonitoredSession):
    """Session-like object that handles initialization, recovery and hooks.

  Example usage:

  ```python
  saver_hook = CheckpointSaverHook(...)
  summary_hook = SummarySaverHook(...)
  with MonitoredSession(session_creator=ChiefSessionCreator(...),
                        hooks=[saver_hook, summary_hook]) as sess:
    while not sess.should_stop():
      sess.run(train_op)
  ```

  Initialization: At creation time the monitored session does following things
  in given order:

  * calls `hook.begin()` for each given hook
  * finalizes the graph via `scaffold.finalize()`
  * create session
  * initializes the model via initialization ops provided by `Scaffold`
  * restores variables if a checkpoint exists
  * launches queue runners
  * calls `hook.after_create_session()`

  Run: When `run()` is called, the monitored session does following things:

  * calls `hook.before_run()`
  * calls TensorFlow `session.run()` with merged fetches and feed_dict
  * calls `hook.after_run()`
  * returns result of `session.run()` asked by user
  * if `AbortedError` or `UnavailableError` occurs, it recovers or
    reinitializes the session before executing the run() call again


  Exit: At the `close()`, the monitored session does following things in order:

  * calls `hook.end()`
  * closes the queue runners and the session
  * suppresses `OutOfRange` error which indicates that all inputs have been
    processed if the monitored_session is used as a context

  How to set `tf.compat.v1.Session` arguments:

  * In most cases you can set session arguments as follows:

  ```python
  MonitoredSession(
    session_creator=ChiefSessionCreator(master=..., config=...))
  ```

  * In distributed setting for a non-chief worker, you can use following:

  ```python
  MonitoredSession(
    session_creator=WorkerSessionCreator(master=..., config=...))
  ```

  See `MonitoredTrainingSession` for an example usage based on chief or worker.

  Note: This is not a `tf.compat.v1.Session`. For example, it cannot do
  following:

  * it cannot be set as default session.
  * it cannot be sent to saver.save.
  * it cannot be sent to tf.train.start_queue_runners.

  @compatibility(TF2)
  This API is not compatible with eager execution and `tf.function`. To migrate
  to TF2, rewrite the code to be compatible with eager execution. Check the
  [migration
  guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
  on replacing `Session.run` calls. In Keras, session hooks can be replaced by
  Callbacks e.g. [logging hook notebook](
  https://github.com/tensorflow/docs/blob/master/site/en/guide/migrate/logging_stop_hook.ipynb)
  For more details please read [Better
  performance with tf.function](https://www.tensorflow.org/guide/function).
  @end_compatibility

  Args:
    session_creator: A factory object to create session. Typically a
      `ChiefSessionCreator` which is the default one.
    hooks: An iterable of `SessionRunHook' objects.

  Returns:
    A MonitoredSession object.
  """
    def __init__(self, session_creator: Incomplete | None = None, hooks: Incomplete | None = None, stop_grace_period_secs: int = 120) -> None: ...

class SingularMonitoredSession(_MonitoredSession):
    """Session-like object that handles initialization, restoring, and hooks.

  Please note that this utility is not recommended for distributed settings.
  For distributed settings, please use `tf.compat.v1.train.MonitoredSession`.
  The
  differences between `MonitoredSession` and `SingularMonitoredSession` are:

  * `MonitoredSession` handles `AbortedError` and `UnavailableError` for
    distributed settings, but `SingularMonitoredSession` does not.
  * `MonitoredSession` can be created in `chief` or `worker` modes.
    `SingularMonitoredSession` is always created as `chief`.
  * You can access the raw `tf.compat.v1.Session` object used by
    `SingularMonitoredSession`, whereas in MonitoredSession the raw session is
    private. This can be used:
      - To `run` without hooks.
      - To save and restore.
  * All other functionality is identical.

  Example usage:
  ```python
  saver_hook = CheckpointSaverHook(...)
  summary_hook = SummarySaverHook(...)
  with SingularMonitoredSession(hooks=[saver_hook, summary_hook]) as sess:
    while not sess.should_stop():
      sess.run(train_op)
  ```

  Initialization: At creation time the hooked session does following things
  in given order:

  * calls `hook.begin()` for each given hook
  * finalizes the graph via `scaffold.finalize()`
  * create session
  * initializes the model via initialization ops provided by `Scaffold`
  * restores variables if a checkpoint exists
  * launches queue runners

  Run: When `run()` is called, the hooked session does following things:

  * calls `hook.before_run()`
  * calls TensorFlow `session.run()` with merged fetches and feed_dict
  * calls `hook.after_run()`
  * returns result of `session.run()` asked by user

  Exit: At the `close()`, the hooked session does following things in order:

  * calls `hook.end()`
  * closes the queue runners and the session
  * suppresses `OutOfRange` error which indicates that all inputs have been
    processed if the `SingularMonitoredSession` is used as a context.

  @compatibility(TF2)
  This API is not compatible with eager execution and `tf.function`. To migrate
  to TF2, rewrite the code to be compatible with eager execution. Check the
  [migration
  guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
  on replacing `Session.run` calls. In Keras, session hooks can be replaced by
  Callbacks e.g. [logging hook notebook](
  https://github.com/tensorflow/docs/blob/master/site/en/guide/migrate/logging_stop_hook.ipynb)
  For more details please read [Better
  performance with tf.function](https://www.tensorflow.org/guide/function).
  @end_compatibility
  """
    def __init__(self, hooks: Incomplete | None = None, scaffold: Incomplete | None = None, master: str = '', config: Incomplete | None = None, checkpoint_dir: Incomplete | None = None, stop_grace_period_secs: int = 120, checkpoint_filename_with_path: Incomplete | None = None) -> None:
        """Creates a SingularMonitoredSession.

    Args:
      hooks: An iterable of `SessionRunHook' objects.
      scaffold: A `Scaffold` used for gathering or building supportive ops. If
        not specified a default one is created. It's used to finalize the graph.
      master: `String` representation of the TensorFlow master to use.
      config: `ConfigProto` proto used to configure the session.
      checkpoint_dir: A string.  Optional path to a directory where to restore
        variables.
      stop_grace_period_secs: Number of seconds given to threads to stop after
        `close()` has been called.
      checkpoint_filename_with_path: A string. Optional path to a checkpoint
        file from which to restore variables.
    """
    def raw_session(self):
        """Returns underlying `TensorFlow.Session` object."""

class _WrappedSession:
    """Wrapper around a `tf.compat.v1.Session`.

  This wrapper is used as a base class for various session wrappers
  that provide additional functionality such as monitoring, coordination,
  and recovery.

  In addition to the methods exported by `SessionInterface` the wrapper
  provides a method to check for stop and never raises exceptions from
  calls to `close()`.
  """
    def __init__(self, sess) -> None:
        """Creates a `_WrappedSession`.

    Args:
      sess: A `tf.compat.v1.Session` or `_WrappedSession` object.  The wrapped
        session.
    """
    @property
    def graph(self): ...
    @property
    def sess_str(self): ...
    def should_stop(self):
        """Return true if this session should not be used anymore.

    Always return True if the session was closed.

    Returns:
      True if the session should stop, False otherwise.
    """
    def close(self) -> None: ...
    def run(self, *args, **kwargs): ...
    def run_step_fn(self, step_fn, raw_session, run_with_hooks): ...

class _RecoverableSession(_WrappedSession):
    """A wrapped session that recreates a session upon certain kinds of errors.

  The constructor is passed a SessionCreator object, not a session.

  Calls to `run()` are delegated to the wrapped session.  If a call raises the
  exception `tf.errors.AbortedError` or `tf.errors.UnavailableError`, the
  wrapped session is closed, and a new one is created by calling the factory
  again.
  """
    def __init__(self, sess_creator) -> None:
        """Create a new `_RecoverableSession`.

    The value returned by calling `sess_creator.create_session()` will be the
    session wrapped by this recoverable session.

    Args:
      sess_creator: A 'SessionCreator' to be wrapped by recoverable.
    """
    def run(self, fetches, feed_dict: Incomplete | None = None, options: Incomplete | None = None, run_metadata: Incomplete | None = None): ...
    def run_step_fn(self, step_fn, raw_session, run_with_hooks): ...

class _CoordinatedSession(_WrappedSession):
    """A wrapped session that works with a `tf.Coordinator`.

  Calls to `run()` are delegated to the wrapped session.  If a call
  raises an exception, the exception is reported to the coordinator.

  In addition, after each call to `run()` this session ask the coordinator if
  the session should stop.  In that case it will join all the threads
  registered with the coordinator before returning.

  If the coordinator was requested to stop with an exception, that exception
  will be re-raised from the call to `run()`.
  """
    def __init__(self, sess, coord, stop_grace_period_secs: int = 120) -> None:
        """Create a new `_CoordinatedSession`.

    Args:
      sess: A `tf.compat.v1.Session` object.  The wrapped session.
      coord: A `tf.train.Coordinator` object.
      stop_grace_period_secs: Number of seconds given to threads to stop after
        `close()` has been called.
    """
    def close(self) -> None: ...
    def run(self, *args, **kwargs): ...

class _HookedSession(_WrappedSession):
    """A _WrappedSession that calls hooks during calls to run().

  The list of hooks to call is passed in the constructor.  Before each call
  to `run()` the session calls the `before_run()` method of the hooks, which
  can return additional ops or tensors to run.  These are added to the arguments
  of the call to `run()`.

  When the `run()` call finishes, the session calls the `after_run()` methods of
  the hooks, passing the values returned by the `run()` call corresponding to
  the ops and tensors that each hook requested.

  If any call to the hooks, requests stop via run_context the session will be
  marked as needing to stop and its `should_stop()` method will now return
  `True`.
  """
    def __init__(self, sess, hooks) -> None:
        """Initializes a _HookedSession object.

    Args:
      sess: A `tf.compat.v1.Session` or a `_WrappedSession` object.
      hooks: An iterable of `SessionRunHook' objects.
    """
    def run(self, fetches, feed_dict: Incomplete | None = None, options: Incomplete | None = None, run_metadata: Incomplete | None = None):
        """See base class."""
