from _typeshed import Incomplete
from collections.abc import Generator
from torch.backends import ContextProp as ContextProp, PropModule as PropModule
from typing import Any

def is_available() -> bool:
    """Returns a bool indicating if opt_einsum is currently available."""
def get_opt_einsum() -> Any:
    """Returns the opt_einsum package if opt_einsum is currently available, else None."""
def set_flags(_enabled: Incomplete | None = None, _strategy: Incomplete | None = None): ...
def flags(enabled: Incomplete | None = None, strategy: Incomplete | None = None) -> Generator[None, None, None]: ...

class OptEinsumModule(PropModule):
    def __init__(self, m, name) -> None: ...
    enabled: Incomplete
    strategy: Incomplete

enabled: Incomplete
strategy: Incomplete
