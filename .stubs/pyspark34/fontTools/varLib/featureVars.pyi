from .errors import VarLibError as VarLibError, VarLibValidationError as VarLibValidationError
from _typeshed import Incomplete
from fontTools.misc.dictTools import hashdict as hashdict
from fontTools.misc.intTools import bit_count as bit_count
from fontTools.otlLib.builder import buildLookup as buildLookup, buildSingleSubstSubtable as buildSingleSubstSubtable
from fontTools.ttLib import newTable as newTable
from fontTools.ttLib.ttVisitor import TTVisitor as TTVisitor

def addFeatureVariations(font, conditionalSubstitutions, featureTag: str = 'rvrn') -> None:
    '''Add conditional substitutions to a Variable Font.

    The `conditionalSubstitutions` argument is a list of (Region, Substitutions)
    tuples.

    A Region is a list of Boxes. A Box is a dict mapping axisTags to
    (minValue, maxValue) tuples. Irrelevant axes may be omitted and they are
    interpretted as extending to end of axis in each direction.  A Box represents
    an orthogonal \'rectangular\' subset of an N-dimensional design space.
    A Region represents a more complex subset of an N-dimensional design space,
    ie. the union of all the Boxes in the Region.
    For efficiency, Boxes within a Region should ideally not overlap, but
    functionality is not compromised if they do.

    The minimum and maximum values are expressed in normalized coordinates.

    A Substitution is a dict mapping source glyph names to substitute glyph names.

    Example:

    # >>> f = TTFont(srcPath)
    # >>> condSubst = [
    # ...     # A list of (Region, Substitution) tuples.
    # ...     ([{"wdth": (0.5, 1.0)}], {"cent": "cent.rvrn"}),
    # ...     ([{"wght": (0.5, 1.0)}], {"dollar": "dollar.rvrn"}),
    # ... ]
    # >>> addFeatureVariations(f, condSubst)
    # >>> f.save(dstPath)

    The `featureTag` parameter takes either a str or a iterable of str (the single str
    is kept for backwards compatibility), and defines which feature(s) will be
    associated with the feature variations.
    Note, if this is "rvrn", then the substitution lookup will be inserted at the
    beginning of the lookup list so that it is processed before others, otherwise
    for any other feature tags it will be appended last.
    '''
def overlayFeatureVariations(conditionalSubstitutions):
    '''Compute overlaps between all conditional substitutions.

    The `conditionalSubstitutions` argument is a list of (Region, Substitutions)
    tuples.

    A Region is a list of Boxes. A Box is a dict mapping axisTags to
    (minValue, maxValue) tuples. Irrelevant axes may be omitted and they are
    interpretted as extending to end of axis in each direction.  A Box represents
    an orthogonal \'rectangular\' subset of an N-dimensional design space.
    A Region represents a more complex subset of an N-dimensional design space,
    ie. the union of all the Boxes in the Region.
    For efficiency, Boxes within a Region should ideally not overlap, but
    functionality is not compromised if they do.

    The minimum and maximum values are expressed in normalized coordinates.

    A Substitution is a dict mapping source glyph names to substitute glyph names.

    Returns data is in similar but different format.  Overlaps of distinct
    substitution Boxes (*not* Regions) are explicitly listed as distinct rules,
    and rules with the same Box merged.  The more specific rules appear earlier
    in the resulting list.  Moreover, instead of just a dictionary of substitutions,
    a list of dictionaries is returned for substitutions corresponding to each
    unique space, with each dictionary being identical to one of the input
    substitution dictionaries.  These dictionaries are not merged to allow data
    sharing when they are converted into font tables.

    Example::

        >>> condSubst = [
        ...     # A list of (Region, Substitution) tuples.
        ...     ([{"wght": (0.5, 1.0)}], {"dollar": "dollar.rvrn"}),
        ...     ([{"wght": (0.5, 1.0)}], {"dollar": "dollar.rvrn"}),
        ...     ([{"wdth": (0.5, 1.0)}], {"cent": "cent.rvrn"}),
        ...     ([{"wght": (0.5, 1.0), "wdth": (-1, 1.0)}], {"dollar": "dollar.rvrn"}),
        ... ]
        >>> from pprint import pprint
        >>> pprint(overlayFeatureVariations(condSubst))
        [({\'wdth\': (0.5, 1.0), \'wght\': (0.5, 1.0)},
          [{\'dollar\': \'dollar.rvrn\'}, {\'cent\': \'cent.rvrn\'}]),
         ({\'wdth\': (0.5, 1.0)}, [{\'cent\': \'cent.rvrn\'}]),
         ({\'wght\': (0.5, 1.0)}, [{\'dollar\': \'dollar.rvrn\'}])]

    '''
def overlayBox(top, bot):
    """Overlays ``top`` box on top of ``bot`` box.

    Returns two items:

    * Box for intersection of ``top`` and ``bot``, or None if they don't intersect.
    * Box for remainder of ``bot``.  Remainder box might not be exact (since the
      remainder might not be a simple box), but is inclusive of the exact
      remainder.
    """
def cleanupBox(box):
    """Return a sparse copy of `box`, without redundant (default) values.

    >>> cleanupBox({})
    {}
    >>> cleanupBox({'wdth': (0.0, 1.0)})
    {'wdth': (0.0, 1.0)}
    >>> cleanupBox({'wdth': (-1.0, 1.0)})
    {}

    """
def addFeatureVariationsRaw(font, table, conditionalSubstitutions, featureTag: str = 'rvrn') -> None:
    """Low level implementation of addFeatureVariations that directly
    models the possibilities of the FeatureVariations table."""
def buildGSUB():
    """Build a GSUB table from scratch."""
def makeSubstitutionsHashable(conditionalSubstitutions):
    """Turn all the substitution dictionaries in sorted tuples of tuples so
    they are hashable, to detect duplicates so we don't write out redundant
    data."""

class ShifterVisitor(TTVisitor):
    shift: Incomplete
    def __init__(self, shift) -> None: ...

def buildSubstitutionLookups(gsub, allSubstitutions, processLast: bool = False):
    """Build the lookups for the glyph substitutions, return a dict mapping
    the substitution to lookup indices."""
def buildFeatureVariations(featureVariationRecords):
    """Build the FeatureVariations subtable."""
def buildFeatureRecord(featureTag, lookupListIndices):
    """Build a FeatureRecord."""
def buildFeatureVariationRecord(conditionTable, substitutionRecords):
    """Build a FeatureVariationRecord."""
def buildFeatureTableSubstitutionRecord(featureIndex, lookupListIndices):
    """Build a FeatureTableSubstitutionRecord."""
def buildConditionTable(axisIndex, filterRangeMinValue, filterRangeMaxValue):
    """Build a ConditionTable."""
def findFeatureVariationRecord(featureVariations, conditionTable):
    """Find a FeatureVariationRecord that has the same conditionTable."""
def sortFeatureList(table) -> None:
    """Sort the feature list by feature tag, and remap the feature indices
    elsewhere. This is needed after the feature list has been modified.
    """
def remapFeatures(table, featureRemap) -> None:
    """Go through the scripts list, and remap feature indices."""
