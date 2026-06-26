from .base import Preprocessor as Preprocessor
from _typeshed import Incomplete

class LatexPreprocessor(Preprocessor):
    """Preprocessor for latex destined documents.

    Populates the ``latex`` key in the resources dict,
    adding definitions for pygments highlight styles.

    Sets the authors, date and title of the latex document,
    overriding the values given in the metadata.
    """
    date: Incomplete
    title: Incomplete
    author_names: Incomplete
    style: Incomplete
    def preprocess(self, nb, resources):
        """Preprocessing to apply on each notebook.

        Parameters
        ----------
        nb : NotebookNode
            Notebook being converted
        resources : dictionary
            Additional resources used in the conversion process.  Allows
            preprocessors to pass variables into the Jinja engine.
        """
