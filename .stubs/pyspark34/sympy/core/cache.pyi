from _typeshed import Incomplete
from typing import Callable

class _cache(list):
    """ List of cached functions """
    def print_cache(self) -> None:
        """print cache info"""
    def clear_cache(self) -> None:
        """clear cache content"""

CACHE: Incomplete
print_cache: Incomplete
clear_cache: Incomplete
USE_CACHE: Incomplete
scs: Incomplete
SYMPY_CACHE_SIZE: Incomplete
cacheit: Incomplete

def cached_property(func):
    """Decorator to cache property method"""
def lazy_function(module: str, name: str) -> Callable:
    """Create a lazy proxy for a function in a module.

    The module containing the function is not imported until the function is used.

    """
