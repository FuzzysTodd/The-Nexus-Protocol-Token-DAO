from .nbbase import nbformat as nbformat, nbformat_minor as nbformat_minor, new_code_cell as new_code_cell, new_heading_cell as new_heading_cell, new_notebook as new_notebook, new_text_cell as new_text_cell, new_worksheet as new_worksheet
from .rwbase import NotebookReader as NotebookReader, NotebookWriter as NotebookWriter
from _typeshed import Incomplete
from collections.abc import Generator

class PyReaderError(Exception):
    """An error raised for a pyreader error."""

class PyReader(NotebookReader):
    """A python notebook reader."""
    def reads(self, s, **kwargs):
        """Convert a string to a notebook"""
    def to_notebook(self, s, **kwargs):
        """Convert a string to a notebook"""
    def new_cell(self, state, lines, **kwargs):
        """Create a new cell."""
    def split_lines_into_blocks(self, lines) -> Generator[Incomplete, None, None]:
        """Split lines into code blocks."""

class PyWriter(NotebookWriter):
    """A Python notebook writer."""
    def writes(self, nb, **kwargs):
        """Convert a notebook to a string."""

reads: Incomplete
read: Incomplete
to_notebook: Incomplete
write: Incomplete
writes: Incomplete
