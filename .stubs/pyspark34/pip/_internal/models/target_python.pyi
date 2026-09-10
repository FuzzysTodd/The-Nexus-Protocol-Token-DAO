from _typeshed import Incomplete
from pip._internal.utils.compatibility_tags import get_supported as get_supported, version_info_to_nodot as version_info_to_nodot
from pip._internal.utils.misc import normalize_version_info as normalize_version_info
from pip._vendor.packaging.tags import Tag as Tag
from typing import List, Set, Tuple

class TargetPython:
    """
    Encapsulates the properties of a Python interpreter one is targeting
    for a package install, download, etc.
    """
    abis: Incomplete
    implementation: Incomplete
    platforms: Incomplete
    py_version: Incomplete
    py_version_info: Incomplete
    def __init__(self, platforms: List[str] | None = None, py_version_info: Tuple[int, ...] | None = None, abis: List[str] | None = None, implementation: str | None = None) -> None:
        """
        :param platforms: A list of strings or None. If None, searches for
            packages that are supported by the current system. Otherwise, will
            find packages that can be built on the platforms passed in. These
            packages will only be downloaded for distribution: they will
            not be built locally.
        :param py_version_info: An optional tuple of ints representing the
            Python version information to use (e.g. `sys.version_info[:3]`).
            This can have length 1, 2, or 3 when provided.
        :param abis: A list of strings or None. This is passed to
            compatibility_tags.py's get_supported() function as is.
        :param implementation: A string or None. This is passed to
            compatibility_tags.py's get_supported() function as is.
        """
    def format_given(self) -> str:
        """
        Format the given, non-None attributes for display.
        """
    def get_sorted_tags(self) -> List[Tag]:
        """
        Return the supported PEP 425 tags to check wheel candidates against.

        The tags are returned in order of preference (most preferred first).
        """
    def get_unsorted_tags(self) -> Set[Tag]:
        """Exactly the same as get_sorted_tags, but returns a set.

        This is important for performance.
        """
