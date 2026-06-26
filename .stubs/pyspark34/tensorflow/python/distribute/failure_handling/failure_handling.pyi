from _typeshed import Incomplete
from tensorflow.core.distributed_runtime.preemption import gen_check_preemption_op as gen_check_preemption_op
from tensorflow.python.checkpoint import checkpoint_management as checkpoint_management
from tensorflow.python.distribute import distribute_lib as distribute_lib, multi_worker_util as multi_worker_util
from tensorflow.python.distribute.failure_handling import failure_handling_util as failure_handling_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors as errors
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util import tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import tf_export as tf_export

PREEMPTION_KEY: str

class TerminationConfig:
    """Customization of `PreemptionCheckpointHandler` for various platforms.

  A `TerminationConfig` can be created and passed to a
  `tf.distribute.experimental.PreemptionCheckpointHandler` to provide
  customization based on the platform. It can deliver three pieces of
  information:

  * How to decide if there is a termination event soon

  The form of termination notification and how to fetch it vary across
  platforms. Thus `PreemptionCheckpointHandler` may take a user-defined
  function, `termination_watcher_fn`, and execute it repeatedly to check for
  termination notification. `termination_watcher_fn` should be a function
  that returns `True` if a termination notification is available and
  `False` otherwise. The function should be lightweight and non-blocking so that
  resources can be cleaned up properly if no termination signal is ever raised
  until training finishes.

  * How to exit the program

  A user can configure this through the `exit_fn`, which
  `PreemptionCheckpointHandler` executes after saving the checkpoint to exit the
  training program gracefully. For `tf.distribute.MultiWorkerMirroredStrategy`,
  a restart is necessary to reset the program's state. However, having a
  customized `exit_fn` may facilitate the restart and smoothen the training
  experience. How so? Maybe the platform has an agreement to a `RESTART_CODE`
  recognized as a program auto-restart signal, or maybe the user has a
  coordinating script that starts up the training, in which they can configure
  the program to auto-restart if it ever exits with this `RESTART_CODE`. In both
  cases, configuring the `exit_fn` to be `sys.exit(RESTART_CODE)` makes the
  training seamless.

  * How long does `PreemptionCheckpointHandler` have from receiving a
  termination event notice till the actual termination

  Some platforms have a gap time as long as one hour or so. In these cases,
  there is the option to utilize this gap time for training as much as possible
  before saving a checkpoint and exiting. This can be achieved by passing the
  `grace_period` argument a nonzero value. Note, for a user with a grace period
  that is not multiple times longer than their checkpoint writing time (e.g.,
  three times or more), we advise not to configure this argument, in which case
  `PreemptionCheckpointHandler` will directly save a checkpoint and exit.


  **The default behavior**:

  * For Google Borg Platform:
      * Automatically know how to detect preemption signal
      * Exit with a platform-recognized restart code
      * Save a checkpoint and exit immediately

  * For Google Cloud Platform:
      * Automatically know how to detect maintenance signal.
      * Exit with a code (User may configure this)
      * Automatically utilized the extended training period before save and exit

  * For Other platform:
      * If `termination_watcher_fn` is `None`, we will treat `signal.SIGTERM` as
      a termination signal.
      * If `exit_fn` is not configured, we exit the program with an arbitrary
      code.
      * If `grace_period` is not configured, we will wrap up the current
      training step, save a checkpoint, and exit the program as soon as we
      receive the termination signal.
  """
    termination_watcher_fn: Incomplete
    exit_fn: Incomplete
    grace_period: Incomplete
    save_fn: Incomplete
    def __init__(self, termination_watcher_fn: Incomplete | None = None, exit_fn: Incomplete | None = None, grace_period: Incomplete | None = None, save_fn: Incomplete | None = None) -> None:
        """Creates a `TerminationConfig` object.

    Args:
      termination_watcher_fn: a function to execute repeatedly that returns
        `True` if a preemption signal is available and False otherwise. The
        function cannot block until a preemption signal is available, which
        prevents proper cleanup of the program. A change is **NOT** recommended
        for users on Google Borg or Google Cloud Platform.
      exit_fn: a function to execute after a checkpoint is saved and before the
        preemption happens. Usually, it should be in the form of
        `lambda: sys.exit(RESTART_CODE)`, where `RESTART_CODE` varies by
        platform. A change is **NOT** recommended for users on Google Borg.
        Users on Google Cloud Platform may configure it to use a customized
        `RESTART_CODE`.
      grace_period: the length of time between receiving a preemption signal and
        the actual preemption. A change is **NOT** recommended for users on
        Google Borg, Google Cloud Platform, or users with a short grace period.
      save_fn: an optional function letting you configure how to save a
        checkpoint. This is useful if you'd like to pass extra argument to
        `tf.train.CheckpointManager.save` or `tf.train.Checkpoint.save`. By
        default, if not configured, the API will save checkpoint without extra
        arguments.
    """

class GcpGpuTerminationConfig(TerminationConfig):
    """Configurations for GCP GPU VM."""
    termination_watcher_fn: Incomplete
    exit_fn: Incomplete
    grace_period: Incomplete
    save_fn: Incomplete
    def __init__(self, termination_watcher_fn: Incomplete | None = None, exit_fn: Incomplete | None = None, grace_period: Incomplete | None = None, save_fn: Incomplete | None = None) -> None: ...

class GcpCpuTerminationConfig(TerminationConfig):
    """Configurations for GCP CPU VM."""
    termination_watcher_fn: Incomplete
    exit_fn: Incomplete
    grace_period: Incomplete
    save_fn: Incomplete
    def __init__(self, termination_watcher_fn: Incomplete | None = None, exit_fn: Incomplete | None = None, grace_period: Incomplete | None = None, save_fn: Incomplete | None = None) -> None: ...

class BorgTerminationConfig(TerminationConfig):
    """Configurations for Borg."""
    termination_watcher_fn: Incomplete
    exit_fn: Incomplete
    grace_period: Incomplete
    save_fn: Incomplete
    def __init__(self, termination_watcher_fn: Incomplete | None = None, exit_fn: Incomplete | None = None, grace_period: Incomplete | None = None, save_fn: Incomplete | None = None) -> None: ...

class BorgTPUTerminationConfig(TerminationConfig):
    """Configurations for Borg."""
    termination_watcher_fn: Incomplete
    exit_fn: Incomplete
    grace_period: Incomplete
    save_fn: Incomplete
    def __init__(self, termination_watcher_fn: Incomplete | None = None, exit_fn: Incomplete | None = None, grace_period: Incomplete | None = None, save_fn: Incomplete | None = None) -> None: ...

class PreemptionCheckpointHandler:
    """Preemption and error handler for synchronous training.

  Note: This API only supports use with
  `tf.distribute.MultiWorkerMirroredStrategy` for now.

  A `PreemptionCheckpointHandler` coordinates all workers to save a checkpoint
  upon receiving a preemption signal. It also helps disseminate application
  error messages accurately among the cluster. When a
  `PreemptionCheckpointHandler` object is created, it restores values from
  the latest checkpoint file if any exists.

  Right after the initialization, a thread starts to watch out for a termination
  signal for any member in the cluster. If receiving a signal, the next time the
  worker enters a `PreemptionCheckpointHandler.run` call, the
  `PreemptionCheckpointHandler` will align the worker steps to save a checkpoint
  and maybe exit -- depending on the `exit_fn` in
  `tf.distribute.experimental.TerminationConfig`.

  Note: by default, the program exits after saving a checkpoint. Users of
  `tf.distribute.MultiWorkerMirroredStrategy` who choose to configure their own
  `exit_fn` in `tf.distribute.experimental.TerminationConfig` must include a
  `sys.exit(CODE_OR_MESSAGE)` in the `exit_fn` to guarantee that after the
  restart, the workers can initialize communication services correctly.

  Example usage:
  ```python
  strategy = tf.distribute.MultiWorkerMirroredStrategy()

  with strategy.scope():
    dataset, model, optimizer = ...

    checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)

    preemption_handler = tf.distribute.experimental.PreemptionCheckpointHandler(cluster_resolver, checkpoint, checkpoint_directory)

    # preemption_handler.total_run_calls will be restored to its saved value if
    # training is restored after interruption.
    for epoch in range(preemption_handler.total_run_calls // STEPS_PER_EPOCH, num_epochs):
      for step in range(preemption_handler.total_run_calls % STEPS_PER_EPOCH, STEPS_PER_EPOCH):
        # distributed_train_step is a single-step training function wrapped by tf.distribute.Strategy.run.
        loss += preemption_handler.run(distributed_train_step, args=(next(dataset),))
  ```

  Not all interruptions come with advance notice so that the
  `PreemptionCheckpointHandler` can handle them, e.g., those caused by hardware
  failure. For a user who saves checkpoints for these cases themselves outside
  the `PreemptionCheckpointHandler`, if they are using a
  `tf.train.CheckpointManager`, pass it as the
  `checkpoint_or_checkpoint_manager` argument to the
  `PreemptionCheckpointHandler`. If they do not have a
  `tf.train.CheckpointManager` but are directly working with
  `tf.train.Checkpoint`, we advise saving the checkpoints in the directory
  that's passed as the `checkpoint_dir` argument. In this way, at the program
  beginning, `PreemptionCheckpointHandler` can restore the latest checkpoint
  from the directory, no matter it's saved by the user themselves or saved by
  the `PreemptionCheckpointHandler` before preemption happens.

  If a user cannot infer the start epoch and start step from
  `PreemptionCheckpointHandler.total_run_calls` (e.g., if there is no preknown
  `STEPS_PER_EPOCH` or if their `STEPS_PER_EPOCH` may vary from epoch to epoch),
  we recommend tracking the epoch and step numbers themselves and save them in
  the passed-in checkpoint:

  ```python
  strategy = tf.distribute.MultiWorkerMirroredStrategy()

  trained_epoch = tf.Variable(initial_value=tf.constant(0, dtype=tf.dtypes.int64), name='epoch')
  step_in_epoch = tf.Variable(initial_value=tf.constant(0, dtype=tf.dtypes.int64), name='step_in_epoch')

  with strategy.scope():
    dataset, model, optimizer = ...

    checkpoint = tf.train.Checkpoint(optimizer=optimizer,
                                     model=model,
                                     trained_epoch=trained_epoch,
                                     step_in_epoch=step_in_epoch)

    preemption_handler = tf.distribute.experimental.PreemptionCheckpointHandler(cluster_resolver, checkpoint, checkpoint_dir)

  while trained_epoch.numpy() < NUM_EPOCH:

    while step_in_epoch.numpy() < STEPS_PER_EPOCH:

      loss += failure_handler.run(train_step, args=(next(iterator),))
      step_in_epoch.assign_add(1)
      ...

    epoch.assign_add(1)
    step_in_epoch.assign(0)
  ```

  **A note on the platform:**

  `PreemptionCheckpointHandler` can only handle the kind of termination with
  advance notice. For now, the API recognizes the Google Borg and the Google
  Cloud Platform, where it can automatically adopt the correct
  preemption/maintenance notification detection mechanism. Users of other
  platforms can configure it through a
  `tf.distribute.experimental.TerminationConfig`. Customization for the exit
  behavior and grace period length could also be done here.
  """
    def __init__(self, cluster_resolver, checkpoint_or_checkpoint_manager, checkpoint_dir: Incomplete | None = None, termination_config: Incomplete | None = None) -> None:
        """Creates the `PreemptionCheckpointHandler`.

    Args:
      cluster_resolver: a `tf.distribute.cluster_resolver.ClusterResolver`
        object. You may also obtain it through the `cluster_resolver` attribute
        of the distribution strategy in use.
      checkpoint_or_checkpoint_manager: a `tf.train.CheckpointManager` or a
        `tf.train.Checkpoint`. If you are using a `tf.train.CheckpointManager`
        to manage checkpoints outside the `PreemptionCheckpointHandler` for
        backup purpose as well, pass it as `checkpoint_or_checkpoint_manager`
        argument. Otherwise, pass a `tf.train.Checkpoint` and the
        `PreemptionCheckpointHandler` will create
        a `tf.train.CheckpointManager` to manage it in the `checkpoint_dir`.
      checkpoint_dir: a directory where the `PreemptionCheckpointHandler` saves
        and restores checkpoints. When a `PreemptionCheckpointHandler` is
        created, the latest checkpoint in the `checkpoint_dir` will be restored.
        (This is not needed if a `tf.train.CheckpointManager` instead of a
        `tf.train.Checkpoint` is passed as the
        `checkpoint_or_checkpoint_manager` argument.)
      termination_config: optional, a
        `tf.distribute.experimental.TerminationConfig` object to configure for a
        platform other than Google Borg or GCP.
    """
    def __del__(self) -> None: ...
    @property
    def total_run_calls(self):
        """Returns the number of times `PreemptionCheckpointHandler.run` is called.

    This value tracks the number of all calls to
    `PreemptionCheckpointHandler.run` including those before the program is
    restarted and the training is restored, by saving and reading the value in
    the checkpoint. A user can compute their total number of iterations
    by `PreemptionCheckpointHandler.total_run_calls *
    number_of_steps_in_train_function`,
    while `number_of_steps_in_train_function` should be one for
    `tf.distribute.MultiWorkerMirroredStrategy` users. They can also use this
    value to infer the starting epoch and step after training restores, as shown
    in the example above.
    """
    def run(self, distributed_train_function, *args, **kwargs):
        """Runs a training function with error and preemption handling.

    This function handles the preemption signal from any peer in the cluster by
    saving the training progress and exiting gracefully. It will
    also broadcase any program error encountered during the execution of
    `distributed_train_function` to all workers so that they can raise the same
    error.

    The `distributed_train_function` argument should be a distributed train
    function (i.e., containing a call to `tf.distribute.Strategy.run`). For
    `tf.distribute.MultiWorkerMirroredStrategy` users, we recommend passing in a
    single-step `distributed_train_function` to
    `PreemptionCheckpointHandler.run` so that the checkpoint can be saved in
    time in case a preemption signal or maintenance notice is sent.

    Besides the preemption and error handling part,
    `PreemptionCheckpointHandler.run(distributed_train_function, *args,
    **kwargs)` has the same effect and output as
    `distributed_train_function(*args, **kwargs)`. `distributed_train_function`
    can return either some or no result. The following is a shortened example:

    ```python

    @tf.function
    def distributed_train_step(iterator):
      # A distributed single-step training function.

      def step_fn(inputs):
        # A per-replica single-step training function.
        x, y = inputs
        ...
        return loss

      per_replica_losses = strategy.run(step_fn, args=(next(iterator),))
      return strategy.reduce(
          tf.distribute.ReduceOp.SUM, per_replica_losses, axis=None)

    for epoch in range(preemption_handler.total_run_calls // STEPS_PER_EPOCH,
                       EPOCHS_TO_RUN):
      iterator = iter(multi_worker_dataset)
      total_loss = 0.0
      num_batches = 0

      for step in range(preemption_handler.total_run_calls % STEPS_PER_EPOCH,
                        STEPS_PER_EPOCH):
        total_loss += preemption_handler.run(distributed_train_step)
        num_batches += 1

      train_loss = total_loss / num_batches
      print('Epoch: %d, train_loss: %f.' %(epoch.numpy(), train_loss))

      train_accuracy.reset_states()
    ```

    Args:
      distributed_train_function: A (single-step) distributed training function.
      *args: args for `distributed_train_function`.
      **kwargs: kwargs for `distributed_train_function`.

    Raises:
      Program error encountered by any member in the cluster while executing the
      `distributed_train_function`, or any error from the program error
      propagation process.

    Returns:
      Result of running the `distributed_train_function`.
    """
WorkerPreemptionHandler = PreemptionCheckpointHandler
