from _typeshed import Incomplete
from jax._src import ad_util as ad_util, core as core
from jax._src.interpreters import ad as ad, batching as batching
from jax._src.lax import lax as lax
from jax._src.state.types import AbstractRef as AbstractRef, AccumEffect as AccumEffect, ReadEffect as ReadEffect, WriteEffect as WriteEffect
from jax._src.typing import Array as Array
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip, tuple_insert as tuple_insert
from typing import Any

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
get_p: Incomplete
Indexer = tuple[int | slice | Array, ...]

def ref_get(ref: Any, idx: Indexer) -> Array:
    """Reads a value from a `Ref`, a.k.a. value <- ref[idx]."""

swap_p: Incomplete

def ref_swap(ref: AbstractRef, idx: Indexer, value: Array) -> Array:
    """Sets a `Ref`'s value and returns the original value."""
def ref_set(ref: AbstractRef, idx: Indexer, value: Array) -> None:
    """Sets a `Ref`'s value, a.k.a. ref[idx] <- value."""

addupdate_p: Incomplete

def ref_addupdate(ref: AbstractRef, idx: Indexer, x: Array) -> None:
    """Mutates a ref with an additive update i.e. `ref[idx] += x`."""

pp_ref: Incomplete

def addupdate_jvp_rule(primals: list[Any], tangents: list[Any], **params: Any): ...
def addupdate_transpose(cts_in, ref, x, *idx, **params): ...
