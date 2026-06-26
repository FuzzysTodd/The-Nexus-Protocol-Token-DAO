from .convert import downgrade as downgrade, upgrade as upgrade
from .nbbase import NotebookNode as NotebookNode, new_author as new_author, new_code_cell as new_code_cell, new_metadata as new_metadata, new_notebook as new_notebook, new_output as new_output, new_text_cell as new_text_cell, new_worksheet as new_worksheet

nbformat: int
nbformat_minor: int

def parse_filename(fname):
    """Parse a notebook filename.

    This function takes a notebook filename and returns the notebook
    format (json/py) and the notebook name. This logic can be
    summarized as follows:

    * notebook.ipynb -> (notebook.ipynb, notebook, json)
    * notebook.json  -> (notebook.json, notebook, json)
    * notebook.py    -> (notebook.py, notebook, py)
    * notebook       -> (notebook.ipynb, notebook, json)

    Parameters
    ----------
    fname : unicode
        The notebook filename. The filename can use a specific filename
        extention (.ipynb, .json, .py) or none, in which case .ipynb will
        be assumed.

    Returns
    -------
    (fname, name, format) : (unicode, unicode, unicode)
        The filename, notebook name and format.
    """
