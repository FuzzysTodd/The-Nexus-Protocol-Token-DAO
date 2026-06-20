from _typeshed import Incomplete
from nbformat._struct import Struct as Struct

class NotebookNode(Struct):
    """A notebook node object."""

def from_dict(d):
    """Create notebook node(s) from an object."""
def new_code_cell(code: Incomplete | None = None, prompt_number: Incomplete | None = None):
    """Create a new code cell with input and output"""
def new_text_cell(text: Incomplete | None = None):
    """Create a new text cell."""
def new_notebook(cells: Incomplete | None = None):
    """Create a notebook by name, id and a list of worksheets."""
