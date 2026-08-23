from .base import Preprocessor as Preprocessor

class TagRemovePreprocessor(Preprocessor):
    """
    Removes inputs, outputs, or cells from a notebook that
    have tags that designate they are to be removed prior to exporting
    the notebook.

    remove_cell_tags
        removes cells tagged with these values

    remove_all_outputs_tags
        removes entire output areas on cells
        tagged with these values

    remove_single_output_tags
        removes individual output objects on
        outputs tagged with these values

    remove_input_tags
        removes inputs tagged with these values
    """
    remove_cell_tags: set[str]
    remove_all_outputs_tags: set[str]
    remove_single_output_tags: set[str]
    remove_input_tags: set[str]
    remove_metadata_fields: set[str]
    def check_cell_conditions(self, cell, resources, index):
        """
        Checks that a cell has a tag that is to be removed

        Returns: Boolean.
        True means cell should *not* be removed.
        """
    def preprocess(self, nb, resources):
        """
        Preprocessing to apply to each notebook. See base.py for details.
        """
    def preprocess_cell(self, cell, resources, cell_index):
        """
        Apply a transformation on each cell. See base.py for details.
        """
    def check_output_conditions(self, output, resources, cell_index, output_index):
        """
        Checks that an output has a tag that indicates removal.

        Returns: Boolean.
        True means output should *not* be removed.
        """
