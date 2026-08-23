from ._mathtext import RasterParse as RasterParse, VectorParse as VectorParse, get_unicode_index as get_unicode_index
from _typeshed import Incomplete
from matplotlib.font_manager import FontProperties as FontProperties
from matplotlib.ft2font import FT2Image as FT2Image, LOAD_NO_HINTING as LOAD_NO_HINTING
from typing import NamedTuple

class MathtextBackend:
    """
    The base class for the mathtext backend-specific code.  `MathtextBackend`
    subclasses interface between mathtext and specific Matplotlib graphics
    backends.

    Subclasses need to override the following:

    - :meth:`render_glyph`
    - :meth:`render_rect_filled`
    - :meth:`get_results`

    And optionally, if you need to use a FreeType hinting style:

    - :meth:`get_hinting_type`
    """
    width: int
    height: int
    depth: int
    def __init__(self) -> None: ...
    def set_canvas_size(self, w, h, d) -> None:
        """Set the dimension of the drawing canvas."""
    def render_glyph(self, ox, oy, info) -> None:
        """
        Draw a glyph described by *info* to the reference point (*ox*,
        *oy*).
        """
    def render_rect_filled(self, x1, y1, x2, y2) -> None:
        """
        Draw a filled black rectangle from (*x1*, *y1*) to (*x2*, *y2*).
        """
    def get_results(self, box) -> None:
        """
        Return a backend-specific tuple to return to the backend after
        all processing is done.
        """
    def get_hinting_type(self):
        """
        Get the FreeType hinting type to use with this particular
        backend.
        """

class MathtextBackendAgg(MathtextBackend):
    """
    Render glyphs and rectangles to an FTImage buffer, which is later
    transferred to the Agg image by the Agg backend.
    """
    ox: int
    oy: int
    image: Incomplete
    mode: str
    bbox: Incomplete
    def __init__(self) -> None: ...
    def set_canvas_size(self, w, h, d) -> None: ...
    def render_glyph(self, ox, oy, info) -> None: ...
    def render_rect_filled(self, x1, y1, x2, y2) -> None: ...
    def get_results(self, box): ...
    def get_hinting_type(self): ...

class MathtextBackendPath(MathtextBackend):
    """
    Store information to write a mathtext rendering to the text path
    machinery.
    """

    class _Result(NamedTuple):
        width: Incomplete
        height: Incomplete
        depth: Incomplete
        glyphs: Incomplete
        rects: Incomplete
    glyphs: Incomplete
    rects: Incomplete
    def __init__(self) -> None: ...
    def render_glyph(self, ox, oy, info) -> None: ...
    def render_rect_filled(self, x1, y1, x2, y2) -> None: ...
    def get_results(self, box): ...

class MathTextWarning(Warning): ...

class MathTextParser:
    def __init__(self, output) -> None:
        '''
        Create a MathTextParser for the given backend *output*.

        Parameters
        ----------
        output : {"path", "agg"}
            Whether to return a `VectorParse` ("path") or a
            `RasterParse` ("agg", or its synonym "macosx").
        '''
    def parse(self, s, dpi: int = 72, prop: Incomplete | None = None):
        '''
        Parse the given math expression *s* at the given *dpi*.  If *prop* is
        provided, it is a `.FontProperties` object specifying the "default"
        font to use in the math expression, used for all non-math text.

        The results are cached, so multiple calls to `parse`
        with the same expression should be fast.

        Depending on the *output* type, this returns either a `VectorParse` or
        a `RasterParse`.
        '''

def math_to_image(s, filename_or_obj, prop: Incomplete | None = None, dpi: Incomplete | None = None, format: Incomplete | None = None, *, color: Incomplete | None = None):
    """
    Given a math expression, renders it in a closely-clipped bounding
    box to an image file.

    Parameters
    ----------
    s : str
        A math expression.  The math portion must be enclosed in dollar signs.
    filename_or_obj : str or path-like or file-like
        Where to write the image data.
    prop : `.FontProperties`, optional
        The size and style of the text.
    dpi : float, optional
        The output dpi.  If not set, the dpi is determined as for
        `.Figure.savefig`.
    format : str, optional
        The output format, e.g., 'svg', 'pdf', 'ps' or 'png'.  If not set, the
        format is determined as for `.Figure.savefig`.
    color : str, optional
        Foreground color, defaults to :rc:`text.color`.
    """
