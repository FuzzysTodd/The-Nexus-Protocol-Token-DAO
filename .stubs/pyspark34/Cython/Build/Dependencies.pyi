from .. import Utils as Utils, __version__ as __version__
from ..Compiler import Errors as Errors
from ..Compiler.Main import Context as Context
from ..Compiler.Options import CompilationOptions as CompilationOptions, default_options as default_options, get_directive_defaults as get_directive_defaults
from ..Utils import cached_function as cached_function, cached_method as cached_method, copy_file_to_dir_if_newer as copy_file_to_dir_if_newer, is_package_dir as is_package_dir, path_exists as path_exists, safe_makedirs as safe_makedirs, write_depfile as write_depfile
from _typeshed import Incomplete
from collections.abc import Generator

gzip_open: Incomplete
gzip_ext: str
gzip_open = open
zipfile_compression_mode: Incomplete
join_path: Incomplete
copy_once_if_newer: Incomplete
safe_makedirs_once: Incomplete

def encode_filename_in_py2(filename): ...
basestring = str

def extended_iglob(pattern) -> Generator[Incomplete, None, None]: ...
def nonempty(it, error_msg: str = 'expected non-empty iterator') -> Generator[Incomplete, None, None]: ...
def file_hash(filename): ...
def update_pythran_extension(ext) -> None: ...
def parse_list(s):
    '''
    >>> parse_list("")
    []
    >>> parse_list("a")
    [\'a\']
    >>> parse_list("a b c")
    [\'a\', \'b\', \'c\']
    >>> parse_list("[a, b, c]")
    [\'a\', \'b\', \'c\']
    >>> parse_list(\'a " " b\')
    [\'a\', \' \', \'b\']
    >>> parse_list(\'[a, ",a", "a,", ",", ]\')
    [\'a\', \',a\', \'a,\', \',\']
    '''

transitive_str: Incomplete
transitive_list: Incomplete
bool_or: Incomplete
distutils_settings: Incomplete

def line_iter(source) -> Generator[Incomplete, None, None]: ...

class DistutilsInfo:
    values: Incomplete
    def __init__(self, source: Incomplete | None = None, exn: Incomplete | None = None) -> None: ...
    def merge(self, other): ...
    def subs(self, aliases): ...
    def apply(self, extension) -> None: ...

def strip_string_literals(code, prefix: str = '__Pyx_L'):
    """
    Normalizes every string literal to be of the form '__Pyx_Lxxx',
    returning the normalized code and a mapping of labels to
    string literals.
    """

dependency_regex: Incomplete
dependency_after_from_regex: Incomplete

def normalize_existing(base_path, rel_paths): ...
def normalize_existing0(base_dir, rel_paths):
    """
    Given some base directory ``base_dir`` and a list of path names
    ``rel_paths``, normalize each relative path name ``rel`` by
    replacing it by ``os.path.join(base, rel)`` if that file exists.

    Return a couple ``(normalized, needed_base)`` where ``normalized``
    if the list of normalized file names and ``needed_base`` is
    ``base_dir`` if we actually needed ``base_dir``. If no paths were
    changed (for example, if all paths were already absolute), then
    ``needed_base`` is ``None``.
    """
def resolve_depends(depends, include_dirs): ...
def resolve_depend(depend, include_dirs): ...
def package(filename): ...
def fully_qualified_name(filename): ...
def parse_dependencies(source_filename): ...

class DependencyTree:
    context: Incomplete
    quiet: Incomplete
    def __init__(self, context, quiet: bool = False) -> None: ...
    def parse_dependencies(self, source_filename): ...
    def included_files(self, filename): ...
    def cimports_externs_incdirs(self, filename): ...
    def cimports(self, filename): ...
    def package(self, filename): ...
    def fully_qualified_name(self, filename): ...
    def find_pxd(self, module, filename: Incomplete | None = None): ...
    def cimported_files(self, filename): ...
    def immediate_dependencies(self, filename): ...
    def all_dependencies(self, filename): ...
    def timestamp(self, filename): ...
    def extract_timestamp(self, filename): ...
    def newest_dependency(self, filename): ...
    def transitive_fingerprint(self, filename, module, compilation_options):
        """
        Return a fingerprint of a cython file that is about to be cythonized.

        Fingerprints are looked up in future compilations. If the fingerprint
        is found, the cythonization can be skipped. The fingerprint must
        incorporate everything that has an influence on the generated code.
        """
    def distutils_info0(self, filename): ...
    def distutils_info(self, filename, aliases: Incomplete | None = None, base: Incomplete | None = None): ...
    def transitive_merge(self, node, extract, merge): ...
    def transitive_merge_helper(self, node, extract, merge, seen, stack, outgoing): ...

def create_dependency_tree(ctx: Incomplete | None = None, quiet: bool = False): ...
def default_create_extension(template, kwds): ...
def create_extension_list(patterns, exclude: Incomplete | None = None, ctx: Incomplete | None = None, aliases: Incomplete | None = None, quiet: bool = False, language: Incomplete | None = None, exclude_failures: bool = False): ...
def cythonize(module_list, exclude: Incomplete | None = None, nthreads: int = 0, aliases: Incomplete | None = None, quiet: bool = False, force: Incomplete | None = None, language: Incomplete | None = None, exclude_failures: bool = False, show_all_warnings: bool = False, **options):
    '''
    Compile a set of source modules into C/C++ files and return a list of distutils
    Extension objects for them.

    :param module_list: As module list, pass either a glob pattern, a list of glob
                        patterns or a list of Extension objects.  The latter
                        allows you to configure the extensions separately
                        through the normal distutils options.
                        You can also pass Extension objects that have
                        glob patterns as their sources. Then, cythonize
                        will resolve the pattern and create a
                        copy of the Extension for every matching file.

    :param exclude: When passing glob patterns as ``module_list``, you can exclude certain
                    module names explicitly by passing them into the ``exclude`` option.

    :param nthreads: The number of concurrent builds for parallel compilation
                     (requires the ``multiprocessing`` module).

    :param aliases: If you want to use compiler directives like ``# distutils: ...`` but
                    can only know at compile time (when running the ``setup.py``) which values
                    to use, you can use aliases and pass a dictionary mapping those aliases
                    to Python strings when calling :func:`cythonize`. As an example, say you
                    want to use the compiler
                    directive ``# distutils: include_dirs = ../static_libs/include/``
                    but this path isn\'t always fixed and you want to find it when running
                    the ``setup.py``. You can then do ``# distutils: include_dirs = MY_HEADERS``,
                    find the value of ``MY_HEADERS`` in the ``setup.py``, put it in a python
                    variable called ``foo`` as a string, and then call
                    ``cythonize(..., aliases={\'MY_HEADERS\': foo})``.

    :param quiet: If True, Cython won\'t print error, warning, or status messages during the
                  compilation.

    :param force: Forces the recompilation of the Cython modules, even if the timestamps
                  don\'t indicate that a recompilation is necessary.

    :param language: To globally enable C++ mode, you can pass ``language=\'c++\'``. Otherwise, this
                     will be determined at a per-file level based on compiler directives.  This
                     affects only modules found based on file names.  Extension instances passed
                     into :func:`cythonize` will not be changed. It is recommended to rather
                     use the compiler directive ``# distutils: language = c++`` than this option.

    :param exclude_failures: For a broad \'try to compile\' mode that ignores compilation
                             failures and simply excludes the failed extensions,
                             pass ``exclude_failures=True``. Note that this only
                             really makes sense for compiling ``.py`` files which can also
                             be used without compilation.

    :param show_all_warnings: By default, not all Cython warnings are printed.
                              Set to true to show all warnings.

    :param annotate: If ``True``, will produce a HTML file for each of the ``.pyx`` or ``.py``
                     files compiled. The HTML file gives an indication
                     of how much Python interaction there is in
                     each of the source code lines, compared to plain C code.
                     It also allows you to see the C/C++ code
                     generated for each line of Cython code. This report is invaluable when
                     optimizing a function for speed,
                     and for determining when to :ref:`release the GIL <nogil>`:
                     in general, a ``nogil`` block may contain only "white" code.
                     See examples in :ref:`determining_where_to_add_types` or
                     :ref:`primes`.


    :param annotate-fullc: If ``True`` will produce a colorized HTML version of
                           the source which includes entire generated C/C++-code.


    :param compiler_directives: Allow to set compiler directives in the ``setup.py`` like this:
                                ``compiler_directives={\'embedsignature\': True}``.
                                See :ref:`compiler-directives`.

    :param depfile: produce depfiles for the sources if True.
    '''
def fix_windows_unicode_modules(module_list): ...

compile_result_dir: Incomplete

def record_results(func): ...
def cythonize_one(pyx_file, c_file, fingerprint, quiet, options: Incomplete | None = None, raise_on_failure: bool = True, embedded_metadata: Incomplete | None = None, full_module_name: Incomplete | None = None, show_all_warnings: bool = False, progress: str = '') -> None: ...
def cythonize_one_helper(m): ...
def cleanup_cache(cache, target_size, ratio: float = 0.85) -> None: ...
