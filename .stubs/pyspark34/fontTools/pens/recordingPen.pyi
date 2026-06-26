from _typeshed import Incomplete
from collections.abc import Generator
from fontTools.pens.basePen import AbstractPen, DecomposingPen
from fontTools.pens.pointPen import AbstractPointPen, DecomposingPointPen

__all__ = ['replayRecording', 'RecordingPen', 'DecomposingRecordingPen', 'DecomposingRecordingPointPen', 'RecordingPointPen', 'lerpRecordings']

def replayRecording(recording, pen) -> None:
    """Replay a recording, as produced by RecordingPen or DecomposingRecordingPen,
    to a pen.

    Note that recording does not have to be produced by those pens.
    It can be any iterable of tuples of method name and tuple-of-arguments.
    Likewise, pen can be any objects receiving those method calls.
    """

class RecordingPen(AbstractPen):
    """Pen recording operations that can be accessed or replayed.

    The recording can be accessed as pen.value; or replayed using
    pen.replay(otherPen).

    :Example:

            from fontTools.ttLib import TTFont
            from fontTools.pens.recordingPen import RecordingPen

            glyph_name = 'dollar'
            font_path = 'MyFont.otf'

            font = TTFont(font_path)
            glyphset = font.getGlyphSet()
            glyph = glyphset[glyph_name]

            pen = RecordingPen()
            glyph.draw(pen)
            print(pen.value)
    """
    value: Incomplete
    def __init__(self) -> None: ...
    def moveTo(self, p0) -> None: ...
    def lineTo(self, p1) -> None: ...
    def qCurveTo(self, *points) -> None: ...
    def curveTo(self, *points) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def addComponent(self, glyphName, transformation) -> None: ...
    def addVarComponent(self, glyphName, transformation, location) -> None: ...
    def replay(self, pen) -> None: ...
    draw = replay

class DecomposingRecordingPen(DecomposingPen, RecordingPen):
    '''Same as RecordingPen, except that it doesn\'t keep components
    as references, but draws them decomposed as regular contours.

    The constructor takes a required \'glyphSet\' positional argument,
    a dictionary of glyph objects (i.e. with a \'draw\' method) keyed
    by thir name; other arguments are forwarded to the DecomposingPen\'s
    constructor::

    >>> class SimpleGlyph(object):
    ...     def draw(self, pen):
    ...         pen.moveTo((0, 0))
    ...         pen.curveTo((1, 1), (2, 2), (3, 3))
    ...         pen.closePath()
    >>> class CompositeGlyph(object):
    ...     def draw(self, pen):
    ...         pen.addComponent(\'a\', (1, 0, 0, 1, -1, 1))
    >>> class MissingComponent(object):
    ...     def draw(self, pen):
    ...         pen.addComponent(\'foobar\', (1, 0, 0, 1, 0, 0))
    >>> class FlippedComponent(object):
    ...     def draw(self, pen):
    ...         pen.addComponent(\'a\', (-1, 0, 0, 1, 0, 0))
    >>> glyphSet = {
    ...    \'a\': SimpleGlyph(),
    ...    \'b\': CompositeGlyph(),
    ...    \'c\': MissingComponent(),
    ...    \'d\': FlippedComponent(),
    ... }
    >>> for name, glyph in sorted(glyphSet.items()):
    ...     pen = DecomposingRecordingPen(glyphSet)
    ...     try:
    ...         glyph.draw(pen)
    ...     except pen.MissingComponentError:
    ...         pass
    ...     print("{}: {}".format(name, pen.value))
    a: [(\'moveTo\', ((0, 0),)), (\'curveTo\', ((1, 1), (2, 2), (3, 3))), (\'closePath\', ())]
    b: [(\'moveTo\', ((-1, 1),)), (\'curveTo\', ((0, 2), (1, 3), (2, 4))), (\'closePath\', ())]
    c: []
    d: [(\'moveTo\', ((0, 0),)), (\'curveTo\', ((-1, 1), (-2, 2), (-3, 3))), (\'closePath\', ())]
    >>> for name, glyph in sorted(glyphSet.items()):
    ...     pen = DecomposingRecordingPen(
    ...         glyphSet, skipMissingComponents=True, reverseFlipped=True,
    ...     )
    ...     glyph.draw(pen)
    ...     print("{}: {}".format(name, pen.value))
    a: [(\'moveTo\', ((0, 0),)), (\'curveTo\', ((1, 1), (2, 2), (3, 3))), (\'closePath\', ())]
    b: [(\'moveTo\', ((-1, 1),)), (\'curveTo\', ((0, 2), (1, 3), (2, 4))), (\'closePath\', ())]
    c: []
    d: [(\'moveTo\', ((0, 0),)), (\'lineTo\', ((-3, 3),)), (\'curveTo\', ((-2, 2), (-1, 1), (0, 0))), (\'closePath\', ())]
    '''
    skipMissingComponents: bool

class RecordingPointPen(AbstractPointPen):
    """PointPen recording operations that can be accessed or replayed.

    The recording can be accessed as pen.value; or replayed using
    pointPen.replay(otherPointPen).

    :Example:

            from defcon import Font
            from fontTools.pens.recordingPen import RecordingPointPen

            glyph_name = 'a'
            font_path = 'MyFont.ufo'

            font = Font(font_path)
            glyph = font[glyph_name]

            pen = RecordingPointPen()
            glyph.drawPoints(pen)
            print(pen.value)

            new_glyph = font.newGlyph('b')
            pen.replay(new_glyph.getPointPen())
    """
    value: Incomplete
    def __init__(self) -> None: ...
    def beginPath(self, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def endPath(self) -> None: ...
    def addPoint(self, pt, segmentType: Incomplete | None = None, smooth: bool = False, name: Incomplete | None = None, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def addComponent(self, baseGlyphName, transformation, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def addVarComponent(self, baseGlyphName, transformation, location, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def replay(self, pointPen) -> None: ...
    drawPoints = replay

class DecomposingRecordingPointPen(DecomposingPointPen, RecordingPointPen):
    '''Same as RecordingPointPen, except that it doesn\'t keep components
    as references, but draws them decomposed as regular contours.

    The constructor takes a required \'glyphSet\' positional argument,
    a dictionary of pointPen-drawable glyph objects (i.e. with a \'drawPoints\' method)
    keyed by thir name; other arguments are forwarded to the DecomposingPointPen\'s
    constructor::

    >>> from pprint import pprint
    >>> class SimpleGlyph(object):
    ...     def drawPoints(self, pen):
    ...         pen.beginPath()
    ...         pen.addPoint((0, 0), "line")
    ...         pen.addPoint((1, 1))
    ...         pen.addPoint((2, 2))
    ...         pen.addPoint((3, 3), "curve")
    ...         pen.endPath()
    >>> class CompositeGlyph(object):
    ...     def drawPoints(self, pen):
    ...         pen.addComponent(\'a\', (1, 0, 0, 1, -1, 1))
    >>> class MissingComponent(object):
    ...     def drawPoints(self, pen):
    ...         pen.addComponent(\'foobar\', (1, 0, 0, 1, 0, 0))
    >>> class FlippedComponent(object):
    ...     def drawPoints(self, pen):
    ...         pen.addComponent(\'a\', (-1, 0, 0, 1, 0, 0))
    >>> glyphSet = {
    ...    \'a\': SimpleGlyph(),
    ...    \'b\': CompositeGlyph(),
    ...    \'c\': MissingComponent(),
    ...    \'d\': FlippedComponent(),
    ... }
    >>> for name, glyph in sorted(glyphSet.items()):
    ...     pen = DecomposingRecordingPointPen(glyphSet)
    ...     try:
    ...         glyph.drawPoints(pen)
    ...     except pen.MissingComponentError:
    ...         pass
    ...     pprint({name: pen.value})
    {\'a\': [(\'beginPath\', (), {}),
           (\'addPoint\', ((0, 0), \'line\', False, None), {}),
           (\'addPoint\', ((1, 1), None, False, None), {}),
           (\'addPoint\', ((2, 2), None, False, None), {}),
           (\'addPoint\', ((3, 3), \'curve\', False, None), {}),
           (\'endPath\', (), {})]}
    {\'b\': [(\'beginPath\', (), {}),
           (\'addPoint\', ((-1, 1), \'line\', False, None), {}),
           (\'addPoint\', ((0, 2), None, False, None), {}),
           (\'addPoint\', ((1, 3), None, False, None), {}),
           (\'addPoint\', ((2, 4), \'curve\', False, None), {}),
           (\'endPath\', (), {})]}
    {\'c\': []}
    {\'d\': [(\'beginPath\', (), {}),
           (\'addPoint\', ((0, 0), \'line\', False, None), {}),
           (\'addPoint\', ((-1, 1), None, False, None), {}),
           (\'addPoint\', ((-2, 2), None, False, None), {}),
           (\'addPoint\', ((-3, 3), \'curve\', False, None), {}),
           (\'endPath\', (), {})]}
    >>> for name, glyph in sorted(glyphSet.items()):
    ...     pen = DecomposingRecordingPointPen(
    ...         glyphSet, skipMissingComponents=True, reverseFlipped=True,
    ...     )
    ...     glyph.drawPoints(pen)
    ...     pprint({name: pen.value})
    {\'a\': [(\'beginPath\', (), {}),
           (\'addPoint\', ((0, 0), \'line\', False, None), {}),
           (\'addPoint\', ((1, 1), None, False, None), {}),
           (\'addPoint\', ((2, 2), None, False, None), {}),
           (\'addPoint\', ((3, 3), \'curve\', False, None), {}),
           (\'endPath\', (), {})]}
    {\'b\': [(\'beginPath\', (), {}),
           (\'addPoint\', ((-1, 1), \'line\', False, None), {}),
           (\'addPoint\', ((0, 2), None, False, None), {}),
           (\'addPoint\', ((1, 3), None, False, None), {}),
           (\'addPoint\', ((2, 4), \'curve\', False, None), {}),
           (\'endPath\', (), {})]}
    {\'c\': []}
    {\'d\': [(\'beginPath\', (), {}),
           (\'addPoint\', ((0, 0), \'curve\', False, None), {}),
           (\'addPoint\', ((-3, 3), \'line\', False, None), {}),
           (\'addPoint\', ((-2, 2), None, False, None), {}),
           (\'addPoint\', ((-1, 1), None, False, None), {}),
           (\'endPath\', (), {})]}
    '''
    skipMissingComponents: bool

def lerpRecordings(recording1, recording2, factor: float = 0.5) -> Generator[Incomplete, None, None]:
    """Linearly interpolate between two recordings. The recordings
    must be decomposed, i.e. they must not contain any components.

    Factor is typically between 0 and 1. 0 means the first recording,
    1 means the second recording, and 0.5 means the average of the
    two recordings. Other values are possible, and can be useful to
    extrapolate. Defaults to 0.5.

    Returns a generator with the new recording.
    """
