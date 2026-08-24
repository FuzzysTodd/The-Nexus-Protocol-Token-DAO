from . import Image as Image
from _typeshed import Incomplete

def getrgb(color):
    """
     Convert a color string to an RGB or RGBA tuple. If the string cannot be
     parsed, this function raises a :py:exc:`ValueError` exception.

    .. versionadded:: 1.1.4

    :param color: A color string
    :return: ``(red, green, blue[, alpha])``
    """
def getcolor(color, mode):
    """
    Same as :py:func:`~PIL.ImageColor.getrgb` for most modes. However, if
    ``mode`` is HSV, converts the RGB value to a HSV value, or if ``mode`` is
    not color or a palette image, converts the RGB value to a greyscale value.
    If the string cannot be parsed, this function raises a :py:exc:`ValueError`
    exception.

    .. versionadded:: 1.1.4

    :param color: A color string
    :param mode: Convert result to this mode
    :return: ``(graylevel[, alpha]) or (red, green, blue[, alpha])``
    """

colormap: Incomplete
