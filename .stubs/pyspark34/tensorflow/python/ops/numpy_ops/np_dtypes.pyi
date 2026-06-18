from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.ops.numpy_ops import np_export as np_export

bool_: Incomplete
complex_: Incomplete
complex128: Incomplete
complex64: Incomplete
float_: Incomplete
float16: Incomplete
float32: Incomplete
float64: Incomplete
inexact: Incomplete
int_: Incomplete
int16: Incomplete
int32: Incomplete
int64: Incomplete
int8: Incomplete
object_: Incomplete
string_: Incomplete
uint16: Incomplete
uint32: Incomplete
uint64: Incomplete
uint8: Incomplete
unicode_: Incomplete
iinfo: Incomplete
issubdtype: Incomplete

def is_prefer_float32(): ...
def set_prefer_float32(b) -> None: ...
def is_allow_float64(): ...
def set_allow_float64(b) -> None: ...
def canonicalize_dtype(dtype): ...
def default_float_type():
    """Gets the default float type.

  Returns:
    If `is_prefer_float32()` is false and `is_allow_float64()` is true, returns
    float64; otherwise returns float32.
  """
