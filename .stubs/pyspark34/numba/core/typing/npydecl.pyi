from _typeshed import Incomplete
from numba import pndindex as pndindex
from numba.core import config as config, types as types, utils as utils
from numba.core.errors import NumbaAssertionError as NumbaAssertionError, NumbaPerformanceWarning as NumbaPerformanceWarning, NumbaTypeError as NumbaTypeError, TypingError as TypingError
from numba.core.typing.templates import AbstractTemplate as AbstractTemplate, AttributeTemplate as AttributeTemplate, CallableTemplate as CallableTemplate, Registry as Registry, signature as signature
from numba.np.numpy_support import as_dtype as as_dtype, carray as carray, farray as farray, from_dtype as from_dtype, resolve_output_type as resolve_output_type, supported_ufunc_loop as supported_ufunc_loop, ufunc_find_matching_loop as ufunc_find_matching_loop

registry: Incomplete
infer: Incomplete
infer_global: Incomplete
infer_getattr: Incomplete

class Numpy_rules_ufunc(AbstractTemplate):
    @property
    def ufunc(self): ...
    def generic(self, args, kws): ...

class NumpyRulesArrayOperator(Numpy_rules_ufunc):
    @property
    def ufunc(self): ...
    @classmethod
    def install_operations(cls) -> None: ...
    def generic(self, args, kws):
        """Overloads and calls base class generic() method, returning
        None if a TypingError occurred.

        Returning None for operators is important since operators are
        heavily overloaded, and by suppressing type errors, we allow
        type inference to check other possibilities before giving up
        (particularly user-defined operators).
        """

class NumpyRulesInplaceArrayOperator(NumpyRulesArrayOperator):
    def generic(self, args, kws): ...

class NumpyRulesUnaryArrayOperator(NumpyRulesArrayOperator):
    def generic(self, args, kws): ...

math_operations: Incomplete
trigonometric_functions: Incomplete
bit_twiddling_functions: Incomplete
comparison_functions: Incomplete
floating_functions: Incomplete
logic_functions: Incomplete

def register_numpy_ufunc(name, register_global=...) -> None: ...

all_ufuncs: Incomplete
supported_ufuncs: Incomplete
supported_array_operators: Incomplete

class Numpy_method_redirection(AbstractTemplate):
    """
    A template redirecting a Numpy global function (e.g. np.sum) to an
    array method of the same name (e.g. ndarray.sum).
    """
    prefer_literal: bool
    def generic(self, args, kws): ...

np_types: Incomplete

def register_number_classes(register_global) -> None: ...
def parse_shape(shape):
    """
    Given a shape, return the number of dimensions.
    """
def parse_dtype(dtype):
    """
    Return the dtype of a type, if it is either a DtypeSpec (used for most
    dtypes) or a TypeRef (used for record types).
    """

class BaseStackTemplate(CallableTemplate):
    def generic(self): ...

class MatMulTyperMixin:
    def matmul_typer(self, a, b, out: Incomplete | None = None):
        """
        Typer function for Numpy matrix multiplication.
        """

class NdEnumerate(AbstractTemplate):
    def generic(self, args, kws): ...

class NdIter(AbstractTemplate):
    def generic(self, args, kws): ...

class NdIndex(AbstractTemplate):
    def generic(self, args, kws): ...
