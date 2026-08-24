from _typeshed import Incomplete
from numba.core import callconv as callconv, cgutils as cgutils, errors as errors, types as types, typing as typing, utils as utils
from numba.core.extending import intrinsic as intrinsic, overload as overload
from numba.core.imputils import Registry as Registry, force_error_model as force_error_model, impl_ret_new_ref as impl_ret_new_ref
from numba.core.typing import npydecl as npydecl
from numba.cpython import builtins as builtins
from numba.np import arrayobj as arrayobj, numpy_support as numpy_support, ufunc_db as ufunc_db
from numba.np.numpy_support import from_dtype as from_dtype, select_array_wrapper as select_array_wrapper, ufunc_find_matching_loop as ufunc_find_matching_loop
from typing import NamedTuple

registry: Incomplete

class _ScalarIndexingHelper:
    def update_indices(self, loop_indices, name) -> None: ...
    def as_values(self) -> None: ...

class _ScalarHelper:
    '''Helper class to handle scalar arguments (and result).
    Note that store_data is only used when generating code for
    a scalar ufunc and to write the output value.

    For loading, the value is directly used without having any
    kind of indexing nor memory backing it up. This is the use
    for input arguments.

    For storing, a variable is created in the stack where the
    value will be written.

    Note that it is not supported (as it is unneeded for our
    current use-cases) reading back a stored value. This class
    will always "load" the original value it got at its creation.
    '''
    context: Incomplete
    builder: Incomplete
    val: Incomplete
    base_type: Incomplete
    shape: Incomplete
    def __init__(self, ctxt, bld, val, ty) -> None: ...
    def create_iter_indices(self): ...
    def load_data(self, indices): ...
    def store_data(self, indices, val) -> None: ...
    @property
    def return_val(self): ...

class _ArrayIndexingHelper(NamedTuple('_ArrayIndexingHelper', [('array', Incomplete), ('indices', Incomplete)])):
    def update_indices(self, loop_indices, name) -> None: ...
    def as_values(self):
        """
        The indexing helper is built using alloca for each value, so it
        actually contains pointers to the actual indices to load. Note
        that update_indices assumes the same. This method returns the
        indices as values
        """

class _ArrayHelper(NamedTuple('_ArrayHelper', [('context', Incomplete), ('builder', Incomplete), ('shape', Incomplete), ('strides', Incomplete), ('data', Incomplete), ('layout', Incomplete), ('base_type', Incomplete), ('ndim', Incomplete), ('return_val', Incomplete)])):
    """Helper class to handle array arguments/result.
    It provides methods to generate code loading/storing specific
    items as well as support code for handling indices.
    """
    def create_iter_indices(self): ...
    def load_data(self, indices): ...
    def store_data(self, indices, value) -> None: ...

def numpy_ufunc_kernel(context, builder, sig, args, ufunc, kernel_class): ...

class _Kernel:
    context: Incomplete
    builder: Incomplete
    outer_sig: Incomplete
    def __init__(self, context, builder, outer_sig) -> None: ...
    def cast(self, val, fromty, toty):
        """Numpy uses cast semantics that are different from standard Python
        (for example, it does allow casting from complex to float).

        This method acts as a patch to context.cast so that it allows
        complex to real/int casts.

        """

def register_ufunc_kernel(ufunc, kernel, lower): ...
def register_unary_operator_kernel(operator, ufunc, kernel, lower, inplace: bool = False): ...
def register_binary_operator_kernel(op, ufunc, kernel, lower, inplace: bool = False): ...
def array_positive_impl(context, builder, sig, args):
    """Lowering function for +(array) expressions.  Defined here
    (numba.targets.npyimpl) since the remaining array-operator
    lowering functions are also registered in this module.
    """
def register_ufuncs(ufuncs, lower) -> None: ...
def numpy_dtype(desc):
    """Provide an implementation so that numpy.dtype function can be lowered.
    """
