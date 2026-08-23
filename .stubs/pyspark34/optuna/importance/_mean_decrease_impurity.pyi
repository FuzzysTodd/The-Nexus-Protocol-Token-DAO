from optuna._imports import try_import as try_import
from optuna.importance._base import BaseImportanceEvaluator as BaseImportanceEvaluator
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from typing import Callable, Dict, List

class MeanDecreaseImpurityImportanceEvaluator(BaseImportanceEvaluator):
    """Mean Decrease Impurity (MDI) parameter importance evaluator.

    This evaluator fits a random forest that predicts objective values given hyperparameter
    configurations. Feature importances are then computed using MDI.

    .. note::

        This evaluator requires the `sklean <https://scikit-learn.org/stable/>`_ Python package and
        is based on `sklearn.ensemble.RandomForestClassifier.feature_importances_
        <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.feature_importances_>`_.

    Args:
        n_trees:
            Number of trees in the random forest.
        max_depth:
            The maximum depth of each tree in the random forest.
        seed:
            Seed for the random forest.
    """
    def __init__(self, *, n_trees: int = 64, max_depth: int = 64, seed: int | None = None) -> None: ...
    def evaluate(self, study: Study, params: List[str] | None = None, *, target: Callable[[FrozenTrial], float] | None = None) -> Dict[str, float]: ...
