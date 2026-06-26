from _typeshed import Incomplete
from mypy.fscache import FileSystemCache
from mypy.modulefinder import BuildSource
from mypy.options import Options as Options
from typing import List, Sequence, Tuple
from typing_extensions import Final

PY_EXTENSIONS: Final[Incomplete]

class InvalidSourceList(Exception):
    """Exception indicating a problem in the list of sources given to mypy."""

def create_source_list(files: Sequence[str], options: Options, fscache: FileSystemCache | None = None, allow_empty_dir: bool = True) -> List[BuildSource]:
    """From a list of source files/directories, makes a list of BuildSources.

    Raises InvalidSourceList on errors.
    """
def keyfunc(name: str) -> Tuple[int, str]:
    """Determines sort order for directory listing.

    The desirable property is foo < foo.pyi < foo.py.
    """

class SourceFinder:
    fscache: Incomplete
    package_cache: Incomplete
    def __init__(self, fscache: FileSystemCache) -> None: ...
    def expand_dir(self, arg: str, mod_prefix: str = '') -> List[BuildSource]:
        """Convert a directory name to a list of sources to build."""
    def crawl_up(self, arg: str) -> Tuple[str, str]:
        """Given a .py[i] filename, return module and base directory

        We crawl up the path until we find a directory without
        __init__.py[i], or until we run out of path components.
        """
    def crawl_up_dir(self, dir: str) -> Tuple[str, str]:
        """Given a directory name, return the corresponding module name and base directory

        Use package_cache to cache results.
        """
    def get_init_file(self, dir: str) -> str | None:
        """Check whether a directory contains a file named __init__.py[i].

        If so, return the file's name (with dir prefixed).  If not, return
        None.

        This prefers .pyi over .py (because of the ordering of PY_EXTENSIONS).
        """

def module_join(parent: str, child: str) -> str:
    """Join module ids, accounting for a possibly empty parent."""
def strip_py(arg: str) -> str | None:
    """Strip a trailing .py or .pyi suffix.

    Return None if no such suffix is found.
    """
