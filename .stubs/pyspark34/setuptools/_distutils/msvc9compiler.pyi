from ._log import log as log
from .ccompiler import CCompiler as CCompiler, gen_lib_options as gen_lib_options
from .errors import CompileError as CompileError, DistutilsExecError as DistutilsExecError, DistutilsPlatformError as DistutilsPlatformError, LibError as LibError, LinkError as LinkError
from .util import get_platform as get_platform
from _typeshed import Incomplete

RegOpenKeyEx: Incomplete
RegEnumKey: Incomplete
RegEnumValue: Incomplete
RegError: Incomplete
HKEYS: Incomplete
NATIVE_WIN64: Incomplete
VS_BASE: str
WINSDK_BASE: str
NET_BASE: str
PLAT_TO_VCVARS: Incomplete

class Reg:
    """Helper class to read values from the registry"""
    def get_value(cls, path, key): ...
    get_value: Incomplete
    def read_keys(cls, base, key):
        """Return list of registry keys."""
    read_keys: Incomplete
    def read_values(cls, base, key):
        """Return dict of registry keys and values.

        All names are converted to lowercase.
        """
    read_values: Incomplete
    def convert_mbcs(s): ...
    convert_mbcs: Incomplete

class MacroExpander:
    macros: Incomplete
    vsbase: Incomplete
    def __init__(self, version) -> None: ...
    def set_macro(self, macro, path, key) -> None: ...
    def load_macros(self, version) -> None: ...
    def sub(self, s): ...

def get_build_version():
    """Return the version of MSVC that was used to build Python.

    For Python 2.3 and up, the version number is included in
    sys.version.  For earlier versions, assume the compiler is MSVC 6.
    """
def normalize_and_reduce_paths(paths):
    """Return a list of normalized paths with duplicates removed.

    The current order of paths is maintained.
    """
def removeDuplicates(variable):
    """Remove duplicate values of an environment variable."""
def find_vcvarsall(version):
    """Find the vcvarsall.bat file

    At first it tries to find the productdir of VS 2008 in the registry. If
    that fails it falls back to the VS90COMNTOOLS env var.
    """
def query_vcvarsall(version, arch: str = 'x86'):
    """Launch vcvarsall.bat and read the settings from its environment"""

VERSION: Incomplete

class MSVCCompiler(CCompiler):
    """Concrete class that implements an interface to Microsoft Visual C++,
    as defined by the CCompiler abstract class."""
    compiler_type: str
    executables: Incomplete
    src_extensions: Incomplete
    res_extension: str
    obj_extension: str
    static_lib_extension: str
    shared_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    exe_extension: str
    plat_name: Incomplete
    initialized: bool
    def __init__(self, verbose: int = 0, dry_run: int = 0, force: int = 0) -> None: ...
    cc: str
    linker: str
    lib: str
    rc: str
    mc: str
    preprocess_options: Incomplete
    compile_options: Incomplete
    compile_options_debug: Incomplete
    ldflags_shared: Incomplete
    ldflags_shared_debug: Incomplete
    ldflags_static: Incomplete
    def initialize(self, plat_name: Incomplete | None = None) -> None: ...
    def object_filenames(self, source_filenames, strip_dir: int = 0, output_dir: str = ''): ...
    def compile(self, sources, output_dir: Incomplete | None = None, macros: Incomplete | None = None, include_dirs: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, depends: Incomplete | None = None): ...
    def create_static_lib(self, objects, output_libname, output_dir: Incomplete | None = None, debug: int = 0, target_lang: Incomplete | None = None) -> None: ...
    def link(self, target_desc, objects, output_filename, output_dir: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, runtime_library_dirs: Incomplete | None = None, export_symbols: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, build_temp: Incomplete | None = None, target_lang: Incomplete | None = None) -> None: ...
    def manifest_setup_ldargs(self, output_filename, build_temp, ld_args) -> None: ...
    def manifest_get_embed_info(self, target_desc, ld_args): ...
    def library_dir_option(self, dir): ...
    def runtime_library_dir_option(self, dir) -> None: ...
    def library_option(self, lib): ...
    def find_library_file(self, dirs, lib, debug: int = 0): ...
    def find_exe(self, exe):
        """Return path to an MSVC executable program.

        Tries to find the program in several places: first, one of the
        MSVC program search paths from the registry; next, the directories
        in the PATH environment variable.  If any of those work, return an
        absolute path that is known to exist.  If none of them work, just
        return the original program name, 'exe'.
        """
