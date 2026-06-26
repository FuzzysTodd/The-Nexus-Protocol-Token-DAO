from . import Errors as Errors, Options as Options
from .. import Utils as Utils
from .CmdLine import parse_command_line as parse_command_line
from .Errors import CompileError as CompileError, PyrexError as PyrexError, error as error, warning as warning
from .Lexicon import unicode_continuation_ch_any as unicode_continuation_ch_any, unicode_continuation_ch_range as unicode_continuation_ch_range, unicode_start_ch_any as unicode_start_ch_any, unicode_start_ch_range as unicode_start_ch_range
from .Options import CompilationOptions as CompilationOptions, default_options as default_options
from .Scanning import FileSourceDescriptor as FileSourceDescriptor, PyrexScanner as PyrexScanner
from .StringEncoding import EncodedString as EncodedString
from .Symtab import ModuleScope as ModuleScope
from _typeshed import Incomplete

basestring = str
module_name_pattern: Incomplete
standard_include_path: Incomplete

class Context:
    cython_scope: Incomplete
    language_level: Incomplete
    modules: Incomplete
    include_directories: Incomplete
    future_directives: Incomplete
    compiler_directives: Incomplete
    cpp: Incomplete
    options: Incomplete
    pxds: Incomplete
    legacy_implicit_noexcept: Incomplete
    gdb_debug_outputwriter: Incomplete
    def __init__(self, include_directories, compiler_directives, cpp: bool = False, language_level: Incomplete | None = None, options: Incomplete | None = None) -> None: ...
    @classmethod
    def from_options(cls, options): ...
    def set_language_level(self, level) -> None: ...
    def intern_ustring(self, value, encoding: Incomplete | None = None): ...
    def process_pxd(self, source_desc, scope, module_name): ...
    def nonfatal_error(self, exc): ...
    def find_module(self, module_name, from_module: Incomplete | None = None, pos: Incomplete | None = None, need_pxd: int = 1, absolute_fallback: bool = True, relative_import: bool = False): ...
    def find_pxd_file(self, qualified_name, pos: Incomplete | None = None, sys_path: bool = True, source_file_path: Incomplete | None = None): ...
    def find_pyx_file(self, qualified_name, pos: Incomplete | None = None, sys_path: bool = True, source_file_path: Incomplete | None = None): ...
    def find_include_file(self, filename, pos: Incomplete | None = None, source_file_path: Incomplete | None = None): ...
    def search_include_directories(self, qualified_name, suffix: Incomplete | None = None, source_pos: Incomplete | None = None, include: bool = False, sys_path: bool = False, source_file_path: Incomplete | None = None): ...
    def find_root_package_dir(self, file_path): ...
    def check_package_dir(self, dir, package_names): ...
    def c_file_out_of_date(self, source_path, output_path): ...
    def find_cimported_module_names(self, source_path): ...
    def is_package_dir(self, dir_path): ...
    def read_dependency_file(self, source_path): ...
    def lookup_submodule(self, name): ...
    def find_submodule(self, name, as_package: bool = False): ...
    def parse(self, source_desc, scope, pxd, full_module_name): ...
    def extract_module_name(self, path, options): ...
    def setup_errors(self, options, result) -> None: ...
    def teardown_errors(self, err, options, result) -> None: ...

def get_output_filename(source_filename, cwd, options): ...
def create_default_resultobj(compilation_source, options): ...
def run_pipeline(source, options, full_module_name: Incomplete | None = None, context: Incomplete | None = None): ...

class CompilationSource:
    """
    Contains the data necessary to start up a compilation pipeline for
    a single compilation unit.
    """
    source_desc: Incomplete
    full_module_name: Incomplete
    cwd: Incomplete
    def __init__(self, source_desc, full_module_name, cwd) -> None: ...

class CompilationResult:
    """
    Results from the Cython compiler:

    c_file           string or None   The generated C source file
    h_file           string or None   The generated C header file
    i_file           string or None   The generated .pxi file
    api_file         string or None   The generated C API .h file
    listing_file     string or None   File of error messages
    object_file      string or None   Result of compiling the C file
    extension_file   string or None   Result of linking the object file
    num_errors       integer          Number of compilation errors
    compilation_source CompilationSource
    """
    c_file: Incomplete
    h_file: Incomplete
    i_file: Incomplete
    api_file: Incomplete
    listing_file: Incomplete
    object_file: Incomplete
    extension_file: Incomplete
    main_source_file: Incomplete
    def __init__(self) -> None: ...

class CompilationResultSet(dict):
    """
    Results from compiling multiple Pyrex source files. A mapping
    from source file paths to CompilationResult instances. Also
    has the following attributes:

    num_errors   integer   Total number of compilation errors
    """
    num_errors: int
    def add(self, source, result) -> None: ...

def compile_single(source, options, full_module_name: Incomplete | None = None):
    """
    compile_single(source, options, full_module_name)

    Compile the given Pyrex implementation file and return a CompilationResult.
    Always compiles a single file; does not perform timestamp checking or
    recursion.
    """
def compile_multiple(sources, options):
    """
    compile_multiple(sources, options)

    Compiles the given sequence of Pyrex implementation files and returns
    a CompilationResultSet. Performs timestamp checking and/or recursion
    if these are specified in the options.
    """
def compile(source, options: Incomplete | None = None, full_module_name: Incomplete | None = None, **kwds):
    """
    compile(source [, options], [, <option> = <value>]...)

    Compile one or more Pyrex implementation files, with optional timestamp
    checking and recursing on dependencies.  The source argument may be a string
    or a sequence of strings.  If it is a string and no recursion or timestamp
    checking is requested, a CompilationResult is returned, otherwise a
    CompilationResultSet is returned.
    """
def search_include_directories(dirs, qualified_name, suffix: str = '', pos: Incomplete | None = None, include: bool = False, source_file_path: Incomplete | None = None):
    """
    Search the list of include directories for the given file name.

    If a source file path or position is given, first searches the directory
    containing that file.  Returns None if not found, but does not report an error.

    The 'include' option will disable package dereferencing.
    """
def search_module_in_dir(package_dir, module_name, suffix): ...
def setuptools_main(): ...
def main(command_line: int = 0) -> None: ...
