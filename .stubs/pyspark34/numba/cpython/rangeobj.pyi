from _typeshed import Incomplete
from numba import prange as prange
from numba.core import cgutils as cgutils, errors as errors, types as types
from numba.core.extending import intrinsic as intrinsic, overload as overload, overload_attribute as overload_attribute, register_jitable as register_jitable
from numba.core.imputils import impl_ret_untracked as impl_ret_untracked, iterator_impl as iterator_impl, lower_builtin as lower_builtin, lower_cast as lower_cast
from numba.core.typing import signature as signature
from numba.cpython.listobj import ListIterInstance as ListIterInstance
from numba.np.arrayobj import make_array as make_array
from numba.parfors.parfor import internal_prange as internal_prange

def make_range_iterator(typ):
    """
    Return the Structure representation of the given *typ* (an
    instance of types.RangeIteratorType).
    """
def make_range_impl(int_type, range_state_type, range_iter_type): ...

range_impl_map: Incomplete

def range_to_range(context, builder, fromty, toty, val): ...
def length_of_iterator(typingctx, val):
    """
    An implementation of len(iter) for internal use.
    Primary use is for array comprehensions (see inline_closurecall).
    """
def make_range_attr(index, attribute): ...
def impl_contains_helper(robj, val): ...
def impl_contains(robj, val): ...
