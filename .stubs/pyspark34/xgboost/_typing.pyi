import ctypes
import numpy as np
import os
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, Sequence, Type, TypeVar

DataType = Any
FeatureInfo = Sequence[str]
FeatureNames = FeatureInfo
FeatureTypes = FeatureInfo
BoosterParam = List | Dict
ArrayLike = Any
PathLike = str | os.PathLike
CupyT = ArrayLike
NumpyOrCupy = Any
NumpyDType = str | Type[np.number]
PandasDType = Any
FloatCompatible: Incomplete
FPreProcCallable = Callable
c_bst_ulong = ctypes.c_uint64
CTypeT = TypeVar('CTypeT', ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_float, ctypes.c_uint, ctypes.c_size_t)
CNumeric = ctypes.c_float | ctypes.c_double | ctypes.c_uint | ctypes.c_uint64 | ctypes.c_int32 | ctypes.c_int64
CStrPtr: Incomplete
CStrPptr: Incomplete
CFloatPtr: Incomplete
CNumericPtr: Incomplete
