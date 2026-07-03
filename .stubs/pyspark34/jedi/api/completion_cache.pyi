from _typeshed import Incomplete
from typing import Callable, Tuple

CacheValues = Tuple[str, str, str]
CacheValuesCallback = Callable[[], CacheValues]

def save_entry(module_name: str, name: str, cache: CacheValues) -> None: ...

get_type: Incomplete
get_docstring_signature: Incomplete
get_docstring: Incomplete
