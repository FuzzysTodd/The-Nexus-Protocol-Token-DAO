import abc
import numpy as np
from _typeshed import Incomplete
from jax._src import traceback_util as traceback_util
from jax._src.config import config as config
from jax._src.typing import DType as DType, DTypeLike as DTypeLike
from typing import Any, Literal, overload

class extended(np.generic, metaclass=abc.ABCMeta):
    """Scalar class for extended dtypes.

  This is an abstract class that should never be instantiated, but rather
  exists for the sake of `jnp.issubdtype`.

  Examples:
    >>> from jax import random
    >>> from jax import dtypes
    >>> key = random.key(0)
    >>> jnp.issubdtype(key.dtype, dtypes.extended)
    True
  """
class prng_key(extended, metaclass=abc.ABCMeta):
    """Scalar class for PRNG Key dtypes.

  This is an abstract class that should never be instantiated, but rather
  exists for the sake of `jnp.issubdtype`.

  Examples:
    >>> from jax import random
    >>> from jax import dtypes
    >>> key = random.key(0)
    >>> jnp.issubdtype(key.dtype, dtypes.prng_key)
    True
  """

class ExtendedDType(metaclass=abc.ABCMeta):
    """Abstract Base Class for extended dtypes"""
    @property
    @abc.abstractmethod
    def type(self) -> type: ...

float8_e4m3b11fnuz: type[np.generic]
float8_e4m3fn: type[np.generic]
float8_e4m3fnuz: type[np.generic]
float8_e5m2: type[np.generic]
float8_e5m2fnuz: type[np.generic]
bfloat16: type[np.generic]
int4: type[np.generic]
uint4: type[np.generic]
bool_: type
int_: type
uint: type
float_: type
complex_: type
float0: np.dtype

def to_numeric_dtype(dtype: DTypeLike) -> DType:
    """Promotes a dtype into an numeric dtype, if it is not already one."""
def to_inexact_dtype(dtype: DTypeLike) -> DType:
    """Promotes a dtype into an inexact dtype, if it is not already one."""
def to_complex_dtype(dtype: DTypeLike) -> DType: ...
@overload
def canonicalize_dtype(dtype: Any, allow_extended_dtype: Literal[False] = False, allow_opaque_dtype: Any = None) -> DType: ...
@overload
def canonicalize_dtype(dtype: Any, allow_extended_dtype: bool = False, allow_opaque_dtype: Any = None) -> DType | ExtendedDType: ...

python_scalar_dtypes: dict[type, DType]

def scalar_type_of(x: Any) -> type:
    """Return the scalar type associated with a JAX value."""
def coerce_to_array(x: Any, dtype: DTypeLike | None = None) -> np.ndarray:
    """Coerces a scalar or NumPy array to an np.array.

  Handles Python scalar type promotion according to JAX's rules, not NumPy's
  rules.
  """

iinfo: Incomplete
finfo: Incomplete

def issubdtype(a: DTypeLike, b: DTypeLike) -> bool:
    """Returns True if first argument is a typecode lower/equal in type hierarchy.

  This is like :func:`numpy.issubdtype`, but can handle dtype extensions such as
  :obj:`jax.dtypes.bfloat16` and `jax.dtypes.prng_key`.
  """
can_cast = np.can_cast
JAXType = type | DType

class TypePromotionError(ValueError): ...

def promote_types(a: DTypeLike, b: DTypeLike) -> DType:
    """Returns the type to which a binary operation should cast its arguments.

  For details of JAX's type promotion semantics, see :ref:`type-promotion`.

  Args:
    a: a :class:`numpy.dtype` or a dtype specifier.
    b: a :class:`numpy.dtype` or a dtype specifier.

  Returns:
    A :class:`numpy.dtype` object.
  """
def is_weakly_typed(x: Any) -> bool: ...
def is_python_scalar(x: Any) -> bool: ...
def check_valid_dtype(dtype: DType) -> None: ...
def dtype(x: Any, *, canonicalize: bool = False) -> DType:
    """Return the dtype object for a value or type, optionally canonicalized based on X64 mode."""
@overload
def result_type(*args: Any, return_weak_type_flag: Literal[True]) -> tuple[DType, bool]: ...
@overload
def result_type(*args: Any, return_weak_type_flag: Literal[False] = False) -> DType: ...
@overload
def result_type(*args: Any, return_weak_type_flag: bool = False) -> DType | tuple[DType, bool]: ...
def check_user_dtype_supported(dtype, fun_name: Incomplete | None = None) -> None: ...
def safe_to_cast(input_dtype_or_value: Any, output_dtype_or_value: Any) -> bool:
    """Check if a dtype/value is safe to cast to another dtype/value

  Args:
    input_dtype_or_value: a dtype or value (to be passed to result_type)
      representing the source dtype.
    output_dtype_or_value: a dtype or value (to be passed to result_type)
      representing the target dtype.

  Returns:
    boolean representing whether the values are safe to cast according to
    default type promotion semantics.

  Raises:
    TypePromotionError: if the inputs have differing types and no type promotion
    path under the current jax_numpy_dtype_promotion setting.

  Examples:

    >>> safe_to_cast('int32', 'float64')
    True
    >>> safe_to_cast('float64', 'int32')
    False
    >>> safe_to_cast('float32', 'complex64')
    True
    >>> safe_to_cast('complex64', 'float64')
    False
  """
