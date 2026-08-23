import json
from .nbbase import from_dict as from_dict
from .rwbase import NotebookReader as NotebookReader, NotebookWriter as NotebookWriter, rejoin_lines as rejoin_lines, split_lines as split_lines, strip_transient as strip_transient
from _typeshed import Incomplete

class BytesEncoder(json.JSONEncoder):
    """A JSON encoder that accepts b64 (and other *ascii*) bytestrings."""
    def default(self, obj):
        """Get the default value of an object."""

class JSONReader(NotebookReader):
    """A JSON notebook reader."""
    def reads(self, s, **kwargs):
        """Convert a string to a notebook."""
    def to_notebook(self, d, **kwargs):
        """Convert a dict to a notebook."""

class JSONWriter(NotebookWriter):
    """A JSON notebook writer."""
    def writes(self, nb, **kwargs):
        """Convert a notebook to a string."""

reads: Incomplete
read: Incomplete
to_notebook: Incomplete
write: Incomplete
writes: Incomplete
