import json
from .rwbase import NotebookReader as NotebookReader, NotebookWriter as NotebookWriter, rejoin_lines as rejoin_lines, split_lines as split_lines, strip_transient as strip_transient
from _typeshed import Incomplete
from nbformat.notebooknode import from_dict as from_dict

class BytesEncoder(json.JSONEncoder):
    """A JSON encoder that accepts b64 (and other *ascii*) bytestrings."""
    def default(self, obj):
        """Get the default value of an object."""

class JSONReader(NotebookReader):
    """A JSON notebook reader."""
    def reads(self, s, **kwargs):
        """Read a JSON string into a Notebook object"""
    def to_notebook(self, d, **kwargs):
        """Convert a disk-format notebook dict to in-memory NotebookNode

        handles multi-line values as strings, scrubbing of transient values, etc.
        """

class JSONWriter(NotebookWriter):
    """A JSON notebook writer."""
    def writes(self, nb, **kwargs):
        """Serialize a NotebookNode object as a JSON string"""

reads: Incomplete
read: Incomplete
to_notebook: Incomplete
write: Incomplete
writes: Incomplete
