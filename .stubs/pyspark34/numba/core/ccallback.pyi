from _typeshed import Incomplete
from functools import cached_property as cached_property
from numba.core import compiler as compiler, registry as registry
from numba.core.caching import FunctionCache as FunctionCache, NullCache as NullCache
from numba.core.compiler_lock import global_compiler_lock as global_compiler_lock
from numba.core.dispatcher import _FunctionCompiler
from numba.core.typing import signature as signature
from numba.core.typing.ctypes_utils import to_ctypes as to_ctypes

class _CFuncCompiler(_FunctionCompiler): ...

class CFunc:
    """
    A compiled C callback, as created by the @cfunc decorator.
    """
    __qualname__: Incomplete
    __wrapped__: Incomplete
    def __init__(self, pyfunc, sig, locals, options, pipeline_class=...) -> None: ...
    def enable_caching(self) -> None: ...
    def compile(self) -> None: ...
    @property
    def native_name(self):
        """
        The process-wide symbol the C callback is exposed as.
        """
    @property
    def address(self):
        """
        The address of the C callback.
        """
    @cached_property
    def cffi(self):
        """
        A cffi function pointer representing the C callback.
        """
    @cached_property
    def ctypes(self):
        """
        A ctypes function object representing the C callback.
        """
    def inspect_llvm(self):
        """
        Return the LLVM IR of the C callback definition.
        """
    @property
    def cache_hits(self): ...
    def __call__(self, *args, **kwargs): ...
