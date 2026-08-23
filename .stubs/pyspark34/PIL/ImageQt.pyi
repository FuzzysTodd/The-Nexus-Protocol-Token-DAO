from . import Image as Image
from ._util import is_path as is_path
from PySide6.QtGui import QImage
from _typeshed import Incomplete

qt_versions: Incomplete
qt_is_installed: bool
qt_version: Incomplete

def rgb(r, g, b, a: int = 255):
    """(Internal) Turns an RGB color into a Qt compatible color integer."""
def fromqimage(im):
    """
    :param im: QImage or PIL ImageQt object
    """
def fromqpixmap(im): ...
def align8to32(bytes, width, mode):
    """
    converts each scanline of data from 8 bit to 32 bit aligned
    """

class ImageQt(QImage):
    def __init__(self, im) -> None:
        """
            An PIL image wrapper for Qt.  This is a subclass of PyQt's QImage
            class.

            :param im: A PIL Image object, or a file name (given either as
                Python string or a PyQt string object).
            """

def toqimage(im): ...
def toqpixmap(im): ...
