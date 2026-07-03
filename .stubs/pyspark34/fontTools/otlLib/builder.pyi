from _typeshed import Incomplete
from fontTools import ttLib as ttLib
from fontTools.feaLib.ast import STATNameStatement as STATNameStatement
from fontTools.misc.fixedTools import fixedToFloat as fixedToFloat
from fontTools.misc.roundTools import otRound as otRound
from fontTools.otlLib.error import OpenTypeLibError as OpenTypeLibError
from fontTools.otlLib.optimize.gpos import compact_lookup as compact_lookup
from fontTools.ttLib.tables import otBase as otBase
from fontTools.ttLib.tables.otBase import CountReference as CountReference, OTLOffsetOverflowError as OTLOffsetOverflowError, OTTableWriter as OTTableWriter, ValueRecord as ValueRecord, valueRecordFormatDict as valueRecordFormatDict
from typing import NamedTuple

log: Incomplete

def buildCoverage(glyphs, glyphMap):
    '''Builds a coverage table.

    Coverage tables (as defined in the `OpenType spec <https://docs.microsoft.com/en-gb/typography/opentype/spec/chapter2#coverage-table>`__)
    are used in all OpenType Layout lookups apart from the Extension type, and
    define the glyphs involved in a layout subtable. This allows shaping engines
    to compare the glyph stream with the coverage table and quickly determine
    whether a subtable should be involved in a shaping operation.

    This function takes a list of glyphs and a glyphname-to-ID map, and
    returns a ``Coverage`` object representing the coverage table.

    Example::

        glyphMap = font.getReverseGlyphMap()
        glyphs = [ "A", "B", "C" ]
        coverage = buildCoverage(glyphs, glyphMap)

    Args:
        glyphs: a sequence of glyph names.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        An ``otTables.Coverage`` object or ``None`` if there are no glyphs
        supplied.
    '''

LOOKUP_FLAG_RIGHT_TO_LEFT: int
LOOKUP_FLAG_IGNORE_BASE_GLYPHS: int
LOOKUP_FLAG_IGNORE_LIGATURES: int
LOOKUP_FLAG_IGNORE_MARKS: int
LOOKUP_FLAG_USE_MARK_FILTERING_SET: int

def buildLookup(subtables, flags: int = 0, markFilterSet: Incomplete | None = None):
    """Turns a collection of rules into a lookup.

    A Lookup (as defined in the `OpenType Spec <https://docs.microsoft.com/en-gb/typography/opentype/spec/chapter2#lookupTbl>`__)
    wraps the individual rules in a layout operation (substitution or
    positioning) in a data structure expressing their overall lookup type -
    for example, single substitution, mark-to-base attachment, and so on -
    as well as the lookup flags and any mark filtering sets. You may import
    the following constants to express lookup flags:

    - ``LOOKUP_FLAG_RIGHT_TO_LEFT``
    - ``LOOKUP_FLAG_IGNORE_BASE_GLYPHS``
    - ``LOOKUP_FLAG_IGNORE_LIGATURES``
    - ``LOOKUP_FLAG_IGNORE_MARKS``
    - ``LOOKUP_FLAG_USE_MARK_FILTERING_SET``

    Args:
        subtables: A list of layout subtable objects (e.g.
            ``MultipleSubst``, ``PairPos``, etc.) or ``None``.
        flags (int): This lookup's flags.
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup's
            flags.

    Returns:
        An ``otTables.Lookup`` object or ``None`` if there are no subtables
        supplied.
    """

class LookupBuilder:
    SUBTABLE_BREAK_: str
    font: Incomplete
    glyphMap: Incomplete
    location: Incomplete
    lookupflag: int
    markFilterSet: Incomplete
    lookup_index: Incomplete
    def __init__(self, font, location, table, lookup_type) -> None: ...
    def equals(self, other): ...
    def inferGlyphClasses(self):
        '''Infers glyph glasses for the GDEF table, such as {"cedilla":3}.'''
    def getAlternateGlyphs(self):
        """Helper for building 'aalt' features."""
    def buildLookup_(self, subtables): ...
    def buildMarkClasses_(self, marks):
        '''{"cedilla": ("BOTTOM", ast.Anchor), ...} --> {"BOTTOM":0, "TOP":1}

        Helper for MarkBasePostBuilder, MarkLigPosBuilder, and
        MarkMarkPosBuilder. Seems to return the same numeric IDs
        for mark classes as the AFDKO makeotf tool.
        '''
    def setBacktrackCoverage_(self, prefix, subtable) -> None: ...
    def setLookAheadCoverage_(self, suffix, subtable) -> None: ...
    def setInputCoverage_(self, glyphs, subtable) -> None: ...
    def setCoverage_(self, glyphs, subtable) -> None: ...
    def build_subst_subtables(self, mapping, klass): ...
    def add_subtable_break(self, location) -> None:
        """Add an explicit subtable break.

        Args:
            location: A string or tuple representing the location in the
                original source which produced this break, or ``None`` if
                no location is provided.
        """

class AlternateSubstBuilder(LookupBuilder):
    '''Builds an Alternate Substitution (GSUB3) lookup.

    Users are expected to manually add alternate glyph substitutions to
    the ``alternates`` attribute after the object has been initialized,
    e.g.::

        builder.alternates["A"] = ["A.alt1", "A.alt2"]

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        alternates: An ordered dictionary of alternates, mapping glyph names
            to a list of names of alternates.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    alternates: Incomplete
    def __init__(self, font, location) -> None: ...
    def equals(self, other): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the alternate
            substitution lookup.
        """
    def getAlternateGlyphs(self): ...
    def add_subtable_break(self, location) -> None: ...

class ChainContextualRule(NamedTuple('ChainContextualRule', [('prefix', Incomplete), ('glyphs', Incomplete), ('suffix', Incomplete), ('lookups', Incomplete)])):
    @property
    def is_subtable_break(self): ...

class ChainContextualRuleset:
    rules: Incomplete
    def __init__(self) -> None: ...
    def addRule(self, rule) -> None: ...
    @property
    def hasPrefixOrSuffix(self): ...
    @property
    def hasAnyGlyphClasses(self): ...
    def format2ClassDefs(self): ...

class ChainContextualBuilder(LookupBuilder):
    def equals(self, other): ...
    def rulesets(self): ...
    def getCompiledSize_(self, subtables): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the chained
            contextual positioning lookup.
        """
    def buildFormat1Subtable(self, ruleset, chaining: bool = True): ...
    def buildFormat2Subtable(self, ruleset, classdefs, chaining: bool = True): ...
    def buildFormat3Subtable(self, rule, chaining: bool = True): ...
    def buildLookupList(self, rule, st) -> None: ...
    def add_subtable_break(self, location) -> None: ...
    def newSubtable_(self, chaining: bool = True): ...
    def ruleSetAttr_(self, format: int = 1, chaining: bool = True): ...
    def ruleAttr_(self, format: int = 1, chaining: bool = True): ...
    def newRuleSet_(self, format: int = 1, chaining: bool = True): ...
    def newRule_(self, format: int = 1, chaining: bool = True): ...
    def attachSubtableWithCount_(self, st, subtable_name, count_name, existing: Incomplete | None = None, index: Incomplete | None = None, chaining: bool = False): ...
    def newLookupRecord_(self, st): ...

class ChainContextPosBuilder(ChainContextualBuilder):
    '''Builds a Chained Contextual Positioning (GPOS8) lookup.

    Users are expected to manually add rules to the ``rules`` attribute after
    the object has been initialized, e.g.::

        # pos [A B] [C D] x\' lookup lu1 y\' z\' lookup lu2 E;

        prefix  = [ ["A", "B"], ["C", "D"] ]
        suffix  = [ ["E"] ]
        glyphs  = [ ["x"], ["y"], ["z"] ]
        lookups = [ [lu1], None,  [lu2] ]
        builder.rules.append( (prefix, glyphs, suffix, lookups) )

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        rules: A list of tuples representing the rules in this lookup.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    rules: Incomplete
    subtable_type: str
    def __init__(self, font, location) -> None: ...
    def find_chainable_single_pos(self, lookups, glyphs, value):
        """Helper for add_single_pos_chained_()"""

class ChainContextSubstBuilder(ChainContextualBuilder):
    '''Builds a Chained Contextual Substitution (GSUB6) lookup.

    Users are expected to manually add rules to the ``rules`` attribute after
    the object has been initialized, e.g.::

        # sub [A B] [C D] x\' lookup lu1 y\' z\' lookup lu2 E;

        prefix  = [ ["A", "B"], ["C", "D"] ]
        suffix  = [ ["E"] ]
        glyphs  = [ ["x"], ["y"], ["z"] ]
        lookups = [ [lu1], None,  [lu2] ]
        builder.rules.append( (prefix, glyphs, suffix, lookups) )

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        rules: A list of tuples representing the rules in this lookup.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    rules: Incomplete
    subtable_type: str
    def __init__(self, font, location) -> None: ...
    def getAlternateGlyphs(self): ...
    def find_chainable_subst(self, mapping, builder_class):
        """Helper for add_{single,multi}_subst_chained_()"""

class LigatureSubstBuilder(LookupBuilder):
    '''Builds a Ligature Substitution (GSUB4) lookup.

    Users are expected to manually add ligatures to the ``ligatures``
    attribute after the object has been initialized, e.g.::

        # sub f i by f_i;
        builder.ligatures[("f","f","i")] = "f_f_i"

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        ligatures: An ordered dictionary mapping a tuple of glyph names to the
            ligature glyphname.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    ligatures: Incomplete
    def __init__(self, font, location) -> None: ...
    def equals(self, other): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the ligature
            substitution lookup.
        """
    def add_subtable_break(self, location) -> None: ...

class MultipleSubstBuilder(LookupBuilder):
    '''Builds a Multiple Substitution (GSUB2) lookup.

    Users are expected to manually add substitutions to the ``mapping``
    attribute after the object has been initialized, e.g.::

        # sub uni06C0 by uni06D5.fina hamza.above;
        builder.mapping["uni06C0"] = [ "uni06D5.fina", "hamza.above"]

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        mapping: An ordered dictionary mapping a glyph name to a list of
            substituted glyph names.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    mapping: Incomplete
    def __init__(self, font, location) -> None: ...
    def equals(self, other): ...
    def build(self): ...
    def add_subtable_break(self, location) -> None: ...

class CursivePosBuilder(LookupBuilder):
    """Builds a Cursive Positioning (GPOS3) lookup.

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        attachments: An ordered dictionary mapping a glyph name to a two-element
            tuple of ``otTables.Anchor`` objects.
        lookupflag (int): The lookup's flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup's
            flags.
    """
    attachments: Incomplete
    def __init__(self, font, location) -> None: ...
    def equals(self, other): ...
    def add_attachment(self, location, glyphs, entryAnchor, exitAnchor) -> None:
        """Adds attachment information to the cursive positioning lookup.

        Args:
            location: A string or tuple representing the location in the
                original source which produced this lookup. (Unused.)
            glyphs: A list of glyph names sharing these entry and exit
                anchor locations.
            entryAnchor: A ``otTables.Anchor`` object representing the
                entry anchor, or ``None`` if no entry anchor is present.
            exitAnchor: A ``otTables.Anchor`` object representing the
                exit anchor, or ``None`` if no exit anchor is present.
        """
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the cursive
            positioning lookup.
        """

class MarkBasePosBuilder(LookupBuilder):
    '''Builds a Mark-To-Base Positioning (GPOS4) lookup.

    Users are expected to manually add marks and bases to the ``marks``
    and ``bases`` attributes after the object has been initialized, e.g.::

        builder.marks["acute"]   = (0, a1)
        builder.marks["grave"]   = (0, a1)
        builder.marks["cedilla"] = (1, a2)
        builder.bases["a"] = {0: a3, 1: a5}
        builder.bases["b"] = {0: a4, 1: a5}

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        marks: An dictionary mapping a glyph name to a two-element
            tuple containing a mark class ID and ``otTables.Anchor`` object.
        bases: An dictionary mapping a glyph name to a dictionary of
            mark class IDs and ``otTables.Anchor`` object.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    marks: Incomplete
    bases: Incomplete
    def __init__(self, font, location) -> None: ...
    def equals(self, other): ...
    def inferGlyphClasses(self): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the mark-to-base
            positioning lookup.
        """

class MarkLigPosBuilder(LookupBuilder):
    '''Builds a Mark-To-Ligature Positioning (GPOS5) lookup.

    Users are expected to manually add marks and bases to the ``marks``
    and ``ligatures`` attributes after the object has been initialized, e.g.::

        builder.marks["acute"]   = (0, a1)
        builder.marks["grave"]   = (0, a1)
        builder.marks["cedilla"] = (1, a2)
        builder.ligatures["f_i"] = [
            { 0: a3, 1: a5 }, # f
            { 0: a4, 1: a5 }  # i
        ]

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        marks: An dictionary mapping a glyph name to a two-element
            tuple containing a mark class ID and ``otTables.Anchor`` object.
        ligatures: An dictionary mapping a glyph name to an array with one
            element for each ligature component. Each array element should be
            a dictionary mapping mark class IDs to ``otTables.Anchor`` objects.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    marks: Incomplete
    ligatures: Incomplete
    def __init__(self, font, location) -> None: ...
    def equals(self, other): ...
    def inferGlyphClasses(self): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the mark-to-ligature
            positioning lookup.
        """

class MarkMarkPosBuilder(LookupBuilder):
    '''Builds a Mark-To-Mark Positioning (GPOS6) lookup.

    Users are expected to manually add marks and bases to the ``marks``
    and ``baseMarks`` attributes after the object has been initialized, e.g.::

        builder.marks["acute"]     = (0, a1)
        builder.marks["grave"]     = (0, a1)
        builder.marks["cedilla"]   = (1, a2)
        builder.baseMarks["acute"] = {0: a3}

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        marks: An dictionary mapping a glyph name to a two-element
            tuple containing a mark class ID and ``otTables.Anchor`` object.
        baseMarks: An dictionary mapping a glyph name to a dictionary
            containing one item: a mark class ID and a ``otTables.Anchor`` object.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    marks: Incomplete
    baseMarks: Incomplete
    def __init__(self, font, location) -> None: ...
    def equals(self, other): ...
    def inferGlyphClasses(self): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the mark-to-mark
            positioning lookup.
        """

class ReverseChainSingleSubstBuilder(LookupBuilder):
    '''Builds a Reverse Chaining Contextual Single Substitution (GSUB8) lookup.

    Users are expected to manually add substitutions to the ``substitutions``
    attribute after the object has been initialized, e.g.::

        # reversesub [a e n] d\' by d.alt;
        prefix = [ ["a", "e", "n"] ]
        suffix = []
        mapping = { "d": "d.alt" }
        builder.substitutions.append( (prefix, suffix, mapping) )

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        substitutions: A three-element tuple consisting of a prefix sequence,
            a suffix sequence, and a dictionary of single substitutions.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    rules: Incomplete
    def __init__(self, font, location) -> None: ...
    def equals(self, other): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the chained
            contextual substitution lookup.
        """
    def add_subtable_break(self, location) -> None: ...

class SingleSubstBuilder(LookupBuilder):
    '''Builds a Single Substitution (GSUB1) lookup.

    Users are expected to manually add substitutions to the ``mapping``
    attribute after the object has been initialized, e.g.::

        # sub x by y;
        builder.mapping["x"] = "y"

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        mapping: A dictionary mapping a single glyph name to another glyph name.
        lookupflag (int): The lookup\'s flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup\'s
            flags.
    '''
    mapping: Incomplete
    def __init__(self, font, location) -> None: ...
    def equals(self, other): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the multiple
            substitution lookup.
        """
    def getAlternateGlyphs(self): ...
    def add_subtable_break(self, location) -> None: ...

class ClassPairPosSubtableBuilder:
    """Builds class-based Pair Positioning (GPOS2 format 2) subtables.

    Note that this does *not* build a GPOS2 ``otTables.Lookup`` directly,
    but builds a list of ``otTables.PairPos`` subtables. It is used by the
    :class:`PairPosBuilder` below.

    Attributes:
        builder (PairPosBuilder): A pair positioning lookup builder.
    """
    builder_: Incomplete
    values_: Incomplete
    forceSubtableBreak_: bool
    subtables_: Incomplete
    def __init__(self, builder) -> None: ...
    classDef1_: Incomplete
    classDef2_: Incomplete
    def addPair(self, gc1, value1, gc2, value2) -> None:
        '''Add a pair positioning rule.

        Args:
            gc1: A set of glyph names for the "left" glyph
            value1: An ``otTables.ValueRecord`` object for the left glyph\'s
                positioning.
            gc2: A set of glyph names for the "right" glyph
            value2: An ``otTables.ValueRecord`` object for the right glyph\'s
                positioning.
        '''
    def addSubtableBreak(self) -> None:
        """Add an explicit subtable break at this point."""
    def subtables(self):
        """Return the list of ``otTables.PairPos`` subtables constructed."""
    def flush_(self) -> None: ...

class PairPosBuilder(LookupBuilder):
    """Builds a Pair Positioning (GPOS2) lookup.

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        pairs: An array of class-based pair positioning tuples. Usually
            manipulated with the :meth:`addClassPair` method below.
        glyphPairs: A dictionary mapping a tuple of glyph names to a tuple
            of ``otTables.ValueRecord`` objects. Usually manipulated with the
            :meth:`addGlyphPair` method below.
        lookupflag (int): The lookup's flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup's
            flags.
    """
    pairs: Incomplete
    glyphPairs: Incomplete
    locations: Incomplete
    def __init__(self, font, location) -> None: ...
    def addClassPair(self, location, glyphclass1, value1, glyphclass2, value2) -> None:
        '''Add a class pair positioning rule to the current lookup.

        Args:
            location: A string or tuple representing the location in the
                original source which produced this rule. Unused.
            glyphclass1: A set of glyph names for the "left" glyph in the pair.
            value1: A ``otTables.ValueRecord`` for positioning the left glyph.
            glyphclass2: A set of glyph names for the "right" glyph in the pair.
            value2: A ``otTables.ValueRecord`` for positioning the right glyph.
        '''
    def addGlyphPair(self, location, glyph1, value1, glyph2, value2) -> None:
        '''Add a glyph pair positioning rule to the current lookup.

        Args:
            location: A string or tuple representing the location in the
                original source which produced this rule.
            glyph1: A glyph name for the "left" glyph in the pair.
            value1: A ``otTables.ValueRecord`` for positioning the left glyph.
            glyph2: A glyph name for the "right" glyph in the pair.
            value2: A ``otTables.ValueRecord`` for positioning the right glyph.
        '''
    def add_subtable_break(self, location) -> None: ...
    def equals(self, other): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the pair positioning
            lookup.
        """

class SinglePosBuilder(LookupBuilder):
    """Builds a Single Positioning (GPOS1) lookup.

    Attributes:
        font (``fontTools.TTLib.TTFont``): A font object.
        location: A string or tuple representing the location in the original
            source which produced this lookup.
        mapping: A dictionary mapping a glyph name to a ``otTables.ValueRecord``
            objects. Usually manipulated with the :meth:`add_pos` method below.
        lookupflag (int): The lookup's flag
        markFilterSet: Either ``None`` if no mark filtering set is used, or
            an integer representing the filtering set to be used for this
            lookup. If a mark filtering set is provided,
            `LOOKUP_FLAG_USE_MARK_FILTERING_SET` will be set on the lookup's
            flags.
    """
    locations: Incomplete
    mapping: Incomplete
    def __init__(self, font, location) -> None: ...
    def add_pos(self, location, glyph, otValueRecord) -> None:
        """Add a single positioning rule.

        Args:
            location: A string or tuple representing the location in the
                original source which produced this lookup.
            glyph: A glyph name.
            otValueRection: A ``otTables.ValueRecord`` used to position the
                glyph.
        """
    def can_add(self, glyph, value): ...
    def equals(self, other): ...
    def build(self):
        """Build the lookup.

        Returns:
            An ``otTables.Lookup`` object representing the single positioning
            lookup.
        """

def buildSingleSubstSubtable(mapping):
    """Builds a single substitution (GSUB1) subtable.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.SingleSubstBuilder` instead.

    Args:
        mapping: A dictionary mapping input glyph names to output glyph names.

    Returns:
        An ``otTables.SingleSubst`` object, or ``None`` if the mapping dictionary
        is empty.
    """
def buildMultipleSubstSubtable(mapping):
    '''Builds a multiple substitution (GSUB2) subtable.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.MultipleSubstBuilder` instead.

    Example::

        # sub uni06C0 by uni06D5.fina hamza.above
        # sub uni06C2 by uni06C1.fina hamza.above;

        subtable = buildMultipleSubstSubtable({
            "uni06C0": [ "uni06D5.fina", "hamza.above"],
            "uni06C2": [ "uni06D1.fina", "hamza.above"]
        })

    Args:
        mapping: A dictionary mapping input glyph names to a list of output
            glyph names.

    Returns:
        An ``otTables.MultipleSubst`` object or ``None`` if the mapping dictionary
        is empty.
    '''
def buildAlternateSubstSubtable(mapping):
    """Builds an alternate substitution (GSUB3) subtable.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.AlternateSubstBuilder` instead.

    Args:
        mapping: A dictionary mapping input glyph names to a list of output
            glyph names.

    Returns:
        An ``otTables.AlternateSubst`` object or ``None`` if the mapping dictionary
        is empty.
    """
def buildLigatureSubstSubtable(mapping):
    '''Builds a ligature substitution (GSUB4) subtable.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.LigatureSubstBuilder` instead.

    Example::

        # sub f f i by f_f_i;
        # sub f i by f_i;

        subtable = buildLigatureSubstSubtable({
            ("f", "f", "i"): "f_f_i",
            ("f", "i"): "f_i",
        })

    Args:
        mapping: A dictionary mapping tuples of glyph names to output
            glyph names.

    Returns:
        An ``otTables.LigatureSubst`` object or ``None`` if the mapping dictionary
        is empty.
    '''
def buildAnchor(x, y, point: Incomplete | None = None, deviceX: Incomplete | None = None, deviceY: Incomplete | None = None):
    """Builds an Anchor table.

    This determines the appropriate anchor format based on the passed parameters.

    Args:
        x (int): X coordinate.
        y (int): Y coordinate.
        point (int): Index of glyph contour point, if provided.
        deviceX (``otTables.Device``): X coordinate device table, if provided.
        deviceY (``otTables.Device``): Y coordinate device table, if provided.

    Returns:
        An ``otTables.Anchor`` object.
    """
def buildBaseArray(bases, numMarkClasses, glyphMap):
    '''Builds a base array record.

    As part of building mark-to-base positioning rules, you will need to define
    a ``BaseArray`` record, which "defines for each base glyph an array of
    anchors, one for each mark class." This function builds the base array
    subtable.

    Example::

        bases = {"a": {0: a3, 1: a5}, "b": {0: a4, 1: a5}}
        basearray = buildBaseArray(bases, 2, font.getReverseGlyphMap())

    Args:
        bases (dict): A dictionary mapping anchors to glyphs; the keys being
            glyph names, and the values being dictionaries mapping mark class ID
            to the appropriate ``otTables.Anchor`` object used for attaching marks
            of that class.
        numMarkClasses (int): The total number of mark classes for which anchors
            are defined.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        An ``otTables.BaseArray`` object.
    '''
def buildBaseRecord(anchors): ...
def buildComponentRecord(anchors):
    '''Builds a component record.

    As part of building mark-to-ligature positioning rules, you will need to
    define ``ComponentRecord`` objects, which contain "an array of offsets...
    to the Anchor tables that define all the attachment points used to attach
    marks to the component." This function builds the component record.

    Args:
        anchors: A list of ``otTables.Anchor`` objects or ``None``.

    Returns:
        A ``otTables.ComponentRecord`` object or ``None`` if no anchors are
        supplied.
    '''
def buildCursivePosSubtable(attach, glyphMap):
    '''Builds a cursive positioning (GPOS3) subtable.

    Cursive positioning lookups are made up of a coverage table of glyphs,
    and a set of ``EntryExitRecord`` records containing the anchors for
    each glyph. This function builds the cursive positioning subtable.

    Example::

        subtable = buildCursivePosSubtable({
            "AlifIni": (None, buildAnchor(0, 50)),
            "BehMed": (buildAnchor(500,250), buildAnchor(0,50)),
            # ...
        }, font.getReverseGlyphMap())

    Args:
        attach (dict): A mapping between glyph names and a tuple of two
            ``otTables.Anchor`` objects representing entry and exit anchors.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        An ``otTables.CursivePos`` object, or ``None`` if the attachment
        dictionary was empty.
    '''
def buildDevice(deltas):
    """Builds a Device record as part of a ValueRecord or Anchor.

    Device tables specify size-specific adjustments to value records
    and anchors to reflect changes based on the resolution of the output.
    For example, one could specify that an anchor's Y position should be
    increased by 1 pixel when displayed at 8 pixels per em. This routine
    builds device records.

    Args:
        deltas: A dictionary mapping pixels-per-em sizes to the delta
            adjustment in pixels when the font is displayed at that size.

    Returns:
        An ``otTables.Device`` object if any deltas were supplied, or
        ``None`` otherwise.
    """
def buildLigatureArray(ligs, numMarkClasses, glyphMap):
    '''Builds a LigatureArray subtable.

    As part of building a mark-to-ligature lookup, you will need to define
    the set of anchors (for each mark class) on each component of the ligature
    where marks can be attached. For example, for an Arabic divine name ligature
    (lam lam heh), you may want to specify mark attachment positioning for
    superior marks (fatha, etc.) and inferior marks (kasra, etc.) on each glyph
    of the ligature. This routine builds the ligature array record.

    Example::

        buildLigatureArray({
            "lam-lam-heh": [
                { 0: superiorAnchor1, 1: inferiorAnchor1 }, # attach points for lam1
                { 0: superiorAnchor2, 1: inferiorAnchor2 }, # attach points for lam2
                { 0: superiorAnchor3, 1: inferiorAnchor3 }, # attach points for heh
            ]
        }, 2, font.getReverseGlyphMap())

    Args:
        ligs (dict): A mapping of ligature names to an array of dictionaries:
            for each component glyph in the ligature, an dictionary mapping
            mark class IDs to anchors.
        numMarkClasses (int): The number of mark classes.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        An ``otTables.LigatureArray`` object if deltas were supplied.
    '''
def buildLigatureAttach(components): ...
def buildMarkArray(marks, glyphMap):
    '''Builds a mark array subtable.

    As part of building mark-to-* positioning rules, you will need to define
    a MarkArray subtable, which "defines the class and the anchor point
    for a mark glyph." This function builds the mark array subtable.

    Example::

        mark = {
            "acute": (0, buildAnchor(300,712)),
            # ...
        }
        markarray = buildMarkArray(marks, font.getReverseGlyphMap())

    Args:
        marks (dict): A dictionary mapping anchors to glyphs; the keys being
            glyph names, and the values being a tuple of mark class number and
            an ``otTables.Anchor`` object representing the mark\'s attachment
            point.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        An ``otTables.MarkArray`` object.
    '''
def buildMarkBasePos(marks, bases, glyphMap):
    '''Build a list of MarkBasePos (GPOS4) subtables.

    This routine turns a set of marks and bases into a list of mark-to-base
    positioning subtables. Currently the list will contain a single subtable
    containing all marks and bases, although at a later date it may return the
    optimal list of subtables subsetting the marks and bases into groups which
    save space. See :func:`buildMarkBasePosSubtable` below.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.MarkBasePosBuilder` instead.

    Example::

        # a1, a2, a3, a4, a5 = buildAnchor(500, 100), ...

        marks = {"acute": (0, a1), "grave": (0, a1), "cedilla": (1, a2)}
        bases = {"a": {0: a3, 1: a5}, "b": {0: a4, 1: a5}}
        markbaseposes = buildMarkBasePos(marks, bases, font.getReverseGlyphMap())

    Args:
        marks (dict): A dictionary mapping anchors to glyphs; the keys being
            glyph names, and the values being a tuple of mark class number and
            an ``otTables.Anchor`` object representing the mark\'s attachment
            point. (See :func:`buildMarkArray`.)
        bases (dict): A dictionary mapping anchors to glyphs; the keys being
            glyph names, and the values being dictionaries mapping mark class ID
            to the appropriate ``otTables.Anchor`` object used for attaching marks
            of that class. (See :func:`buildBaseArray`.)
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        A list of ``otTables.MarkBasePos`` objects.
    '''
def buildMarkBasePosSubtable(marks, bases, glyphMap):
    """Build a single MarkBasePos (GPOS4) subtable.

    This builds a mark-to-base lookup subtable containing all of the referenced
    marks and bases. See :func:`buildMarkBasePos`.

    Args:
        marks (dict): A dictionary mapping anchors to glyphs; the keys being
            glyph names, and the values being a tuple of mark class number and
            an ``otTables.Anchor`` object representing the mark's attachment
            point. (See :func:`buildMarkArray`.)
        bases (dict): A dictionary mapping anchors to glyphs; the keys being
            glyph names, and the values being dictionaries mapping mark class ID
            to the appropriate ``otTables.Anchor`` object used for attaching marks
            of that class. (See :func:`buildBaseArray`.)
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        A ``otTables.MarkBasePos`` object.
    """
def buildMarkLigPos(marks, ligs, glyphMap):
    '''Build a list of MarkLigPos (GPOS5) subtables.

    This routine turns a set of marks and ligatures into a list of mark-to-ligature
    positioning subtables. Currently the list will contain a single subtable
    containing all marks and ligatures, although at a later date it may return
    the optimal list of subtables subsetting the marks and ligatures into groups
    which save space. See :func:`buildMarkLigPosSubtable` below.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.MarkLigPosBuilder` instead.

    Example::

        # a1, a2, a3, a4, a5 = buildAnchor(500, 100), ...
        marks = {
            "acute": (0, a1),
            "grave": (0, a1),
            "cedilla": (1, a2)
        }
        ligs = {
            "f_i": [
                { 0: a3, 1: a5 }, # f
                { 0: a4, 1: a5 }  # i
                ],
        #   "c_t": [{...}, {...}]
        }
        markligposes = buildMarkLigPos(marks, ligs,
            font.getReverseGlyphMap())

    Args:
        marks (dict): A dictionary mapping anchors to glyphs; the keys being
            glyph names, and the values being a tuple of mark class number and
            an ``otTables.Anchor`` object representing the mark\'s attachment
            point. (See :func:`buildMarkArray`.)
        ligs (dict): A mapping of ligature names to an array of dictionaries:
            for each component glyph in the ligature, an dictionary mapping
            mark class IDs to anchors. (See :func:`buildLigatureArray`.)
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        A list of ``otTables.MarkLigPos`` objects.

    '''
def buildMarkLigPosSubtable(marks, ligs, glyphMap):
    """Build a single MarkLigPos (GPOS5) subtable.

    This builds a mark-to-base lookup subtable containing all of the referenced
    marks and bases. See :func:`buildMarkLigPos`.

    Args:
        marks (dict): A dictionary mapping anchors to glyphs; the keys being
            glyph names, and the values being a tuple of mark class number and
            an ``otTables.Anchor`` object representing the mark's attachment
            point. (See :func:`buildMarkArray`.)
        ligs (dict): A mapping of ligature names to an array of dictionaries:
            for each component glyph in the ligature, an dictionary mapping
            mark class IDs to anchors. (See :func:`buildLigatureArray`.)
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        A ``otTables.MarkLigPos`` object.
    """
def buildMarkRecord(classID, anchor): ...
def buildMark2Record(anchors): ...
def buildPairPosClassesSubtable(pairs, glyphMap, valueFormat1: Incomplete | None = None, valueFormat2: Incomplete | None = None):
    '''Builds a class pair adjustment (GPOS2 format 2) subtable.

    Kerning tables are generally expressed as pair positioning tables using
    class-based pair adjustments. This routine builds format 2 PairPos
    subtables.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.ClassPairPosSubtableBuilder`
    instead, as this takes care of ensuring that the supplied pairs can be
    formed into non-overlapping classes and emitting individual subtables
    whenever the non-overlapping requirement means that a new subtable is
    required.

    Example::

        pairs = {}

        pairs[(
            [ "K", "X" ],
            [ "W", "V" ]
        )] = ( buildValue(xAdvance=+5), buildValue() )
        # pairs[(... , ...)] = (..., ...)

        pairpos = buildPairPosClassesSubtable(pairs, font.getReverseGlyphMap())

    Args:
        pairs (dict): Pair positioning data; the keys being a two-element
            tuple of lists of glyphnames, and the values being a two-element
            tuple of ``otTables.ValueRecord`` objects.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.
        valueFormat1: Force the "left" value records to the given format.
        valueFormat2: Force the "right" value records to the given format.

    Returns:
        A ``otTables.PairPos`` object.
    '''
def buildPairPosGlyphs(pairs, glyphMap):
    '''Builds a list of glyph-based pair adjustment (GPOS2 format 1) subtables.

    This organises a list of pair positioning adjustments into subtables based
    on common value record formats.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.PairPosBuilder`
    instead.

    Example::

        pairs = {
            ("K", "W"): ( buildValue(xAdvance=+5), buildValue() ),
            ("K", "V"): ( buildValue(xAdvance=+5), buildValue() ),
            # ...
        }

        subtables = buildPairPosGlyphs(pairs, font.getReverseGlyphMap())

    Args:
        pairs (dict): Pair positioning data; the keys being a two-element
            tuple of glyphnames, and the values being a two-element
            tuple of ``otTables.ValueRecord`` objects.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        A list of ``otTables.PairPos`` objects.
    '''
def buildPairPosGlyphsSubtable(pairs, glyphMap, valueFormat1: Incomplete | None = None, valueFormat2: Incomplete | None = None):
    '''Builds a single glyph-based pair adjustment (GPOS2 format 1) subtable.

    This builds a PairPos subtable from a dictionary of glyph pairs and
    their positioning adjustments. See also :func:`buildPairPosGlyphs`.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.PairPosBuilder` instead.

    Example::

        pairs = {
            ("K", "W"): ( buildValue(xAdvance=+5), buildValue() ),
            ("K", "V"): ( buildValue(xAdvance=+5), buildValue() ),
            # ...
        }

        pairpos = buildPairPosGlyphsSubtable(pairs, font.getReverseGlyphMap())

    Args:
        pairs (dict): Pair positioning data; the keys being a two-element
            tuple of glyphnames, and the values being a two-element
            tuple of ``otTables.ValueRecord`` objects.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.
        valueFormat1: Force the "left" value records to the given format.
        valueFormat2: Force the "right" value records to the given format.

    Returns:
        A ``otTables.PairPos`` object.
    '''
def buildSinglePos(mapping, glyphMap):
    '''Builds a list of single adjustment (GPOS1) subtables.

    This builds a list of SinglePos subtables from a dictionary of glyph
    names and their positioning adjustments. The format of the subtables are
    determined to optimize the size of the resulting subtables.
    See also :func:`buildSinglePosSubtable`.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.SinglePosBuilder` instead.

    Example::

        mapping = {
            "V": buildValue({ "xAdvance" : +5 }),
            # ...
        }

        subtables = buildSinglePos(pairs, font.getReverseGlyphMap())

    Args:
        mapping (dict): A mapping between glyphnames and
            ``otTables.ValueRecord`` objects.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        A list of ``otTables.SinglePos`` objects.
    '''
def buildSinglePosSubtable(values, glyphMap):
    '''Builds a single adjustment (GPOS1) subtable.

    This builds a list of SinglePos subtables from a dictionary of glyph
    names and their positioning adjustments. The format of the subtable is
    determined to optimize the size of the output.
    See also :func:`buildSinglePos`.

    Note that if you are implementing a layout compiler, you may find it more
    flexible to use
    :py:class:`fontTools.otlLib.lookupBuilders.SinglePosBuilder` instead.

    Example::

        mapping = {
            "V": buildValue({ "xAdvance" : +5 }),
            # ...
        }

        subtable = buildSinglePos(pairs, font.getReverseGlyphMap())

    Args:
        mapping (dict): A mapping between glyphnames and
            ``otTables.ValueRecord`` objects.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        A ``otTables.SinglePos`` object.
    '''

class _DeviceTuple(NamedTuple):
    DeltaFormat: Incomplete
    StartSize: Incomplete
    EndSize: Incomplete
    DeltaValue: Incomplete

def buildValue(value):
    """Builds a positioning value record.

    Value records are used to specify coordinates and adjustments for
    positioning and attaching glyphs. Many of the positioning functions
    in this library take ``otTables.ValueRecord`` objects as arguments.
    This function builds value records from dictionaries.

    Args:
        value (dict): A dictionary with zero or more of the following keys:
            - ``xPlacement``
            - ``yPlacement``
            - ``xAdvance``
            - ``yAdvance``
            - ``xPlaDevice``
            - ``yPlaDevice``
            - ``xAdvDevice``
            - ``yAdvDevice``

    Returns:
        An ``otTables.ValueRecord`` object.
    """
def buildAttachList(attachPoints, glyphMap):
    """Builds an AttachList subtable.

    A GDEF table may contain an Attachment Point List table (AttachList)
    which stores the contour indices of attachment points for glyphs with
    attachment points. This routine builds AttachList subtables.

    Args:
        attachPoints (dict): A mapping between glyph names and a list of
            contour indices.

    Returns:
        An ``otTables.AttachList`` object if attachment points are supplied,
            or ``None`` otherwise.
    """
def buildAttachPoint(points): ...
def buildCaretValueForCoord(coord): ...
def buildCaretValueForPoint(point): ...
def buildLigCaretList(coords, points, glyphMap):
    '''Builds a ligature caret list table.

    Ligatures appear as a single glyph representing multiple characters; however
    when, for example, editing text containing a ``f_i`` ligature, the user may
    want to place the cursor between the ``f`` and the ``i``. The ligature caret
    list in the GDEF table specifies the position to display the "caret" (the
    character insertion indicator, typically a flashing vertical bar) "inside"
    the ligature to represent an insertion point. The insertion positions may
    be specified either by coordinate or by contour point.

    Example::

        coords = {
            "f_f_i": [300, 600] # f|fi cursor at 300 units, ff|i cursor at 600.
        }
        points = {
            "c_t": [28] # c|t cursor appears at coordinate of contour point 28.
        }
        ligcaretlist = buildLigCaretList(coords, points, font.getReverseGlyphMap())

    Args:
        coords: A mapping between glyph names and a list of coordinates for
            the insertion point of each ligature component after the first one.
        points: A mapping between glyph names and a list of contour points for
            the insertion point of each ligature component after the first one.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns:
        A ``otTables.LigCaretList`` object if any carets are present, or
            ``None`` otherwise.'''
def buildLigGlyph(coords, points): ...
def buildMarkGlyphSetsDef(markSets, glyphMap):
    '''Builds a mark glyph sets definition table.

    OpenType Layout lookups may choose to use mark filtering sets to consider
    or ignore particular combinations of marks. These sets are specified by
    setting a flag on the lookup, but the mark filtering sets are defined in
    the ``GDEF`` table. This routine builds the subtable containing the mark
    glyph set definitions.

    Example::

        set0 = set("acute", "grave")
        set1 = set("caron", "grave")

        markglyphsets = buildMarkGlyphSetsDef([set0, set1], font.getReverseGlyphMap())

    Args:

        markSets: A list of sets of glyphnames.
        glyphMap: a glyph name to ID map, typically returned from
            ``font.getReverseGlyphMap()``.

    Returns
        An ``otTables.MarkGlyphSetsDef`` object.
    '''

class ClassDefBuilder:
    """Helper for building ClassDef tables."""
    classes_: Incomplete
    glyphs_: Incomplete
    useClass0_: Incomplete
    def __init__(self, useClass0) -> None: ...
    def canAdd(self, glyphs): ...
    def add(self, glyphs) -> None: ...
    def classes(self): ...
    def build(self): ...

AXIS_VALUE_NEGATIVE_INFINITY: Incomplete
AXIS_VALUE_POSITIVE_INFINITY: Incomplete

def buildStatTable(ttFont, axes, locations: Incomplete | None = None, elidedFallbackName: int = 2, windowsNames: bool = True, macNames: bool = True) -> None:
    '''Add a \'STAT\' table to \'ttFont\'.

    \'axes\' is a list of dictionaries describing axes and their
    values.

    Example::

        axes = [
            dict(
                tag="wght",
                name="Weight",
                ordering=0,  # optional
                values=[
                    dict(value=100, name=\'Thin\'),
                    dict(value=300, name=\'Light\'),
                    dict(value=400, name=\'Regular\', flags=0x2),
                    dict(value=900, name=\'Black\'),
                ],
            )
        ]

    Each axis dict must have \'tag\' and \'name\' items. \'tag\' maps
    to the \'AxisTag\' field. \'name\' can be a name ID (int), a string,
    or a dictionary containing multilingual names (see the
    addMultilingualName() name table method), and will translate to
    the AxisNameID field.

    An axis dict may contain an \'ordering\' item that maps to the
    AxisOrdering field. If omitted, the order of the axes list is
    used to calculate AxisOrdering fields.

    The axis dict may contain a \'values\' item, which is a list of
    dictionaries describing AxisValue records belonging to this axis.

    Each value dict must have a \'name\' item, which can be a name ID
    (int), a string, or a dictionary containing multilingual names,
    like the axis name. It translates to the ValueNameID field.

    Optionally the value dict can contain a \'flags\' item. It maps to
    the AxisValue Flags field, and will be 0 when omitted.

    The format of the AxisValue is determined by the remaining contents
    of the value dictionary:

    If the value dict contains a \'value\' item, an AxisValue record
    Format 1 is created. If in addition to the \'value\' item it contains
    a \'linkedValue\' item, an AxisValue record Format 3 is built.

    If the value dict contains a \'nominalValue\' item, an AxisValue
    record Format 2 is built. Optionally it may contain \'rangeMinValue\'
    and \'rangeMaxValue\' items. These map to -Infinity and +Infinity
    respectively if omitted.

    You cannot specify Format 4 AxisValue tables this way, as they are
    not tied to a single axis, and specify a name for a location that
    is defined by multiple axes values. Instead, you need to supply the
    \'locations\' argument.

    The optional \'locations\' argument specifies AxisValue Format 4
    tables. It should be a list of dicts, where each dict has a \'name\'
    item, which works just like the value dicts above, an optional
    \'flags\' item (defaulting to 0x0), and a \'location\' dict. A
    location dict key is an axis tag, and the associated value is the
    location on the specified axis. They map to the AxisIndex and Value
    fields of the AxisValueRecord.

    Example::

        locations = [
            dict(name=\'Regular ABCD\', location=dict(wght=300, ABCD=100)),
            dict(name=\'Bold ABCD XYZ\', location=dict(wght=600, ABCD=200)),
        ]

    The optional \'elidedFallbackName\' argument can be a name ID (int),
    a string, a dictionary containing multilingual names, or a list of
    STATNameStatements. It translates to the ElidedFallbackNameID field.

    The \'ttFont\' argument must be a TTFont instance that already has a
    \'name\' table. If a \'STAT\' table already exists, it will be
    overwritten by the newly created one.
    '''
def buildMathTable(ttFont, constants: Incomplete | None = None, italicsCorrections: Incomplete | None = None, topAccentAttachments: Incomplete | None = None, extendedShapes: Incomplete | None = None, mathKerns: Incomplete | None = None, minConnectorOverlap: int = 0, vertGlyphVariants: Incomplete | None = None, horizGlyphVariants: Incomplete | None = None, vertGlyphAssembly: Incomplete | None = None, horizGlyphAssembly: Incomplete | None = None) -> None:
    '''
    Add a \'MATH\' table to \'ttFont\'.

    \'constants\' is a dictionary of math constants. The keys are the constant
    names from the MATH table specification (with capital first letter), and the
    values are the constant values as numbers.

    \'italicsCorrections\' is a dictionary of italic corrections. The keys are the
    glyph names, and the values are the italic corrections as numbers.

    \'topAccentAttachments\' is a dictionary of top accent attachments. The keys
    are the glyph names, and the values are the top accent horizontal positions
    as numbers.

    \'extendedShapes\' is a set of extended shape glyphs.

    \'mathKerns\' is a dictionary of math kerns. The keys are the glyph names, and
    the values are dictionaries. The keys of these dictionaries are the side
    names (\'TopRight\', \'TopLeft\', \'BottomRight\', \'BottomLeft\'), and the values
    are tuples of two lists. The first list contains the correction heights as
    numbers, and the second list contains the kern values as numbers.

    \'minConnectorOverlap\' is the minimum connector overlap as a number.

    \'vertGlyphVariants\' is a dictionary of vertical glyph variants. The keys are
    the glyph names, and the values are tuples of glyph name and full advance height.

    \'horizGlyphVariants\' is a dictionary of horizontal glyph variants. The keys
    are the glyph names, and the values are tuples of glyph name and full
    advance width.

    \'vertGlyphAssembly\' is a dictionary of vertical glyph assemblies. The keys
    are the glyph names, and the values are tuples of assembly parts and italics
    correction. The assembly parts are tuples of glyph name, flags, start
    connector length, end connector length, and full advance height.

    \'horizGlyphAssembly\' is a dictionary of horizontal glyph assemblies. The
    keys are the glyph names, and the values are tuples of assembly parts
    and italics correction. The assembly parts are tuples of glyph name, flags,
    start connector length, end connector length, and full advance width.

    Where a number is expected, an integer or a float can be used. The floats
    will be rounded.

    Example::

        constants = {
            "ScriptPercentScaleDown": 70,
            "ScriptScriptPercentScaleDown": 50,
            "DelimitedSubFormulaMinHeight": 24,
            "DisplayOperatorMinHeight": 60,
            ...
        }
        italicsCorrections = {
            "fitalic-math": 100,
            "fbolditalic-math": 120,
            ...
        }
        topAccentAttachments = {
            "circumflexcomb": 500,
            "acutecomb": 400,
            "A": 300,
            "B": 340,
            ...
        }
        extendedShapes = {"parenleft", "parenright", ...}
        mathKerns = {
            "A": {
                "TopRight": ([-50, -100], [10, 20, 30]),
                "TopLeft": ([50, 100], [10, 20, 30]),
                ...
            },
            ...
        }
        vertGlyphVariants = {
            "parenleft": [("parenleft", 700), ("parenleft.size1", 1000), ...],
            "parenright": [("parenright", 700), ("parenright.size1", 1000), ...],
            ...
        }
        vertGlyphAssembly = {
            "braceleft": [
                (
                    ("braceleft.bottom", 0, 0, 200, 500),
                    ("braceleft.extender", 1, 200, 200, 200)),
                    ("braceleft.middle", 0, 100, 100, 700),
                    ("braceleft.extender", 1, 200, 200, 200),
                    ("braceleft.top", 0, 200, 0, 500),
                ),
                100,
            ],
            ...
        }
    '''
