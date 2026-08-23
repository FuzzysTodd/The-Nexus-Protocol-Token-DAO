from . import EpsImagePlugin as EpsImagePlugin
from _typeshed import Incomplete

class PSDraw:
    """
    Sets up printing to the given file. If ``fp`` is omitted,
    ``sys.stdout.buffer`` or ``sys.stdout`` is assumed.
    """
    fp: Incomplete
    def __init__(self, fp: Incomplete | None = None) -> None: ...
    isofont: Incomplete
    def begin_document(self, id: Incomplete | None = None) -> None:
        """Set up printing of a document. (Write PostScript DSC header.)"""
    def end_document(self) -> None:
        """Ends printing. (Write PostScript DSC footer.)"""
    def setfont(self, font, size) -> None:
        """
        Selects which font to use.

        :param font: A PostScript font name
        :param size: Size in points.
        """
    def line(self, xy0, xy1) -> None:
        """
        Draws a line between the two points. Coordinates are given in
        PostScript point coordinates (72 points per inch, (0, 0) is the lower
        left corner of the page).
        """
    def rectangle(self, box) -> None:
        """
        Draws a rectangle.

        :param box: A tuple of four integers, specifying left, bottom, width and
           height.
        """
    def text(self, xy, text) -> None:
        """
        Draws text at the given position. You must use
        :py:meth:`~PIL.PSDraw.PSDraw.setfont` before calling this method.
        """
    def image(self, box, im, dpi: Incomplete | None = None) -> None:
        """Draw a PIL image, centered in the given box."""

EDROFF_PS: bytes
VDI_PS: bytes
ERROR_PS: bytes
