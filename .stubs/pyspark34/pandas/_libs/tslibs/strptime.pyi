import numpy as np
from pandas._typing import npt as npt

def array_strptime(values: npt.NDArray[np.object_], fmt: str | None, exact: bool = ..., errors: str = ..., utc: bool = ...) -> tuple[np.ndarray, np.ndarray]: ...
