import ast
from _typeshed import Incomplete
from importlib.abc import MetaPathFinder
from importlib.machinery import SourceFileLoader
from typing import Iterable, Type

def optimized_cache_from_source(path, debug_override: Incomplete | None = None): ...

class TypeguardTransformer(ast.NodeVisitor):
    def __init__(self) -> None: ...
    def visit_Module(self, node: ast.Module): ...
    def visit_ClassDef(self, node: ast.ClassDef): ...
    def visit_FunctionDef(self, node: ast.FunctionDef): ...

class TypeguardLoader(SourceFileLoader):
    def source_to_code(self, data, path, *, _optimize: int = -1): ...
    def exec_module(self, module): ...

class TypeguardFinder(MetaPathFinder):
    """
    Wraps another path finder and instruments the module with ``@typechecked`` if
    :meth:`should_instrument` returns ``True``.

    Should not be used directly, but rather via :func:`~.install_import_hook`.

    .. versionadded:: 2.6

    """
    packages: Incomplete
    def __init__(self, packages, original_pathfinder) -> None: ...
    def find_spec(self, fullname, path: Incomplete | None = None, target: Incomplete | None = None): ...
    def should_instrument(self, module_name: str) -> bool:
        """
        Determine whether the module with the given name should be instrumented.

        :param module_name: full name of the module that is about to be imported (e.g. ``xyz.abc``)

        """

class ImportHookManager:
    hook: Incomplete
    def __init__(self, hook: MetaPathFinder) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def uninstall(self) -> None: ...

def install_import_hook(packages: Iterable[str], *, cls: Type[TypeguardFinder] = ...) -> ImportHookManager:
    """
    Install an import hook that decorates classes and functions with ``@typechecked``.

    This only affects modules loaded **after** this hook has been installed.

    :return: a context manager that uninstalls the hook on exit (or when you call ``.uninstall()``)

    .. versionadded:: 2.6

    """
