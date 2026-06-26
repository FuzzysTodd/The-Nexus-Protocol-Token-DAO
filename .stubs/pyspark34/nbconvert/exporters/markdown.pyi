from .templateexporter import TemplateExporter as TemplateExporter

class MarkdownExporter(TemplateExporter):
    """
    Exports to a markdown document (.md)
    """
    export_from_notebook: str
    output_mimetype: str
    @property
    def default_config(self): ...
