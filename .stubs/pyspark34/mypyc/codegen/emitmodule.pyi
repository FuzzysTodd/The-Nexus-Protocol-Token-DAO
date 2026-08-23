from _typeshed import Incomplete
from mypy.build import BuildResult as BuildResult, BuildSource, State as State
from mypy.fscache import FileSystemCache as FileSystemCache
from mypy.nodes import MypyFile as MypyFile
from mypy.options import Options as Options
from mypy.plugin import Plugin, ReportConfigContext as ReportConfigContext
from mypyc.codegen.cstring import c_string_initializer as c_string_initializer
from mypyc.codegen.emit import Emitter as Emitter, EmitterContext as EmitterContext, HeaderDeclaration as HeaderDeclaration, c_array_initializer as c_array_initializer
from mypyc.codegen.emitclass import generate_class as generate_class, generate_class_type_decl as generate_class_type_decl
from mypyc.codegen.emitfunc import generate_native_function as generate_native_function, native_function_header as native_function_header
from mypyc.codegen.emitwrapper import generate_legacy_wrapper_function as generate_legacy_wrapper_function, generate_wrapper_function as generate_wrapper_function, legacy_wrapper_function_header as legacy_wrapper_function_header, wrapper_function_header as wrapper_function_header
from mypyc.codegen.literals import Literals as Literals
from mypyc.common import MODULE_PREFIX as MODULE_PREFIX, PREFIX as PREFIX, RUNTIME_C_FILES as RUNTIME_C_FILES, TOP_LEVEL_NAME as TOP_LEVEL_NAME, shared_lib_name as shared_lib_name, short_id_from_name as short_id_from_name, use_vectorcall as use_vectorcall
from mypyc.errors import Errors as Errors
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.func_ir import FuncIR as FuncIR
from mypyc.ir.module_ir import ModuleIR as ModuleIR, ModuleIRs as ModuleIRs, deserialize_modules as deserialize_modules
from mypyc.ir.ops import DeserMaps as DeserMaps, LoadLiteral as LoadLiteral
from mypyc.ir.rtypes import RType as RType
from mypyc.irbuild.main import build_ir as build_ir
from mypyc.irbuild.mapper import Mapper as Mapper
from mypyc.irbuild.prepare import load_type_map as load_type_map
from mypyc.namegen import NameGenerator as NameGenerator, exported_name as exported_name
from mypyc.options import CompilerOptions as CompilerOptions
from mypyc.transform.exceptions import insert_exception_handling as insert_exception_handling
from mypyc.transform.refcount import insert_ref_count_opcodes as insert_ref_count_opcodes
from mypyc.transform.uninit import insert_uninit_checks as insert_uninit_checks
from typing import Iterable, List, Tuple, TypeVar

Group = Tuple[List[BuildSource], str | None]
Groups = List[Group]
FileContents = List[Tuple[str, str]]

class MarkedDeclaration:
    """Add a mark, useful for topological sort."""
    declaration: Incomplete
    mark: bool
    def __init__(self, declaration: HeaderDeclaration, mark: bool) -> None: ...

class MypycPlugin(Plugin):
    """Plugin for making mypyc interoperate properly with mypy incremental mode.

    Basically the point of this plugin is to force mypy to recheck things
    based on the demands of mypyc in a couple situations:
      * Any modules in the same group must be compiled together, so we
        tell mypy that modules depend on all their groupmates.
      * If the IR metadata is missing or stale or any of the generated
        C source files associated missing or stale, then we need to
        recompile the module so we mark it as stale.
    """
    group_map: Incomplete
    compiler_options: Incomplete
    metastore: Incomplete
    def __init__(self, options: Options, compiler_options: CompilerOptions, groups: Groups) -> None: ...
    def report_config_data(self, ctx: ReportConfigContext) -> tuple[str | None, list[str]] | None: ...
    def get_additional_deps(self, file: MypyFile) -> list[tuple[int, str, int]]: ...

def parse_and_typecheck(sources: list[BuildSource], options: Options, compiler_options: CompilerOptions, groups: Groups, fscache: FileSystemCache | None = None, alt_lib_path: str | None = None) -> BuildResult: ...
def compile_scc_to_ir(scc: list[MypyFile], result: BuildResult, mapper: Mapper, compiler_options: CompilerOptions, errors: Errors) -> ModuleIRs:
    """Compile an SCC into ModuleIRs.

    Any modules that this SCC depends on must have either compiled or
    loaded from a cache into mapper.

    Arguments:
        scc: The list of MypyFiles to compile
        result: The BuildResult from the mypy front-end
        mapper: The Mapper object mapping mypy ASTs to class and func IRs
        compiler_options: The compilation options
        errors: Where to report any errors encountered

    Returns the IR of the modules.
    """
def compile_modules_to_ir(result: BuildResult, mapper: Mapper, compiler_options: CompilerOptions, errors: Errors) -> ModuleIRs:
    """Compile a collection of modules into ModuleIRs.

    The modules to compile are specified as part of mapper's group_map.

    Returns the IR of the modules.
    """
def compile_ir_to_c(groups: Groups, modules: ModuleIRs, result: BuildResult, mapper: Mapper, compiler_options: CompilerOptions) -> dict[str | None, list[tuple[str, str]]]:
    """Compile a collection of ModuleIRs to C source text.

    Returns a dictionary mapping group names to a list of (file name,
    file text) pairs.
    """
def get_ir_cache_name(id: str, path: str, options: Options) -> str: ...
def get_state_ir_cache_name(state: State) -> str: ...
def write_cache(modules: ModuleIRs, result: BuildResult, group_map: dict[str, str | None], ctext: dict[str | None, list[tuple[str, str]]]) -> None:
    """Write out the cache information for modules.

    Each module has the following cache information written (which is
    in addition to the cache information written by mypy itself):
      * A serialized version of its mypyc IR, minus the bodies of
        functions. This allows code that depends on it to use
        these serialized data structures when compiling against it
        instead of needing to recompile it. (Compiling against a
        module requires access to both its mypy and mypyc data
        structures.)
      * The hash of the mypy metadata cache file for the module.
        This is used to ensure that the mypyc cache and the mypy
        cache are in sync and refer to the same version of the code.
        This is particularly important if mypyc crashes/errors/is
        stopped after mypy has written its cache but before mypyc has.
      * The hashes of all of the source file outputs for the group
        the module is in. This is so that the module will be
        recompiled if the source outputs are missing.
    """
def load_scc_from_cache(scc: list[MypyFile], result: BuildResult, mapper: Mapper, ctx: DeserMaps) -> ModuleIRs:
    """Load IR for an SCC of modules from the cache.

    Arguments and return are as compile_scc_to_ir.
    """
def compile_modules_to_c(result: BuildResult, compiler_options: CompilerOptions, errors: Errors, groups: Groups) -> tuple[ModuleIRs, list[FileContents]]:
    '''Compile Python module(s) to the source of Python C extension modules.

    This generates the source code for the "shared library" module
    for each group. The shim modules are generated in mypyc.build.
    Each shared library module provides, for each module in its group,
    a PyCapsule containing an initialization function.
    Additionally, it provides a capsule containing an export table of
    pointers to all of the group\'s functions and static variables.

    Arguments:
        result: The BuildResult from the mypy front-end
        compiler_options: The compilation options
        errors: Where to report any errors encountered
        groups: The groups that we are compiling. See documentation of Groups type above.

    Returns the IR of the modules and a list containing the generated files for each group.
    '''
def generate_function_declaration(fn: FuncIR, emitter: Emitter) -> None: ...
def pointerize(decl: str, name: str) -> str:
    """Given a C decl and its name, modify it to be a declaration to a pointer."""
def group_dir(group_name: str) -> str:
    """Given a group name, return the relative directory path for it."""

class GroupGenerator:
    modules: Incomplete
    source_paths: Incomplete
    context: Incomplete
    names: Incomplete
    simple_inits: Incomplete
    group_name: Incomplete
    use_shared_lib: Incomplete
    compiler_options: Incomplete
    multi_file: Incomplete
    def __init__(self, modules: dict[str, ModuleIR], source_paths: dict[str, str], group_name: str | None, group_map: dict[str, str | None], names: NameGenerator, compiler_options: CompilerOptions) -> None:
        """Generator for C source for a compilation group.

        The code for a compilation group contains an internal and an
        external .h file, and then one .c if not in multi_file mode or
        one .c file per module if in multi_file mode.)

        Arguments:
            modules: (name, ir) pairs for each module in the group
            source_paths: Map from module names to source file paths
            group_name: The name of the group (or None if this is single-module compilation)
            group_map: A map of modules to their group names
            names: The name generator for the compilation
            multi_file: Whether to put each module in its own source file regardless
                        of group structure.
        """
    @property
    def group_suffix(self) -> str: ...
    @property
    def short_group_suffix(self) -> str: ...
    def generate_c_for_modules(self) -> list[tuple[str, str]]: ...
    def generate_literal_tables(self) -> None:
        """Generate tables containing descriptions of Python literals to construct.

        We will store the constructed literals in a single array that contains
        literals of all types. This way we can refer to an arbitrary literal by
        its index.
        """
    def generate_export_table(self, decl_emitter: Emitter, code_emitter: Emitter) -> None:
        '''Generate the declaration and definition of the group\'s export struct.

        To avoid needing to deal with deeply platform specific issues
        involving dynamic library linking (and some possibly
        insurmountable issues involving cyclic dependencies), compiled
        code accesses functions and data in other compilation groups
        via an explicit "export struct".

        Each group declares a struct type that contains a pointer to
        every function and static variable it exports. It then
        populates this struct and stores a pointer to it in a capsule
        stored as an attribute named \'exports\' on the group\'s shared
        library\'s python module.

        On load, a group\'s init function will import all of its
        dependencies\' exports tables using the capsule mechanism and
        copy the contents into a local copy of the table (to eliminate
        the need for a pointer indirection when accessing it).

        Then, all calls to functions in another group and accesses to statics
        from another group are done indirectly via the export table.

        For example, a group containing a module b, where b contains a class B
        and a function bar, would declare an export table like:
            struct export_table_b {
                PyTypeObject **CPyType_B;
                PyObject *(*CPyDef_B)(CPyTagged cpy_r_x);
                CPyTagged (*CPyDef_B___foo)(PyObject *cpy_r_self, CPyTagged cpy_r_y);
                tuple_T2OI (*CPyDef_bar)(PyObject *cpy_r_x);
                char (*CPyDef___top_level__)(void);
            };
        that would be initialized with:
            static struct export_table_b exports = {
                &CPyType_B,
                &CPyDef_B,
                &CPyDef_B___foo,
                &CPyDef_bar,
                &CPyDef___top_level__,
            };
        To call `b.foo`, then, a function in another group would do
        `exports_b.CPyDef_bar(...)`.
        '''
    def generate_shared_lib_init(self, emitter: Emitter) -> None:
        """Generate the init function for a shared library.

        A shared library contains all of the actual code for a
        compilation group.

        The init function is responsible for creating Capsules that
        wrap pointers to the initialization function of all the real
        init functions for modules in this shared library as well as
        the export table containing all of the exported functions and
        values from all the modules.

        These capsules are stored in attributes of the shared library.
        """
    def generate_globals_init(self, emitter: Emitter) -> None: ...
    def generate_module_def(self, emitter: Emitter, module_name: str, module: ModuleIR) -> None:
        """Emit the PyModuleDef struct for a module and the module init function."""
    def generate_top_level_call(self, module: ModuleIR, emitter: Emitter) -> None:
        """Generate call to function representing module top level."""
    def toposort_declarations(self) -> list[HeaderDeclaration]:
        """Topologically sort the declaration dict by dependencies.

        Declarations can require other declarations to come prior in C (such as declaring structs).
        In order to guarantee that the C output will compile the declarations will thus need to
        be properly ordered. This simple DFS guarantees that we have a proper ordering.

        This runs in O(V + E).
        """
    def declare_global(self, type_spaced: str, name: str, *, initializer: str | None = None) -> None: ...
    def declare_internal_globals(self, module_name: str, emitter: Emitter) -> None: ...
    def module_internal_static_name(self, module_name: str, emitter: Emitter) -> str: ...
    def declare_module(self, module_name: str, emitter: Emitter) -> None: ...
    def declare_imports(self, imps: Iterable[str], emitter: Emitter) -> None: ...
    def declare_finals(self, module: str, final_names: Iterable[tuple[str, RType]], emitter: Emitter) -> None: ...
    def final_definition(self, module: str, name: str, typ: RType, emitter: Emitter) -> str: ...
    def declare_static_pyobject(self, identifier: str, emitter: Emitter) -> None: ...

def sort_classes(classes: list[tuple[str, ClassIR]]) -> list[tuple[str, ClassIR]]: ...
T = TypeVar('T')

def toposort(deps: dict[T, set[T]]) -> list[T]:
    """Topologically sort a dict from item to dependencies.

    This runs in O(V + E).
    """
def is_fastcall_supported(fn: FuncIR, capi_version: tuple[int, int]) -> bool: ...
def collect_literals(fn: FuncIR, literals: Literals) -> None:
    """Store all Python literal object refs in fn.

    Collecting literals must happen only after we have the final IR.
    This way we won't include literals that have been optimized away.
    """
def c_string_array_initializer(components: list[bytes]) -> str: ...
