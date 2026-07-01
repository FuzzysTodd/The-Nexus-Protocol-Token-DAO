from .html import HTMLExporter as HTMLExporter
from _typeshed import Incomplete

class QtExporter(HTMLExporter):
    """A qt exporter."""
    paginate: Incomplete
    format: str
    def from_notebook_node(self, nb, resources: Incomplete | None = None, **kw):
        """Convert from notebook node."""
