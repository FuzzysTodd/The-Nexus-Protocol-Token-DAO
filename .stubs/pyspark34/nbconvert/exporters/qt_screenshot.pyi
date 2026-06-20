from PyQt5.QtWebEngineWidgets import QWebEngineView
from _typeshed import Incomplete

QT_INSTALLED: bool
APP: Incomplete

class QtScreenshot(QWebEngineView):
    """A qt screenshot exporter."""
    app: Incomplete
    def __init__(self) -> None:
        """Initialize the exporter."""
    output_file: Incomplete
    paginate: Incomplete
    data: bytes
    export: Incomplete
    def capture(self, url, output_file, paginate) -> None:
        """Capture the screenshot."""
    size: Incomplete
    def on_loaded(self) -> None:
        """Handle app load."""
    def export_pdf(self) -> None:
        """Export to pdf."""
    def export_png(self) -> None:
        """Export to png."""
    def get_data(self) -> None:
        """Get output data."""
