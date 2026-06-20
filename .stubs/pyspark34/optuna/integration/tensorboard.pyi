import optuna
from optuna._experimental import experimental as experimental
from optuna._imports import try_import as try_import

class TensorBoardCallback:
    """Callback to track Optuna trials with TensorBoard.

    This callback adds relevant information that is tracked by Optuna to TensorBoard.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    tensorboard/tensorboard_simple.py>`_.

    Args:
        dirname:
            Directory to store TensorBoard logs.
        metric_name:
            Name of the metric. Since the metric itself is just a number,
            `metric_name` can be used to give it a name. So you know later
            if it was roc-auc or accuracy.

    """
    def __init__(self, dirname: str, metric_name: str) -> None: ...
    def __call__(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial) -> None: ...
