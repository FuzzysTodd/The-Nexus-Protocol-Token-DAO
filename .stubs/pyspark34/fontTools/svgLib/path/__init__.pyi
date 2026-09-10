from .parser import parse_path as parse_path
from .shapes import PathBuilder as PathBuilder
from _typeshed import Incomplete
from fontTools.misc import etree as etree
from fontTools.misc.textTools import tostr as tostr
from fontTools.pens.transformPen import TransformPen as TransformPen

class SVGPath:
    '''Parse SVG ``path`` elements from a file or string, and draw them
    onto a glyph object that supports the FontTools Pen protocol.

    For example, reading from an SVG file and drawing to a Defcon Glyph:

        import defcon
        glyph = defcon.Glyph()
        pen = glyph.getPen()
        svg = SVGPath("path/to/a.svg")
        svg.draw(pen)

    Or reading from a string containing SVG data, using the alternative
    \'fromstring\' (a class method):

        data = \'<?xml version="1.0" ...\'
        svg = SVGPath.fromstring(data)
        svg.draw(pen)

    Both constructors can optionally take a \'transform\' matrix (6-float
    tuple, or a FontTools Transform object) to modify the draw output.
    '''
    root: Incomplete
    transform: Incomplete
    def __init__(self, filename: Incomplete | None = None, transform: Incomplete | None = None) -> None: ...
    @classmethod
    def fromstring(cls, data, transform: Incomplete | None = None): ...
    def draw(self, pen) -> None: ...
