import dataclasses
from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import core as core, effects as effects
from jax._src.typing import Array as Array
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip
from typing import Any, Generic, TypeVar

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete

class RefEffect(effects.JaxprInputEffect):
    name: str
    def __eq__(self, other): ...
    def __hash__(self): ...

class ReadEffect(RefEffect):
    name: str

class WriteEffect(RefEffect):
    name: str

class AccumEffect(RefEffect):
    name: str
StateEffect = ReadEffect | WriteEffect | AccumEffect
Aval = TypeVar('Aval', bound=core.AbstractValue)

@dataclasses.dataclass
class RefIndexer:
    ref: Any
    def __getitem__(self, slc): ...
    def __init__(self, ref) -> None: ...

@dataclasses.dataclass
class RefView:
    ref: Any
    indexer: Any
    @property
    def at(self) -> None: ...
    def __init__(self, ref, indexer) -> None: ...

class AbstractRef(core.AbstractValue, Generic[Aval]):
    inner_aval: Incomplete
    def __init__(self, inner_aval: core.AbstractValue) -> None: ...
    def join(self, other): ...
    ndim: Incomplete
    size: Incomplete
    @property
    def shape(self): ...
    @property
    def dtype(self): ...
    def at(self): ...
    @staticmethod
    def get(tracer, idx=()): ...
    @staticmethod
    def set(tracer, value, idx=()): ...
    def at_least_vspace(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

def get_ref_state_effects(avals: Sequence[core.AbstractValue], effects: core.Effects) -> list[set[StateEffect]]: ...
def shaped_array_ref(shape: tuple[int, ...], dtype, weak_type: bool = False, named_shape: Incomplete | None = None) -> AbstractRef[core.AbstractValue]: ...
