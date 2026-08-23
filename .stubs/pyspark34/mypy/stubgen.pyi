import mypy.mixedtraverser
import mypy.traverser
from _typeshed import Incomplete
from mypy.build import build as build
from mypy.errors import CompileError as CompileError, Errors as Errors
from mypy.find_sources import InvalidSourceList as InvalidSourceList, create_source_list as create_source_list
from mypy.modulefinder import BuildSource as BuildSource, FindModuleCache as FindModuleCache, ModuleNotFoundReason as ModuleNotFoundReason, SearchPaths as SearchPaths, default_lib_path as default_lib_path
from mypy.moduleinspect import ModuleInspect as ModuleInspect
from mypy.nodes import ARG_NAMED as ARG_NAMED, ARG_POS as ARG_POS, ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, AssignmentStmt as AssignmentStmt, Block as Block, BytesExpr as BytesExpr, CallExpr as CallExpr, ClassDef as ClassDef, ComparisonExpr as ComparisonExpr, Decorator as Decorator, DictExpr as DictExpr, EllipsisExpr as EllipsisExpr, Expression as Expression, FloatExpr as FloatExpr, FuncBase as FuncBase, FuncDef as FuncDef, IS_ABSTRACT as IS_ABSTRACT, IfStmt as IfStmt, Import as Import, ImportAll as ImportAll, ImportFrom as ImportFrom, IndexExpr as IndexExpr, IntExpr as IntExpr, ListExpr as ListExpr, MemberExpr as MemberExpr, MypyFile as MypyFile, NOT_ABSTRACT as NOT_ABSTRACT, NameExpr as NameExpr, OpExpr as OpExpr, OverloadedFuncDef as OverloadedFuncDef, Statement as Statement, StrExpr as StrExpr, TupleExpr as TupleExpr, TypeInfo as TypeInfo, UnaryExpr as UnaryExpr, Var as Var
from mypy.options import Options as MypyOptions
from mypy.stubdoc import Sig as Sig, find_unique_signatures as find_unique_signatures, parse_all_signatures as parse_all_signatures
from mypy.stubgenc import DocstringSignatureGenerator as DocstringSignatureGenerator, ExternalSignatureGenerator as ExternalSignatureGenerator, FallbackSignatureGenerator as FallbackSignatureGenerator, SignatureGenerator as SignatureGenerator, generate_stub_for_c_module as generate_stub_for_c_module
from mypy.stubutil import CantImport as CantImport, common_dir_prefix as common_dir_prefix, fail_missing as fail_missing, find_module_path_and_all_py3 as find_module_path_and_all_py3, generate_guarded as generate_guarded, remove_misplaced_type_comments as remove_misplaced_type_comments, report_missing as report_missing, walk_packages as walk_packages
from mypy.traverser import all_yield_expressions as all_yield_expressions, has_return_statement as has_return_statement, has_yield_expression as has_yield_expression, has_yield_from_expression as has_yield_from_expression
from mypy.types import AnyType as AnyType, CallableType as CallableType, Instance as Instance, NoneType as NoneType, OVERLOAD_NAMES as OVERLOAD_NAMES, TPDICT_NAMES as TPDICT_NAMES, TYPED_NAMEDTUPLE_NAMES as TYPED_NAMEDTUPLE_NAMES, TupleType as TupleType, Type as Type, TypeList as TypeList, TypeStrVisitor as TypeStrVisitor, UnboundType as UnboundType, UnionType as UnionType, get_proper_type as get_proper_type
from mypy.visitor import NodeVisitor as NodeVisitor
from typing import Iterable
from typing_extensions import Final

TYPING_MODULE_NAMES: Final[Incomplete]
VENDOR_PACKAGES: Final[Incomplete]
BLACKLIST: Final[Incomplete]
EXTRA_EXPORTED: Final[Incomplete]
IGNORED_DUNDERS: Final[Incomplete]
METHODS_WITH_RETURN_VALUE: Final[Incomplete]
KNOWN_MAGIC_METHODS_RETURN_TYPES: Final[Incomplete]

class Options:
    """Represents stubgen options.

    This class is mutable to simplify testing.
    """
    pyversion: Incomplete
    no_import: Incomplete
    doc_dir: Incomplete
    search_path: Incomplete
    interpreter: Incomplete
    decointerpreter: Incomplete
    parse_only: Incomplete
    ignore_errors: Incomplete
    include_private: Incomplete
    output_dir: Incomplete
    modules: Incomplete
    packages: Incomplete
    files: Incomplete
    verbose: Incomplete
    quiet: Incomplete
    export_less: Incomplete
    def __init__(self, pyversion: tuple[int, int], no_import: bool, doc_dir: str, search_path: list[str], interpreter: str, parse_only: bool, ignore_errors: bool, include_private: bool, output_dir: str, modules: list[str], packages: list[str], files: list[str], verbose: bool, quiet: bool, export_less: bool) -> None: ...

class StubSource:
    """A single source for stub: can be a Python or C module.

    A simple extension of BuildSource that also carries the AST and
    the value of __all__ detected at runtime.
    """
    source: Incomplete
    runtime_all: Incomplete
    ast: Incomplete
    def __init__(self, module: str, path: str | None = None, runtime_all: list[str] | None = None) -> None: ...
    @property
    def module(self) -> str: ...
    @property
    def path(self) -> str | None: ...

EMPTY: Final[str]
FUNC: Final[str]
CLASS: Final[str]
EMPTY_CLASS: Final[str]
VAR: Final[str]
NOT_IN_ALL: Final[str]
ERROR_MARKER: Final[str]

class AnnotationPrinter(TypeStrVisitor):
    """Visitor used to print existing annotations in a file.

    The main difference from TypeStrVisitor is a better treatment of
    unbound types.

    Notes:
    * This visitor doesn't add imports necessary for annotations, this is done separately
      by ImportTracker.
    * It can print all kinds of types, but the generated strings may not be valid (notably
      callable types) since it prints the same string that reveal_type() does.
    * For Instance types it prints the fully qualified names.
    """
    stubgen: Incomplete
    def __init__(self, stubgen: StubGenerator) -> None: ...
    def visit_any(self, t: AnyType) -> str: ...
    def visit_unbound_type(self, t: UnboundType) -> str: ...
    def visit_none_type(self, t: None) -> str: ...
    def visit_type_list(self, t: TypeList) -> str: ...
    def visit_union_type(self, t: UnionType) -> str: ...
    def args_str(self, args: Iterable[Type]) -> str:
        """Convert an array of arguments to strings and join the results with commas.

        The main difference from list_str is the preservation of quotes for string
        arguments
        """

class AliasPrinter(NodeVisitor[str]):
    """Visitor used to collect type aliases _and_ type variable definitions.

    Visit r.h.s of the definition to get the string representation of type alias.
    """
    stubgen: Incomplete
    def __init__(self, stubgen: StubGenerator) -> None: ...
    def visit_call_expr(self, node: CallExpr) -> str: ...
    def visit_name_expr(self, node: NameExpr) -> str: ...
    def visit_member_expr(self, o: MemberExpr) -> str: ...
    def visit_str_expr(self, node: StrExpr) -> str: ...
    def visit_index_expr(self, node: IndexExpr) -> str: ...
    def visit_tuple_expr(self, node: TupleExpr) -> str: ...
    def visit_list_expr(self, node: ListExpr) -> str: ...
    def visit_dict_expr(self, o: DictExpr) -> str: ...
    def visit_ellipsis(self, node: EllipsisExpr) -> str: ...
    def visit_op_expr(self, o: OpExpr) -> str: ...

class ImportTracker:
    """Record necessary imports during stub generation."""
    module_for: Incomplete
    direct_imports: Incomplete
    reverse_alias: Incomplete
    required_names: Incomplete
    reexports: Incomplete
    def __init__(self) -> None: ...
    def add_import_from(self, module: str, names: list[tuple[str, str | None]]) -> None: ...
    def add_import(self, module: str, alias: str | None = None) -> None: ...
    def require_name(self, name: str) -> None: ...
    def reexport(self, name: str) -> None:
        """Mark a given non qualified name as needed in __all__.

        This means that in case it comes from a module, it should be
        imported with an alias even is the alias is the same as the name.
        """
    def import_lines(self) -> list[str]:
        """The list of required import lines (as strings with python code)."""

def find_defined_names(file: MypyFile) -> set[str]: ...

class DefinitionFinder(mypy.traverser.TraverserVisitor):
    """Find names of things defined at the top level of a module."""
    names: Incomplete
    def __init__(self) -> None: ...
    def visit_class_def(self, o: ClassDef) -> None: ...
    def visit_func_def(self, o: FuncDef) -> None: ...

def find_referenced_names(file: MypyFile) -> set[str]: ...

class ReferenceFinder(mypy.mixedtraverser.MixedTraverserVisitor):
    """Find all name references (both local and global)."""
    refs: Incomplete
    def __init__(self) -> None: ...
    def visit_block(self, block: Block) -> None: ...
    def visit_name_expr(self, e: NameExpr) -> None: ...
    def visit_instance(self, t: Instance) -> None: ...
    def visit_unbound_type(self, t: UnboundType) -> None: ...
    def visit_tuple_type(self, t: TupleType) -> None: ...
    def visit_callable_type(self, t: CallableType) -> None: ...
    def add_ref(self, fullname: str) -> None: ...

class StubGenerator(mypy.traverser.TraverserVisitor):
    """Generate stub text from a mypy AST."""
    import_tracker: Incomplete
    analyzed: Incomplete
    export_less: Incomplete
    defined_names: Incomplete
    method_names: Incomplete
    def __init__(self, _all_: list[str] | None, include_private: bool = False, analyzed: bool = False, export_less: bool = False) -> None: ...
    module: Incomplete
    path: Incomplete
    referenced_names: Incomplete
    def visit_mypy_file(self, o: MypyFile) -> None: ...
    def visit_overloaded_func_def(self, o: OverloadedFuncDef) -> None:
        """@property with setters and getters, @overload chain and some others."""
    def visit_func_def(self, o: FuncDef) -> None: ...
    def is_none_expr(self, expr: Expression) -> bool: ...
    def visit_decorator(self, o: Decorator) -> None: ...
    def process_decorator(self, o: Decorator) -> None:
        """Process a series of decorators.

        Only preserve certain special decorators such as @abstractmethod.
        """
    def get_fullname(self, expr: Expression) -> str:
        """Return the full name resolving imports and import aliases."""
    def visit_class_def(self, o: ClassDef) -> None: ...
    def get_base_types(self, cdef: ClassDef) -> list[str]:
        """Get list of base classes for a class."""
    def visit_block(self, o: Block) -> None: ...
    def visit_assignment_stmt(self, o: AssignmentStmt) -> None: ...
    def is_namedtuple(self, expr: CallExpr) -> bool: ...
    def is_typed_namedtuple(self, expr: CallExpr) -> bool: ...
    def process_namedtuple(self, lvalue: NameExpr, rvalue: CallExpr) -> None: ...
    def is_typeddict(self, expr: CallExpr) -> bool: ...
    def process_typeddict(self, lvalue: NameExpr, rvalue: CallExpr) -> None: ...
    def annotate_as_incomplete(self, lvalue: NameExpr) -> None: ...
    def is_alias_expression(self, expr: Expression, top_level: bool = True) -> bool:
        """Return True for things that look like target for an alias.

        Used to know if assignments look like type aliases, function alias,
        or module alias.
        """
    def process_typealias(self, lvalue: NameExpr, rvalue: Expression) -> None: ...
    def visit_if_stmt(self, o: IfStmt) -> None: ...
    def visit_import_all(self, o: ImportAll) -> None: ...
    def visit_import_from(self, o: ImportFrom) -> None: ...
    def visit_import(self, o: Import) -> None: ...
    def get_init(self, lvalue: str, rvalue: Expression, annotation: Type | None = None) -> str | None:
        """Return initializer for a variable.

        Return None if we've generated one already or if the variable is internal.
        """
    def add(self, string: str) -> None:
        """Add text to generated stub."""
    def add_decorator(self, name: str, require_name: bool = False) -> None: ...
    def clear_decorators(self) -> None: ...
    def typing_name(self, name: str) -> str: ...
    def add_typing_import(self, name: str) -> None:
        """Add a name to be imported for typing, unless it's imported already.

        The import will be internal to the stub.
        """
    def add_import_line(self, line: str) -> None:
        """Add a line of text to the import section, unless it's already there."""
    def output(self) -> str:
        """Return the text for the stub."""
    def is_not_in_all(self, name: str) -> bool: ...
    def is_private_name(self, name: str, fullname: str | None = None) -> bool: ...
    def is_private_member(self, fullname: str) -> bool: ...
    def get_str_type_of_node(self, rvalue: Expression, can_infer_optional: bool = False, can_be_any: bool = True) -> str: ...
    def print_annotation(self, t: Type) -> str: ...
    def is_top_level(self) -> bool:
        """Are we processing the top level of a file?"""
    def record_name(self, name: str) -> None:
        """Mark a name as defined.

        This only does anything if at the top level of a module.
        """
    def is_recorded_name(self, name: str) -> bool:
        """Has this name been recorded previously?"""

def find_method_names(defs: list[Statement]) -> set[str]: ...

class SelfTraverser(mypy.traverser.TraverserVisitor):
    results: Incomplete
    def __init__(self) -> None: ...
    def visit_assignment_stmt(self, o: AssignmentStmt) -> None: ...

def find_self_initializers(fdef: FuncBase) -> list[tuple[str, Expression]]:
    """Find attribute initializers in a method.

    Return a list of pairs (attribute name, r.h.s. expression).
    """
def get_qualified_name(o: Expression) -> str: ...
def remove_blacklisted_modules(modules: list[StubSource]) -> list[StubSource]: ...
def is_blacklisted_path(path: str) -> bool: ...
def normalize_path_separators(path: str) -> str: ...
def collect_build_targets(options: Options, mypy_opts: MypyOptions) -> tuple[list[StubSource], list[StubSource]]:
    """Collect files for which we need to generate stubs.

    Return list of Python modules and C modules.
    """
def find_module_paths_using_imports(modules: list[str], packages: list[str], verbose: bool, quiet: bool) -> tuple[list[StubSource], list[StubSource]]:
    """Find path and runtime value of __all__ (if possible) for modules and packages.

    This function uses runtime Python imports to get the information.
    """
def is_non_library_module(module: str) -> bool:
    """Does module look like a test module or a script?"""
def translate_module_name(module: str, relative: int) -> tuple[str, int]: ...
def find_module_paths_using_search(modules: list[str], packages: list[str], search_path: list[str], pyversion: tuple[int, int]) -> list[StubSource]:
    """Find sources for modules and packages requested.

    This function just looks for source files at the file system level.
    This is used if user passes --no-import, and will not find C modules.
    Exit if some of the modules or packages can't be found.
    """
def mypy_options(stubgen_options: Options) -> MypyOptions:
    """Generate mypy options using the flag passed by user."""
def parse_source_file(mod: StubSource, mypy_options: MypyOptions) -> None:
    """Parse a source file.

    On success, store AST in the corresponding attribute of the stub source.
    If there are syntax errors, print them and exit.
    """
def generate_asts_for_modules(py_modules: list[StubSource], parse_only: bool, mypy_options: MypyOptions, verbose: bool) -> None:
    """Use mypy to parse (and optionally analyze) source files."""
def generate_stub_from_ast(mod: StubSource, target: str, parse_only: bool = False, include_private: bool = False, export_less: bool = False) -> None:
    """Use analysed (or just parsed) AST to generate type stub for single file.

    If directory for target doesn't exist it will created. Existing stub
    will be overwritten.
    """
def get_sig_generators(options: Options) -> list[SignatureGenerator]: ...
def collect_docs_signatures(doc_dir: str) -> tuple[dict[str, str], dict[str, str]]:
    """Gather all function and class signatures in the docs.

    Return a tuple (function signatures, class signatures).
    Currently only used for C modules.
    """
def generate_stubs(options: Options) -> None:
    """Main entry point for the program."""

HEADER: str
DESCRIPTION: str

def parse_options(args: list[str]) -> Options: ...
def main(args: list[str] | None = None) -> None: ...
