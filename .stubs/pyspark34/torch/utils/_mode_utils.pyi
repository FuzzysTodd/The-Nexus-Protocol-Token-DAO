from collections.abc import Generator
from typing import TypeVar

T = TypeVar('T')

def all_same_mode(modes): ...
def no_dispatch() -> Generator[None, None, None]: ...
