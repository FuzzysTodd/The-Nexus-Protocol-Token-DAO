from _typeshed import Incomplete
from jax._src import core as core, traceback_util as traceback_util
from jax._src.core import Primitive as Primitive, get_aval as get_aval, lattice_join as lattice_join, raise_to_shaped as raise_to_shaped, valid_jaxtype as valid_jaxtype
from jax._src.tree_util import register_pytree_node as register_pytree_node
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from jax._src.util import safe_map as safe_map
from typing import Any, Callable, TypeVar

T = TypeVar('T')
map = safe_map
jaxval_adders: dict[type, Callable[[ArrayLike, ArrayLike], Array]]

def add_jaxvals(x: ArrayLike, y: ArrayLike) -> Array: ...

add_jaxvals_p: Primitive
add_any_p = add_jaxvals_p

def add_impl(xs, ys): ...
def add_abstract(xs, ys): ...

jaxval_zeros_likers: dict[type, Callable[[Any], Array]]

def instantiate(z: Zero | Array) -> Array: ...
def zeros_like_aval(aval: core.AbstractValue) -> Array: ...

aval_zeros_likers: dict[type, Callable[[Any], Array]]

def zeros_like_jaxval(val: ArrayLike) -> Array: ...

zeros_like_p: Primitive

def zeros_like_impl(example): ...

class Zero:
    aval: Incomplete
    def __init__(self, aval: core.AbstractValue) -> None: ...
    @staticmethod
    def from_value(val: Any) -> Zero: ...

stop_gradient_p: Primitive

class SymbolicZero:
    aval: Incomplete
    def __init__(self, aval: core.AbstractValue) -> None: ...
    def __getattr__(self, name): ...
JaxTypeOrTracer = Any

def replace_internal_symbolic_zeros(x: JaxTypeOrTracer | Zero) -> JaxTypeOrTracer | SymbolicZero: ...
def replace_rule_output_symbolic_zeros(x: JaxTypeOrTracer | SymbolicZero) -> JaxTypeOrTracer | Zero: ...
