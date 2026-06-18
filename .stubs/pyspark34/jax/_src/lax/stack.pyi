from jax import lax as lax
from typing import Any

class Stack:
    """A bounded functional stack implementation. Elements may be pytrees."""
    def __init__(self, size, data) -> None:
        """Private constructor."""
    @staticmethod
    def create(capacity: int, prototype: Any) -> Stack:
        """Creates a stack with size `capacity` with elements like `prototype`.

    `prototype` can be any JAX pytree. This function looks only at its
    structure; the specific values are ignored.
    """
    def empty(self) -> Any:
        """Returns true if the stack is empty."""
    def push(self, elem: Any) -> Stack:
        """Pushes `elem` onto the stack, returning the updated stack."""
    def pop(self) -> tuple[Any, Stack]:
        """Pops from the stack, returning an (elem, updated stack) pair."""
    def flatten(self): ...
    @staticmethod
    def unflatten(treedef, leaves): ...
