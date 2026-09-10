from ._collections import RangeMap as RangeMap
from .errors import CCompilerError as CCompilerError, CompileError as CompileError, DistutilsExecError as DistutilsExecError, DistutilsPlatformError as DistutilsPlatformError
from .file_util import write_file as write_file
from .unixccompiler import UnixCCompiler as UnixCCompiler
from .version import LooseVersion as LooseVersion, suppress_known_deprecation as suppress_known_deprecation
from _typeshed import Incomplete

def get_msvcr():
    """Include the appropriate MSVC runtime library if Python was built
    with MSVC 7.0 or later.
    """

class CygwinCCompiler(UnixCCompiler):
    """Handles the Cygwin port of the GNU C compiler to Windows."""
    compiler_type: str
    obj_extension: str
    static_lib_extension: str
    shared_lib_extension: str
    dylib_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    dylib_lib_format: str
    exe_extension: str
    cc: Incomplete
    cxx: Incomplete
    linker_dll: Incomplete
    dll_libraries: Incomplete
    def __init__(self, verbose: int = 0, dry_run: int = 0, force: int = 0) -> None: ...
    @property
    def gcc_version(self): ...
    def link(self, target_desc, objects, output_filename, output_dir: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, runtime_library_dirs: Incomplete | None = None, export_symbols: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, build_temp: Incomplete | None = None, target_lang: Incomplete | None = None) -> None:
        """Link the objects."""
    def runtime_library_dir_option(self, dir): ...
    @property
    def out_extensions(self):
        """
        Add support for rc and res files.
        """

class Mingw32CCompiler(CygwinCCompiler):
    """Handles the Mingw32 port of the GNU C compiler to Windows."""
    compiler_type: str
    def __init__(self, verbose: int = 0, dry_run: int = 0, force: int = 0) -> None: ...
    def runtime_library_dir_option(self, dir) -> None: ...

CONFIG_H_OK: str
CONFIG_H_NOTOK: str
CONFIG_H_UNCERTAIN: str

def check_config_h():
    '''Check if the current Python installation appears amenable to building
    extensions with GCC.

    Returns a tuple (status, details), where \'status\' is one of the following
    constants:

    - CONFIG_H_OK: all is well, go ahead and compile
    - CONFIG_H_NOTOK: doesn\'t look good
    - CONFIG_H_UNCERTAIN: not sure -- unable to read pyconfig.h

    \'details\' is a human-readable string explaining the situation.

    Note there are two ways to conclude "OK": either \'sys.version\' contains
    the string "GCC" (implying that this Python was built with GCC), or the
    installed "pyconfig.h" contains the string "__GNUC__".
    '''
def is_cygwincc(cc):
    """Try to determine if the compiler that would be used is from cygwin."""

get_versions: Incomplete
