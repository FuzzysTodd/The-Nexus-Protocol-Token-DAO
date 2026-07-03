from .base import Preprocessor as Preprocessor
from _typeshed import Incomplete

class ClearOutputPreprocessor(Preprocessor):
    """
    Removes the output from all code cells in a notebook.
    """
    remove_metadata_fields: Incomplete
    def preprocess_cell(self, cell, resources, cell_index):
        """
        Apply a transformation on each cell. See base.py for details.
        """
