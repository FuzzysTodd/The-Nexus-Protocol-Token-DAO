import optuna
from optuna._experimental import experimental as experimental
from optuna._study_direction import StudyDirection as StudyDirection
from optuna.pruners import BasePruner as BasePruner

class PatientPruner(BasePruner):
    '''Pruner which wraps another pruner with tolerance.

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
                pruner=optuna.pruners.PatientPruner(optuna.pruners.MedianPruner(), patience=1),
            )
            study.optimize(objective, n_trials=20)

    Args:
        wrapped_pruner:
            Wrapped pruner to perform pruning when :class:`~optuna.pruners.PatientPruner` allows a
            trial to be pruned. If it is :obj:`None`, this pruner is equivalent to
            early-stopping taken the intermediate values in the individual trial.
        patience:
            Pruning is disabled until the objective doesn\'t improve for
            ``patience`` consecutive steps.
        min_delta:
            Tolerance value to check whether or not the objective improves.
            This value should be non-negative.

    '''
    def __init__(self, wrapped_pruner: BasePruner | None, patience: int, min_delta: float = 0.0) -> None: ...
    def prune(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial) -> bool: ...
