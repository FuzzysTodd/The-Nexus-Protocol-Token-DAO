import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Generator, Mapping
from fontTools.misc.fixedTools import otRound as otRound
from fontTools.misc.loggingTools import deprecateFunction as deprecateFunction
from fontTools.misc.transform import DecomposedTransform as DecomposedTransform, Transform as Transform
from fontTools.misc.vector import Vector as Vector
from fontTools.pens.recordingPen import DecomposingRecordingPen as DecomposingRecordingPen, lerpRecordings as lerpRecordings, replayRecording as replayRecording
from fontTools.pens.transformPen import TransformPen as TransformPen, TransformPointPen as TransformPointPen
from types import SimpleNamespace as SimpleNamespace

class _TTGlyphSet(Mapping, metaclass=abc.ABCMeta):
    """Generic dict-like GlyphSet class that pulls metrics from hmtx and
    glyph shape from TrueType or CFF.
    """
    recalcBounds: Incomplete
    font: Incomplete
    defaultLocationNormalized: Incomplete
    location: Incomplete
    rawLocation: Incomplete
    originalLocation: Incomplete
    depth: int
    locationStack: Incomplete
    rawLocationStack: Incomplete
    glyphsMapping: Incomplete
    hMetrics: Incomplete
    vMetrics: Incomplete
    hvarTable: Incomplete
    hvarInstancer: Incomplete
    def __init__(self, font, location, glyphsMapping, *, recalcBounds: bool = True) -> None: ...
    def pushLocation(self, location, reset: bool): ...
    def pushDepth(self) -> Generator[Incomplete, None, None]: ...
    def __contains__(self, glyphName) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def has_key(self, glyphName): ...

class _TTGlyphSetGlyf(_TTGlyphSet):
    glyfTable: Incomplete
    gvarTable: Incomplete
    def __init__(self, font, location, recalcBounds: bool = True) -> None: ...
    def __getitem__(self, glyphName): ...

class _TTGlyphSetGlyf(_TTGlyphSet):
    glyfTable: Incomplete
    gvarTable: Incomplete
    def __init__(self, font, location, recalcBounds: bool = True) -> None: ...
    def __getitem__(self, glyphName): ...

class _TTGlyphSetCFF(_TTGlyphSet):
    charStrings: Incomplete
    blender: Incomplete
    def __init__(self, font, location) -> None: ...
    def __getitem__(self, glyphName): ...

class _TTGlyphSetVARC(_TTGlyphSet):
    glyphSet: Incomplete
    varcTable: Incomplete
    def __init__(self, font, location, glyphSet) -> None: ...
    def __getitem__(self, glyphName): ...

class _TTGlyph(ABC, metaclass=abc.ABCMeta):
    """Glyph object that supports the Pen protocol, meaning that it has
    .draw() and .drawPoints() methods that take a pen object as their only
    argument. Additionally there are 'width' and 'lsb' attributes, read from
    the 'hmtx' table.

    If the font contains a 'vmtx' table, there will also be 'height' and 'tsb'
    attributes.
    """
    glyphSet: Incomplete
    name: Incomplete
    recalcBounds: Incomplete
    def __init__(self, glyphSet, glyphName, *, recalcBounds: bool = True) -> None: ...
    @abstractmethod
    def draw(self, pen):
        """Draw the glyph onto ``pen``. See fontTools.pens.basePen for details
        how that works.
        """
    def drawPoints(self, pen) -> None:
        """Draw the glyph onto ``pen``. See fontTools.pens.pointPen for details
        how that works.
        """

class _TTGlyphGlyf(_TTGlyph):
    def draw(self, pen) -> None:
        """Draw the glyph onto ``pen``. See fontTools.pens.basePen for details
        how that works.
        """
    def drawPoints(self, pen) -> None:
        """Draw the glyph onto ``pen``. See fontTools.pens.pointPen for details
        how that works.
        """

class _TTGlyphCFF(_TTGlyph):
    def draw(self, pen) -> None:
        """Draw the glyph onto ``pen``. See fontTools.pens.basePen for details
        how that works.
        """

class _TTGlyphVARC(_TTGlyph):
    def draw(self, pen) -> None: ...
    def drawPoints(self, pen) -> None: ...

class LerpGlyphSet(Mapping):
    """A glyphset that interpolates between two other glyphsets.

    Factor is typically between 0 and 1. 0 means the first glyphset,
    1 means the second glyphset, and 0.5 means the average of the
    two glyphsets. Other values are possible, and can be useful to
    extrapolate. Defaults to 0.5.
    """
    glyphset1: Incomplete
    glyphset2: Incomplete
    factor: Incomplete
    def __init__(self, glyphset1, glyphset2, factor: float = 0.5) -> None: ...
    def __getitem__(self, glyphname): ...
    def __contains__(self, glyphname) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class LerpGlyph:
    glyphset: Incomplete
    glyphname: Incomplete
    def __init__(self, glyphname, glyphset) -> None: ...
    def draw(self, pen) -> None: ...
