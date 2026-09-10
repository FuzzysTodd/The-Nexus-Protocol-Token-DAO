from _typeshed import Incomplete
from fontTools.misc.loggingTools import LogMixin
from fontTools.pens.basePen import LoggingPen
from fontTools.pens.pointPen import AbstractPointPen
from fontTools.pens.transformPen import TransformPen, TransformPointPen
from fontTools.ttLib.tables._g_l_y_f import Glyph
from typing import Any, Callable, Dict, Tuple

__all__ = ['TTGlyphPen', 'TTGlyphPointPen']

class _TTGlyphBasePen:
    glyphSet: Incomplete
    handleOverflowingTransforms: Incomplete
    def __init__(self, glyphSet: Dict[str, Any] | None, handleOverflowingTransforms: bool = True) -> None:
        """
        Construct a new pen.

        Args:
            glyphSet (Dict[str, Any]): A glyphset object, used to resolve components.
            handleOverflowingTransforms (bool): See below.

        If ``handleOverflowingTransforms`` is True, the components' transform values
        are checked that they don't overflow the limits of a F2Dot14 number:
        -2.0 <= v < +2.0. If any transform value exceeds these, the composite
        glyph is decomposed.

        An exception to this rule is done for values that are very close to +2.0
        (both for consistency with the -2.0 case, and for the relative frequency
        these occur in real fonts). When almost +2.0 values occur (and all other
        values are within the range -2.0 <= x <= +2.0), they are clamped to the
        maximum positive value that can still be encoded as an F2Dot14: i.e.
        1.99993896484375.

        If False, no check is done and all components are translated unmodified
        into the glyf table, followed by an inevitable ``struct.error`` once an
        attempt is made to compile them.

        If both contours and components are present in a glyph, the components
        are decomposed.
        """
    points: Incomplete
    endPts: Incomplete
    types: Incomplete
    components: Incomplete
    def init(self) -> None: ...
    def addComponent(self, baseGlyphName: str, transformation: Tuple[float, float, float, float, float, float], identifier: str | None = None, **kwargs: Any) -> None:
        """
        Add a sub glyph.
        """
    def glyph(self, componentFlags: int = 4, dropImpliedOnCurves: bool = False, *, round: Callable[[float], int] = ...) -> Glyph:
        """
        Returns a :py:class:`~._g_l_y_f.Glyph` object representing the glyph.

        Args:
            componentFlags: Flags to use for component glyphs. (default: 0x04)

            dropImpliedOnCurves: Whether to remove implied-oncurve points. (default: False)
        """

class TTGlyphPen(_TTGlyphBasePen, LoggingPen):
    """
    Pen used for drawing to a TrueType glyph.

    This pen can be used to construct or modify glyphs in a TrueType format
    font. After using the pen to draw, use the ``.glyph()`` method to retrieve
    a :py:class:`~._g_l_y_f.Glyph` object representing the glyph.
    """
    drawMethod: str
    transformPen = TransformPen
    outputImpliedClosingLine: Incomplete
    def __init__(self, glyphSet: Dict[str, Any] | None = None, handleOverflowingTransforms: bool = True, outputImpliedClosingLine: bool = False) -> None: ...
    def lineTo(self, pt: Tuple[float, float]) -> None: ...
    def moveTo(self, pt: Tuple[float, float]) -> None: ...
    def curveTo(self, *points) -> None: ...
    def qCurveTo(self, *points) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...

class TTGlyphPointPen(_TTGlyphBasePen, LogMixin, AbstractPointPen):
    """
    Point pen used for drawing to a TrueType glyph.

    This pen can be used to construct or modify glyphs in a TrueType format
    font. After using the pen to draw, use the ``.glyph()`` method to retrieve
    a :py:class:`~._g_l_y_f.Glyph` object representing the glyph.
    """
    drawMethod: str
    transformPen = TransformPointPen
    def init(self) -> None: ...
    def beginPath(self, identifier: str | None = None, **kwargs: Any) -> None:
        """
        Start a new sub path.
        """
    def endPath(self) -> None:
        """
        End the current sub path.
        """
    def addPoint(self, pt: Tuple[float, float], segmentType: str | None = None, smooth: bool = False, name: str | None = None, identifier: str | None = None, **kwargs: Any) -> None:
        """
        Add a point to the current sub path.
        """
