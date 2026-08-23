import inspect
import mypy.types
import types
import typing_extensions
from _typeshed import Incomplete
from mypy import nodes as nodes
from mypy.config_parser import parse_config_file as parse_config_file
from mypy.evalexpr import UNKNOWN as UNKNOWN, evaluate_expression as evaluate_expression
from mypy.options import Options as Options
from mypy.util import FancyFormatter as FancyFormatter, bytes_to_human_readable_repr as bytes_to_human_readable_repr, is_dunder as is_dunder, plural_s as plural_s
from typing import Any, Generic, Iterator, TypeVar

class Missing:
    """Marker object for things that are missing (from a stub or the runtime)."""

MISSING: typing_extensions.Final
T = TypeVar('T')
MaybeMissing: typing_extensions.TypeAlias

class StubtestFailure(Exception): ...

class Error:
    object_path: Incomplete
    object_desc: Incomplete
    message: Incomplete
    stub_object: Incomplete
    runtime_object: Incomplete
    stub_desc: Incomplete
    runtime_desc: Incomplete
    def __init__(self, object_path: list[str], message: str, stub_object: MaybeMissing[nodes.Node], runtime_object: MaybeMissing[Any], *, stub_desc: str | None = None, runtime_desc: str | None = None) -> None:
        '''Represents an error found by stubtest.

        :param object_path: Location of the object with the error,
            e.g. ``["module", "Class", "method"]``
        :param message: Error message
        :param stub_object: The mypy node representing the stub
        :param runtime_object: Actual object obtained from the runtime
        :param stub_desc: Specialised description for the stub object, should you wish
        :param runtime_desc: Specialised description for the runtime object, should you wish

        '''
    def is_missing_stub(self) -> bool:
        """Whether or not the error is for something missing from the stub."""
    def is_positional_only_related(self) -> bool:
        """Whether or not the error is for something being (or not being) positional-only."""
    def get_description(self, concise: bool = False) -> str:
        """Returns a description of the error.

        :param concise: Whether to return a concise, one-line description

        """

def silent_import_module(module_name: str) -> types.ModuleType: ...
def test_module(module_name: str) -> Iterator[Error]:
    """Tests a given module's stub against introspecting it at runtime.

    Requires the stub to have been built already, accomplished by a call to ``build_stubs``.

    :param module_name: The module to test

    """
def verify(stub: MaybeMissing[nodes.Node], runtime: MaybeMissing[Any], object_path: list[str]) -> Iterator[Error]:
    """Entry point for comparing a stub to a runtime object.

    We use single dispatch based on the type of ``stub``.

    :param stub: The mypy node representing a part of the stub
    :param runtime: The runtime object corresponding to ``stub``

    """
def verify_mypyfile(stub: nodes.MypyFile, runtime: MaybeMissing[types.ModuleType], object_path: list[str]) -> Iterator[Error]: ...
def verify_typeinfo(stub: nodes.TypeInfo, runtime: MaybeMissing[type[Any]], object_path: list[str]) -> Iterator[Error]: ...
def maybe_strip_cls(name: str, args: list[nodes.Argument]) -> list[nodes.Argument]: ...

class Signature(Generic[T]):
    pos: Incomplete
    kwonly: Incomplete
    varpos: Incomplete
    varkw: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def from_funcitem(stub: nodes.FuncItem) -> Signature[nodes.Argument]: ...
    @staticmethod
    def from_inspect_signature(signature: inspect.Signature) -> Signature[inspect.Parameter]: ...
    @staticmethod
    def from_overloadedfuncdef(stub: nodes.OverloadedFuncDef) -> Signature[nodes.Argument]:
        """Returns a Signature from an OverloadedFuncDef.

        If life were simple, to verify_overloadedfuncdef, we'd just verify_funcitem for each of its
        items. Unfortunately, life isn't simple and overloads are pretty deceitful. So instead, we
        try and combine the overload's items into a single signature that is compatible with any
        lies it might try to tell.

        """

def verify_funcitem(stub: nodes.FuncItem, runtime: MaybeMissing[Any], object_path: list[str]) -> Iterator[Error]: ...
def verify_none(stub: Missing, runtime: MaybeMissing[Any], object_path: list[str]) -> Iterator[Error]: ...
def verify_var(stub: nodes.Var, runtime: MaybeMissing[Any], object_path: list[str]) -> Iterator[Error]: ...
def verify_overloadedfuncdef(stub: nodes.OverloadedFuncDef, runtime: MaybeMissing[Any], object_path: list[str]) -> Iterator[Error]: ...
def verify_typevarexpr(stub: nodes.TypeVarExpr, runtime: MaybeMissing[Any], object_path: list[str]) -> Iterator[Error]: ...
def verify_paramspecexpr(stub: nodes.ParamSpecExpr, runtime: MaybeMissing[Any], object_path: list[str]) -> Iterator[Error]: ...
def verify_decorator(stub: nodes.Decorator, runtime: MaybeMissing[Any], object_path: list[str]) -> Iterator[Error]: ...
def verify_typealias(stub: nodes.TypeAlias, runtime: MaybeMissing[Any], object_path: list[str]) -> Iterator[Error]: ...

IGNORED_MODULE_DUNDERS: typing_extensions.Final
IGNORABLE_CLASS_DUNDERS: typing_extensions.Final

def is_probably_private(name: str) -> bool: ...
def is_probably_a_function(runtime: Any) -> bool: ...
def is_read_only_property(runtime: object) -> bool: ...
def safe_inspect_signature(runtime: Any) -> inspect.Signature | None: ...
def is_subtype_helper(left: mypy.types.Type, right: mypy.types.Type) -> bool:
    """Checks whether ``left`` is a subtype of ``right``."""
def get_mypy_type_of_runtime_value(runtime: Any) -> mypy.types.Type | None:
    """Returns a mypy type object representing the type of ``runtime``.

    Returns None if we can't find something that works.

    """
def build_stubs(modules: list[str], options: Options, find_submodules: bool = False) -> list[str]:
    """Uses mypy to construct stub objects for the given modules.

    This sets global state that ``get_stub`` can access.

    Returns all modules we might want to check. If ``find_submodules`` is False, this is equal
    to ``modules``.

    :param modules: List of modules to build stubs for.
    :param options: Mypy options for finding and building stubs.
    :param find_submodules: Whether to attempt to find submodules of the given modules as well.

    """
def get_stub(module: str) -> nodes.MypyFile | None:
    """Returns a stub object for the given module, if we've built one."""
def get_typeshed_stdlib_modules(custom_typeshed_dir: str | None, version_info: tuple[int, int] | None = None) -> list[str]:
    """Returns a list of stdlib modules in typeshed (for current Python version)."""
def get_allowlist_entries(allowlist_file: str) -> Iterator[str]: ...

class _Arguments:
    modules: list[str]
    concise: bool
    ignore_missing_stub: bool
    ignore_positional_only: bool
    allowlist: list[str]
    generate_allowlist: bool
    ignore_unused_allowlist: bool
    mypy_config_file: str
    custom_typeshed_dir: str
    check_typeshed: bool
    version: str

def test_stubs(args: _Arguments, use_builtins_fixtures: bool = False) -> int:
    """This is stubtest! It's time to test the stubs!"""
def parse_options(args: list[str]) -> _Arguments: ...
def main() -> int: ...
