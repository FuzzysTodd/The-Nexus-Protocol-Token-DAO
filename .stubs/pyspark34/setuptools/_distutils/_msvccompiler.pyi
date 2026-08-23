from ._log import log as log
from .ccompiler import CCompiler as CCompiler, gen_lib_options as gen_lib_options
from .errors import CompileError as CompileError, DistutilsExecError as DistutilsExecError, DistutilsPlatformError as DistutilsPlatformError, LibError as LibError, LinkError as LinkError
from .util import get_platform as get_platform
from _typeshed import Incomplete

PLAT_SPEC_TO_RUNTIME: Incomplete
PLAT_TO_VCVARS: Incomplete

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
    cc: Incomplete
    linker: Incomplete
    lib: Incomplete
    rc: Incomplete
    mc: Incomplete
    mt: Incomplete
    preprocess_options: Incomplete
    compile_options: Incomplete
    compile_options_debug: Incomplete
    ldflags_exe: Incomplete
    ldflags_exe_debug: Incomplete
    ldflags_shared: Incomplete
    ldflags_shared_debug: Incomplete
    ldflags_static: Incomplete
    ldflags_static_debug: Incomplete
    def initialize(self, plat_name: Incomplete | None = None) -> None: ...
    @property
    def out_extensions(self): ...
    def compile(self, sources, output_dir: Incomplete | None = None, macros: Incomplete | None = None, include_dirs: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, depends: Incomplete | None = None): ...
    def create_static_lib(self, objects, output_libname, output_dir: Incomplete | None = None, debug: int = 0, target_lang: Incomplete | None = None) -> None: ...
    def link(self, target_desc, objects, output_filename, output_dir: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, runtime_library_dirs: Incomplete | None = None, export_symbols: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, build_temp: Incomplete | None = None, target_lang: Incomplete | None = None) -> None: ...
    def spawn(self, cmd): ...
    def library_dir_option(self, dir): ...
    def runtime_library_dir_option(self, dir) -> None: ...
    def library_option(self, lib): ...
    def find_library_file(self, dirs, lib, debug: int = 0): ...
