import numpy as np
from _typeshed import Incomplete
from pandas._typing import NpDtype as NpDtype

RANDS_CHARS: Incomplete

def rands_array(nchars, size, dtype: NpDtype = 'O', replace: bool = True) -> np.ndarray:
    """
    Generate an array of byte strings.
    """
def rands(nchars) -> str:
    """
    Generate one random byte string.

    See `rands_array` if you want to create an array of random strings.

    """
