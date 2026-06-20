from .base import Preprocessor as Preprocessor
from _typeshed import Incomplete

class ExtractAttachmentsPreprocessor(Preprocessor):
    """
    Extracts attachments from all (markdown and raw) cells in a notebook.
    The extracted attachments are stored in a directory ('attachments' by default).
    https://nbformat.readthedocs.io/en/latest/format_description.html#cell-attachments
    """
    attachments_directory_template: Incomplete
    use_separate_dir: Incomplete
    path_name: str
    resources_item_key: str
    def __init__(self, **kw) -> None:
        """
        Public constructor
        """
    def preprocess(self, nb, resources):
        """
        Determine some settings and apply preprocessor to notebook
        """
    def preprocess_cell(self, cell, resources, index):
        """
        Extract attachments to individual files and
        change references to them.
        E.g.
        '![image.png](attachment:021fdd80.png)'
        becomes
        '![image.png]({path_name}/021fdd80.png)'
        Assumes self.path_name and self.resources_item_key is set properly (usually in preprocess).
        """
