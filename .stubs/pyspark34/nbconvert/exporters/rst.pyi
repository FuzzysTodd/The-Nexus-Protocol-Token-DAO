from .templateexporter import TemplateExporter as TemplateExporter

class RSTExporter(TemplateExporter):
    """
    Exports reStructuredText documents.
    """
    output_mimetype: str
    export_from_notebook: str
    @property
    def default_config(self): ...
