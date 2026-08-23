from .base import Preprocessor as Preprocessor
from _typeshed import Incomplete

class HighlightMagicsPreprocessor(Preprocessor):
    """
    Detects and tags code cells that use a different languages than Python.
    """
    default_languages: Incomplete
    languages: Incomplete
    re_magic_language: Incomplete
    def __init__(self, config: Incomplete | None = None, **kw) -> None:
        """Public constructor"""
    def which_magic_language(self, source):
        """
        When a cell uses another language through a magic extension,
        the other language is returned.
        If no language magic is detected, this function returns None.

        Parameters
        ----------
        source: str
            Source code of the cell to highlight
        """
    def preprocess_cell(self, cell, resources, cell_index):
        """
        Tags cells using a magic extension language

        Parameters
        ----------
        cell : NotebookNode cell
            Notebook cell being processed
        resources : dictionary
            Additional resources used in the conversion process.  Allows
            preprocessors to pass variables into the Jinja engine.
        cell_index : int
            Index of the cell being processed (see base.py)
        """
