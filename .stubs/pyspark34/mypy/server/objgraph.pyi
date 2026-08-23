from _typeshed import Incomplete
from typing import Iterator
from typing_extensions import Final

method_descriptor_type: Final[Incomplete]
method_wrapper_type: Final[Incomplete]
wrapper_descriptor_type: Final[Incomplete]
FUNCTION_TYPES: Final[Incomplete]
ATTR_BLACKLIST: Final[Incomplete]
ATOMIC_TYPE_BLACKLIST: Final[Incomplete]
COLLECTION_TYPE_BLACKLIST: Final[Incomplete]
TYPE_BLACKLIST: Final[Incomplete]

def isproperty(o: object, attr: str) -> bool: ...
def get_edge_candidates(o: object) -> Iterator[tuple[object, object]]: ...
def get_edges(o: object) -> Iterator[tuple[object, object]]: ...
def get_reachable_graph(root: object) -> tuple[dict[int, object], dict[int, tuple[int, object]]]: ...
def get_path(o: object, seen: dict[int, object], parents: dict[int, tuple[int, object]]) -> list[tuple[object, object]]: ...
