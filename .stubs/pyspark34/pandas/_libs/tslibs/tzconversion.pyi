import numpy as np
from datetime import timedelta, tzinfo
from pandas._typing import npt as npt
from typing import Iterable

def tz_convert_from_utc_single(val: np.int64, tz: tzinfo, creso: int = ...) -> np.int64: ...
def tz_localize_to_utc(vals: npt.NDArray[np.int64], tz: tzinfo | None, ambiguous: str | bool | Iterable[bool] | None = ..., nonexistent: str | timedelta | np.timedelta64 | None = ..., creso: int = ...) -> npt.NDArray[np.int64]: ...
