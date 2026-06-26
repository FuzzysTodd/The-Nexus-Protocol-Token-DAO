from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, NamedTuple

__all__ = ['early_stopping', 'log_evaluation', 'record_evaluation', 'reset_parameter']

class EarlyStopException(Exception):
    """Exception of early stopping."""
    best_iteration: Incomplete
    best_score: Incomplete
    def __init__(self, best_iteration: int, best_score: _ListOfEvalResultTuples) -> None:
        """Create early stopping exception.

        Parameters
        ----------
        best_iteration : int
            The best iteration stopped.
        best_score : list of (eval_name, metric_name, eval_result, is_higher_better) tuple or (eval_name, metric_name, eval_result, is_higher_better, stdv) tuple
            Scores for each metric, on each validation set, as of the best iteration.
        """

class CallbackEnv(NamedTuple):
    model: Incomplete
    params: Incomplete
    iteration: Incomplete
    begin_iteration: Incomplete
    end_iteration: Incomplete
    evaluation_result_list: Incomplete

class _LogEvaluationCallback:
    """Internal log evaluation callable class."""
    order: int
    before_iteration: bool
    period: Incomplete
    show_stdv: Incomplete
    def __init__(self, period: int = 1, show_stdv: bool = True) -> None: ...
    def __call__(self, env: CallbackEnv) -> None: ...

def log_evaluation(period: int = 1, show_stdv: bool = True) -> _LogEvaluationCallback:
    """Create a callback that logs the evaluation results.

    By default, standard output resource is used.
    Use ``register_logger()`` function to register a custom logger.

    Note
    ----
    Requires at least one validation data.

    Parameters
    ----------
    period : int, optional (default=1)
        The period to log the evaluation results.
        The last boosting stage or the boosting stage found by using ``early_stopping`` callback is also logged.
    show_stdv : bool, optional (default=True)
        Whether to log stdv (if provided).

    Returns
    -------
    callback : _LogEvaluationCallback
        The callback that logs the evaluation results every ``period`` boosting iteration(s).
    """

class _RecordEvaluationCallback:
    """Internal record evaluation callable class."""
    order: int
    before_iteration: bool
    eval_result: Incomplete
    def __init__(self, eval_result: _EvalResultDict) -> None: ...
    def __call__(self, env: CallbackEnv) -> None: ...

def record_evaluation(eval_result: Dict[str, Dict[str, List[Any]]]) -> Callable:
    """Create a callback that records the evaluation history into ``eval_result``.

    Parameters
    ----------
    eval_result : dict
        Dictionary used to store all evaluation results of all validation sets.
        This should be initialized outside of your call to ``record_evaluation()`` and should be empty.
        Any initial contents of the dictionary will be deleted.

        .. rubric:: Example

        With two validation sets named 'eval' and 'train', and one evaluation metric named 'logloss'
        this dictionary after finishing a model training process will have the following structure:

        .. code-block::

            {
             'train':
                 {
                  'logloss': [0.48253, 0.35953, ...]
                 },
             'eval':
                 {
                  'logloss': [0.480385, 0.357756, ...]
                 }
            }

    Returns
    -------
    callback : _RecordEvaluationCallback
        The callback that records the evaluation history into the passed dictionary.
    """

class _ResetParameterCallback:
    """Internal reset parameter callable class."""
    order: int
    before_iteration: bool
    kwargs: Incomplete
    def __init__(self, **kwargs: list | Callable) -> None: ...
    def __call__(self, env: CallbackEnv) -> None: ...

def reset_parameter(**kwargs: list | Callable) -> Callable:
    """Create a callback that resets the parameter after the first iteration.

    .. note::

        The initial parameter will still take in-effect on first iteration.

    Parameters
    ----------
    **kwargs : value should be list or callable
        List of parameters for each boosting round
        or a callable that calculates the parameter in terms of
        current number of round (e.g. yields learning rate decay).
        If list lst, parameter = lst[current_round].
        If callable func, parameter = func(current_round).

    Returns
    -------
    callback : _ResetParameterCallback
        The callback that resets the parameter after the first iteration.
    """

class _EarlyStoppingCallback:
    """Internal early stopping callable class."""
    order: int
    before_iteration: bool
    stopping_rounds: Incomplete
    first_metric_only: Incomplete
    verbose: Incomplete
    min_delta: Incomplete
    enabled: bool
    def __init__(self, stopping_rounds: int, first_metric_only: bool = False, verbose: bool = True, min_delta: float | List[float] = 0.0) -> None: ...
    def __call__(self, env: CallbackEnv) -> None: ...

def early_stopping(stopping_rounds: int, first_metric_only: bool = False, verbose: bool = True, min_delta: float | List[float] = 0.0) -> _EarlyStoppingCallback:
    """Create a callback that activates early stopping.

    Activates early stopping.
    The model will train until the validation score doesn't improve by at least ``min_delta``.
    Validation score needs to improve at least every ``stopping_rounds`` round(s)
    to continue training.
    Requires at least one validation data and one metric.
    If there's more than one, will check all of them. But the training data is ignored anyway.
    To check only the first metric set ``first_metric_only`` to True.
    The index of iteration that has the best performance will be saved in the ``best_iteration`` attribute of a model.

    Parameters
    ----------
    stopping_rounds : int
        The possible number of rounds without the trend occurrence.
    first_metric_only : bool, optional (default=False)
        Whether to use only the first metric for early stopping.
    verbose : bool, optional (default=True)
        Whether to log message with early stopping information.
        By default, standard output resource is used.
        Use ``register_logger()`` function to register a custom logger.
    min_delta : float or list of float, optional (default=0.0)
        Minimum improvement in score to keep training.
        If float, this single value is used for all metrics.
        If list, its length should match the total number of metrics.

        .. versionadded:: 4.0.0

    Returns
    -------
    callback : _EarlyStoppingCallback
        The callback that activates early stopping.
    """
