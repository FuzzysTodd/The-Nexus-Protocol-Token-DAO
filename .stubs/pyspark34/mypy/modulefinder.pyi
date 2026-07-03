from _typeshed import Incomplete
from enum import Enum
from mypy import pyinfo as pyinfo
from mypy.errors import CompileError as CompileError
from mypy.fscache import FileSystemCache as FileSystemCache
from mypy.nodes import MypyFile as MypyFile
from mypy.options import Options as Options
from mypy.stubinfo import approved_stub_package_exists as approved_stub_package_exists
from typing import List, NamedTuple, Tuple, Union
from typing_extensions import Final, TypeAlias as _TypeAlias

class SearchPaths(NamedTuple):
    python_path: tuple[str, ...]
    mypy_path: tuple[str, ...]
    package_path: tuple[str, ...]
    typeshed_path: tuple[str, ...]
OnePackageDir = Tuple[str, bool]
PackageDirs = List[OnePackageDir]
StdlibVersions: _TypeAlias
PYTHON_EXTENSIONS: Final[Incomplete]

class ModuleNotFoundReason(Enum):
    NOT_FOUND: int
    FOUND_WITHOUT_TYPE_HINTS: int
    WRONG_WORKING_DIRECTORY: int
    APPROVED_STUBS_NOT_INSTALLED: int
    def error_message_templates(self, daemon: bool) -> tuple[str, list[str]]: ...
ModuleSearchResult = Union[str, ModuleNotFoundReason]

class BuildSource:
    """A single source file."""
    path: Incomplete
    module: Incomplete
    text: Incomplete
    base_dir: Incomplete
    followed: Incomplete
    def __init__(self, path: str | None, module: str | None, text: str | None = None, base_dir: str | None = None, followed: bool = False) -> None: ...

class BuildSourceSet:
    """Helper to efficiently test a file's membership in a set of build sources."""
    source_text_present: bool
    source_modules: Incomplete
    source_paths: Incomplete
    def __init__(self, sources: list[BuildSource]) -> None: ...
    def is_source(self, file: MypyFile) -> bool: ...

class FindModuleCache:
    """Module finder with integrated cache.

    Module locations and some intermediate results are cached internally
    and can be cleared with the clear() method.

    All file system accesses are performed through a FileSystemCache,
    which is not ever cleared by this class. If necessary it must be
    cleared by client code.
    """
    search_paths: Incomplete
    source_set: Incomplete
    fscache: Incomplete
    initial_components: Incomplete
    results: Incomplete
    ns_ancestors: Incomplete
    options: Incomplete
    stdlib_py_versions: Incomplete
    def __init__(self, search_paths: SearchPaths, fscache: FileSystemCache | None, options: Options | None, stdlib_py_versions: StdlibVersions | None = None, source_set: BuildSourceSet | None = None) -> None: ...
    def clear(self) -> None: ...
    def find_module_via_source_set(self, id: str) -> ModuleSearchResult | None:
        """Fast path to find modules by looking through the input sources

        This is only used when --fast-module-lookup is passed on the command line."""
    def find_lib_path_dirs(self, id: str, lib_path: tuple[str, ...]) -> PackageDirs:
        """Find which elements of a lib_path have the directory a module needs to exist.

        This is run for the python_path, mypy_path, and typeshed_path search paths.
        """
    def get_toplevel_possibilities(self, lib_path: tuple[str, ...], id: str) -> list[str]:
        """Find which elements of lib_path could contain a particular top-level module.

        In practice, almost all modules can be routed to the correct entry in
        lib_path by looking at just the first component of the module name.

        We take advantage of this by enumerating the contents of all of the
        directories on the lib_path and building a map of which entries in
        the lib_path could contain each potential top-level module that appears.
        """
    def find_module(self, id: str, *, fast_path: bool = False) -> ModuleSearchResult:
        """Return the path of the module source file or why it wasn't found.

        If fast_path is True, prioritize performance over generating detailed
        error descriptions.
        """
    def find_modules_recursive(self, module: str) -> list[BuildSource]: ...

def matches_exclude(subpath: str, excludes: list[str], fscache: FileSystemCache, verbose: bool) -> bool: ...
def is_init_file(path: str) -> bool: ...
def verify_module(fscache: FileSystemCache, id: str, path: str, prefix: str) -> bool:
    """Check that all packages containing id have a __init__ file."""
def highest_init_level(fscache: FileSystemCache, id: str, path: str, prefix: str) -> int:
    """Compute the highest level where an __init__ file is found."""
def mypy_path() -> list[str]: ...
def default_lib_path(data_dir: str, pyversion: tuple[int, int], custom_typeshed_dir: str | None) -> list[str]:
    """Return default standard library search paths."""
def get_search_dirs(python_executable: str | None) -> tuple[list[str], list[str]]:
    """Find package directories for given python.

    This runs a subprocess call, which generates a list of the directories in sys.path.
    To avoid repeatedly calling a subprocess (which can be slow!) we
    lru_cache the results.
    """
def compute_search_paths(sources: list[BuildSource], options: Options, data_dir: str, alt_lib_path: str | None = None) -> SearchPaths:
    """Compute the search paths as specified in PEP 561.

    There are the following 4 members created:
    - User code (from `sources`)
    - MYPYPATH (set either via config or environment variable)
    - installed package directories (which will later be split into stub-only and inline)
    - typeshed
    """
def load_stdlib_py_versions(custom_typeshed_dir: str | None) -> StdlibVersions:
    """Return dict with minimum and maximum Python versions of stdlib modules.

    The contents look like
    {..., 'secrets': ((3, 6), None), 'symbol': ((2, 7), (3, 9)), ...}

    None means there is no maximum version.
    """
def parse_version(version: str) -> tuple[int, int]: ...
def typeshed_py_version(options: Options) -> tuple[int, int]:
    """Return Python version used for checking whether module supports typeshed."""
