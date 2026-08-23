from . import Image as Image
from _typeshed import Incomplete

class PhotoImage:
    """
    A Tkinter-compatible photo image.  This can be used
    everywhere Tkinter expects an image object.  If the image is an RGBA
    image, pixels having alpha 0 are treated as transparent.

    The constructor takes either a PIL image, or a mode and a size.
    Alternatively, you can use the ``file`` or ``data`` options to initialize
    the photo image object.

    :param image: Either a PIL image, or a mode string.  If a mode string is
                  used, a size must also be given.
    :param size: If the first argument is a mode string, this defines the size
                 of the image.
    :keyword file: A filename to load the image from (using
                   ``Image.open(file)``).
    :keyword data: An 8-bit string containing image data (as loaded from an
                   image file).
    """
    tk: Incomplete
    def __init__(self, image: Incomplete | None = None, size: Incomplete | None = None, **kw) -> None: ...
    def __del__(self) -> None: ...
    def width(self):
        """
        Get the width of the image.

        :return: The width, in pixels.
        """
    def height(self):
        """
        Get the height of the image.

        :return: The height, in pixels.
        """
    def paste(self, im) -> None:
        """
        Paste a PIL image into the photo image.  Note that this can
        be very slow if the photo image is displayed.

        :param im: A PIL image. The size must match the target region.  If the
                   mode does not match, the image is converted to the mode of
                   the bitmap image.
        """

class BitmapImage:
    '''
    A Tkinter-compatible bitmap image.  This can be used everywhere Tkinter
    expects an image object.

    The given image must have mode "1".  Pixels having value 0 are treated as
    transparent.  Options, if any, are passed on to Tkinter.  The most commonly
    used option is ``foreground``, which is used to specify the color for the
    non-transparent parts.  See the Tkinter documentation for information on
    how to specify colours.

    :param image: A PIL image.
    '''
    def __init__(self, image: Incomplete | None = None, **kw) -> None: ...
    def __del__(self) -> None: ...
    def width(self):
        """
        Get the width of the image.

        :return: The width, in pixels.
        """
    def height(self):
        """
        Get the height of the image.

        :return: The height, in pixels.
        """

def getimage(photo):
    """Copies the contents of a PhotoImage to a PIL image memory."""
