from .qt_exporter import QtExporter as QtExporter
from _typeshed import Incomplete

class QtPDFExporter(QtExporter):
    """Writer designed to write to PDF files.

    This inherits from :class:`HTMLExporter`. It creates the HTML using the
    template machinery, and then uses pyqtwebengine to create a pdf.
    """
    export_from_notebook: str
    format: str
    paginate: Incomplete
