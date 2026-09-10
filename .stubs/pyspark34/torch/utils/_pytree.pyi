from dataclasses import dataclass
from typing import Any, Callable, Dict, List, NamedTuple, Tuple, Type, TypeVar, overload

T = TypeVar('T')
S = TypeVar('S')
U = TypeVar('U')
R = TypeVar('R')
Context = Any
PyTree = Any
FlattenFunc = Callable[[PyTree], Tuple[List, Context]]
UnflattenFunc = Callable[[List, Context], PyTree]

class NodeDef(NamedTuple):
    flatten_fn: FlattenFunc
    unflatten_fn: UnflattenFunc

SUPPORTED_NODES: Dict[Type[Any], NodeDef]

@dataclass
class TreeSpec:
    type: Any
    context: Context
    children_specs: List['TreeSpec']
    num_leaves = ...
    def __post_init__(self) -> None: ...
    def __init__(self, type, context, children_specs) -> None: ...

class LeafSpec(TreeSpec):
    num_leaves: int
    def __init__(self) -> None: ...

def tree_flatten(pytree: PyTree) -> Tuple[List[Any], TreeSpec]:
    """Flattens a pytree into a list of values and a TreeSpec that can be used
    to reconstruct the pytree.
    """
def tree_unflatten(values: List[Any], spec: TreeSpec) -> PyTree:
    """Given a list of values and a TreeSpec, builds a pytree.
    This is the inverse operation of `tree_flatten`.
    """
def tree_map(fn: Any, pytree: PyTree) -> PyTree: ...
Type2 = Tuple[Type[T], Type[S]]
Type3 = Tuple[Type[T], Type[S], Type[U]]
TypeAny = Type[Any] | Tuple[Type[Any], ...]
Fn3 = Callable[[T | S | U], R]
Fn2 = Callable[[T | S], R]
Fn = Callable[[T], R]
FnAny = Callable[[Any], R]
MapOnlyFn = Callable[[T], Callable[[Any], Any]]

@overload
def map_only(ty: Type2[T, S]) -> MapOnlyFn[Fn2[T, S, Any]]: ...
@overload
def map_only(ty: Type[T]) -> MapOnlyFn[Fn[T, Any]]: ...
@overload
def map_only(ty: TypeAny) -> MapOnlyFn[FnAny[Any]]: ...
@overload
def tree_map_only(ty: Type[T], fn: Fn[T, Any], pytree: PyTree) -> PyTree: ...
@overload
def tree_map_only(ty: Type2[T, S], fn: Fn2[T, S, Any], pytree: PyTree) -> PyTree: ...
@overload
def tree_map_only(ty: Type3[T, S, U], fn: Fn3[T, S, U, Any], pytree: PyTree) -> PyTree: ...
def tree_all(pred: Callable[[Any], bool], pytree: PyTree) -> bool: ...
def tree_any(pred: Callable[[Any], bool], pytree: PyTree) -> bool: ...
@overload
def tree_all_only(ty: Type[T], pred: Fn[T, bool], pytree: PyTree) -> bool: ...
@overload
def tree_all_only(ty: Type2[T, S], pred: Fn2[T, S, bool], pytree: PyTree) -> bool: ...
@overload
def tree_all_only(ty: Type3[T, S, U], pred: Fn3[T, S, U, bool], pytree: PyTree) -> bool: ...
@overload
def tree_any_only(ty: Type[T], pred: Fn[T, bool], pytree: PyTree) -> bool: ...
@overload
def tree_any_only(ty: Type2[T, S], pred: Fn2[T, S, bool], pytree: PyTree) -> bool: ...
