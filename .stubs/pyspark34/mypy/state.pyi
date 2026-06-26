from _typeshed import Incomplete
from typing import Iterator
from typing_extensions import Final

class StrictOptionalState:
    strict_optional: Incomplete
    def __init__(self, strict_optional: bool) -> None: ...
    def strict_optional_set(self, value: bool) -> Iterator[None]: ...

state: Final[Incomplete]
find_occurrences: tuple[str, str] | None
