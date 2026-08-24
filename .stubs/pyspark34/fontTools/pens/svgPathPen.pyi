from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen as BasePen
from typing import Callable

def pointToString(pt, ntos=...): ...

class SVGPathPen(BasePen):
    """Pen to draw SVG path d commands.

    Example::
        >>> pen = SVGPathPen(None)
        >>> pen.moveTo((0, 0))
        >>> pen.lineTo((1, 1))
        >>> pen.curveTo((2, 2), (3, 3), (4, 4))
        >>> pen.closePath()
        >>> pen.getCommands()
        'M0 0 1 1C2 2 3 3 4 4Z'

    Args:
        glyphSet: a dictionary of drawable glyph objects keyed by name
            used to resolve component references in composite glyphs.
        ntos: a callable that takes a number and returns a string, to
            customize how numbers are formatted (default: str).

    Note:
        Fonts have a coordinate system where Y grows up, whereas in SVG,
        Y grows down.  As such, rendering path data from this pen in
        SVG typically results in upside-down glyphs.  You can fix this
        by wrapping the data from this pen in an SVG group element with
        transform, or wrap this pen in a transform pen.  For example:

            spen = svgPathPen.SVGPathPen(glyphset)
            pen= TransformPen(spen , (1, 0, 0, -1, 0, 0))
            glyphset[glyphname].draw(pen)
            print(tpen.getCommands())
    """
    def __init__(self, glyphSet, ntos: Callable[[float], str] = ...) -> None: ...
    def getCommands(self): ...

def main(args: Incomplete | None = None) -> None:
    """Generate per-character SVG from font and text"""
