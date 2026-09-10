import numpy as np
from collections.abc import Sequence
from typing import Any, Protocol

DType = np.dtype
ExtendedDType = Any

class SupportsDType(Protocol):
    @property
    def dtype(self) -> DType: ...
DTypeLike = Any | str | np.dtype | SupportsDType
DimSize = int | Any
Shape = Sequence[DimSize]

class DuckTypedArray(Protocol):
    @property
    def dtype(self) -> DType: ...
    @property
    def shape(self) -> Shape: ...
