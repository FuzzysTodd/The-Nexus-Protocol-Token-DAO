from ._log import log as log
from .ccompiler import CCompiler as CCompiler, gen_preprocess_options as gen_preprocess_options
from .dep_util import newer as newer
from .errors import CompileError as CompileError, DistutilsExecError as DistutilsExecError, LibError as LibError, LinkError as LinkError, UnknownFileError as UnknownFileError
from .file_util import write_file as write_file
from _typeshed import Incomplete

class BCPPCompiler(CCompiler):
    """Concrete class that implements an interface to the Borland C/C++
    compiler, as defined by the CCompiler abstract class.
    """
    compiler_type: str
    executables: Incomplete
    src_extensions: Incomplete
    obj_extension: str
    static_lib_extension: str
    shared_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    exe_extension: str
    cc: str
    linker: str
    lib: str
    preprocess_options: Incomplete
    compile_options: Incomplete
    compile_options_debug: Incomplete
    ldflags_shared: Incomplete
    ldflags_shared_debug: Incomplete
    ldflags_static: Incomplete
    ldflags_exe: Incomplete
    ldflags_exe_debug: Incomplete
    def __init__(self, verbose: int = 0, dry_run: int = 0, force: int = 0) -> None: ...
    def compile(self, sources, output_dir: Incomplete | None = None, macros: Incomplete | None = None, include_dirs: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, depends: Incomplete | None = None): ...
    def create_static_lib(self, objects, output_libname, output_dir: Incomplete | None = None, debug: int = 0, target_lang: Incomplete | None = None) -> None: ...
    def link(self, target_desc, objects, output_filename, output_dir: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, runtime_library_dirs: Incomplete | None = None, export_symbols: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, build_temp: Incomplete | None = None, target_lang: Incomplete | None = None) -> None: ...
    def find_library_file(self, dirs, lib, debug: int = 0): ...
    def object_filenames(self, source_filenames, strip_dir: int = 0, output_dir: str = ''): ...
    def preprocess(self, source, output_file: Incomplete | None = None, macros: Incomplete | None = None, include_dirs: Incomplete | None = None, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None) -> None: ...
