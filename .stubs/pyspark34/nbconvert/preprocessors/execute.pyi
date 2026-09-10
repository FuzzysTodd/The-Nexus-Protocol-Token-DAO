import typing as t
from .base import Preprocessor as Preprocessor
from jupyter_client.manager import KernelManager as KernelManager
from nbclient.client import NotebookClient
from nbclient.exceptions import CellExecutionError as CellExecutionError
from nbformat import NotebookNode

def executenb(*args, **kwargs):
    """DEPRECATED."""

class ExecutePreprocessor(Preprocessor, NotebookClient):
    """
    Executes all the cells in a notebook
    """
    def __init__(self, **kw) -> None:
        """Initialize the preprocessor."""
    def preprocess(self, nb: NotebookNode, resources: t.Any = None, km: KernelManager | None = None) -> tuple[NotebookNode, dict[str, t.Any]]:
        """
        Preprocess notebook executing each code cell.

        The input argument *nb* is modified in-place.

        Note that this function recalls NotebookClient.__init__, which may look wrong.
        However since the preprocess call acts line an init on execution state it's expected.
        Therefore, we need to capture it here again to properly reset because traitlet
        assignments are not passed. There is a risk if traitlets apply any side effects for
        dual init.
        The risk should be manageable, and this approach minimizes side-effects relative
        to other alternatives.

        One alternative but rejected implementation would be to copy the client's init internals
        which has already gotten out of sync with nbclient 0.5 release before nbconvert 6.0 released.

        Parameters
        ----------
        nb : NotebookNode
            Notebook being executed.
        resources : dictionary (optional)
            Additional resources used in the conversion process. For example,
            passing ``{'metadata': {'path': run_path}}`` sets the
            execution path to ``run_path``.
        km: KernelManager (optional)
            Optional kernel manager. If none is provided, a kernel manager will
            be created.

        Returns
        -------
        nb : NotebookNode
            The executed notebook.
        resources : dictionary
            Additional resources used in the conversion process.
        """
    def preprocess_cell(self, cell, resources, index):
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
