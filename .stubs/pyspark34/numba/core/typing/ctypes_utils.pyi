from .typeof import typeof_impl as typeof_impl
from numba.core import types as types
from numba.core.typing import templates as templates

def from_ctypes(ctypeobj):
    """
    Convert the given ctypes type to a Numba type.
    """
def to_ctypes(ty):
    """
    Convert the given Numba type to a ctypes type.
    """
def is_ctypes_funcptr(obj): ...
def get_pointer(ctypes_func):
    """
    Get a pointer to the underlying function for a ctypes function as an
    integer.
    """
def make_function_type(cfnptr):
    """
    Return a Numba type for the given ctypes function pointer.
    """
