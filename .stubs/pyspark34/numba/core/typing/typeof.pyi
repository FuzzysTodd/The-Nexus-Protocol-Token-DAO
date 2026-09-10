import enum
from _typeshed import Incomplete
from numba.core import errors as errors, types as types, utils as utils
from numba.np import numpy_support as numpy_support
from typing import NamedTuple

class Purpose(enum.Enum):
    argument: int
    constant: int

class _TypeofContext(NamedTuple):
    purpose: Incomplete

def typeof(val, purpose=...):
    """
    Get the Numba type of a Python value for the given purpose.
    """
def typeof_impl(val, c):
    """
    Generic typeof() implementation.
    """
def typeof_numpy_random_bitgen(val, c): ...
def typeof_random_generator(val, c): ...
