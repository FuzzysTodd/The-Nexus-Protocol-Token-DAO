from .exporter import Exporter as Exporter
from _typeshed import Incomplete

class NotebookExporter(Exporter):
    """Exports to an IPython notebook.

    This is useful when you want to use nbconvert's preprocessors to operate on
    a notebook (e.g. to execute it) and then write it back to a notebook file.
    """
    nbformat_version: Incomplete
    output_mimetype: str
    export_from_notebook: str
    def from_notebook_node(self, nb, resources: Incomplete | None = None, **kw):
        """Convert from notebook node."""
