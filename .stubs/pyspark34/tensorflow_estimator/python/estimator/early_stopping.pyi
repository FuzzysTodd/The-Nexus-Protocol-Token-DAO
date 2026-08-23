import tensorflow as tf
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export

def make_early_stopping_hook(estimator, should_stop_fn, run_every_secs: int = 60, run_every_steps: Incomplete | None = None):
    """Creates early-stopping hook.

  Returns a `SessionRunHook` that stops training when `should_stop_fn` returns
  `True`.

  Usage example:

  ```python
  estimator = ...
  hook = early_stopping.make_early_stopping_hook(
      estimator, should_stop_fn=make_stop_fn(...))
  train_spec = tf.estimator.TrainSpec(..., hooks=[hook])
  tf.estimator.train_and_evaluate(estimator, train_spec, ...)
  ```

  Caveat: Current implementation supports early-stopping both training and
  evaluation in local mode. In distributed mode, training can be stopped but
  evaluation (where it's a separate job) will indefinitely wait for new model
  checkpoints to evaluate, so you will need other means to detect and stop it.
  Early-stopping evaluation in distributed mode requires changes in
  `train_and_evaluate` API and will be addressed in a future revision.

  Args:
    estimator: A `tf.estimator.Estimator` instance.
    should_stop_fn: `callable`, function that takes no arguments and returns a
      `bool`. If the function returns `True`, stopping will be initiated by the
      chief.
    run_every_secs: If specified, calls `should_stop_fn` at an interval of
      `run_every_secs` seconds. Defaults to 60 seconds. Either this or
      `run_every_steps` must be set.
    run_every_steps: If specified, calls `should_stop_fn` every
      `run_every_steps` steps. Either this or `run_every_secs` must be set.

  Returns:
    A `SessionRunHook` that periodically executes `should_stop_fn` and initiates
    early stopping if the function returns `True`.

  Raises:
    TypeError: If `estimator` is not of type `tf.estimator.Estimator`.
    ValueError: If both `run_every_secs` and `run_every_steps` are set.
  """
def stop_if_higher_hook(estimator, metric_name, threshold, eval_dir: Incomplete | None = None, min_steps: int = 0, run_every_secs: int = 60, run_every_steps: Incomplete | None = None):
    '''Creates hook to stop if the given metric is higher than the threshold.

  Usage example:

  ```python
  estimator = ...
  # Hook to stop training if accuracy becomes higher than 0.9.
  hook = early_stopping.stop_if_higher_hook(estimator, "accuracy", 0.9)
  train_spec = tf.estimator.TrainSpec(..., hooks=[hook])
  tf.estimator.train_and_evaluate(estimator, train_spec, ...)
  ```

  Caveat: Current implementation supports early-stopping both training and
  evaluation in local mode. In distributed mode, training can be stopped but
  evaluation (where it\'s a separate job) will indefinitely wait for new model
  checkpoints to evaluate, so you will need other means to detect and stop it.
  Early-stopping evaluation in distributed mode requires changes in
  `train_and_evaluate` API and will be addressed in a future revision.

  Args:
    estimator: A `tf.estimator.Estimator` instance.
    metric_name: `str`, metric to track. "loss", "accuracy", etc.
    threshold: Numeric threshold for the given metric.
    eval_dir: If set, directory containing summary files with eval metrics. By
      default, `estimator.eval_dir()` will be used.
    min_steps: `int`, stop is never requested if global step is less than this
      value. Defaults to 0.
    run_every_secs: If specified, calls `should_stop_fn` at an interval of
      `run_every_secs` seconds. Defaults to 60 seconds. Either this or
      `run_every_steps` must be set.
    run_every_steps: If specified, calls `should_stop_fn` every
      `run_every_steps` steps. Either this or `run_every_secs` must be set.

  Returns:
    An early-stopping hook of type `SessionRunHook` that periodically checks
    if the given metric is higher than specified threshold and initiates
    early stopping if true.
  '''
def stop_if_lower_hook(estimator, metric_name, threshold, eval_dir: Incomplete | None = None, min_steps: int = 0, run_every_secs: int = 60, run_every_steps: Incomplete | None = None):
    '''Creates hook to stop if the given metric is lower than the threshold.

  Usage example:

  ```python
  estimator = ...
  # Hook to stop training if loss becomes lower than 100.
  hook = early_stopping.stop_if_lower_hook(estimator, "loss", 100)
  train_spec = tf.estimator.TrainSpec(..., hooks=[hook])
  tf.estimator.train_and_evaluate(estimator, train_spec, ...)
  ```

  Caveat: Current implementation supports early-stopping both training and
  evaluation in local mode. In distributed mode, training can be stopped but
  evaluation (where it\'s a separate job) will indefinitely wait for new model
  checkpoints to evaluate, so you will need other means to detect and stop it.
  Early-stopping evaluation in distributed mode requires changes in
  `train_and_evaluate` API and will be addressed in a future revision.

  Args:
    estimator: A `tf.estimator.Estimator` instance.
    metric_name: `str`, metric to track. "loss", "accuracy", etc.
    threshold: Numeric threshold for the given metric.
    eval_dir: If set, directory containing summary files with eval metrics. By
      default, `estimator.eval_dir()` will be used.
    min_steps: `int`, stop is never requested if global step is less than this
      value. Defaults to 0.
    run_every_secs: If specified, calls `should_stop_fn` at an interval of
      `run_every_secs` seconds. Defaults to 60 seconds. Either this or
      `run_every_steps` must be set.
    run_every_steps: If specified, calls `should_stop_fn` every
      `run_every_steps` steps. Either this or `run_every_secs` must be set.

  Returns:
    An early-stopping hook of type `SessionRunHook` that periodically checks
    if the given metric is lower than specified threshold and initiates
    early stopping if true.
  '''
def stop_if_no_increase_hook(estimator, metric_name, max_steps_without_increase, eval_dir: Incomplete | None = None, min_steps: int = 0, run_every_secs: int = 60, run_every_steps: Incomplete | None = None):
    '''Creates hook to stop if metric does not increase within given max steps.

  Usage example:

  ```python
  estimator = ...
  # Hook to stop training if accuracy does not increase in over 100000 steps.
  hook = early_stopping.stop_if_no_increase_hook(estimator, "accuracy", 100000)
  train_spec = tf.estimator.TrainSpec(..., hooks=[hook])
  tf.estimator.train_and_evaluate(estimator, train_spec, ...)
  ```

  Caveat: Current implementation supports early-stopping both training and
  evaluation in local mode. In distributed mode, training can be stopped but
  evaluation (where it\'s a separate job) will indefinitely wait for new model
  checkpoints to evaluate, so you will need other means to detect and stop it.
  Early-stopping evaluation in distributed mode requires changes in
  `train_and_evaluate` API and will be addressed in a future revision.

  Args:
    estimator: A `tf.estimator.Estimator` instance.
    metric_name: `str`, metric to track. "loss", "accuracy", etc.
    max_steps_without_increase: `int`, maximum number of training steps with no
      increase in the given metric.
    eval_dir: If set, directory containing summary files with eval metrics. By
      default, `estimator.eval_dir()` will be used.
    min_steps: `int`, stop is never requested if global step is less than this
      value. Defaults to 0.
    run_every_secs: If specified, calls `should_stop_fn` at an interval of
      `run_every_secs` seconds. Defaults to 60 seconds. Either this or
      `run_every_steps` must be set.
    run_every_steps: If specified, calls `should_stop_fn` every
      `run_every_steps` steps. Either this or `run_every_secs` must be set.

  Returns:
    An early-stopping hook of type `SessionRunHook` that periodically checks
    if the given metric shows no increase over given maximum number of
    training steps, and initiates early stopping if true.
  '''
def stop_if_no_decrease_hook(estimator, metric_name, max_steps_without_decrease, eval_dir: Incomplete | None = None, min_steps: int = 0, run_every_secs: int = 60, run_every_steps: Incomplete | None = None):
    '''Creates hook to stop if metric does not decrease within given max steps.

  Usage example:

  ```python
  estimator = ...
  # Hook to stop training if loss does not decrease in over 100000 steps.
  hook = early_stopping.stop_if_no_decrease_hook(estimator, "loss", 100000)
  train_spec = tf.estimator.TrainSpec(..., hooks=[hook])
  tf.estimator.train_and_evaluate(estimator, train_spec, ...)
  ```

  Caveat: Current implementation supports early-stopping both training and
  evaluation in local mode. In distributed mode, training can be stopped but
  evaluation (where it\'s a separate job) will indefinitely wait for new model
  checkpoints to evaluate, so you will need other means to detect and stop it.
  Early-stopping evaluation in distributed mode requires changes in
  `train_and_evaluate` API and will be addressed in a future revision.

  Args:
    estimator: A `tf.estimator.Estimator` instance.
    metric_name: `str`, metric to track. "loss", "accuracy", etc.
    max_steps_without_decrease: `int`, maximum number of training steps with no
      decrease in the given metric.
    eval_dir: If set, directory containing summary files with eval metrics. By
      default, `estimator.eval_dir()` will be used.
    min_steps: `int`, stop is never requested if global step is less than this
      value. Defaults to 0.
    run_every_secs: If specified, calls `should_stop_fn` at an interval of
      `run_every_secs` seconds. Defaults to 60 seconds. Either this or
      `run_every_steps` must be set.
    run_every_steps: If specified, calls `should_stop_fn` every
      `run_every_steps` steps. Either this or `run_every_secs` must be set.

  Returns:
    An early-stopping hook of type `SessionRunHook` that periodically checks
    if the given metric shows no decrease over given maximum number of
    training steps, and initiates early stopping if true.
  '''
def read_eval_metrics(eval_dir):
    """Helper to read eval metrics from eval summary files.

  Args:
    eval_dir: Directory containing summary files with eval metrics.

  Returns:
    A `dict` with global steps mapping to `dict` of metric names and values.
  """

class _StopOnPredicateHook(tf.compat.v1.train.SessionRunHook):
    """Hook that requests stop when `should_stop_fn` returns `True`."""
    def __init__(self, should_stop_fn, run_every_secs: int = 60, run_every_steps: Incomplete | None = None) -> None: ...
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class _CheckForStoppingHook(tf.compat.v1.train.SessionRunHook):
    """Hook that requests stop if stop is requested by `_StopOnPredicateHook`."""
    def __init__(self) -> None: ...
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class _MultiWorkerEarlyStoppingHook(tf.compat.v1.train.SessionRunHook):
    """Hook that requests stop when `should_stop_fn` returns `True`."""
    def __init__(self, should_stop_fn, run_every_steps: Incomplete | None = None) -> None: ...
    def begin(self): ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...
