from .base import Preprocessor as Preprocessor
from _typeshed import Incomplete
from collections.abc import Generator

class ClearMetadataPreprocessor(Preprocessor):
    """
    Removes all the metadata from all code cells in a notebook.
    """
    clear_cell_metadata: Incomplete
    clear_notebook_metadata: Incomplete
    preserve_nb_metadata_mask: Incomplete
    preserve_cell_metadata_mask: Incomplete
    def current_key(self, mask_key):
        """Get the current key for a mask key."""
    def current_mask(self, mask):
        """Get the current mask for a mask."""
    def nested_masks(self, mask):
        """Get the nested masks for a mask."""
    def nested_filter(self, items, mask) -> Generator[Incomplete, None, None]:
        """Get the nested filter for items given a mask."""
    def preprocess_cell(self, cell, resources, cell_index):
        """
        All the code cells are returned with an empty metadata field.
        """
    def preprocess(self, nb, resources):
        """
        Preprocessing to apply on each notebook.

        Must return modified nb, resources.

        Parameters
        ----------
        nb : NotebookNode
            Notebook being converted
        resources : dictionary
            Additional resources used in the conversion process.  Allows
            preprocessors to pass variables into the Jinja engine.
        """
