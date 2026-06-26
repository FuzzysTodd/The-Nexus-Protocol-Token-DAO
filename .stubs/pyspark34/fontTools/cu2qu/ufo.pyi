from _typeshed import Incomplete
from fontTools.pens.basePen import AbstractPen

__all__ = ['fonts_to_quadratic', 'font_to_quadratic']

class GetSegmentsPen(AbstractPen):
    """Pen to collect segments into lists of points for conversion.

    Curves always include their initial on-curve point, so some points are
    duplicated between segments.
    """
    segments: Incomplete
    def __init__(self) -> None: ...
    def moveTo(self, pt) -> None: ...
    def lineTo(self, pt) -> None: ...
    def qCurveTo(self, *points) -> None: ...
    def curveTo(self, *points) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def addComponent(self, glyphName, transformation) -> None: ...

def fonts_to_quadratic(fonts, max_err_em: Incomplete | None = None, max_err: Incomplete | None = None, reverse_direction: bool = False, stats: Incomplete | None = None, dump_stats: bool = False, remember_curve_type: bool = True, all_quadratic: bool = True):
    '''Convert the curves of a collection of fonts to quadratic.

    All curves will be converted to quadratic at once, ensuring interpolation
    compatibility. If this is not required, calling fonts_to_quadratic with one
    font at a time may yield slightly more optimized results.

    Return the set of modified glyph names if any, else return an empty set.

    By default, cu2qu stores the curve type in the fonts\' lib, under a private
    key "com.github.googlei18n.cu2qu.curve_type", and will not try to convert
    them again if the curve type is already set to "quadratic".
    Setting \'remember_curve_type\' to False disables this optimization.

    Raises IncompatibleFontsError if same-named glyphs from different fonts
    have non-interpolatable outlines.
    '''
def font_to_quadratic(font, **kwargs):
    """Convenience wrapper around fonts_to_quadratic, for just one font.
    Return the set of modified glyph names if any, else return empty set.
    """
