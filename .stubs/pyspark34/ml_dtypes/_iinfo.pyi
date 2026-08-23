import numpy as np
from ml_dtypes._ml_dtypes_ext import int4 as int4, uint4 as uint4

class iinfo:
    kind: str
    bits: int
    min: int
    max: int
    dtype: np.dtype
    def __init__(self, int_type) -> None: ...
