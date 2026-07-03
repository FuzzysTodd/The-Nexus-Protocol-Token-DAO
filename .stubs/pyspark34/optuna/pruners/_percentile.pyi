import optuna
from optuna._study_direction import StudyDirection as StudyDirection
from optuna.pruners import BasePruner as BasePruner
from optuna.trial._state import TrialState as TrialState

class PercentilePruner(BasePruner):
    '''Pruner to keep the specified percentile of the trials.

    Prune if the best intermediate value is in the bottom percentile among trials at the same step.

    Example:

        .. testcode::

            import numpy as np
            from sklearn.datasets import load_iris
            from sklearn.linear_model import SGDClassifier
            from sklearn.model_selection import train_test_split

            import optuna

            X, y = load_iris(return_X_y=True)
            X_train, X_valid, y_train, y_valid = train_test_split(X, y)
            classes = np.unique(y)


            def objective(trial):
                alpha = trial.suggest_float("alpha", 0.0, 1.0)
                clf = SGDClassifier(alpha=alpha)
                n_train_iter = 100

                for step in range(n_train_iter):
                    clf.partial_fit(X_train, y_train, classes=classes)

                    intermediate_value = clf.score(X_valid, y_valid)
                    trial.report(intermediate_value, step)

                    if trial.should_prune():
                        raise optuna.TrialPruned()

                return clf.score(X_valid, y_valid)


            study = optuna.create_study(
                direction="maximize",
                pruner=optuna.pruners.PercentilePruner(
                    25.0, n_startup_trials=5, n_warmup_steps=30, interval_steps=10
                ),
            )
            study.optimize(objective, n_trials=20)

    Args:
        percentile:
            Percentile which must be between 0 and 100 inclusive
            (e.g., When given 25.0, top of 25th percentile trials are kept).
        n_startup_trials:
            Pruning is disabled until the given number of trials finish in the same study.
        n_warmup_steps:
            Pruning is disabled until the trial exceeds the given number of step. Note that
            this feature assumes that ``step`` starts at zero.
        interval_steps:
            Interval in number of steps between the pruning checks, offset by the warmup steps.
            If no value has been reported at the time of a pruning check, that particular check
            will be postponed until a value is reported. Value must be at least 1.
        n_min_trials:
            Minimum number of reported trial results at a step to judge whether to prune.
            If the number of reported intermediate values from all trials at the current step
            is less than ``n_min_trials``, the trial will not be pruned. This can be used to ensure
            that a minimum number of trials are run to completion without being pruned.
    '''
    def __init__(self, percentile: float, n_startup_trials: int = 5, n_warmup_steps: int = 0, interval_steps: int = 1, *, n_min_trials: int = 1) -> None: ...
    def prune(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial) -> bool: ...
