from _typeshed import Incomplete
from nbformat._struct import Struct as Struct

nbformat: int
nbformat_minor: int
nbformat_schema: Incomplete

class NotebookNode(Struct):
    """A notebook node object."""

def from_dict(d):
    """Create notebook node(s) from an object."""
def str_passthrough(obj):
    """
    Used to be cast_unicode, add this temporarily to make sure no further breakage.
    """
def cast_str(obj):
    """Cast an object as a string."""
def new_output(output_type, output_text: Incomplete | None = None, output_png: Incomplete | None = None, output_html: Incomplete | None = None, output_svg: Incomplete | None = None, output_latex: Incomplete | None = None, output_json: Incomplete | None = None, output_javascript: Incomplete | None = None, output_jpeg: Incomplete | None = None, prompt_number: Incomplete | None = None, ename: Incomplete | None = None, evalue: Incomplete | None = None, traceback: Incomplete | None = None, stream: Incomplete | None = None, metadata: Incomplete | None = None):
    """Create a new output, to go in the ``cell.outputs`` list of a code cell."""
def new_code_cell(input: Incomplete | None = None, prompt_number: Incomplete | None = None, outputs: Incomplete | None = None, language: str = 'python', collapsed: bool = False, metadata: Incomplete | None = None):
    """Create a new code cell with input and output"""
def new_text_cell(cell_type, source: Incomplete | None = None, rendered: Incomplete | None = None, metadata: Incomplete | None = None):
    """Create a new text cell."""
def new_heading_cell(source: Incomplete | None = None, level: int = 1, rendered: Incomplete | None = None, metadata: Incomplete | None = None):
    """Create a new section cell with a given integer level."""
def new_worksheet(name: Incomplete | None = None, cells: Incomplete | None = None, metadata: Incomplete | None = None):
    """Create a worksheet by name with with a list of cells."""
def new_notebook(name: Incomplete | None = None, metadata: Incomplete | None = None, worksheets: Incomplete | None = None):
    """Create a notebook by name, id and a list of worksheets."""
def new_metadata(name: Incomplete | None = None, authors: Incomplete | None = None, license: Incomplete | None = None, created: Incomplete | None = None, modified: Incomplete | None = None, gistid: Incomplete | None = None):
    """Create a new metadata node."""
def new_author(name: Incomplete | None = None, email: Incomplete | None = None, affiliation: Incomplete | None = None, url: Incomplete | None = None):
    """Create a new author."""
