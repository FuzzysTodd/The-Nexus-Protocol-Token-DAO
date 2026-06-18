import numpy as np
from datetime import datetime, tzinfo

DT64NS_DTYPE: np.dtype
TD64NS_DTYPE: np.dtype

def precision_from_unit(unit: str) -> tuple[int, int]: ...
def localize_pydatetime(dt: datetime, tz: tzinfo | None) -> datetime: ...
