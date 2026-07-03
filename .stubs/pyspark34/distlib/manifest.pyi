from _typeshed import Incomplete

__all__ = ['Manifest']

class Manifest:
    """
    A list of files built by exploring the filesystem and filtered by applying various
    patterns to what we find there.
    """
    base: Incomplete
    prefix: Incomplete
    allfiles: Incomplete
    files: Incomplete
    def __init__(self, base: Incomplete | None = None) -> None:
        """
        Initialise an instance.

        :param base: The base directory to explore under.
        """
    def findall(self) -> None:
        """Find all files under the base and set ``allfiles`` to the absolute
        pathnames of files found.
        """
    def add(self, item) -> None:
        """
        Add a file to the manifest.

        :param item: The pathname to add. This can be relative to the base.
        """
    def add_many(self, items) -> None:
        """
        Add a list of files to the manifest.

        :param items: The pathnames to add. These can be relative to the base.
        """
    def sorted(self, wantdirs: bool = False):
        """
        Return sorted files in directory order
        """
    def clear(self) -> None:
        """Clear all collected files."""
    def process_directive(self, directive) -> None:
        """
        Process a directive which either adds some files from ``allfiles`` to
        ``files``, or removes some files from ``files``.

        :param directive: The directive to process. This should be in a format
                     compatible with distutils ``MANIFEST.in`` files:

                     http://docs.python.org/distutils/sourcedist.html#commands
        """
