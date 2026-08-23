from _typeshed import Incomplete
from fontTools.misc.fixedTools import otRound as otRound
from fontTools.misc.textTools import safeEval as safeEval

EMBEDDED_PEAK_TUPLE: int
INTERMEDIATE_REGION: int
PRIVATE_POINT_NUMBERS: int
DELTAS_ARE_ZERO: int
DELTAS_ARE_WORDS: int
DELTAS_ARE_LONGS: int
DELTAS_SIZE_MASK: int
DELTA_RUN_COUNT_MASK: int
POINTS_ARE_WORDS: int
POINT_RUN_COUNT_MASK: int
TUPLES_SHARE_POINT_NUMBERS: int
TUPLE_COUNT_MASK: int
TUPLE_INDEX_MASK: int
log: Incomplete

class TupleVariation:
    axes: Incomplete
    coordinates: Incomplete
    def __init__(self, axes, coordinates) -> None: ...
    def __eq__(self, other): ...
    def getUsedPoints(self): ...
    def hasImpact(self):
        """Returns True if this TupleVariation has any visible impact.

        If the result is False, the TupleVariation can be omitted from the font
        without making any visible difference.
        """
    def toXML(self, writer, axisTags) -> None: ...
    def fromXML(self, name, attrs, _content) -> None: ...
    def compile(self, axisTags, sharedCoordIndices={}, pointData: Incomplete | None = None): ...
    def compileCoord(self, axisTags): ...
    def compileIntermediateCoord(self, axisTags): ...
    @staticmethod
    def decompileCoord_(axisTags, data, offset): ...
    @staticmethod
    def compilePoints(points): ...
    @staticmethod
    def decompilePoints_(numPoints, data, offset, tableTag):
        """(numPoints, data, offset, tableTag) --> ([point1, point2, ...], newOffset)"""
    def compileDeltas(self): ...
    @staticmethod
    def compileDeltaValues_(deltas, bytearr: Incomplete | None = None):
        """[value1, value2, value3, ...] --> bytearray

        Emits a sequence of runs. Each run starts with a
        byte-sized header whose 6 least significant bits
        (header & 0x3F) indicate how many values are encoded
        in this run. The stored length is the actual length
        minus one; run lengths are thus in the range [1..64].
        If the header byte has its most significant bit (0x80)
        set, all values in this run are zero, and no data
        follows. Otherwise, the header byte is followed by
        ((header & 0x3F) + 1) signed values.  If (header &
        0x40) is clear, the delta values are stored as signed
        bytes; if (header & 0x40) is set, the delta values are
        signed 16-bit integers.
        """
    @staticmethod
    def encodeDeltaRunAsZeroes_(deltas, offset, bytearr): ...
    @staticmethod
    def encodeDeltaRunAsBytes_(deltas, offset, bytearr): ...
    @staticmethod
    def encodeDeltaRunAsWords_(deltas, offset, bytearr): ...
    @staticmethod
    def encodeDeltaRunAsLongs_(deltas, offset, bytearr): ...
    @staticmethod
    def decompileDeltas_(numDeltas, data, offset: int = 0):
        """(numDeltas, data, offset) --> ([delta, delta, ...], newOffset)"""
    @staticmethod
    def getTupleSize_(flags, axisCount): ...
    def getCoordWidth(self):
        """Return 2 if coordinates are (x, y) as in gvar, 1 if single values
        as in cvar, or 0 if empty.
        """
    def scaleDeltas(self, scalar) -> None: ...
    def roundDeltas(self) -> None: ...
    def calcInferredDeltas(self, origCoords, endPts) -> None: ...
    def optimize(self, origCoords, endPts, tolerance: float = 0.5, isComposite: bool = False) -> None: ...
    def __imul__(self, scalar): ...
    def __iadd__(self, other): ...

def decompileSharedTuples(axisTags, sharedTupleCount, data, offset): ...
def compileSharedTuples(axisTags, variations, MAX_NUM_SHARED_COORDS=...): ...
def compileTupleVariationStore(variations, pointCount, axisTags, sharedTupleIndices, useSharedPoints: bool = True): ...
def decompileTupleVariationStore(tableTag, axisTags, tupleVariationCount, pointCount, sharedTuples, data, pos, dataPos): ...
def decompileTupleVariation_(pointCount, sharedTuples, sharedPoints, tableTag, axisTags, data, tupleData): ...
def inferRegion_(peak):
    """Infer start and end for a (non-intermediate) region

    This helper function computes the applicability region for
    variation tuples whose INTERMEDIATE_REGION flag is not set in the
    TupleVariationHeader structure.  Variation tuples apply only to
    certain regions of the variation space; outside that region, the
    tuple has no effect.  To make the binary encoding more compact,
    TupleVariationHeaders can omit the intermediateStartTuple and
    intermediateEndTuple fields.
    """
