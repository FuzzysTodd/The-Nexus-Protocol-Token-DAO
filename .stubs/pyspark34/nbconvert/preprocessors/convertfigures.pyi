from .base import Preprocessor as Preprocessor
from _typeshed import Incomplete

class ConvertFiguresPreprocessor(Preprocessor):
    """
    Converts all of the outputs in a notebook from one format to another.
    """
    from_format: Incomplete
    to_format: Incomplete
    def __init__(self, **kw) -> None:
        """
        Public constructor
        """
    def convert_figure(self, data_format, data) -> None:
        """Convert the figure."""
    def preprocess_cell(self, cell, resources, cell_index):
        """
        Apply a transformation on each cell,

        See base.py
        """
