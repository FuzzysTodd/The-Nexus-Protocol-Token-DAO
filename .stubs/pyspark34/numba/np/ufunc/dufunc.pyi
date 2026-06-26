from _typeshed import Incomplete
from numba import jit as jit, typeof as typeof
from numba.core import cgutils as cgutils, serialize as serialize, sigutils as sigutils, types as types
from numba.core.extending import is_jitted as is_jitted
from numba.core.typing import npydecl as npydecl
from numba.core.typing.templates import AbstractTemplate as AbstractTemplate, signature as signature
from numba.np import numpy_support as numpy_support
from numba.np.ufunc import _internal, ufuncbuilder as ufuncbuilder
from numba.parfors import array_analysis as array_analysis

def make_dufunc_kernel(_dufunc): ...

class DUFuncLowerer:
    """Callable class responsible for lowering calls to a specific DUFunc.
    """
    kernel: Incomplete
    libs: Incomplete
    def __init__(self, dufunc) -> None: ...
    def __call__(self, context, builder, sig, args): ...

class DUFunc(serialize.ReduceMixin, _internal._DUFunc):
    """
    Dynamic universal function (DUFunc) intended to act like a normal
    Numpy ufunc, but capable of call-time (just-in-time) compilation
    of fast loops specialized to inputs.
    """
    def __init__(self, py_func, identity: Incomplete | None = None, cache: bool = False, targetoptions={}) -> None: ...
    def build_ufunc(self):
        """
        For compatibility with the various *UFuncBuilder classes.
        """
    @property
    def targetoptions(self): ...
    @property
    def nin(self): ...
    @property
    def nout(self): ...
    @property
    def nargs(self): ...
    @property
    def ntypes(self): ...
    @property
    def types(self): ...
    @property
    def identity(self): ...
    def disable_compile(self) -> None:
        """
        Disable the compilation of new signatures at call time.
        """
    def add(self, sig):
        """
        Compile the DUFunc for the given signature.
        """
    def find_ewise_function(self, ewise_types):
        """
        Given a tuple of element-wise argument types, find a matching
        signature in the dispatcher.

        Return a 2-tuple containing the matching signature, and
        compilation result.  Will return two None's if no matching
        signature was found.
        """
