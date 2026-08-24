from _typeshed import Incomplete
from tensorflow.core.framework.summary_pb2 import Summary as Summary
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.core.util.event_pb2 import SessionLog as SessionLog
from tensorflow.python.client import timeline as timeline
from tensorflow.python.framework import dtypes as dtypes, errors as errors, meta_graph as meta_graph, ops as ops
from tensorflow.python.ops import init_ops as init_ops, variable_scope as variable_scope
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.training import session_run_hook as session_run_hook, training_util as training_util
from tensorflow.python.training.session_run_hook import SessionRunArgs as SessionRunArgs
from tensorflow.python.training.summary_io import SummaryWriterCache as SummaryWriterCache
from tensorflow.python.util.tf_export import tf_export as tf_export

class _HookTimer:
    """Base timer for determining when Hooks should trigger.

  Should not be instantiated directly.
  """
    def __init__(self) -> None: ...
    def reset(self) -> None:
        """Resets the timer."""
    def should_trigger_for_step(self, step) -> None:
        """Return true if the timer should trigger for the specified step."""
    def update_last_triggered_step(self, step) -> None:
        """Update the last triggered time and step number.

    Args:
      step: The current step.

    Returns:
      A pair `(elapsed_time, elapsed_steps)`, where `elapsed_time` is the number
      of seconds between the current trigger and the last one (a float), and
      `elapsed_steps` is the number of steps between the current trigger and
      the last one. Both values will be set to `None` on the first trigger.
    """
    def last_triggered_step(self) -> None:
        """Returns the last triggered time step or None if never triggered."""

class SecondOrStepTimer(_HookTimer):
    """Timer that triggers at most once every N seconds or once every N steps.

  This symbol is also exported to v2 in tf.estimator namespace. See
  https://github.com/tensorflow/estimator/blob/master/tensorflow_estimator/python/estimator/hooks/basic_session_run_hooks.py
  """
    def __init__(self, every_secs: Incomplete | None = None, every_steps: Incomplete | None = None) -> None: ...
    def reset(self) -> None: ...
    def should_trigger_for_step(self, step):
        """Return true if the timer should trigger for the specified step.

    Args:
      step: Training step to trigger on.

    Returns:
      True if the difference between the current time and the time of the last
      trigger exceeds `every_secs`, or if the difference between the current
      step and the last triggered step exceeds `every_steps`. False otherwise.
    """
    def update_last_triggered_step(self, step): ...
    def last_triggered_step(self): ...

class NeverTriggerTimer(_HookTimer):
    """Timer that never triggers."""
    def should_trigger_for_step(self, step): ...
    def update_last_triggered_step(self, step): ...
    def last_triggered_step(self) -> None: ...

class LoggingTensorHook(session_run_hook.SessionRunHook):
    """Prints the given tensors every N local steps, every N seconds, or at end.

  The tensors will be printed to the log, with `INFO` severity. If you are not
  seeing the logs, you might want to add the following line after your imports:

  ```python
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)
  ```

  Note that if `at_end` is True, `tensors` should not include any tensor
  whose evaluation produces a side effect such as consuming additional inputs.

  @compatibility(TF2)
  Please check this [notebook][notebook] on how to migrate the API to TF2.

  [notebook]:https://github.com/tensorflow/docs/blob/master/site/en/guide/migrate/logging_stop_hook.ipynb

  @end_compatibility

  """
    def __init__(self, tensors, every_n_iter: Incomplete | None = None, every_n_secs: Incomplete | None = None, at_end: bool = False, formatter: Incomplete | None = None) -> None:
        """Initializes a `LoggingTensorHook`.

    Args:
      tensors: `dict` that maps string-valued tags to tensors/tensor names, or
        `iterable` of tensors/tensor names.
      every_n_iter: `int`, print the values of `tensors` once every N local
        steps taken on the current worker.
      every_n_secs: `int` or `float`, print the values of `tensors` once every N
        seconds. Exactly one of `every_n_iter` and `every_n_secs` should be
        provided.
      at_end: `bool` specifying whether to print the values of `tensors` at the
        end of the run.
      formatter: function, takes dict of `tag`->`Tensor` and returns a string.
        If `None` uses default printing all tensors.

    Raises:
      ValueError: if `every_n_iter` is non-positive.
    """
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...
    def end(self, session) -> None: ...

def get_or_create_steps_per_run_variable():
    """Gets or creates the steps_per_run variable.

  In Estimator, the user provided computation, the model_fn, is wrapped
  inside a tf.while_loop for peak performance. The iterations of the loop are
  specified by this variable, which adjusts its value on the CPU after each
  device program execution and before the next execution.

  The purpose of using a variable, rather than a constant, is to allow
  Estimator adapt the device training iterations according to the final steps
  specified by users. For example, if the user sets the steps_per_run as
  4 and steps as 10 in Estimator.train(), the steps_per_run
  variable will have the following value before each training run.

      - 1-st execution: steps_per_run = 4
      - 2-nd execution: steps_per_run = 4
      - 3-rd execution: steps_per_run = 2

  As model_fn increases the global step once per train_op invocation, the global
  step is 10 after all executions, matching the steps=10 inputs passed in by
  users.

  Returns:
    A TF non-trainable resource variable.

  Raises:
    RuntimeError: If multi steps_per_run variables were found.
  """

class _MultiStepStopAtStepHook(session_run_hook.SessionRunHook):
    """Hook that requests stop at a specified step."""
    def __init__(self, num_steps: Incomplete | None = None, last_step: Incomplete | None = None, steps_per_run: int = 1) -> None:
        """Initializes a `MultiStepStopAtStepHook`.

    This hook requests stop after either a number of steps have been
    executed or a last step has been reached. Only one of the two options can be
    specified.

    if `num_steps` is specified, it indicates the number of steps to execute
    after `begin()` is called. If instead `last_step` is specified, it
    indicates the last step we want to execute, as passed to the `after_run()`
    call.

    In Estimator, the user provided computation, the model_fn, is wrapped
    inside a tf.while_loop for peak performance. The steps_per_run variable
    determines the number of iterations of the loop before returning to the CPU.

    Args:
      num_steps: Number of steps to execute.
      last_step: Step after which to stop.
      steps_per_run: Number of steps executed per run call.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def after_run(self, run_context, run_values) -> None: ...

class StopAtStepHook(session_run_hook.SessionRunHook):
    """Hook that requests stop at a specified step.

  @compatibility(TF2)
  Please check this [notebook][notebook] on how to migrate the API to TF2.

  [notebook]:https://github.com/tensorflow/docs/blob/master/site/en/guide/migrate/logging_stop_hook.ipynb

  @end_compatibility
  """
    def __init__(self, num_steps: Incomplete | None = None, last_step: Incomplete | None = None) -> None:
        """Initializes a `StopAtStepHook`.

    This hook requests stop after either a number of steps have been
    executed or a last step has been reached. Only one of the two options can be
    specified.

    if `num_steps` is specified, it indicates the number of steps to execute
    after `begin()` is called. If instead `last_step` is specified, it
    indicates the last step we want to execute, as passed to the `after_run()`
    call.

    Args:
      num_steps: Number of steps to execute.
      last_step: Step after which to stop.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class CheckpointSaverListener:
    """Interface for listeners that take action before or after checkpoint save.

  `CheckpointSaverListener` triggers only in steps when `CheckpointSaverHook` is
  triggered, and provides callbacks at the following points:
   - before using the session
   - before each call to `Saver.save()`
   - after each call to `Saver.save()`
   - at the end of session

  To use a listener, implement a class and pass the listener to a
  `CheckpointSaverHook`, as in this example:

  ```python
  class ExampleCheckpointSaverListener(CheckpointSaverListener):
    def begin(self):
      # You can add ops to the graph here.
      print('Starting the session.')
      self.your_tensor = ...

    def before_save(self, session, global_step_value):
      print('About to write a checkpoint')

    def after_save(self, session, global_step_value):
      print('Done writing checkpoint.')
      if decided_to_stop_training():
        return True

    def end(self, session, global_step_value):
      print('Done with the session.')

  ...
  listener = ExampleCheckpointSaverListener()
  saver_hook = tf.estimator.CheckpointSaverHook(
      checkpoint_dir, listeners=[listener])
  with
  tf.compat.v1.train.MonitoredTrainingSession(chief_only_hooks=[saver_hook]):
    ...
  ```

  A `CheckpointSaverListener` may simply take some action after every
  checkpoint save. It is also possible for the listener to use its own schedule
  to act less frequently, e.g. based on global_step_value. In this case,
  implementors should implement the `end()` method to handle actions related to
  the last checkpoint save. But the listener should not act twice if
  `after_save()` already handled this last checkpoint save.

  A `CheckpointSaverListener` can request training to be stopped, by returning
  True in `after_save`. Please note that, in replicated distributed training
  setting, only `chief` should use this behavior. Otherwise each worker will do
  their own evaluation, which may be wasteful of resources.
  """
    def begin(self) -> None: ...
    def before_save(self, session, global_step_value) -> None: ...
    def after_save(self, session, global_step_value) -> None: ...
    def end(self, session, global_step_value) -> None: ...

class CheckpointSaverHook(session_run_hook.SessionRunHook):
    """Saves checkpoints every N steps or seconds."""
    def __init__(self, checkpoint_dir, save_secs: Incomplete | None = None, save_steps: Incomplete | None = None, saver: Incomplete | None = None, checkpoint_basename: str = 'model.ckpt', scaffold: Incomplete | None = None, listeners: Incomplete | None = None, save_graph_def: bool = True) -> None:
        """Initializes a `CheckpointSaverHook`.

    Args:
      checkpoint_dir: `str`, base directory for the checkpoint files.
      save_secs: `int`, save every N secs.
      save_steps: `int`, save every N steps.
      saver: `Saver` object, used for saving.
      checkpoint_basename: `str`, base name for the checkpoint files.
      scaffold: `Scaffold`, use to get saver object.
      listeners: List of `CheckpointSaverListener` subclass instances. Used for
        callbacks that run immediately before or after this hook saves the
        checkpoint.
      save_graph_def: Whether to save the GraphDef and MetaGraphDef to
        `checkpoint_dir`. The GraphDef is saved after the session is created as
        `graph.pbtxt`. MetaGraphDefs are saved out for every checkpoint as
        `model.ckpt-*.meta`.

    Raises:
      ValueError: One of `save_steps` or `save_secs` should be set.
      ValueError: At most one of `saver` or `scaffold` should be set.
    """
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...
    def end(self, session) -> None: ...

class StepCounterHook(session_run_hook.SessionRunHook):
    """Hook that counts steps per second."""
    def __init__(self, every_n_steps: int = 100, every_n_secs: Incomplete | None = None, output_dir: Incomplete | None = None, summary_writer: Incomplete | None = None) -> None: ...
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class NanLossDuringTrainingError(RuntimeError): ...

class NanTensorHook(session_run_hook.SessionRunHook):
    """Monitors the loss tensor and stops training if loss is NaN.

  Can either fail with exception or just stop training.
  """
    def __init__(self, loss_tensor, fail_on_nan_loss: bool = True) -> None:
        """Initializes a `NanTensorHook`.

    Args:
      loss_tensor: `Tensor`, the loss tensor.
      fail_on_nan_loss: `bool`, whether to raise exception when loss is NaN.
    """
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class SummarySaverHook(session_run_hook.SessionRunHook):
    """Saves summaries every N steps."""
    def __init__(self, save_steps: Incomplete | None = None, save_secs: Incomplete | None = None, output_dir: Incomplete | None = None, summary_writer: Incomplete | None = None, scaffold: Incomplete | None = None, summary_op: Incomplete | None = None) -> None:
        """Initializes a `SummarySaverHook`.

    Args:
      save_steps: `int`, save summaries every N steps. Exactly one of
        `save_secs` and `save_steps` should be set.
      save_secs: `int`, save summaries every N seconds.
      output_dir: `string`, the directory to save the summaries to. Only used if
        no `summary_writer` is supplied.
      summary_writer: `SummaryWriter`. If `None` and an `output_dir` was passed,
        one will be created accordingly.
      scaffold: `Scaffold` to get summary_op if it's not provided.
      summary_op: `Tensor` of type `string` containing the serialized `Summary`
        protocol buffer or a list of `Tensor`. They are most likely an output by
        TF summary methods like `tf.compat.v1.summary.scalar` or
        `tf.compat.v1.summary.merge_all`. It can be passed in as one tensor; if
        more than one, they must be passed in as a list.

    Raises:
      ValueError: Exactly one of scaffold or summary_op should be set.
    """
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...
    def end(self, session: Incomplete | None = None) -> None: ...

class GlobalStepWaiterHook(session_run_hook.SessionRunHook):
    """Delays execution until global step reaches `wait_until_step`.

  This hook delays execution until global step reaches to `wait_until_step`. It
  is used to gradually start workers in distributed settings. One example usage
  would be setting `wait_until_step=int(K*log(task_id+1))` assuming that
  task_id=0 is the chief.
  """
    def __init__(self, wait_until_step) -> None:
        """Initializes a `GlobalStepWaiterHook`.

    Args:
      wait_until_step: an `int` shows until which global step should we wait.
    """
    def begin(self) -> None: ...
    def before_run(self, run_context) -> None: ...

class FinalOpsHook(session_run_hook.SessionRunHook):
    """A hook which evaluates `Tensors` at the end of a session."""
    def __init__(self, final_ops, final_ops_feed_dict: Incomplete | None = None) -> None:
        """Initializes `FinalOpHook` with ops to run at the end of the session.

    Args:
      final_ops: A single `Tensor`, a list of `Tensors` or a dictionary of names
        to `Tensors`.
      final_ops_feed_dict: A feed dictionary to use when running
        `final_ops_dict`.
    """
    @property
    def final_ops_values(self): ...
    def end(self, session) -> None: ...

class FeedFnHook(session_run_hook.SessionRunHook):
    """Runs `feed_fn` and sets the `feed_dict` accordingly."""
    feed_fn: Incomplete
    def __init__(self, feed_fn) -> None:
        """Initializes a `FeedFnHook`.

    Args:
      feed_fn: function that takes no arguments and returns `dict` of `Tensor`
        to feed.
    """
    def before_run(self, run_context): ...

class ProfilerHook(session_run_hook.SessionRunHook):
    '''Captures CPU/GPU profiling information every N steps or seconds.

  This produces files called "timeline-<step>.json", which are in Chrome
  Trace format.

  For more information see:
  https://github.com/catapult-project/catapult/blob/master/tracing/README.md
  '''
    def __init__(self, save_steps: Incomplete | None = None, save_secs: Incomplete | None = None, output_dir: str = '', show_dataflow: bool = True, show_memory: bool = False) -> None:
        """Initializes a hook that takes periodic profiling snapshots.

    `options.run_metadata` argument of `tf.Session.Run` is used to collect
    metadata about execution. This hook sets the metadata and dumps it in Chrome
    Trace format.


    Args:
      save_steps: `int`, save profile traces every N steps. Exactly one of
        `save_secs` and `save_steps` should be set.
      save_secs: `int` or `float`, save profile traces every N seconds.
      output_dir: `string`, the directory to save the profile traces to.
        Defaults to the current directory.
      show_dataflow: `bool`, if True, add flow events to the trace connecting
        producers and consumers of tensors.
      show_memory: `bool`, if True, add object snapshot events to the trace
        showing the sizes and lifetimes of tensors.
    """
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...
