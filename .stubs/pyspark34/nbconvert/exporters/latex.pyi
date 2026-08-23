from .templateexporter import TemplateExporter as TemplateExporter
from _typeshed import Incomplete
from collections.abc import Generator
from nbconvert.filters.filter_links import resolve_references as resolve_references
from nbconvert.filters.highlight import Highlight2Latex as Highlight2Latex
from nbconvert.filters.pandoc import ConvertExplicitlyRelativePaths as ConvertExplicitlyRelativePaths

class LatexExporter(TemplateExporter):
    '''
    Exports to a Latex template.  Inherit from this class if your template is
    LaTeX based and you need custom transformers/filters.
    If you don\'t need custom transformers/filters, just change the
    \'template_file\' config option.  Place your template in the special "/latex"
    subfolder of the "../templates" folder.
    '''
    export_from_notebook: str
    output_mimetype: str
    def default_filters(self) -> Generator[Incomplete, Incomplete, None]:
        """Get the default filters."""
    @property
    def default_config(self): ...
    def from_notebook_node(self, nb, resources: Incomplete | None = None, **kw):
        """Convert from notebook node."""
