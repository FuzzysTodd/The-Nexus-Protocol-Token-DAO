from mypy.build import BuildSource as BuildSource
from mypy.fscache import FileSystemCache
from mypy.options import Options as Options
from mypyc.codegen import emitmodule as emitmodule
from mypyc.common import RUNTIME_C_FILES as RUNTIME_C_FILES, shared_lib_name as shared_lib_name
from mypyc.errors import Errors as Errors
from mypyc.ir.pprint import format_modules as format_modules
from mypyc.namegen import exported_name as exported_name
from mypyc.options import CompilerOptions as CompilerOptions
from typing import Any, Iterable, NoReturn
from typing_extensions import TypeAlias

Extension: TypeAlias

def get_extension() -> type[Extension]: ...
def setup_mypycify_vars() -> None:
    """Rewrite a bunch of config vars in pretty dubious ways."""
def fail(message: str) -> NoReturn: ...
def emit_messages(options: Options, messages: list[str], dt: float, serious: bool = False) -> None: ...
def get_mypy_config(mypy_options: list[str], only_compile_paths: Iterable[str] | None, compiler_options: CompilerOptions, fscache: FileSystemCache | None) -> tuple[list[BuildSource], list[BuildSource], Options]:
    """Construct mypy BuildSources and Options from file and options lists"""
def generate_c_extension_shim(full_module_name: str, module_name: str, dir_name: str, group_name: str) -> str:
    """Create a C extension shim with a passthrough PyInit function.

    Arguments:
        full_module_name: the dotted full module name
        module_name: the final component of the module name
        dir_name: the directory to place source code
        group_name: the name of the group
    """
def group_name(modules: list[str]) -> str:
    """Produce a probably unique name for a group from a list of module names."""
def include_dir() -> str:
    """Find the path of the lib-rt dir that needs to be included"""
def generate_c(sources: list[BuildSource], options: Options, groups: emitmodule.Groups, fscache: FileSystemCache, compiler_options: CompilerOptions) -> tuple[list[list[tuple[str, str]]], str]:
    """Drive the actual core compilation step.

    The groups argument describes how modules are assigned to C
    extension modules. See the comments on the Groups type in
    mypyc.emitmodule for details.

    Returns the C source code and (for debugging) the pretty printed IR.
    """
def build_using_shared_lib(sources: list[BuildSource], group_name: str, cfiles: list[str], deps: list[str], build_dir: str, extra_compile_args: list[str]) -> list[Extension]:
    """Produce the list of extension modules when a shared library is needed.

    This creates one shared library extension module that all of the
    others import and then one shim extension module for each
    module in the build, that simply calls an initialization function
    in the shared library.

    The shared library (which lib_name is the name of) is a python
    extension module that exports the real initialization functions in
    Capsules stored in module attributes.
    """
def build_single_module(sources: list[BuildSource], cfiles: list[str], extra_compile_args: list[str]) -> list[Extension]:
    """Produce the list of extension modules for a standalone extension.

    This contains just one module, since there is no need for a shared module.
    """
def write_file(path: str, contents: str) -> None:
    """Write data into a file.

    If the file already exists and has the same contents we
    want to write, skip writing so as to preserve the mtime
    and avoid triggering recompilation.
    """
def construct_groups(sources: list[BuildSource], separate: bool | list[tuple[list[str], str | None]], use_shared_lib: bool) -> emitmodule.Groups:
    """Compute Groups given the input source list and separate configs.

    separate is the user-specified configuration for how to assign
    modules to compilation groups (see mypycify docstring for details).

    This takes that and expands it into our internal representation of
    group configuration, documented in mypyc.emitmodule's definition
    of Group.
    """
def get_header_deps(cfiles: list[tuple[str, str]]) -> list[str]:
    """Find all the headers used by a group of cfiles.

    We do this by just regexping the source, which is a bit simpler than
    properly plumbing the data through.

    Arguments:
        cfiles: A list of (file name, file contents) pairs.
    """
def mypyc_build(paths: list[str], compiler_options: CompilerOptions, *, separate: bool | list[tuple[list[str], str | None]] = False, only_compile_paths: Iterable[str] | None = None, skip_cgen_input: Any | None = None, always_use_shared_lib: bool = False) -> tuple[emitmodule.Groups, list[tuple[list[str], list[str]]]]:
    """Do the front and middle end of mypyc building, producing and writing out C source."""
def mypycify(paths: list[str], *, only_compile_paths: Iterable[str] | None = None, verbose: bool = False, opt_level: str = '3', debug_level: str = '1', strip_asserts: bool = False, multi_file: bool = False, separate: bool | list[tuple[list[str], str | None]] = False, skip_cgen_input: Any | None = None, target_dir: str | None = None, include_runtime_files: bool | None = None) -> list[Extension]:
    """Main entry point to building using mypyc.

    This produces a list of Extension objects that should be passed as the
    ext_modules parameter to setup.

    Arguments:
        paths: A list of file paths to build. It may also contain mypy options.
        only_compile_paths: If not None, an iterable of paths that are to be
                            the only modules compiled, even if other modules
                            appear in the mypy command line given to paths.
                            (These modules must still be passed to paths.)

        verbose: Should mypyc be more verbose. Defaults to false.

        opt_level: The optimization level, as a string. Defaults to '3' (meaning '-O3').
        debug_level: The debug level, as a string. Defaults to '1' (meaning '-g1').
        strip_asserts: Should asserts be stripped from the generated code.

        multi_file: Should each Python module be compiled into its own C source file.
                    This can reduce compile time and memory requirements at the likely
                    cost of runtime performance of compiled code. Defaults to false.
        separate: Should compiled modules be placed in separate extension modules.
                  If False, all modules are placed in a single shared library.
                  If True, every module is placed in its own library.
                  Otherwise separate should be a list of
                  (file name list, optional shared library name) pairs specifying
                  groups of files that should be placed in the same shared library
                  (while all other modules will be placed in its own library).

                  Each group can be compiled independently, which can
                  speed up compilation, but calls between groups can
                  be slower than calls within a group and can't be
                  inlined.
        target_dir: The directory to write C output files. Defaults to 'build'.
        include_runtime_files: If not None, whether the mypyc runtime library
                               should be directly #include'd instead of linked
                               separately in order to reduce compiler invocations.
                               Defaults to False in multi_file mode, True otherwise.
    """
