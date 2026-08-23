from .base import Preprocessor as Preprocessor
from _typeshed import Incomplete

def guess_extension_without_jpe(mimetype):
    """
    This function fixes a problem with '.jpe' extensions
    of jpeg images which are then not recognised by latex.
    For any other case, the function works in the same way
    as mimetypes.guess_extension
    """
def platform_utf_8_encode(data):
    """Encode data based on platform."""

class ExtractOutputPreprocessor(Preprocessor):
    """
    Extracts all of the outputs from the notebook file.  The extracted
    outputs are returned in the 'resources' dictionary.
    """
    output_filename_template: Incomplete
    extract_output_types: Incomplete
    def preprocess_cell(self, cell, resources, cell_index):
        """
        Apply a transformation on each cell,

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
