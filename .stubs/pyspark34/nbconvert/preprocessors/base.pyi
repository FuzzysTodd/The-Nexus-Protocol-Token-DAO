from _typeshed import Incomplete
from nbconvert.utils.base import NbConvertBase as NbConvertBase

class Preprocessor(NbConvertBase):
    """A configurable preprocessor

    Inherit from this class if you wish to have configurability for your
    preprocessor.

    Any configurable traitlets this class exposed will be configurable in
    profiles using c.SubClassName.attribute = value

    You can overwrite `preprocess_cell()` to apply a transformation
    independently on each cell or `preprocess()` if you prefer your own
    logic. See corresponding docstring for information.

    Disabled by default and can be enabled via the config by
        'c.YourPreprocessorName.enabled = True'
    """
    enabled: Incomplete
    def __init__(self, **kw) -> None:
        """
        Public constructor

        Parameters
        ----------
        config : Config
            Configuration file structure
        `**kw`
            Additional keyword arguments passed to parent
        """
    def __call__(self, nb, resources):
        """Apply the preprocessor."""
    def preprocess(self, nb, resources):
        """
        Preprocessing to apply on each notebook.

        Must return modified nb, resources.

        If you wish to apply your preprocessing to each cell, you might want
        to override preprocess_cell method instead.

        Parameters
        ----------
        nb : NotebookNode
            Notebook being converted
        resources : dictionary
            Additional resources used in the conversion process.  Allows
            preprocessors to pass variables into the Jinja engine.
        """
    def preprocess_cell(self, cell, resources, index) -> None:
        """
        Override if you want to apply some preprocessing to each cell.
        Must return modified cell and resource dictionary.

        Parameters
        ----------
        cell : NotebookNode cell
            Notebook cell being processed
        resources : dictionary
            Additional resources used in the conversion process.  Allows
            preprocessors to pass variables into the Jinja engine.
        index : int
            Index of the cell being processed
        """
