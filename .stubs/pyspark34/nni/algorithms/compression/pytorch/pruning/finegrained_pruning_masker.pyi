from .weight_masker import WeightMasker
from _typeshed import Incomplete

__all__ = ['LevelPrunerMasker']

class LevelPrunerMasker(WeightMasker):
    """
    Prune to an exact pruning level specification
    """
    def calc_mask(self, sparsity, wrapper, wrapper_idx: Incomplete | None = None): ...
