from . import sysconfig as sysconfig
from ._log import log as log
from ._macos_compat import compiler_fixup as compiler_fixup
from .ccompiler import CCompiler as CCompiler, gen_lib_options as gen_lib_options, gen_preprocess_options as gen_preprocess_options
from .dep_util import newer as newer
from .errors import CompileError as CompileError, DistutilsExecError as DistutilsExecError, LibError as LibError, LinkError as LinkError
from _typeshed import Incomplete

class UnixCCompiler(CCompiler):
    compiler_type: str
    executables: Incomplete
    src_extensions: Incomplete
    obj_extension: str
    static_lib_extension: str
    shared_lib_extension: str
    dylib_lib_extension: str
    xcode_stub_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    dylib_lib_format: str
    xcode_stub_lib_format = dylib_lib_format
    def preprocess(self, source, output_file: Incomplete | None = None, macros: Incomplete | None = None, include_dirs: Incomplete | None = None, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None) -> None: ...
    def create_static_lib(self, objects, output_libname, output_dir: Incomplete | None = None, debug: int = 0, target_lang: Incomplete | None = None) -> None: ...
    def link(self, target_desc, objects, output_filename, output_dir: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, runtime_library_dirs: Incomplete | None = None, export_symbols: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, build_temp: Incomplete | None = None, target_lang: Incomplete | None = None) -> None: ...
    def library_dir_option(self, dir): ...
    def runtime_library_dir_option(self, dir): ...
    def library_option(self, lib): ...
    def find_library_file(self, dirs, lib, debug: int = 0):
        '''
        Second-guess the linker with not much hard
        data to go on: GCC seems to prefer the shared library, so
        assume that *all* Unix C compilers do,
        ignoring even GCC\'s "-static" option.

        >>> compiler = UnixCCompiler()
        >>> compiler._library_root = lambda dir: dir
        >>> monkeypatch = getfixture(\'monkeypatch\')
        >>> monkeypatch.setattr(os.path, \'exists\', lambda d: \'existing\' in d)
        >>> dirs = (\'/foo/bar/missing\', \'/foo/bar/existing\')
        >>> compiler.find_library_file(dirs, \'abc\').replace(\'\\\\\', \'/\')
        \'/foo/bar/existing/libabc.dylib\'
        >>> compiler.find_library_file(reversed(dirs), \'abc\').replace(\'\\\\\', \'/\')
        \'/foo/bar/existing/libabc.dylib\'
        >>> monkeypatch.setattr(os.path, \'exists\',
        ...     lambda d: \'existing\' in d and \'.a\' in d)
        >>> compiler.find_library_file(dirs, \'abc\').replace(\'\\\\\', \'/\')
        \'/foo/bar/existing/libabc.a\'
        >>> compiler.find_library_file(reversed(dirs), \'abc\').replace(\'\\\\\', \'/\')
        \'/foo/bar/existing/libabc.a\'
        '''
