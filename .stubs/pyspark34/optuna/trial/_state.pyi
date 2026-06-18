import enum

class TrialState(enum.Enum):
    """State of a :class:`~optuna.trial.Trial`.

    Attributes:
        RUNNING:
            The :class:`~optuna.trial.Trial` is running.
        WAITING:
            The :class:`~optuna.trial.Trial` is waiting and unfinished.
        COMPLETE:
            The :class:`~optuna.trial.Trial` has been finished without any error.
        PRUNED:
            The :class:`~optuna.trial.Trial` has been pruned with
            :class:`~optuna.exceptions.TrialPruned`.
        FAIL:
            The :class:`~optuna.trial.Trial` has failed due to an uncaught error.
    """
    RUNNING: int
    COMPLETE: int
    PRUNED: int
    FAIL: int
    WAITING: int
    def is_finished(self) -> bool: ...
