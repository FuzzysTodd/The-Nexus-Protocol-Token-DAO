from . import Image as Image, ImageColor as ImageColor, ImageDraw as ImageDraw, ImageFont as ImageFont, ImagePath as ImagePath
from _typeshed import Incomplete

class Pen:
    """Stores an outline color and width."""
    color: Incomplete
    width: Incomplete
    def __init__(self, color, width: int = 1, opacity: int = 255) -> None: ...

class Brush:
    """Stores a fill color"""
    color: Incomplete
    def __init__(self, color, opacity: int = 255) -> None: ...

class Font:
    """Stores a TrueType font and color"""
    color: Incomplete
    font: Incomplete
    def __init__(self, color, file, size: int = 12) -> None: ...

class Draw:
    """
    (Experimental) WCK-style drawing interface
    """
    draw: Incomplete
    image: Incomplete
    transform: Incomplete
    def __init__(self, image, size: Incomplete | None = None, color: Incomplete | None = None) -> None: ...
    def flush(self): ...
    def render(self, op, xy, pen, brush: Incomplete | None = None) -> None: ...
    def settransform(self, offset) -> None:
        """Sets a transformation offset."""
    def arc(self, xy, start, end, *options) -> None:
        """
        Draws an arc (a portion of a circle outline) between the start and end
        angles, inside the given bounding box.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.arc`
        """
    def chord(self, xy, start, end, *options) -> None:
        """
        Same as :py:meth:`~PIL.ImageDraw2.Draw.arc`, but connects the end points
        with a straight line.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.chord`
        """
    def ellipse(self, xy, *options) -> None:
        """
        Draws an ellipse inside the given bounding box.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.ellipse`
        """
    def line(self, xy, *options) -> None:
        """
        Draws a line between the coordinates in the ``xy`` list.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.line`
        """
    def pieslice(self, xy, start, end, *options) -> None:
        """
        Same as arc, but also draws straight lines between the end points and the
        center of the bounding box.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.pieslice`
        """
    def polygon(self, xy, *options) -> None:
        """
        Draws a polygon.

        The polygon outline consists of straight lines between the given
        coordinates, plus a straight line between the last and the first
        coordinate.


        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.polygon`
        """
    def rectangle(self, xy, *options) -> None:
        """
        Draws a rectangle.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.rectangle`
        """
    def text(self, xy, text, font) -> None:
        """
        Draws the string at the given position.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.text`
        """
    def textbbox(self, xy, text, font):
        """
        Returns bounding box (in pixels) of given text.

        :return: ``(left, top, right, bottom)`` bounding box

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.textbbox`
        """
    def textlength(self, text, font):
        """
        Returns length (in pixels) of given text.
        This is the amount by which following text should be offset.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.textlength`
        """
