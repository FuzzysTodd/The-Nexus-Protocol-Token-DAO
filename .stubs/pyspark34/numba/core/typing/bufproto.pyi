from numba.core import types as types

def decode_pep3118_format(fmt, itemsize):
    """
    Return the Numba type for an item with format string *fmt* and size
    *itemsize* (in bytes).
    """
def get_type_class(typ):
    """
    Get the Numba type class for buffer-compatible Python *typ*.
    """
def infer_layout(val):
    """
    Infer layout of the given memoryview *val*.
    """
