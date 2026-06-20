import enum
import functools
from _typeshed import Incomplete
from jax import lax as lax, tree_util as tree_util
from jax._src import ad_util as ad_util, state as state
from jax._src.pallas import indexing as indexing
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip
from jax.interpreters import ad as ad, mlir as mlir, xla as xla
from typing import Any

partial = functools.partial
Slice: Incomplete
NDIndexer: Incomplete
map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
program_id_p: Incomplete

def program_id(axis): ...
def program_id_bind(*, axis: int): ...

class AtomicOpType(enum.Enum):
    XCHG: str
    ADD: str
    MAX: str
    MIN: str
    AND: str
    OR: str
    XOR: str

atomic_rmw_p: Incomplete

def atomic_rmw(x_ref, idx, val, *, mask: Any | None = None, atomic_type: AtomicOpType): ...

atomic_xchg: Incomplete
atomic_add: Incomplete
atomic_max: Incomplete
atomic_min: Incomplete
atomic_and: Incomplete
atomic_or: Incomplete
atomic_xor: Incomplete
atomic_cas_p: Incomplete

def atomic_cas(ref, cmp, val): ...

max_contiguous_p: Incomplete

def max_contiguous(x, values): ...

multiple_of_p: Incomplete

def multiple_of(x, values): ...

load_p: Incomplete
swap_p: Incomplete

def load(x_ref, idx, *, mask: Incomplete | None = None, other: Incomplete | None = None, cache_modifier: str = '', eviction_policy: str = '', volatile: bool = False): ...
def swap(x_ref, idx, val, *, mask: Incomplete | None = None, eviction_policy: str = '') -> Any: ...
def store(x_ref, idx, val, *, mask: Incomplete | None = None, eviction_policy: str = '') -> None: ...
def dot(a, b, trans_a: bool = False, trans_b: bool = False, allow_tf32: bool | None = None, precision: Incomplete | None = None): ...
