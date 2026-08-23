import os
from typing import Dict, List, Tuple, TypeVar

T = TypeVar('T')
ListLike = List[T] | Tuple[T, ...]
NestedDataStructureLike = T | List[T] | Dict[str, T]
PathLike = str | bytes | os.PathLike
