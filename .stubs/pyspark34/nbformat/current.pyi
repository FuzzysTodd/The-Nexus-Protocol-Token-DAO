from .converter import convert as convert
from .validator import validate as validate
from nbformat.v3 import NotebookNode as NotebookNode, nbformat as nbformat, nbformat_minor as nbformat_minor, nbformat_schema as nbformat_schema, new_author as new_author, new_code_cell as new_code_cell, new_heading_cell as new_heading_cell, new_metadata as new_metadata, new_notebook as new_notebook, new_output as new_output, new_text_cell as new_text_cell, new_worksheet as new_worksheet, parse_filename as parse_filename, to_notebook_json as to_notebook_json

__all__ = ['NotebookNode', 'new_code_cell', 'new_text_cell', 'new_notebook', 'new_output', 'new_worksheet', 'parse_filename', 'new_metadata', 'new_author', 'new_heading_cell', 'nbformat', 'nbformat_minor', 'nbformat_schema', 'to_notebook_json', 'convert', 'validate', 'NBFormatError', 'parse_py', 'reads_json', 'writes_json', 'reads_py', 'writes_py', 'reads', 'writes', 'read', 'write']

current_nbformat = nbformat
current_nbformat_minor = nbformat_minor

class NBFormatError(ValueError):
    """An error raised for an nbformat error."""

def parse_py(s, **kwargs):
    """Parse a string into a (nbformat, string) tuple."""
def reads_json(nbjson, **kwargs):
    """DEPRECATED, use reads"""
def writes_json(nb, **kwargs):
    """DEPRECATED, use writes"""
def reads_py(s, **kwargs):
    """DEPRECATED: use nbconvert"""
def writes_py(nb, **kwargs):
    """DEPRECATED: use nbconvert"""
def reads(s, format: str = 'DEPRECATED', version=..., **kwargs):
    """Read a notebook from a string and return the NotebookNode object.

    This function properly handles notebooks of any version. The notebook
    returned will always be in the current version's format.

    Parameters
    ----------
    s : unicode
        The raw unicode string to read the notebook from.

    Returns
    -------
    nb : NotebookNode
        The notebook that was read.
    """
def writes(nb, format: str = 'DEPRECATED', version=..., **kwargs):
    """Write a notebook to a string in a given format in the current nbformat version.

    This function always writes the notebook in the current nbformat version.

    Parameters
    ----------
    nb : NotebookNode
        The notebook to write.
    version : int
        The nbformat version to write.
        Used for downgrading notebooks.

    Returns
    -------
    s : unicode
        The notebook string.
    """
def read(fp, format: str = 'DEPRECATED', **kwargs):
    """Read a notebook from a file and return the NotebookNode object.

    This function properly handles notebooks of any version. The notebook
    returned will always be in the current version's format.

    Parameters
    ----------
    fp : file
        Any file-like object with a read method.

    Returns
    -------
    nb : NotebookNode
        The notebook that was read.
    """
def write(nb, fp, format: str = 'DEPRECATED', **kwargs):
    """Write a notebook to a file in a given format in the current nbformat version.

    This function always writes the notebook in the current nbformat version.

    Parameters
    ----------
    nb : NotebookNode
        The notebook to write.
    fp : file
        Any file-like object with a write method.
    """
