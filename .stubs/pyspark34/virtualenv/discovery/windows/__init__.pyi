from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.discovery.py_info import PythonInfo

__all__ = ['Pep514PythonInfo', 'propose_interpreters']

class Pep514PythonInfo(PythonInfo):
    """A Python information acquired from PEP-514."""

def propose_interpreters(spec, cache_dir, env) -> Generator[Incomplete, None, Incomplete]: ...
