from .runners import CCompilerRunner as CCompilerRunner, CppCompilerRunner as CppCompilerRunner, FortranCompilerRunner as FortranCompilerRunner
from .util import ArbitraryDepthGlob as ArbitraryDepthGlob, CompileError as CompileError, Glob as Glob, copy as copy, get_abspath as get_abspath, glob_at_depth as glob_at_depth, import_module_from_file as import_module_from_file, make_dirs as make_dirs, pyx_is_cplus as pyx_is_cplus, sha256_of_file as sha256_of_file, sha256_of_string as sha256_of_string
from _typeshed import Incomplete

objext: str

def compile_sources(files, Runner: Incomplete | None = None, destdir: Incomplete | None = None, cwd: Incomplete | None = None, keep_dir_struct: bool = False, per_file_kwargs: Incomplete | None = None, **kwargs):
    """ Compile source code files to object files.

    Parameters
    ==========

    files : iterable of str
        Paths to source files, if ``cwd`` is given, the paths are taken as relative.
    Runner: CompilerRunner subclass (optional)
        Could be e.g. ``FortranCompilerRunner``. Will be inferred from filename
        extensions if missing.
    destdir: str
        Output directory, if cwd is given, the path is taken as relative.
    cwd: str
        Working directory. Specify to have compiler run in other directory.
        also used as root of relative paths.
    keep_dir_struct: bool
        Reproduce directory structure in `destdir`. default: ``False``
    per_file_kwargs: dict
        Dict mapping instances in ``files`` to keyword arguments.
    \\*\\*kwargs: dict
        Default keyword arguments to pass to ``Runner``.

    """
def get_mixed_fort_c_linker(vendor: Incomplete | None = None, cplus: bool = False, cwd: Incomplete | None = None): ...
def link(obj_files, out_file: Incomplete | None = None, shared: bool = False, Runner: Incomplete | None = None, cwd: Incomplete | None = None, cplus: bool = False, fort: bool = False, **kwargs):
    """ Link object files.

    Parameters
    ==========

    obj_files: iterable of str
        Paths to object files.
    out_file: str (optional)
        Path to executable/shared library, if ``None`` it will be
        deduced from the last item in obj_files.
    shared: bool
        Generate a shared library?
    Runner: CompilerRunner subclass (optional)
        If not given the ``cplus`` and ``fort`` flags will be inspected
        (fallback is the C compiler).
    cwd: str
        Path to the root of relative paths and working directory for compiler.
    cplus: bool
        C++ objects? default: ``False``.
    fort: bool
        Fortran objects? default: ``False``.
    \\*\\*kwargs: dict
        Keyword arguments passed to ``Runner``.

    Returns
    =======

    The absolute path to the generated shared object / executable.

    """
def link_py_so(obj_files, so_file: Incomplete | None = None, cwd: Incomplete | None = None, libraries: Incomplete | None = None, cplus: bool = False, fort: bool = False, **kwargs):
    """ Link Python extension module (shared object) for importing

    Parameters
    ==========

    obj_files: iterable of str
        Paths to object files to be linked.
    so_file: str
        Name (path) of shared object file to create. If not specified it will
        have the basname of the last object file in `obj_files` but with the
        extension '.so' (Unix).
    cwd: path string
        Root of relative paths and working directory of linker.
    libraries: iterable of strings
        Libraries to link against, e.g. ['m'].
    cplus: bool
        Any C++ objects? default: ``False``.
    fort: bool
        Any Fortran objects? default: ``False``.
    kwargs**: dict
        Keyword arguments passed to ``link(...)``.

    Returns
    =======

    Absolute path to the generate shared object.
    """
def simple_cythonize(src, destdir: Incomplete | None = None, cwd: Incomplete | None = None, **cy_kwargs):
    """ Generates a C file from a Cython source file.

    Parameters
    ==========

    src: str
        Path to Cython source.
    destdir: str (optional)
        Path to output directory (default: '.').
    cwd: path string (optional)
        Root of relative paths (default: '.').
    **cy_kwargs:
        Second argument passed to cy_compile. Generates a .cpp file if ``cplus=True`` in ``cy_kwargs``,
        else a .c file.
    """

extension_mapping: Incomplete

def src2obj(srcpath, Runner: Incomplete | None = None, objpath: Incomplete | None = None, cwd: Incomplete | None = None, inc_py: bool = False, **kwargs):
    ''' Compiles a source code file to an object file.

    Files ending with \'.pyx\' assumed to be cython files and
    are dispatched to pyx2obj.

    Parameters
    ==========

    srcpath: str
        Path to source file.
    Runner: CompilerRunner subclass (optional)
        If ``None``: deduced from extension of srcpath.
    objpath : str (optional)
        Path to generated object. If ``None``: deduced from ``srcpath``.
    cwd: str (optional)
        Working directory and root of relative paths. If ``None``: current dir.
    inc_py: bool
        Add Python include path to kwarg "include_dirs". Default: False
    \\*\\*kwargs: dict
        keyword arguments passed to Runner or pyx2obj

    '''
def pyx2obj(pyxpath, objpath: Incomplete | None = None, destdir: Incomplete | None = None, cwd: Incomplete | None = None, include_dirs: Incomplete | None = None, cy_kwargs: Incomplete | None = None, cplus: Incomplete | None = None, **kwargs):
    """
    Convenience function

    If cwd is specified, pyxpath and dst are taken to be relative
    If only_update is set to `True` the modification time is checked
    and compilation is only run if the source is newer than the
    destination

    Parameters
    ==========

    pyxpath: str
        Path to Cython source file.
    objpath: str (optional)
        Path to object file to generate.
    destdir: str (optional)
        Directory to put generated C file. When ``None``: directory of ``objpath``.
    cwd: str (optional)
        Working directory and root of relative paths.
    include_dirs: iterable of path strings (optional)
        Passed onto src2obj and via cy_kwargs['include_path']
        to simple_cythonize.
    cy_kwargs: dict (optional)
        Keyword arguments passed onto `simple_cythonize`
    cplus: bool (optional)
        Indicate whether C++ is used. default: auto-detect using ``.util.pyx_is_cplus``.
    compile_kwargs: dict
        keyword arguments passed onto src2obj

    Returns
    =======

    Absolute path of generated object file.

    """
def any_fortran_src(srcs): ...
def any_cplus_src(srcs): ...
def compile_link_import_py_ext(sources, extname: Incomplete | None = None, build_dir: str = '.', compile_kwargs: Incomplete | None = None, link_kwargs: Incomplete | None = None):
    """ Compiles sources to a shared object (Python extension) and imports it

    Sources in ``sources`` which is imported. If shared object is newer than the sources, they
    are not recompiled but instead it is imported.

    Parameters
    ==========

    sources : string
        List of paths to sources.
    extname : string
        Name of extension (default: ``None``).
        If ``None``: taken from the last file in ``sources`` without extension.
    build_dir: str
        Path to directory in which objects files etc. are generated.
    compile_kwargs: dict
        keyword arguments passed to ``compile_sources``
    link_kwargs: dict
        keyword arguments passed to ``link_py_so``

    Returns
    =======

    The imported module from of the Python extension.
    """
def compile_link_import_strings(sources, build_dir: Incomplete | None = None, **kwargs):
    """ Compiles, links and imports extension module from source.

    Parameters
    ==========

    sources : iterable of name/source pair tuples
    build_dir : string (default: None)
        Path. ``None`` implies use a temporary directory.
    **kwargs:
        Keyword arguments passed onto `compile_link_import_py_ext`.

    Returns
    =======

    mod : module
        The compiled and imported extension module.
    info : dict
        Containing ``build_dir`` as 'build_dir'.

    """
def compile_run_strings(sources, build_dir: Incomplete | None = None, clean: bool = False, compile_kwargs: Incomplete | None = None, link_kwargs: Incomplete | None = None):
    """ Compiles, links and runs a program built from sources.

    Parameters
    ==========

    sources : iterable of name/source pair tuples
    build_dir : string (default: None)
        Path. ``None`` implies use a temporary directory.
    clean : bool
        Whether to remove build_dir after use. This will only have an
        effect if ``build_dir`` is ``None`` (which creates a temporary directory).
        Passing ``clean == True`` and ``build_dir != None`` raises a ``ValueError``.
        This will also set ``build_dir`` in returned info dictionary to ``None``.
    compile_kwargs: dict
        Keyword arguments passed onto ``compile_sources``
    link_kwargs: dict
        Keyword arguments passed onto ``link``

    Returns
    =======

    (stdout, stderr): pair of strings
    info: dict
        Containing exit status as 'exit_status' and ``build_dir`` as 'build_dir'

    """
