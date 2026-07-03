from .convertfigures import ConvertFiguresPreprocessor as ConvertFiguresPreprocessor
from _typeshed import Incomplete
from nbconvert.utils.io import FormatSafeDict as FormatSafeDict

INKSCAPE_APP: str
INKSCAPE_APP_v1: str

class SVG2PDFPreprocessor(ConvertFiguresPreprocessor):
    """
    Converts all of the outputs in a notebook from SVG to PDF.
    """
    inkscape_version: Incomplete
    command: Incomplete
    inkscape: Incomplete
    def convert_figure(self, data_format, data):
        """
        Convert a single SVG figure to PDF.  Returns converted data.
        """
