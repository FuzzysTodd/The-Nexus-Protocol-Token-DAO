import optuna
import tensorflow as tf
from optuna._imports import try_import as try_import
from tensorflow.estimator import SessionRunHook

SessionRunHook = object

class TensorFlowPruningHook(SessionRunHook):
    """TensorFlow SessionRunHook to prune unpromising trials.

    See `the example <https://github.com/optuna/optuna-examples/tree/main/
    tensorflow/tensorflow_estimator_integration.py>`_
    if you want to add a pruning hook to TensorFlow's estimator.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of
            the objective function.
        estimator:
            An estimator which you will use.
        metric:
            An evaluation metric for pruning, e.g., ``accuracy`` and ``loss``.
        run_every_steps:
           An interval to watch the summary file.
    """
    def __init__(self, trial: optuna.trial.Trial, estimator: tf.estimator.Estimator, metric: str, run_every_steps: int) -> None: ...
    def begin(self) -> None: ...
    def before_run(self, run_context: tf.estimator.SessionRunContext) -> tf.estimator.SessionRunArgs: ...
    def after_run(self, run_context: tf.estimator.SessionRunContext, run_values: tf.estimator.SessionRunValues) -> None: ...
