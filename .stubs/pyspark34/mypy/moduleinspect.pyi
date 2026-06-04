from _typeshed import Incomplete
from multiprocessing import Queue
from types import ModuleType

class ModuleProperties:
    name: Incomplete
    file: Incomplete
    path: Incomplete
    all: Incomplete
    is_c_module: Incomplete
    subpackages: Incomplete
    def __init__(self, name: str = '', file: str | None = None, path: list[str] | None = None, all: list[str] | None = None, is_c_module: bool = False, subpackages: list[str] | None = None) -> None: ...

def is_c_module(module: ModuleType) -> bool: ...

class InspectError(Exception): ...

def get_package_properties(package_id: str) -> ModuleProperties:
    """Use runtime introspection to get information about a module/package."""
def worker(tasks: Queue[str], results: Queue[str | ModuleProperties], sys_path: list[str]) -> None:
    """The main loop of a worker introspection process."""

class ModuleInspect:
    """Perform runtime introspection of modules in a separate process.

    Reuse the process for multiple modules for efficiency. However, if there is an
    error, retry using a fresh process to avoid cross-contamination of state between
    modules.

    We use a separate process to isolate us from many side effects. For example, the
    import of a module may kill the current process, and we want to recover from that.

    Always use in a with statement for proper clean-up:

      with ModuleInspect() as m:
          p = m.get_package_properties('urllib.parse')
    """
    def __init__(self) -> None: ...
    def close(self) -> None:
        """Free any resources used."""
    def get_package_properties(self, package_id: str) -> ModuleProperties:
        """Return some properties of a module/package using runtime introspection.

        Raise InspectError if the target couldn't be imported.
        """
    def __enter__(self) -> ModuleInspect: ...
    def __exit__(self, *args: object) -> None: ...
