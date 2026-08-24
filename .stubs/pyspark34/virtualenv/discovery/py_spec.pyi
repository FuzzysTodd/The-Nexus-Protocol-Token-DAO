from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['PythonSpec']

class PythonSpec:
    """Contains specification about a Python Interpreter."""
    str_spec: Incomplete
    implementation: Incomplete
    major: Incomplete
    minor: Incomplete
    micro: Incomplete
    architecture: Incomplete
    path: Incomplete
    def __init__(self, str_spec, implementation, major, minor, micro, architecture, path) -> None: ...
    @classmethod
    def from_string_spec(cls, string_spec): ...
    def generate_names(self) -> Generator[Incomplete, None, None]: ...
    @property
    def is_abs(self): ...
    def satisfies(self, spec):
        """Called when there's a candidate metadata spec to see if compatible - e.g. PEP-514 on Windows."""
