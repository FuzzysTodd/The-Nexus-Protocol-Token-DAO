import numpy.typing as npt
from typing import Tuple

def nnls(a: npt.ArrayLike, mda: int, m: int, n: int, b: npt.ArrayLike, x: npt.ArrayLike, rnorm: float, w: float, zz: float, index_bn: int, mode: int, maxiter: int) -> Tuple[npt.ArrayLike, float, int]: ...
