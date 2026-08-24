from .base import get_exporter as get_exporter
from .templateexporter import TemplateExporter as TemplateExporter
from _typeshed import Incomplete

class ScriptExporter(TemplateExporter):
    """A script exporter."""
    export_from_notebook: str
    file_extension: Incomplete
    output_mimetype: Incomplete
    def from_notebook_node(self, nb, resources: Incomplete | None = None, **kw):
        """Convert from notebook node."""
