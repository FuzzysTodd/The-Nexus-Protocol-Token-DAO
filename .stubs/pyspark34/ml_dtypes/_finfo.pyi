import numpy as np
from _typeshed import Incomplete
from ml_dtypes._ml_dtypes_ext import bfloat16 as bfloat16, float8_e4m3b11fnuz as float8_e4m3b11fnuz, float8_e4m3fn as float8_e4m3fn, float8_e4m3fnuz as float8_e4m3fnuz, float8_e5m2 as float8_e5m2, float8_e5m2fnuz as float8_e5m2fnuz

class _Bfloat16MachArLike:
    smallest_normal: Incomplete
    smallest_subnormal: Incomplete
    def __init__(self) -> None: ...

class _Float8E4m3b11fnuzMachArLike:
    smallest_normal: Incomplete
    smallest_subnormal: Incomplete
    def __init__(self) -> None: ...

class _Float8E4m3fnMachArLike:
    smallest_normal: Incomplete
    smallest_subnormal: Incomplete
    def __init__(self) -> None: ...

class _Float8E4m3fnuzMachArLike:
    smallest_normal: Incomplete
    smallest_subnormal: Incomplete
    def __init__(self) -> None: ...

class _Float8E5m2MachArLike:
    smallest_normal: Incomplete
    smallest_subnormal: Incomplete
    def __init__(self) -> None: ...

class _Float8E5m2fnuzMachArLike:
    smallest_normal: Incomplete
    smallest_subnormal: Incomplete
    def __init__(self) -> None: ...

class finfo(np.finfo):
    __doc__: Incomplete
    def __new__(cls, dtype): ...
