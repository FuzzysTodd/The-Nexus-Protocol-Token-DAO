from _typeshed import Incomplete
from fontTools.pens.basePen import AbstractPen as AbstractPen, DecomposingPen as DecomposingPen
from fontTools.pens.pointPen import AbstractPointPen as AbstractPointPen, DecomposingPointPen as DecomposingPointPen
from fontTools.pens.recordingPen import RecordingPen as RecordingPen

class _PassThruComponentsMixin:
    def addComponent(self, glyphName, transformation, **kwargs) -> None: ...

class FilterPen(_PassThruComponentsMixin, AbstractPen):
    """Base class for pens that apply some transformation to the coordinates
    they receive and pass them to another pen.

    You can override any of its methods. The default implementation does
    nothing, but passes the commands unmodified to the other pen.

    >>> from fontTools.pens.recordingPen import RecordingPen
    >>> rec = RecordingPen()
    >>> pen = FilterPen(rec)
    >>> v = iter(rec.value)

    >>> pen.moveTo((0, 0))
    >>> next(v)
    ('moveTo', ((0, 0),))

    >>> pen.lineTo((1, 1))
    >>> next(v)
    ('lineTo', ((1, 1),))

    >>> pen.curveTo((2, 2), (3, 3), (4, 4))
    >>> next(v)
    ('curveTo', ((2, 2), (3, 3), (4, 4)))

    >>> pen.qCurveTo((5, 5), (6, 6), (7, 7), (8, 8))
    >>> next(v)
    ('qCurveTo', ((5, 5), (6, 6), (7, 7), (8, 8)))

    >>> pen.closePath()
    >>> next(v)
    ('closePath', ())

    >>> pen.moveTo((9, 9))
    >>> next(v)
    ('moveTo', ((9, 9),))

    >>> pen.endPath()
    >>> next(v)
    ('endPath', ())

    >>> pen.addComponent('foo', (1, 0, 0, 1, 0, 0))
    >>> next(v)
    ('addComponent', ('foo', (1, 0, 0, 1, 0, 0)))
    """
    current_pt: Incomplete
    def __init__(self, outPen) -> None: ...
    def moveTo(self, pt) -> None: ...
    def lineTo(self, pt) -> None: ...
    def curveTo(self, *points) -> None: ...
    def qCurveTo(self, *points) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...

class ContourFilterPen(_PassThruComponentsMixin, RecordingPen):
    '''A "buffered" filter pen that accumulates contour data, passes
    it through a ``filterContour`` method when the contour is closed or ended,
    and finally draws the result with the output pen.

    Components are passed through unchanged.
    '''
    def __init__(self, outPen) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def filterContour(self, contour) -> None:
        '''Subclasses must override this to perform the filtering.

        The contour is a list of pen (operator, operands) tuples.
        Operators are strings corresponding to the AbstractPen methods:
        "moveTo", "lineTo", "curveTo", "qCurveTo", "closePath" and
        "endPath". The operands are the positional arguments that are
        passed to each method.

        If the method doesn\'t return a value (i.e. returns None), it\'s
        assumed that the argument was modified in-place.
        Otherwise, the return value is drawn with the output pen.
        '''

class FilterPointPen(_PassThruComponentsMixin, AbstractPointPen):
    '''Baseclass for point pens that apply some transformation to the
    coordinates they receive and pass them to another point pen.

    You can override any of its methods. The default implementation does
    nothing, but passes the commands unmodified to the other pen.

    >>> from fontTools.pens.recordingPen import RecordingPointPen
    >>> rec = RecordingPointPen()
    >>> pen = FilterPointPen(rec)
    >>> v = iter(rec.value)
    >>> pen.beginPath(identifier="abc")
    >>> next(v)
    (\'beginPath\', (), {\'identifier\': \'abc\'})
    >>> pen.addPoint((1, 2), "line", False)
    >>> next(v)
    (\'addPoint\', ((1, 2), \'line\', False, None), {})
    >>> pen.addComponent("a", (2, 0, 0, 2, 10, -10), identifier="0001")
    >>> next(v)
    (\'addComponent\', (\'a\', (2, 0, 0, 2, 10, -10)), {\'identifier\': \'0001\'})
    >>> pen.endPath()
    >>> next(v)
    (\'endPath\', (), {})
    '''
    def __init__(self, outPen) -> None: ...
    def beginPath(self, **kwargs) -> None: ...
    def endPath(self) -> None: ...
    def addPoint(self, pt, segmentType: Incomplete | None = None, smooth: bool = False, name: Incomplete | None = None, **kwargs) -> None: ...

class _DecomposingFilterPenMixin:
    """Mixin class that decomposes components as regular contours.

    Shared by both DecomposingFilterPen and DecomposingFilterPointPen.

    Takes two required parameters, another (segment or point) pen 'outPen' to draw
    with, and a 'glyphSet' dict of drawable glyph objects to draw components from.

    The 'skipMissingComponents' and 'reverseFlipped' optional arguments work the
    same as in the DecomposingPen/DecomposingPointPen. Both are False by default.

    In addition, the decomposing filter pens also take the following two options:

    'include' is an optional set of component base glyph names to consider for
    decomposition; the default include=None means decompose all components no matter
    the base glyph name).

    'decomposeNested' (bool) controls whether to recurse decomposition into nested
    components of components (this only matters when 'include' was also provided);
    if False, only decompose top-level components included in the set, but not
    also their children.
    """
    skipMissingComponents: bool
    include: Incomplete
    decomposeNested: Incomplete
    def __init__(self, outPen, glyphSet, skipMissingComponents: Incomplete | None = None, reverseFlipped: bool = False, include: set[str] | None = None, decomposeNested: bool = True) -> None: ...
    def addComponent(self, baseGlyphName, transformation, **kwargs) -> None: ...

class DecomposingFilterPen(_DecomposingFilterPenMixin, DecomposingPen, FilterPen):
    """Filter pen that draws components as regular contours."""
class DecomposingFilterPointPen(_DecomposingFilterPenMixin, DecomposingPointPen, FilterPointPen):
    """Filter point pen that draws components as regular contours."""
