from .nbbase import from_dict as from_dict
from .rwbase import NotebookReader as NotebookReader, NotebookWriter as NotebookWriter
from _typeshed import Incomplete

class JSONReader(NotebookReader):
    """A JSON notebook reader."""
    def reads(self, s, **kwargs):
        """Convert a string to a notebook object."""
    def to_notebook(self, d, **kwargs):
        """Convert from a raw JSON dict to a nested NotebookNode structure."""

class JSONWriter(NotebookWriter):
    """A JSON notebook writer."""
    def writes(self, nb, **kwargs):
        """Convert a notebook object to a string."""

reads: Incomplete
read: Incomplete
to_notebook: Incomplete
write: Incomplete
writes: Incomplete
