from _typeshed import Incomplete
from mypy.modulefinder import ModuleNotFoundReason as ModuleNotFoundReason
from mypy.moduleinspect import InspectError as InspectError, ModuleInspect as ModuleInspect
from typing import Iterator
from typing_extensions import overload

NOT_IMPORTABLE_MODULES: Incomplete

class CantImport(Exception):
    module: Incomplete
    message: Incomplete
    def __init__(self, module: str, message: str) -> None: ...

def walk_packages(inspect: ModuleInspect, packages: list[str], verbose: bool = False) -> Iterator[str]:
    """Iterates through all packages and sub-packages in the given list.

    This uses runtime imports (in another process) to find both Python and C modules.
    For Python packages we simply pass the __path__ attribute to pkgutil.walk_packages() to
    get the content of the package (all subpackages and modules).  However, packages in C
    extensions do not have this attribute, so we have to roll out our own logic: recursively
    find all modules imported in the package that have matching names.
    """
def find_module_path_using_sys_path(module: str, sys_path: list[str]) -> str | None: ...
def find_module_path_and_all_py3(inspect: ModuleInspect, module: str, verbose: bool) -> tuple[str | None, list[str] | None] | None:
    """Find module and determine __all__ for a Python 3 module.

    Return None if the module is a C module. Return (module_path, __all__) if
    it is a Python module. Raise CantImport if import failed.
    """
def generate_guarded(mod: str, target: str, ignore_errors: bool = True, verbose: bool = False) -> Iterator[None]:
    """Ignore or report errors during stub generation.

    Optionally report success.
    """
def report_missing(mod: str, message: str | None = '', traceback: str = '') -> None: ...
def fail_missing(mod: str, reason: ModuleNotFoundReason) -> None: ...
@overload
def remove_misplaced_type_comments(source: bytes) -> bytes: ...
@overload
def remove_misplaced_type_comments(source: str) -> str: ...
def common_dir_prefix(paths: list[str]) -> str: ...
