from .discover import Discover
from .py_info import PythonInfo
from _typeshed import Incomplete

__all__ = ['get_interpreter', 'Builtin', 'PathPythonInfo']

class Builtin(Discover):
    python_spec: Incomplete
    app_data: Incomplete
    try_first_with: Incomplete
    def __init__(self, options) -> None: ...
    @classmethod
    def add_parser_arguments(cls, parser) -> None: ...
    def run(self): ...

def get_interpreter(key, try_first_with, app_data: Incomplete | None = None, env: Incomplete | None = None): ...

class LazyPathDump:
    pos: Incomplete
    path: Incomplete
    env: Incomplete
    def __init__(self, pos, path, env) -> None: ...

class PathPythonInfo(PythonInfo):
    """python info from path."""
