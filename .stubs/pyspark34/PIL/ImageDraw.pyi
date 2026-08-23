from . import Image as Image, ImageColor as ImageColor
from _typeshed import Incomplete

class ImageDraw:
    font: Incomplete
    palette: Incomplete
    im: Incomplete
    draw: Incomplete
    mode: Incomplete
    ink: Incomplete
    fontmode: str
    fill: bool
    def __init__(self, im, mode: Incomplete | None = None) -> None:
        """
        Create a drawing instance.

        :param im: The image to draw in.
        :param mode: Optional mode to use for color values.  For RGB
           images, this argument can be RGB or RGBA (to blend the
           drawing into the image).  For all other modes, this argument
           must be the same as the image mode.  If omitted, the mode
           defaults to the mode of the image.
        """
    def getfont(self):
        '''
        Get the current default font.

        To set the default font for this ImageDraw instance::

            from PIL import ImageDraw, ImageFont
            draw.font = ImageFont.truetype("Tests/fonts/FreeMono.ttf")

        To set the default font for all future ImageDraw instances::

            from PIL import ImageDraw, ImageFont
            ImageDraw.ImageDraw.font = ImageFont.truetype("Tests/fonts/FreeMono.ttf")

        If the current default font is ``None``,
        it is initialized with ``ImageFont.load_default()``.

        :returns: An image font.'''
    def arc(self, xy, start, end, fill: Incomplete | None = None, width: int = 1) -> None:
        """Draw an arc."""
    def bitmap(self, xy, bitmap, fill: Incomplete | None = None) -> None:
        """Draw a bitmap."""
    def chord(self, xy, start, end, fill: Incomplete | None = None, outline: Incomplete | None = None, width: int = 1) -> None:
        """Draw a chord."""
    def ellipse(self, xy, fill: Incomplete | None = None, outline: Incomplete | None = None, width: int = 1) -> None:
        """Draw an ellipse."""
    def line(self, xy, fill: Incomplete | None = None, width: int = 0, joint: Incomplete | None = None):
        """Draw a line, or a connected sequence of line segments."""
    def shape(self, shape, fill: Incomplete | None = None, outline: Incomplete | None = None) -> None:
        """(Experimental) Draw a shape."""
    def pieslice(self, xy, start, end, fill: Incomplete | None = None, outline: Incomplete | None = None, width: int = 1) -> None:
        """Draw a pieslice."""
    def point(self, xy, fill: Incomplete | None = None) -> None:
        """Draw one or more individual pixels."""
    def polygon(self, xy, fill: Incomplete | None = None, outline: Incomplete | None = None, width: int = 1) -> None:
        """Draw a polygon."""
    def regular_polygon(self, bounding_circle, n_sides, rotation: int = 0, fill: Incomplete | None = None, outline: Incomplete | None = None, width: int = 1) -> None:
        """Draw a regular polygon."""
    def rectangle(self, xy, fill: Incomplete | None = None, outline: Incomplete | None = None, width: int = 1) -> None:
        """Draw a rectangle."""
    def rounded_rectangle(self, xy, radius: int = 0, fill: Incomplete | None = None, outline: Incomplete | None = None, width: int = 1, *, corners: Incomplete | None = None):
        """Draw a rounded rectangle."""
    def text(self, xy, text, fill: Incomplete | None = None, font: Incomplete | None = None, anchor: Incomplete | None = None, spacing: int = 4, align: str = 'left', direction: Incomplete | None = None, features: Incomplete | None = None, language: Incomplete | None = None, stroke_width: int = 0, stroke_fill: Incomplete | None = None, embedded_color: bool = False, *args, **kwargs):
        """Draw text."""
    def multiline_text(self, xy, text, fill: Incomplete | None = None, font: Incomplete | None = None, anchor: Incomplete | None = None, spacing: int = 4, align: str = 'left', direction: Incomplete | None = None, features: Incomplete | None = None, language: Incomplete | None = None, stroke_width: int = 0, stroke_fill: Incomplete | None = None, embedded_color: bool = False) -> None: ...
    def textlength(self, text, font: Incomplete | None = None, direction: Incomplete | None = None, features: Incomplete | None = None, language: Incomplete | None = None, embedded_color: bool = False):
        """Get the length of a given string, in pixels with 1/64 precision."""
    def textbbox(self, xy, text, font: Incomplete | None = None, anchor: Incomplete | None = None, spacing: int = 4, align: str = 'left', direction: Incomplete | None = None, features: Incomplete | None = None, language: Incomplete | None = None, stroke_width: int = 0, embedded_color: bool = False):
        """Get the bounding box of a given string, in pixels."""
    def multiline_textbbox(self, xy, text, font: Incomplete | None = None, anchor: Incomplete | None = None, spacing: int = 4, align: str = 'left', direction: Incomplete | None = None, features: Incomplete | None = None, language: Incomplete | None = None, stroke_width: int = 0, embedded_color: bool = False): ...

def Draw(im, mode: Incomplete | None = None):
    """
    A simple 2D drawing interface for PIL images.

    :param im: The image to draw in.
    :param mode: Optional mode to use for color values.  For RGB
       images, this argument can be RGB or RGBA (to blend the
       drawing into the image).  For all other modes, this argument
       must be the same as the image mode.  If omitted, the mode
       defaults to the mode of the image.
    """

Outline: Incomplete

def getdraw(im: Incomplete | None = None, hints: Incomplete | None = None):
    """
    (Experimental) A more advanced 2D drawing interface for PIL images,
    based on the WCK interface.

    :param im: The image to draw in.
    :param hints: An optional list of hints.
    :returns: A (drawing context, drawing resource factory) tuple.
    """
def floodfill(image, xy, value, border: Incomplete | None = None, thresh: int = 0) -> None:
    """
    (experimental) Fills a bounded region with a given color.

    :param image: Target image.
    :param xy: Seed position (a 2-item coordinate tuple). See
        :ref:`coordinate-system`.
    :param value: Fill color.
    :param border: Optional border value.  If given, the region consists of
        pixels with a color different from the border color.  If not given,
        the region consists of pixels having the same color as the seed
        pixel.
    :param thresh: Optional threshold value which specifies a maximum
        tolerable difference of a pixel value from the 'background' in
        order for it to be replaced. Useful for filling regions of
        non-homogeneous, but similar, colors.
    """
