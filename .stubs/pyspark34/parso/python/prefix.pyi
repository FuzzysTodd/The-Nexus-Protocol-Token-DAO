from _typeshed import Incomplete
from collections.abc import Generator
from parso.python.tokenize import group as group
from typing import Tuple

unicode_bom: Incomplete

class PrefixPart:
    parent: Incomplete
    type: Incomplete
    value: Incomplete
    spacing: Incomplete
    start_pos: Incomplete
    def __init__(self, leaf, typ, value, spacing: str = '', start_pos: Incomplete | None = None) -> None: ...
    @property
    def end_pos(self) -> Tuple[int, int]: ...
    def create_spacing_part(self): ...
    def search_ancestor(self, *node_types): ...

def split_prefix(leaf, start_pos) -> Generator[Incomplete, None, None]: ...
