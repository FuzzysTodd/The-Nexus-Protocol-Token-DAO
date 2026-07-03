from _typeshed import Incomplete
from nbformat.notebooknode import NotebookNode as NotebookNode

nbformat: int
nbformat_minor: int
nbformat_schema: Incomplete

def validate(node, ref: Incomplete | None = None):
    """validate a v4 node"""
def new_output(output_type, data: Incomplete | None = None, **kwargs):
    """Create a new output, to go in the ``cell.outputs`` list of a code cell."""
def output_from_msg(msg):
    """Create a NotebookNode for an output from a kernel's IOPub message.

    Returns
    -------
    NotebookNode: the output as a notebook node.

    Raises
    ------
    ValueError: if the message is not an output message.

    """
def new_code_cell(source: str = '', **kwargs):
    """Create a new code cell"""
def new_markdown_cell(source: str = '', **kwargs):
    """Create a new markdown cell"""
def new_raw_cell(source: str = '', **kwargs):
    """Create a new raw cell"""
def new_notebook(**kwargs):
    """Create a new notebook"""
