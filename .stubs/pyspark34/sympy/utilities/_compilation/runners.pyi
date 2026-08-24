from .util import CompileError as CompileError, find_binary_of_command as find_binary_of_command, unique_list as unique_list
from _typeshed import Incomplete
from typing import Callable

class CompilerRunner:
    """ CompilerRunner base class.

    Parameters
    ==========

    sources : list of str
        Paths to sources.
    out : str
    flags : iterable of str
        Compiler flags.
    run_linker : bool
    compiler_name_exe : (str, str) tuple
        Tuple of compiler name &  command to call.
    cwd : str
        Path of root of relative paths.
    include_dirs : list of str
        Include directories.
    libraries : list of str
        Libraries to link against.
    library_dirs : list of str
        Paths to search for shared libraries.
    std : str
        Standard string, e.g. ``'c++11'``, ``'c99'``, ``'f2003'``.
    define: iterable of strings
        macros to define
    undef : iterable of strings
        macros to undefine
    preferred_vendor : string
        name of preferred vendor e.g. 'gnu' or 'intel'

    Methods
    =======

    run():
        Invoke compilation as a subprocess.

    """
    compiler_dict: dict[str, str]
    standards: tuple[None | str, ...]
    std_formater: dict[str, Callable[[str | None], str]]
    compiler_name_vendor_mapping: dict[str, str]
    sources: Incomplete
    out: Incomplete
    flags: Incomplete
    cwd: Incomplete
    define: Incomplete
    undef: Incomplete
    include_dirs: Incomplete
    libraries: Incomplete
    library_dirs: Incomplete
    std: Incomplete
    run_linker: Incomplete
    linkline: Incomplete
    def __init__(self, sources, out, flags: Incomplete | None = None, run_linker: bool = True, compiler: Incomplete | None = None, cwd: str = '.', include_dirs: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, std: Incomplete | None = None, define: Incomplete | None = None, undef: Incomplete | None = None, strict_aliasing: Incomplete | None = None, preferred_vendor: Incomplete | None = None, linkline: Incomplete | None = None, **kwargs) -> None: ...
    @classmethod
    def find_compiler(cls, preferred_vendor: Incomplete | None = None):
        """ Identify a suitable C/fortran/other compiler. """
    def cmd(self):
        """ List of arguments (str) to be passed to e.g. ``subprocess.Popen``. """
    cmd_outerr: Incomplete
    cmd_returncode: Incomplete
    def run(self): ...

class CCompilerRunner(CompilerRunner):
    compiler_dict: Incomplete
    standards: Incomplete
    std_formater: Incomplete
    compiler_name_vendor_mapping: Incomplete

class CppCompilerRunner(CompilerRunner):
    compiler_dict: Incomplete
    standards: Incomplete
    std_formater: Incomplete
    compiler_name_vendor_mapping: Incomplete

class FortranCompilerRunner(CompilerRunner):
    standards: Incomplete
    std_formater: Incomplete
    compiler_dict: Incomplete
    compiler_name_vendor_mapping: Incomplete
