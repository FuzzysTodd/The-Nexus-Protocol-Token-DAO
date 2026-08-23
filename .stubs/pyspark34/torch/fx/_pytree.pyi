from torch.utils._pytree import LeafSpec as LeafSpec, PyTree as PyTree, TreeSpec as TreeSpec
from typing import Any, Callable, Dict, List, Type

FlattenFuncSpec = Callable[[PyTree, TreeSpec], List]
SUPPORTED_NODES: Dict[Type[Any], Any]

def register_pytree_flatten_spec(typ: Any, flatten_fn_spec: FlattenFuncSpec) -> None: ...
def tree_flatten_spec(pytree: PyTree, spec: TreeSpec) -> List[Any]: ...
