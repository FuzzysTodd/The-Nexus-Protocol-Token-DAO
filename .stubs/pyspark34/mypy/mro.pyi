from mypy.nodes import TypeInfo as TypeInfo
from mypy.types import Instance as Instance
from mypy.typestate import type_state as type_state
from typing import Callable

def calculate_mro(info: TypeInfo, obj_type: Callable[[], Instance] | None = None) -> None:
    """Calculate and set mro (method resolution order).

    Raise MroError if cannot determine mro.
    """

class MroError(Exception):
    """Raised if a consistent mro cannot be determined for a class."""

def linearize_hierarchy(info: TypeInfo, obj_type: Callable[[], Instance] | None = None) -> list[TypeInfo]: ...
def merge(seqs: list[list[TypeInfo]]) -> list[TypeInfo]: ...
