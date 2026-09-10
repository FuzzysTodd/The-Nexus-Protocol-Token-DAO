from .templateexporter import TemplateExporter as TemplateExporter
from _typeshed import Incomplete
from collections.abc import Generator
from nbconvert.filters.highlight import Highlight2HTML as Highlight2HTML
from nbconvert.filters.markdown_mistune import IPythonRenderer as IPythonRenderer, MarkdownWithMath as MarkdownWithMath
from nbconvert.filters.widgetsdatatypefilter import WidgetsDataTypeFilter as WidgetsDataTypeFilter
from nbconvert.utils.iso639_1 import iso639_1 as iso639_1
from nbformat import NotebookNode as NotebookNode
from typing import Any, Dict, Tuple

def find_lab_theme(theme_name):
    """
    Find a JupyterLab theme location by name.

    Parameters
    ----------
    theme_name : str
        The name of the labextension theme you want to find.

    Raises
    ------
    ValueError
        If the theme was not found, or if it was not specific enough.

    Returns
    -------
    theme_name: str
        Full theme name (with scope, if any)
    labextension_path : Path
        The path to the found labextension on the system.
    """

class HTMLExporter(TemplateExporter):
    """
    Exports a basic HTML document.  This exporter assists with the export of
    HTML.  Inherit from it if you are writing your own HTML template and need
    custom preprocessors/filters.  If you don't need custom preprocessors/
    filters, just change the 'template_file' config option.
    """
    export_from_notebook: str
    anchor_link_text: Incomplete
    exclude_anchor_links: Incomplete
    require_js_url: Incomplete
    mathjax_url: Incomplete
    mermaid_js_url: Incomplete
    jquery_url: Incomplete
    jupyter_widgets_base_url: Incomplete
    widget_renderer_url: Incomplete
    html_manager_semver_range: Incomplete
    theme: Incomplete
    sanitize_html: Incomplete
    embed_images: Incomplete
    output_mimetype: str
    @property
    def default_config(self): ...
    language_code: Incomplete
    def markdown2html(self, context, source):
        """Markdown to HTML filter respecting the anchor_link_text setting"""
    def default_filters(self) -> Generator[Incomplete, Incomplete, None]:
        """Get the default filters."""
    def from_notebook_node(self, nb: NotebookNode, resources: Dict[str, Any] | None = None, **kw: Any) -> Tuple[str, Dict[str, Any]]:
        """Convert from notebook node."""
