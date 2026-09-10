import numpy as np
from flaml.internal.fanova._fanova import FanovaTree as FanovaTree
from optuna._transform import _SearchSpaceTransform
from optuna.importance._base import BaseImportanceEvaluator
from sklearn.ensemble import RandomForestRegressor
from typing import Dict, List, Tuple

class FanovaImportanceEvaluator(BaseImportanceEvaluator):
    """Cython accelerated fANOVA importance evaluator.

    Args:
        n_trees:
            The number of trees in the forest.
        max_depth:
            The maximum depth of the trees in the forest.
        seed:
            Controls the randomness of the forest. For deterministic behavior, specify a value
            other than :obj:`None`.
        completed_trials:
            Avoid to call ``study.get_trials()`` and use this value instead (default: None).
    """
    def __init__(self, *, n_trees: int = 64, max_depth: int = 64, seed: int | None = None) -> None: ...
    def evaluate(self, hp_df, scores, search_space) -> Dict[str, float]: ...

def compute_importance(forest: RandomForestRegressor, transform: _SearchSpaceTransform, param_names: List[str]) -> Dict[str, float]: ...
def get_importance(trees: List[FanovaTree], feature: int, variances: np.ndarray) -> Tuple[float, float]: ...
