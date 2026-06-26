from .templateexporter import TemplateExporter as TemplateExporter

class ASCIIDocExporter(TemplateExporter):
    """
    Exports to an ASCIIDoc document (.asciidoc)
    """
    output_mimetype: str
    export_from_notebook: str
    @property
    def default_config(self): ...
