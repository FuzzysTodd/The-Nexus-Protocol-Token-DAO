from _typeshed import Incomplete
from mypy.fscache import FileSystemCache as FileSystemCache
from mypy.modulefinder import BuildSource as BuildSource, PYTHON_EXTENSIONS as PYTHON_EXTENSIONS, matches_exclude as matches_exclude, mypy_path as mypy_path
from mypy.options import Options as Options
from typing import Sequence
from typing_extensions import Final

PY_EXTENSIONS: Final[Incomplete]

class InvalidSourceList(Exception):
    """Exception indicating a problem in the list of sources given to mypy."""

def create_source_list(paths: Sequence[str], options: Options, fscache: FileSystemCache | None = None, allow_empty_dir: bool = False) -> list[BuildSource]:
    """From a list of source files/directories, makes a list of BuildSources.

    Raises InvalidSourceList on errors.
    """
def keyfunc(name: str) -> tuple[bool, int, str]:
    """Determines sort order for directory listing.

    The desirable properties are:
    1) foo < foo.pyi < foo.py
    2) __init__.py[i] < foo
    """
def normalise_package_base(root: str) -> str: ...
def get_explicit_package_bases(options: Options) -> list[str] | None:
    """Returns explicit package bases to use if the option is enabled, or None if disabled.

    We currently use MYPYPATH and the current directory as the package bases. In the future,
    when --namespace-packages is the default could also use the values passed with the
    --package-root flag, see #9632.

    Values returned are normalised so we can use simple string comparisons in
    SourceFinder.is_explicit_package_base
    """

class SourceFinder:
    fscache: Incomplete
    explicit_package_bases: Incomplete
    namespace_packages: Incomplete
    exclude: Incomplete
    verbosity: Incomplete
    def __init__(self, fscache: FileSystemCache, options: Options) -> None: ...
    def is_explicit_package_base(self, path: str) -> bool: ...
    def find_sources_in_dir(self, path: str) -> list[BuildSource]: ...
    def crawl_up(self, path: str) -> tuple[str, str]:
        '''Given a .py[i] filename, return module and base directory.

        For example, given "xxx/yyy/foo/bar.py", we might return something like:
        ("foo.bar", "xxx/yyy")

        If namespace packages is off, we crawl upwards until we find a directory without
        an __init__.py

        If namespace packages is on, we crawl upwards until the nearest explicit base directory.
        Failing that, we return one past the highest directory containing an __init__.py

        We won\'t crawl past directories with invalid package names.
        The base directory returned is an absolute path.
        '''
    def crawl_up_dir(self, dir: str) -> tuple[str, str]: ...
    def get_init_file(self, dir: str) -> str | None:
        """Check whether a directory contains a file named __init__.py[i].

        If so, return the file's name (with dir prefixed).  If not, return None.

        This prefers .pyi over .py (because of the ordering of PY_EXTENSIONS).
        """

def module_join(parent: str, child: str) -> str:
    """Join module ids, accounting for a possibly empty parent."""
def strip_py(arg: str) -> str | None:
    """Strip a trailing .py or .pyi suffix.

    Return None if no such suffix is found.
    """
