import optuna
from optuna.pruners import BasePruner as BasePruner

class ThresholdPruner(BasePruner):
    """Pruner to detect outlying metrics of the trials.

    Prune if a metric exceeds upper threshold,
    falls behind lower threshold or reaches ``nan``.

    Example:
        .. testcode::

            from optuna import create_study
            from optuna.pruners import ThresholdPruner
            from optuna import TrialPruned


            def objective_for_upper(trial):
                for step, y in enumerate(ys_for_upper):
                    trial.report(y, step)

                    if trial.should_prune():
                        raise TrialPruned()
                return ys_for_upper[-1]


            def objective_for_lower(trial):
                for step, y in enumerate(ys_for_lower):
                    trial.report(y, step)

                    if trial.should_prune():
                        raise TrialPruned()
                return ys_for_lower[-1]


            ys_for_upper = [0.0, 0.1, 0.2, 0.5, 1.2]
            ys_for_lower = [100.0, 90.0, 0.1, 0.0, -1]

            study = create_study(pruner=ThresholdPruner(upper=1.0))
            study.optimize(objective_for_upper, n_trials=10)

            study = create_study(pruner=ThresholdPruner(lower=0.0))
            study.optimize(objective_for_lower, n_trials=10)

    Args:
        lower:
            A minimum value which determines whether pruner prunes or not.
            If an intermediate value is smaller than lower, it prunes.
        upper:
            A maximum value which determines whether pruner prunes or not.
            If an intermediate value is larger than upper, it prunes.
        n_warmup_steps:
            Pruning is disabled if the step is less than the given number of warmup steps.
        interval_steps:
            Interval in number of steps between the pruning checks, offset by the warmup steps.
            If no value has been reported at the time of a pruning check, that particular check
            will be postponed until a value is reported. Value must be at least 1.

    """
    def __init__(self, lower: float | None = None, upper: float | None = None, n_warmup_steps: int = 0, interval_steps: int = 1) -> None: ...
    def prune(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial) -> bool: ...
