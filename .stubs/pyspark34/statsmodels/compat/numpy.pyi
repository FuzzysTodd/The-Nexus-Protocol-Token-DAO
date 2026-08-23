import numpy as np
from _typeshed import Incomplete

__all__ = ['NP_LT_123', 'NP_LT_114', 'lstsq', 'np_matrix_rank', 'np_new_unique']

NP_LT_114: Incomplete
NP_LT_123: Incomplete
np_matrix_rank = np.linalg.matrix_rank
np_new_unique: Incomplete

def lstsq(a, b, rcond: Incomplete | None = None):
    """
    Shim that allows modern rcond setting with backward compat for NumPY
    earlier than 1.14
    """
