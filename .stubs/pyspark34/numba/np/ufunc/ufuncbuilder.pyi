from _typeshed import Incomplete
from numba.core import compiler as compiler, config as config, serialize as serialize, sigutils as sigutils, targetconfig as targetconfig, types as types, utils as utils
from numba.core.caching import FunctionCache as FunctionCache, NullCache as NullCache
from numba.core.compiler_lock import global_compiler_lock as global_compiler_lock
from numba.core.decorators import jit as jit
from numba.core.descriptors import TargetDescriptor as TargetDescriptor
from numba.core.errors import NumbaDeprecationWarning as NumbaDeprecationWarning
from numba.core.extending import is_jitted as is_jitted
from numba.core.options import TargetOptions as TargetOptions, include_default_options as include_default_options
from numba.core.registry import cpu_target as cpu_target
from numba.core.target_extension import dispatcher_registry as dispatcher_registry, target_registry as target_registry
from numba.np.numpy_support import as_dtype as as_dtype
from numba.np.ufunc.sigparse import parse_signature as parse_signature
from numba.np.ufunc.wrappers import build_gufunc_wrapper as build_gufunc_wrapper, build_ufunc_wrapper as build_ufunc_wrapper

class UFuncTargetOptions(_options_mixin, TargetOptions):
    def finalize(self, flags, options) -> None: ...

class UFuncTarget(TargetDescriptor):
    options = UFuncTargetOptions
    def __init__(self) -> None: ...
    @property
    def typing_context(self): ...
    @property
    def target_context(self): ...

ufunc_target: Incomplete

class UFuncDispatcher(serialize.ReduceMixin):
    """
    An object handling compilation of various signatures for a ufunc.
    """
    targetdescr = ufunc_target
    py_func: Incomplete
    overloads: Incomplete
    targetoptions: Incomplete
    locals: Incomplete
    cache: Incomplete
    def __init__(self, py_func, locals={}, targetoptions={}) -> None: ...
    def enable_caching(self) -> None: ...
    def compile(self, sig, locals={}, **targetoptions): ...

def parse_identity(identity):
    """
    Parse an identity value and return the corresponding low-level value
    for Numpy.
    """

class _BaseUFuncBuilder:
    def add(self, sig: Incomplete | None = None): ...
    def disable_compile(self) -> None:
        """
        Disable the compilation of new signatures at call time.
        """

class UFuncBuilder(_BaseUFuncBuilder):
    py_func: Incomplete
    identity: Incomplete
    nb_func: Incomplete
    def __init__(self, py_func, identity: Incomplete | None = None, cache: bool = False, targetoptions={}) -> None: ...
    def build_ufunc(self): ...
    def build(self, cres, signature):
        """Slated for deprecation, use
        ufuncbuilder._build_element_wise_ufunc_wrapper().
        """

class GUFuncBuilder(_BaseUFuncBuilder):
    py_func: Incomplete
    identity: Incomplete
    nb_func: Incomplete
    signature: Incomplete
    targetoptions: Incomplete
    cache: Incomplete
    writable_args: Incomplete
    def __init__(self, py_func, signature, identity: Incomplete | None = None, cache: bool = False, targetoptions={}, writable_args=()) -> None: ...
    def build_ufunc(self): ...
    def build(self, cres):
        """
        Returns (dtype numbers, function ptr, EnvironmentObject)
        """
