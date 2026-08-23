from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['enable_python_dispatcher', 'no_python_dispatcher']

def no_python_dispatcher() -> Generator[None, None, None]: ...
def enable_python_dispatcher() -> Generator[None, None, None]: ...

class Lit:
    s: Incomplete
    def __init__(self, s) -> None: ...
