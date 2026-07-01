import optuna
from optuna._experimental import experimental as experimental
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from typing import Tuple

class MaxTrialsCallback:
    '''Set a maximum number of trials before ending the study.

    While the :obj:`n_trials` argument of :obj:`optuna.optimize` sets the number of trials that
    will be run, you may want to continue running until you have a certain number of successfullly
    completed trials or stop the study when you have a certain number of trials that fail.
    This :obj:`MaxTrialsCallback` class allows you to set a maximum number of trials for a
    particular :class:`~optuna.trial.TrialState` before stopping the study.

    Example:

        .. testcode::

            import optuna
            from optuna.study import MaxTrialsCallback
            from optuna.trial import TrialState


            def objective(trial):
                x = trial.suggest_float("x", -1, 1)
                return x ** 2


            study = optuna.create_study()
            study.optimize(
                objective,
                callbacks=[MaxTrialsCallback(10, states=(TrialState.COMPLETE,))],
            )

    Args:
        n_trials:
            The max number of trials. Must be set to an integer.
        states:
            Tuple of the :class:`~optuna.trial.TrialState` to be counted
            towards the max trials limit. Default value is :obj:`(TrialState.COMPLETE,)`.
    '''
    def __init__(self, n_trials: int, states: Tuple[TrialState, ...] = ...) -> None: ...
    def __call__(self, study: optuna.study.Study, trial: FrozenTrial) -> None: ...

class RetryFailedTrialCallback:
    '''Retry a failed trial up to a maximum number of times.

    When a trial fails, this callback can be used with the :class:`optuna.storage` class to
    recreate the trial in :obj:`TrialState.WAITING` to queue up the trial to be run again.

    This is helpful in environments where trials may fail due to external conditions, such as
    being preempted by other processes.

    Usage:

        .. testcode::

            import optuna
            from optuna.storages import RetryFailedTrialCallback

            storage = optuna.storages.RDBStorage(
                url="sqlite:///:memory:",
                heartbeat_interval=60,
                grace_period=120,
                failed_trial_callback=RetryFailedTrialCallback(max_retry=3),
            )

            study = optuna.create_study(
                storage=storage,
            )

    Args:
        max_retry:
            The max number of times a trial can be retried. Must be set to :obj:`None` or an
            integer. If set to the default value of :obj:`None` will retry indefinitely.
            If set to an integer, will only retry that many times.
    '''
    def __init__(self, max_retry: int | None = None) -> None: ...
    def __call__(self, study: optuna.study.Study, trial: FrozenTrial) -> None: ...
    @staticmethod
    def retried_trial_number(trial: FrozenTrial) -> int | None:
        """Return the number of the trial being retried.

        Args:
            trial:
                The trial object.

        Returns:
            The number of the previous trial. If not retry of a previous trial,
            returns :obj:`None`.
        """
