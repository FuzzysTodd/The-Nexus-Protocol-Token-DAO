import tensorflow as tf
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export

class InMemoryEvaluatorHook(tf.compat.v1.train.SessionRunHook):
    """Hook to run evaluation in training without a checkpoint.

  Example:

  ```python
  def train_input_fn():
    ...
    return train_dataset

  def eval_input_fn():
    ...
    return eval_dataset

  estimator = tf.estimator.DNNClassifier(...)

  evaluator = tf.estimator.experimental.InMemoryEvaluatorHook(
      estimator, eval_input_fn)
  estimator.train(train_input_fn, hooks=[evaluator])
  ```

  Current limitations of this approach are:

  * It doesn't support multi-node distributed mode.
  * It doesn't support saveable objects other than variables (such as boosted
    tree support)
  * It doesn't support custom saver logic (such as ExponentialMovingAverage
    support)

  """
    def __init__(self, estimator, input_fn, steps: Incomplete | None = None, hooks: Incomplete | None = None, name: Incomplete | None = None, every_n_iter: int = 100) -> None:
        """Initializes a `InMemoryEvaluatorHook`.

    Args:
      estimator: A `tf.estimator.Estimator` instance to call evaluate.
      input_fn:  Equivalent to the `input_fn` arg to `estimator.evaluate`. A
        function that constructs the input data for evaluation. See [Creating
        input functions](
        https://tensorflow.org/guide/premade_estimators#create_input_functions)
          for more information. The function should construct and return one of
        the following:
          * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
            tuple (features, labels) with same constraints as below.
          * A tuple (features, labels): Where `features` is a `Tensor` or a
            dictionary of string feature name to `Tensor` and `labels` is a
            `Tensor` or a dictionary of string label name to `Tensor`. Both
            `features` and `labels` are consumed by `model_fn`. They should
            satisfy the expectation of `model_fn` from inputs.
      steps: Equivalent to the `steps` arg to `estimator.evaluate`.  Number of
        steps for which to evaluate model. If `None`, evaluates until `input_fn`
        raises an end-of-input exception.
      hooks: Equivalent to the `hooks` arg to `estimator.evaluate`. List of
        `SessionRunHook` subclass instances. Used for callbacks inside the
        evaluation call.
      name:  Equivalent to the `name` arg to `estimator.evaluate`. Name of the
        evaluation if user needs to run multiple evaluations on different data
        sets, such as on training data vs test data. Metrics for different
        evaluations are saved in separate folders, and appear separately in
        tensorboard.
      every_n_iter: `int`, runs the evaluator once every N training iteration.

    Raises:
      ValueError: if `every_n_iter` is non-positive or it's not a single machine
        training
    """
    def begin(self) -> None:
        """Build eval graph and restoring op."""
    def after_create_session(self, session, coord) -> None:
        """Does first run which shows the eval metrics before training."""
    def after_run(self, run_context, run_values) -> None:
        """Runs evaluator."""
    def end(self, session) -> None:
        """Runs evaluator for final model."""

class _StopAtCheckpointStepHook(tf.compat.v1.train.SessionRunHook):
    """Hook that requests stop at a specified step based on checkpoint.

  Note: We recommend using 'make_stop_at_checkpoint_step_hook` to get the proper
  hook.
  """
    def __init__(self, model_dir, last_step, wait_after_file_check_secs: int = 30) -> None:
        """Initializes a `StopAtCheckpointStepHook`.

    This hook requests stop after a last step has been reached. It checks latest
    checkpoint to verify last step is written on disk or not.

    Args:
      model_dir: Directory to read global step from latest checkpoint.
      last_step: Step after which to stop.
      wait_after_file_check_secs: Reading same file by many workers may create
        I/O issues. To throttle that we will wait given secs after each read of
        the file.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

def make_stop_at_checkpoint_step_hook(estimator, last_step, wait_after_file_check_secs: int = 30):
    """Creates a proper StopAtCheckpointStepHook based on chief status."""
