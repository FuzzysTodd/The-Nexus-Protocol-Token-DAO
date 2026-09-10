import os
from .core import DMatrix
from _typeshed import Incomplete
from abc import ABC
from typing import Callable, List, Sequence, Tuple

__all__ = ['TrainingCallback', 'LearningRateScheduler', 'EarlyStopping', 'EvaluationMonitor', 'TrainingCheckPoint', 'CallbackContainer']

class TrainingCallback(ABC):
    """Interface for training callback.

    .. versionadded:: 1.3.0

    """
    EvalsLog: Incomplete
    def __init__(self) -> None: ...
    def before_training(self, model: _Model) -> _Model:
        """Run before training starts."""
    def after_training(self, model: _Model) -> _Model:
        """Run after training is finished."""
    def before_iteration(self, model: _Model, epoch: int, evals_log: EvalsLog) -> bool:
        """Run before each iteration.  Return True when training should stop."""
    def after_iteration(self, model: _Model, epoch: int, evals_log: EvalsLog) -> bool:
        """Run after each iteration.  Return True when training should stop."""

class CallbackContainer:
    """A special internal callback for invoking a list of other callbacks.

    .. versionadded:: 1.3.0

    """
    EvalsLog: Incomplete
    callbacks: Incomplete
    metric: Incomplete
    history: Incomplete
    is_cv: Incomplete
    aggregated_cv: Incomplete
    def __init__(self, callbacks: Sequence[TrainingCallback], metric: Callable = None, output_margin: bool = True, is_cv: bool = False) -> None: ...
    def before_training(self, model: _Model) -> _Model:
        """Function called before training."""
    def after_training(self, model: _Model) -> _Model:
        """Function called after training."""
    def before_iteration(self, model: _Model, epoch: int, dtrain: DMatrix, evals: List[Tuple[DMatrix, str]] | None) -> bool:
        """Function called before training iteration."""
    def after_iteration(self, model: _Model, epoch: int, dtrain: DMatrix, evals: List[Tuple[DMatrix, str]] | None) -> bool:
        """Function called after training iteration."""

class LearningRateScheduler(TrainingCallback):
    """Callback function for scheduling learning rate.

    .. versionadded:: 1.3.0

    Parameters
    ----------

    learning_rates :
        If it's a callable object, then it should accept an integer parameter
        `epoch` and returns the corresponding learning rate.  Otherwise it
        should be a sequence like list or tuple with the same size of boosting
        rounds.

    """
    learning_rates: Incomplete
    def __init__(self, learning_rates: Callable[[int], float] | Sequence[float]) -> None: ...
    def after_iteration(self, model: _Model, epoch: int, evals_log: TrainingCallback.EvalsLog) -> bool: ...

class EarlyStopping(TrainingCallback):
    '''Callback function for early stopping

    .. versionadded:: 1.3.0

    Parameters
    ----------
    rounds :
        Early stopping rounds.
    metric_name :
        Name of metric that is used for early stopping.
    data_name :
        Name of dataset that is used for early stopping.
    maximize :
        Whether to maximize evaluation metric.  None means auto (discouraged).
    save_best :
        Whether training should return the best model or the last model.
    min_delta :
        Minimum absolute change in score to be qualified as an improvement.

        .. versionadded:: 1.5.0

        .. code-block:: python

            clf = xgboost.XGBClassifier(tree_method="gpu_hist")
            es = xgboost.callback.EarlyStopping(
                rounds=2,
                abs_tol=1e-3,
                save_best=True,
                maximize=False,
                data_name="validation_0",
                metric_name="mlogloss",
            )

            X, y = load_digits(return_X_y=True)
            clf.fit(X, y, eval_set=[(X, y)], callbacks=[es])
    '''
    data: Incomplete
    metric_name: Incomplete
    rounds: Incomplete
    save_best: Incomplete
    maximize: Incomplete
    stopping_history: Incomplete
    current_rounds: int
    best_scores: Incomplete
    starting_round: int
    def __init__(self, rounds: int, metric_name: str | None = None, data_name: str | None = None, maximize: bool | None = None, save_best: bool | None = False, min_delta: float = 0.0) -> None: ...
    def before_training(self, model: _Model) -> _Model: ...
    def after_iteration(self, model: _Model, epoch: int, evals_log: TrainingCallback.EvalsLog) -> bool: ...
    def after_training(self, model: _Model) -> _Model: ...

class EvaluationMonitor(TrainingCallback):
    """Print the evaluation result at each iteration.

    .. versionadded:: 1.3.0

    Parameters
    ----------

    metric :
        Extra user defined metric.
    rank :
        Which worker should be used for printing the result.
    period :
        How many epoches between printing.
    show_stdv :
        Used in cv to show standard deviation.  Users should not specify it.
    """
    printer_rank: Incomplete
    show_stdv: Incomplete
    period: Incomplete
    def __init__(self, rank: int = 0, period: int = 1, show_stdv: bool = False) -> None: ...
    def after_iteration(self, model: _Model, epoch: int, evals_log: TrainingCallback.EvalsLog) -> bool: ...
    def after_training(self, model: _Model) -> _Model: ...

class TrainingCheckPoint(TrainingCallback):
    """Checkpointing operation.

    .. versionadded:: 1.3.0

    Parameters
    ----------

    directory :
        Output model directory.
    name :
        pattern of output model file.  Models will be saved as name_0.json, name_1.json,
        name_2.json ....
    as_pickle :
        When set to True, all training parameters will be saved in pickle format, instead
        of saving only the model.
    iterations :
        Interval of checkpointing.  Checkpointing is slow so setting a larger number can
        reduce performance hit.

    """
    def __init__(self, directory: str | os.PathLike, name: str = 'model', as_pickle: bool = False, iterations: int = 100) -> None: ...
    def after_iteration(self, model: _Model, epoch: int, evals_log: TrainingCallback.EvalsLog) -> bool: ...
