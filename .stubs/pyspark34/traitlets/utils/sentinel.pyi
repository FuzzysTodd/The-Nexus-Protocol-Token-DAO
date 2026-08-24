import typing as t
from _typeshed import Incomplete

class Sentinel:
    name: Incomplete
    module: Incomplete
    __doc__: Incomplete
    def __init__(self, name: str, module: t.Any, docstring: str | None = None) -> None: ...
    def __copy__(self) -> Sentinel: ...
    def __deepcopy__(self, memo: t.Any) -> Sentinel: ...
