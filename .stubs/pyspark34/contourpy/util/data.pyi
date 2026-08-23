import numpy as np
from contourpy._contourpy import CoordinateArray as CoordinateArray
from typing import Any

def simple(shape: tuple[int, int], want_mask: bool = False) -> tuple[CoordinateArray, CoordinateArray, CoordinateArray | np.ma.MaskedArray[Any, Any]]:
    """Return simple test data consisting of the sum of two gaussians.

    Args:
        shape (tuple(int, int)): 2D shape of data to return.
        want_mask (bool, optional): Whether test data should be masked or not, default ``False``.

    Return:
        Tuple of 3 arrays: ``x``, ``y``, ``z`` test data, ``z`` will be masked if
        ``want_mask=True``.
    """
def random(shape: tuple[int, int], seed: int = 2187, mask_fraction: float = 0.0) -> tuple[CoordinateArray, CoordinateArray, CoordinateArray | np.ma.MaskedArray[Any, Any]]:
    """Return random test data..

    Args:
        shape (tuple(int, int)): 2D shape of data to return.
        seed (int, optional): Seed for random number generator, default 2187.
        mask_fraction (float, optional): Fraction of elements to mask, default 0.

    Return:
        Tuple of 3 arrays: ``x``, ``y``, ``z`` test data, ``z`` will be masked if
        ``mask_fraction`` is greater than zero.
    """
