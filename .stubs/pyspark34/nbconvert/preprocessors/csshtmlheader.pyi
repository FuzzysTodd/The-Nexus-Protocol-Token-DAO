from .base import Preprocessor as Preprocessor
from _typeshed import Incomplete

class CSSHTMLHeaderPreprocessor(Preprocessor):
    """
    Preprocessor used to pre-process notebook for HTML output.  Adds IPython notebook
    front-end CSS and Pygments CSS to HTML output.
    """
    highlight_class: Incomplete
    style: Incomplete
    def __init__(self, *pargs, **kwargs) -> None:
        """Initialize the preprocessor."""
    def preprocess(self, nb, resources):
        '''Fetch and add CSS to the resource dictionary

        Fetch CSS from IPython and Pygments to add at the beginning
        of the html files.  Add this css in resources in the
        "inlining.css" key

        Parameters
        ----------
        nb : NotebookNode
            Notebook being converted
        resources : dictionary
            Additional resources used in the conversion process.  Allows
            preprocessors to pass variables into the Jinja engine.
        '''
