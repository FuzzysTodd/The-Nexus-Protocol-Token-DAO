import dataclasses
from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import ad_util as ad_util, api_util as api_util, core as core, source_info_util as source_info_util, tree_util as tree_util
from jax._src.config import config as config
from jax._src.interpreters import ad as ad, mlir as mlir
from jax._src.lax import lax as lax
from jax._src.state.primitives import addupdate_p as addupdate_p, get_p as get_p, swap_p as swap_p
from jax._src.state.types import AbstractRef as AbstractRef, RefEffect as RefEffect
from jax._src.state.utils import hoist_consts_to_refs as hoist_consts_to_refs
from jax._src.util import merge_lists as merge_lists, partition_list as partition_list, safe_map as safe_map, safe_zip as safe_zip, split_dict as split_dict, split_list as split_list, weakref_lru_cache as weakref_lru_cache
from typing import Any, Callable, Protocol

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
PyTreeDef: Incomplete

def discharge_state(jaxpr: core.Jaxpr, consts: Sequence[Any], *, should_discharge: bool | Sequence[bool] = True) -> tuple[core.Jaxpr, list[Any]]:
    """Converts a jaxpr that takes in `Ref`s into one that doesn't."""

@dataclasses.dataclass
class Environment:
    env: dict[core.Var, Any]
    def read(self, v: core.Atom) -> Any: ...
    def write(self, v: core.Var, val: Any) -> None: ...
    def __init__(self, env) -> None: ...

class DischargeRule(Protocol):
    def __call__(self, in_avals: Sequence[core.AbstractValue], out_avals: Sequence[core.AbstractValue], *args: Any, **params: Any) -> tuple[Sequence[Any | None], Sequence[Any]]: ...

def register_discharge_rule(prim: core.Primitive): ...

run_state_p: Incomplete

def initial_style_jaxpr(fun: Callable, in_tree: PyTreeDef, in_avals: Sequence[core.AbstractValue]) -> tuple[core.Jaxpr, list[Any], PyTreeDef]: ...
def run_state(f: Callable[..., None]): ...
def run_state_reference(f: Callable[..., None]): ...
