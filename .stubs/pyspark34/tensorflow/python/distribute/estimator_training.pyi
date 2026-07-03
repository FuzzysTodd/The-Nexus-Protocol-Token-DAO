from _typeshed import Incomplete
from tensorflow.python.distribute import multi_worker_util as multi_worker_util
from tensorflow.python.training import server_lib as server_lib

CHIEF: Incomplete
EVALUATOR: Incomplete
PS: Incomplete
WORKER: Incomplete

def init_run_config(config, tf_config) -> None:
    """Initializes RunConfig for distribution strategies."""
def should_run_distribute_coordinator(config):
    """Checks the config to see whether to run distribute coordinator."""
def train_and_evaluate(estimator, train_spec, eval_spec, executor_cls) -> None:
    """Run distribute coordinator for Estimator's `train_and_evaluate`.

  Args:
    estimator: An `Estimator` instance to train and evaluate.
    train_spec: A `TrainSpec` instance to specify the training specification.
    eval_spec: A `EvalSpec` instance to specify the evaluation and export
      specification.
    executor_cls: the evaluation executor class of Estimator.

  Raises:
    ValueError: if `distribute_coordinator_mode` is None in RunConfig.
  """
def estimator_train(estimator, train_distributed_fn, hooks):
    """Run distribute coordinator for Estimator's `train` method."""
def estimator_evaluate(estimator, evaluate_distributed_fn, hooks):
    """Run distribute coordinator for Estimator's `evaluate` method."""
