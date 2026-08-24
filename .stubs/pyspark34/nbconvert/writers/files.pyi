from .base import WriterBase as WriterBase
from _typeshed import Incomplete
from nbconvert.utils.io import link_or_copy as link_or_copy

class FilesWriter(WriterBase):
    """Consumes nbconvert output and produces files."""
    build_directory: Incomplete
    relpath: Incomplete
    def __init__(self, **kw) -> None:
        """Initialize the writer."""
    def write(self, output, resources, notebook_name: Incomplete | None = None, **kw):
        """
        Consume and write Jinja output to the file system.  Output directory
        is set via the 'build_directory' variable of this instance (a
        configurable).

        See base for more...
        """
