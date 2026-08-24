from .html import HTMLExporter as HTMLExporter
from _typeshed import Incomplete

PLAYWRIGHT_INSTALLED: Incomplete
IS_WINDOWS: Incomplete

class WebPDFExporter(HTMLExporter):
    """Writer designed to write to PDF files.

    This inherits from :class:`HTMLExporter`. It creates the HTML using the
    template machinery, and then run playwright to create a pdf.
    """
    export_from_notebook: str
    allow_chromium_download: Incomplete
    paginate: Incomplete
    disable_sandbox: Incomplete
    def run_playwright(self, html):
        """Run playwright."""
    def from_notebook_node(self, nb, resources: Incomplete | None = None, **kw):
        """Convert from a notebook node."""
