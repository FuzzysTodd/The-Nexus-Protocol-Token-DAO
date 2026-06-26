from _typeshed import Incomplete

def cell_preprocessor(function):
    """
    Wrap a function to be executed on all cells of a notebook

    The wrapped function should have these parameters:

    cell : NotebookNode cell
        Notebook cell being processed
    resources : dictionary
        Additional resources used in the conversion process.  Allows
        preprocessors to pass variables into the Jinja engine.
    index : int
        Index of the cell being processed
    """

cr_pat: Incomplete

def coalesce_streams(cell, resources, index):
    """
    Merge consecutive sequences of stream output into single stream
    to prevent extra newlines inserted at flush calls

    Parameters
    ----------
    cell : NotebookNode cell
        Notebook cell being processed
    resources : dictionary
        Additional resources used in the conversion process.  Allows
        transformers to pass variables into the Jinja engine.
    index : int
        Index of the cell being processed
    """
