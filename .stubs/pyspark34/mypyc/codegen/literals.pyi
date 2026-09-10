from _typeshed import Incomplete
from typing import Final, FrozenSet, Tuple

LiteralValue = str | bytes | int | bool | float | complex | Tuple[object, ...] | FrozenSet[object] | None
NUM_SINGLETONS: Final[int]

class Literals:
    """Collection of literal values used in a compilation group and related helpers."""
    str_literals: Incomplete
    bytes_literals: Incomplete
    int_literals: Incomplete
    float_literals: Incomplete
    complex_literals: Incomplete
    tuple_literals: Incomplete
    frozenset_literals: Incomplete
    def __init__(self) -> None: ...
    def record_literal(self, value: LiteralValue) -> None:
        """Ensure that the literal value is available in generated code."""
    def literal_index(self, value: LiteralValue) -> int:
        """Return the index to the literals array for given value."""
    def num_literals(self) -> int: ...
    def encoded_str_values(self) -> list[bytes]: ...
    def encoded_int_values(self) -> list[bytes]: ...
    def encoded_bytes_values(self) -> list[bytes]: ...
    def encoded_float_values(self) -> list[str]: ...
    def encoded_complex_values(self) -> list[str]: ...
    def encoded_tuple_values(self) -> list[str]: ...
    def encoded_frozenset_values(self) -> list[str]: ...

def format_int(n: int) -> bytes:
    """Format an integer using a variable-length binary encoding."""
def format_str_literal(s: str) -> bytes: ...
def float_to_c(x: float) -> str:
    """Return C literal representation of a float value."""
