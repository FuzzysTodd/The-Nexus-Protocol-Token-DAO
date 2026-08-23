from .interpolatableHelpers import *
from .interpolatableTestContourOrder import test_contour_order as test_contour_order
from .interpolatableTestStartingPoint import test_starting_point as test_starting_point
from _typeshed import Incomplete
from collections.abc import Generator
from fontTools.misc.fixedTools import floatToFixedToStr as floatToFixedToStr
from fontTools.misc.transform import Transform as Transform
from fontTools.pens.momentsPen import OpenContourError as OpenContourError
from fontTools.pens.recordingPen import DecomposingRecordingPen as DecomposingRecordingPen, RecordingPen as RecordingPen, lerpRecordings as lerpRecordings
from fontTools.pens.statisticsPen import StatisticsControlPen as StatisticsControlPen, StatisticsPen as StatisticsPen
from fontTools.pens.transformPen import TransformPen as TransformPen
from fontTools.varLib.models import normalizeLocation as normalizeLocation, piecewiseLinearMap as piecewiseLinearMap
from math import atan2 as atan2, pi as pi

log: Incomplete
DEFAULT_TOLERANCE: float
DEFAULT_KINKINESS: float
DEFAULT_KINKINESS_LENGTH: float
DEFAULT_UPEM: int

class Glyph:
    ITEMS: Incomplete
    name: Incomplete
    def __init__(self, glyphname, glyphset) -> None: ...
    def draw(self, pen, countor_idx: Incomplete | None = None) -> None: ...

def test_gen(glyphsets, glyphs: Incomplete | None = None, names: Incomplete | None = None, ignore_missing: bool = False, *, locations: Incomplete | None = None, tolerance=..., kinkiness=..., upem=..., show_all: bool = False) -> Generator[Incomplete, None, Incomplete]: ...
def test(*args, **kwargs): ...
def recursivelyAddGlyph(glyphname, glyphset, ttGlyphSet, glyf) -> None: ...
def ensure_parent_dir(path): ...
def main(args: Incomplete | None = None):
    """Test for interpolatability issues between fonts"""
