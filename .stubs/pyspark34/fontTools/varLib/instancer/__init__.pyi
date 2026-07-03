import dataclasses
from .featureVars import instantiateFeatureVariations as instantiateFeatureVariations
from _typeshed import Incomplete
from collections.abc import Generator
from enum import IntEnum
from fontTools import subset as subset, varLib as varLib
from fontTools.cffLib import privateDictOperators2 as privateDictOperators2
from fontTools.cffLib.specializer import commandsToProgram as commandsToProgram, generalizeCommands as generalizeCommands, programToCommands as programToCommands, specializeCommands as specializeCommands
from fontTools.misc.cliTools import makeOutputFileName as makeOutputFileName
from fontTools.misc.fixedTools import floatToFixedToFloat as floatToFixedToFloat, otRound as otRound, strToFixedToFloat as strToFixedToFloat
from fontTools.ttLib import TTFont as TTFont, newTable as newTable
from fontTools.ttLib.tables.TupleVariation import TupleVariation as TupleVariation
from fontTools.ttLib.tables.otTables import VarComponentFlags as VarComponentFlags
from fontTools.varLib import builder as builder
from fontTools.varLib.instancer import names as names, solver as solver
from fontTools.varLib.merger import MutatorMerger as MutatorMerger
from fontTools.varLib.models import normalizeValue as normalizeValue, piecewiseLinearMap as piecewiseLinearMap
from fontTools.varLib.mvar import MVAR_ENTRIES as MVAR_ENTRIES
from typing import Dict, Iterable, Mapping, Sequence, Tuple

log: Incomplete

def AxisRange(minimum, maximum): ...
def NormalizedAxisRange(minimum, maximum): ...

@dataclasses.dataclass(frozen=True, order=True, repr=False)
class AxisTriple(Sequence):
    """A triple of (min, default, max) axis values.

    Any of the values can be None, in which case the limitRangeAndPopulateDefaults()
    method can be used to fill in the missing values based on the fvar axis values.
    """
    minimum: float | None
    default: float | None
    maximum: float | None
    def __post_init__(self) -> None: ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...
    @classmethod
    def expand(cls, v: AxisTriple | float | Tuple[float, float] | Tuple[float, float, float]) -> AxisTriple:
        """Convert a single value or a tuple into an AxisTriple.

        If the input is a single value, it is interpreted as a pin at that value.
        If the input is a tuple, it is interpreted as (min, max) or (min, default, max).
        """
    def limitRangeAndPopulateDefaults(self, fvarTriple) -> AxisTriple:
        """Return a new AxisTriple with the default value filled in.

        Set default to fvar axis default if the latter is within the min/max range,
        otherwise set default to the min or max value, whichever is closer to the
        fvar axis default.
        If the default value is already set, return self.
        """
    def __init__(self, minimum, default, maximum) -> None: ...

@dataclasses.dataclass(frozen=True, order=True, repr=False)
class NormalizedAxisTriple(AxisTriple):
    """A triple of (min, default, max) normalized axis values."""
    minimum: float
    default: float
    maximum: float
    def __post_init__(self) -> None: ...
    def __init__(self, minimum, default, maximum) -> None: ...

@dataclasses.dataclass(frozen=True, order=True, repr=False)
class NormalizedAxisTripleAndDistances(AxisTriple):
    """A triple of (min, default, max) normalized axis values,
    with distances between min and default, and default and max,
    in the *pre-normalized* space."""
    minimum: float
    default: float
    maximum: float
    distanceNegative: float | None = ...
    distancePositive: float | None = ...
    def __post_init__(self) -> None: ...
    def reverse_negate(self): ...
    def renormalizeValue(self, v, extrapolate: bool = True):
        """Renormalizes a normalized value v to the range of this axis,
        considering the pre-normalized distances as well as the new
        axis limits."""
    def __init__(self, minimum, default, maximum, distanceNegative, distancePositive) -> None: ...

class _BaseAxisLimits(Mapping[str, AxisTriple]):
    def __getitem__(self, key: str) -> AxisTriple: ...
    def __iter__(self) -> Iterable[str]: ...
    def __len__(self) -> int: ...
    def defaultLocation(self) -> Dict[str, float]:
        """Return a dict of default axis values."""
    def pinnedLocation(self) -> Dict[str, float]:
        """Return a location dict with only the pinned axes."""

class AxisLimits(_BaseAxisLimits):
    """Maps axis tags (str) to AxisTriple values."""
    def __init__(self, *args, **kwargs) -> None: ...
    def limitAxesAndPopulateDefaults(self, varfont) -> AxisLimits:
        """Return a new AxisLimits with defaults filled in from fvar table.

        If all axis limits already have defaults, return self.
        """
    def normalize(self, varfont, usingAvar: bool = True) -> NormalizedAxisLimits:
        """Return a new NormalizedAxisLimits with normalized -1..0..+1 values.

        If usingAvar is True, the avar table is used to warp the default normalization.
        """

class NormalizedAxisLimits(_BaseAxisLimits):
    """Maps axis tags (str) to NormalizedAxisTriple values."""
    def __init__(self, *args, **kwargs) -> None: ...

class OverlapMode(IntEnum):
    KEEP_AND_DONT_SET_FLAGS: int
    KEEP_AND_SET_FLAGS: int
    REMOVE: int
    REMOVE_AND_IGNORE_ERRORS: int

def instantiateVARC(varfont, axisLimits) -> None: ...
def instantiateTupleVariationStore(variations, axisLimits, origCoords: Incomplete | None = None, endPts: Incomplete | None = None):
    """Instantiate TupleVariation list at the given location, or limit axes' min/max.

    The 'variations' list of TupleVariation objects is modified in-place.
    The 'axisLimits' (dict) maps axis tags (str) to NormalizedAxisTriple namedtuples
    specifying (minimum, default, maximum) in the -1,0,+1 normalized space. Pinned axes
    have minimum == default == maximum.

    A 'full' instance (i.e. static font) is produced when all the axes are pinned to
    single coordinates; a 'partial' instance (i.e. a less variable font) is produced
    when some of the axes are omitted, or restricted with a new range.

    Tuples that do not participate are kept as they are. Those that have 0 influence
    at the given location are removed from the variation store.
    Those that are fully instantiated (i.e. all their axes are being pinned) are also
    removed from the variation store, their scaled deltas accummulated and returned, so
    that they can be added by the caller to the default instance's coordinates.
    Tuples that are only partially instantiated (i.e. not all the axes that they
    participate in are being pinned) are kept in the store, and their deltas multiplied
    by the scalar support of the axes to be pinned at the desired location.

    Args:
        variations: List[TupleVariation] from either 'gvar' or 'cvar'.
        axisLimits: NormalizedAxisLimits: map from axis tags to (min, default, max)
            normalized coordinates for the full or partial instance.
        origCoords: GlyphCoordinates: default instance's coordinates for computing 'gvar'
            inferred points (cf. table__g_l_y_f._getCoordinatesAndControls).
        endPts: List[int]: indices of contour end points, for inferring 'gvar' deltas.

    Returns:
        List[float]: the overall delta adjustment after applicable deltas were summed.
    """
def changeTupleVariationsAxisLimits(variations, axisLimits): ...
def changeTupleVariationAxisLimit(var, axisTag, axisLimit): ...
def instantiateCFF2(varfont, axisLimits, *, round=..., specialize: bool = True, generalize: bool = False, downgrade: bool = False): ...
def instantiateGvarGlyph(varfont, glyphname, axisLimits, optimize: bool = True) -> None:
    """Remove?
    https://github.com/fonttools/fonttools/pull/2266"""
def instantiateGvar(varfont, axisLimits, optimize: bool = True): ...
def setCvarDeltas(cvt, deltas) -> None: ...
def instantiateCvar(varfont, axisLimits) -> None: ...
def setMvarDeltas(varfont, deltas) -> None: ...
def verticalMetricsKeptInSync(varfont) -> Generator[Incomplete, None, None]:
    """Ensure hhea vertical metrics stay in sync with OS/2 ones after instancing.

    When applying MVAR deltas to the OS/2 table, if the ascender, descender and
    line gap change but they were the same as the respective hhea metrics in the
    original font, this context manager ensures that hhea metrcs also get updated
    accordingly.
    The MVAR spec only has tags for the OS/2 metrics, but it is common in fonts
    to have the hhea metrics be equal to those for compat reasons.

    https://learn.microsoft.com/en-us/typography/opentype/spec/mvar
    https://googlefonts.github.io/gf-guide/metrics.html#7-hhea-and-typo-metrics-should-be-equal
    https://github.com/fonttools/fonttools/issues/3297
    """
def instantiateMVAR(varfont, axisLimits) -> None: ...
def instantiateHVAR(varfont, axisLimits): ...
def instantiateVVAR(varfont, axisLimits): ...

class _TupleVarStoreAdapter:
    regions: Incomplete
    axisOrder: Incomplete
    tupleVarData: Incomplete
    itemCounts: Incomplete
    def __init__(self, regions, axisOrder, tupleVarData, itemCounts) -> None: ...
    @classmethod
    def fromItemVarStore(cls, itemVarStore, fvarAxes): ...
    def rebuildRegions(self) -> None: ...
    def instantiate(self, axisLimits): ...
    def asItemVarStore(self): ...

def instantiateItemVariationStore(itemVarStore, fvarAxes, axisLimits):
    """Compute deltas at partial location, and update varStore in-place.

    Remove regions in which all axes were instanced, or fall outside the new axis
    limits. Scale the deltas of the remaining regions where only some of the axes
    were instanced.

    The number of VarData subtables, and the number of items within each, are
    not modified, in order to keep the existing VariationIndex valid.
    One may call VarStore.optimize() method after this to further optimize those.

    Args:
        varStore: An otTables.VarStore object (Item Variation Store)
        fvarAxes: list of fvar's Axis objects
        axisLimits: NormalizedAxisLimits: mapping axis tags to normalized
            min/default/max axis coordinates. May not specify coordinates/ranges for
            all the fvar axes.

    Returns:
        defaultDeltas: to be added to the default instance, of type dict of floats
            keyed by VariationIndex compound values: i.e. (outer << 16) + inner.
    """
def instantiateOTL(varfont, axisLimits) -> None: ...
def instantiateAvar(varfont, axisLimits) -> None: ...
def isInstanceWithinAxisRanges(location, axisRanges): ...
def instantiateFvar(varfont, axisLimits) -> None: ...
def instantiateSTAT(varfont, axisLimits) -> None: ...
def axisValuesFromAxisLimits(stat, axisLimits): ...
def setMacOverlapFlags(glyfTable) -> None: ...
def normalize(value, triple, avarMapping): ...
def sanityCheckVariableTables(varfont) -> None: ...
def instantiateVariableFont(varfont, axisLimits, inplace: bool = False, optimize: bool = True, overlap=..., updateFontNames: bool = False, *, downgradeCFF2: bool = False):
    """Instantiate variable font, either fully or partially.

    Depending on whether the `axisLimits` dictionary references all or some of the
    input varfont's axes, the output font will either be a full instance (static
    font) or a variable font with possibly less variation data.

    Args:
        varfont: a TTFont instance, which must contain at least an 'fvar' table.
        axisLimits: a dict keyed by axis tags (str) containing the coordinates (float)
            along one or more axes where the desired instance will be located.
            If the value is `None`, the default coordinate as per 'fvar' table for
            that axis is used.
            The limit values can also be (min, max) tuples for restricting an
            axis's variation range. The default axis value must be included in
            the new range.
        inplace (bool): whether to modify input TTFont object in-place instead of
            returning a distinct object.
        optimize (bool): if False, do not perform IUP-delta optimization on the
            remaining 'gvar' table's deltas. Possibly faster, and might work around
            rendering issues in some buggy environments, at the cost of a slightly
            larger file size.
        overlap (OverlapMode): variable fonts usually contain overlapping contours, and
            some font rendering engines on Apple platforms require that the
            `OVERLAP_SIMPLE` and `OVERLAP_COMPOUND` flags in the 'glyf' table be set to
            force rendering using a non-zero fill rule. Thus we always set these flags
            on all glyphs to maximise cross-compatibility of the generated instance.
            You can disable this by passing OverlapMode.KEEP_AND_DONT_SET_FLAGS.
            If you want to remove the overlaps altogether and merge overlapping
            contours and components, you can pass OverlapMode.REMOVE (or
            REMOVE_AND_IGNORE_ERRORS to not hard-fail on tricky glyphs). Note that this
            requires the skia-pathops package (available to pip install).
            The overlap parameter only has effect when generating full static instances.
        updateFontNames (bool): if True, update the instantiated font's name table using
            the Axis Value Tables from the STAT table. The name table and the style bits
            in the head and OS/2 table will be updated so they conform to the R/I/B/BI
            model. If the STAT table is missing or an Axis Value table is missing for
            a given axis coordinate, a ValueError will be raised.
        downgradeCFF2 (bool): if True, downgrade the CFF2 table to CFF table when possible
            ie. full instancing of all axes. This is useful for compatibility with older
            software that does not support CFF2. Defaults to False. Note that this
            operation also removes overlaps within glyph shapes, as CFF does not support
            overlaps but CFF2 does.
    """
def setRibbiBits(font) -> None:
    """Set the `head.macStyle` and `OS/2.fsSelection` style bits
    appropriately."""
def parseLimits(limits: Iterable[str]) -> Dict[str, AxisTriple | None]: ...
def parseArgs(args):
    '''Parse argv.

    Returns:
        3-tuple (infile, axisLimits, options)
        axisLimits is either a Dict[str, Optional[float]], for pinning variation axes
        to specific coordinates along those axes (with `None` as a placeholder for an
        axis\' default value); or a Dict[str, Tuple(float, float)], meaning limit this
        axis to min/max range.
        Axes locations are in user-space coordinates, as defined in the "fvar" table.
    '''
def main(args: Incomplete | None = None) -> None:
    """Partially instantiate a variable font"""
