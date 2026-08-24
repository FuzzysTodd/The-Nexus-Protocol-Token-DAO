import torch
from _typeshed import Incomplete
from torch import fx as fx
from typing import Protocol, Sequence, Tuple

class CompiledFn(Protocol):
    def __call__(self, *args: torch.Tensor) -> Tuple[torch.Tensor, ...]: ...

CompilerFn: Incomplete

def register_backend(compiler_fn: CompilerFn | None = None, name: str | None = None, tags: Sequence[str] = ()):
    """
    Decorator to add a given compiler to the registry to allow calling
    `torch.compile` with string shorthand.  Note: for projects not
    imported by default, it might be easier to pass a function directly
    as a backend and not use a string.

    Args:
        compiler_fn: Callable taking a FX graph and fake tensor inputs
        name: Optional name, defaults to `compiler_fn.__name__`
        tags: Optional set of string tags to categorize backend with
    """

register_debug_backend: Incomplete
register_experimental_backend: Incomplete

def lookup_backend(compiler_fn):
    """Expand backend strings to functions"""
def list_backends(exclude_tags=('debug', 'experimental')):
    '''
    Return valid strings that can be passed to:

        torch.compile(..., backend="name")
    '''
