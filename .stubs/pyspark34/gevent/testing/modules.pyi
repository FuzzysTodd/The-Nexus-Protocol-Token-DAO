from . import sysinfo as sysinfo, util as util
from _typeshed import Incomplete
from collections.abc import Generator

OPTIONAL_MODULES: Incomplete
EXCLUDED_MODULES: Incomplete

def walk_modules(basedir: Incomplete | None = None, modpath: Incomplete | None = None, include_so: bool = False, recursive: bool = False, check_optional: bool = True, include_tests: bool = False, optional_modules=..., excluded_modules=...) -> Generator[Incomplete, None, None]:
    """
    Find gevent modules, yielding tuples of ``(path, importable_module_name)``.

    :keyword bool check_optional: If true (the default), then if we discover a
       module that is known to be optional on this system (such as a backend),
       we will attempt to import it; if the import fails, it will not be returned.
       If false, then we will not make such an attempt, the caller will need to be prepared
       for an `ImportError`; the caller can examine *optional_modules* against
       the yielded *importable_module_name*.
    """
