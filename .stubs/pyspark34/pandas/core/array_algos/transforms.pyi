import numpy as np
from pandas._typing import AxisInt as AxisInt

def shift(values: np.ndarray, periods: int, axis: AxisInt, fill_value) -> np.ndarray: ...
