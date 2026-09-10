from _typeshed import Incomplete
from enum import IntEnum
from numba.core import cgutils as cgutils, types as types, typing as typing
from numba.core.errors import TypingError as TypingError
from numba.core.extending import intrinsic as intrinsic, lower_builtin as lower_builtin, models as models, overload as overload, overload_attribute as overload_attribute, overload_method as overload_method, register_jitable as register_jitable, register_model as register_model
from numba.core.imputils import RefType as RefType, impl_ret_borrowed as impl_ret_borrowed, iternext_impl as iternext_impl
from numba.core.types import ListType as ListType, ListTypeIterableType as ListTypeIterableType, ListTypeIteratorType as ListTypeIteratorType, NoneType as NoneType, Type as Type
from numba.cpython import listobj as listobj

ll_list_type: Incomplete
ll_listiter_type: Incomplete
ll_voidptr_type: Incomplete
ll_status: Incomplete
ll_ssize_t: Incomplete
ll_bytes: Incomplete
INDEXTY: Incomplete
index_types: Incomplete
DEFAULT_ALLOCATED: int

class ListModel(models.StructModel):
    def __init__(self, dmm, fe_type) -> None: ...

class ListIterModel(models.StructModel):
    def __init__(self, dmm, fe_type) -> None: ...

class ListStatus(IntEnum):
    """Status code for other list operations.
    """
    LIST_OK: Incomplete
    LIST_ERR_INDEX: int
    LIST_ERR_NO_MEMORY: int
    LIST_ERR_MUTATED: int
    LIST_ERR_ITER_EXHAUSTED: int
    LIST_ERR_IMMUTABLE: int

class ErrorHandler:
    """ErrorHandler for calling codegen functions from this file.

    Stores the state needed to raise an exception from nopython mode.
    """
    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self, builder, status, msg) -> None: ...

def list_is(context, builder, sig, args): ...
def new_list(item, allocated=...):
    """Construct a new list. (Not implemented in the interpreter yet)

    Parameters
    ----------
    item: TypeRef
        Item type of the new list.
    allocated: int
        number of items to pre-allocate

    """
def impl_new_list(item, allocated=...):
    """Creates a new list.

    Parameters
    ----------
    item: Numba type
        type of the list item.
    allocated: int
        number of items to pre-allocate

    """
def impl_len(l):
    """len(list)
    """
def impl_allocated(l):
    """list._allocated()
    """
def impl_is_mutable(l):
    """list._is_mutable()"""
def impl_make_mutable(l):
    """list._make_mutable()"""
def impl_make_immutable(l):
    """list._make_immutable()"""
def impl_append(l, item): ...
def fix_index(tyctx, list_ty, index_ty): ...
def handle_index(l, index):
    """Handle index.

    If the index is negative, convert it. If the index is out of range, raise
    an IndexError.
    """
def handle_slice(l, s):
    """Handle slice.

    Convert a slice object for a given list into a range object that can be
    used to index the list. Many subtle caveats here, especially if the step is
    negative.
    """
def impl_getitem(l, index): ...
def impl_setitem(l, index, item): ...
def impl_pop(l, index: int = -1): ...
def impl_delitem(l, index): ...
def impl_contains(l, item): ...
def impl_count(l, item): ...
def impl_extend(l, iterable): ...
def impl_insert(l, index, item): ...
def impl_remove(l, item): ...
def impl_clear(l): ...
def impl_reverse(l): ...
def impl_copy(l): ...
def impl_index(l, item, start: Incomplete | None = None, end: Incomplete | None = None): ...
def ol_list_sort(lst, key: Incomplete | None = None, reverse: bool = False): ...
def ol_getitem_unchecked(lst, index): ...
def ol_list_hash(lst): ...
def impl_dtype(l): ...
def impl_equals(this, other): ...
def impl_not_equals(this, other): ...
def compare_not_none(this, other):
    """Oldschool (python 2.x) cmp.

       if this < other return -1
       if this = other return 0
       if this > other return 1
    """
def compare_some_none(this, other, this_is_none, other_is_none):
    """Oldschool (python 2.x) cmp for None typed lists.

       if this < other return -1
       if this = other return 0
       if this > other return 1
    """
def compare_helper(this, other, accepted): ...
def impl_less_than(this, other): ...
def impl_less_than_or_equal(this, other): ...
def impl_greater_than(this, other): ...
def impl_greater_than_or_equal(this, other): ...

class ListIterInstance:
    def __init__(self, context, builder, iter_type, iter_val) -> None: ...
    @classmethod
    def from_list(cls, context, builder, iter_type, list_val): ...
    @property
    def size(self): ...
    @property
    def value(self): ...
    def getitem(self, index): ...
    @property
    def index(self): ...
    @index.setter
    def index(self, value) -> None: ...

def getiter_list(context, builder, sig, args): ...
def iternext_listiter(context, builder, sig, args, result) -> None: ...
