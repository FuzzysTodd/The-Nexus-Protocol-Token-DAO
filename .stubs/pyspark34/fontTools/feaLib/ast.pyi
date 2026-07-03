from _typeshed import Incomplete

__all__ = ['Element', 'FeatureFile', 'Comment', 'GlyphName', 'GlyphClass', 'GlyphClassName', 'MarkClassName', 'AnonymousBlock', 'Block', 'FeatureBlock', 'NestedBlock', 'LookupBlock', 'GlyphClassDefinition', 'GlyphClassDefStatement', 'MarkClass', 'MarkClassDefinition', 'AlternateSubstStatement', 'Anchor', 'AnchorDefinition', 'AttachStatement', 'AxisValueLocationStatement', 'BaseAxis', 'CVParametersNameStatement', 'ChainContextPosStatement', 'ChainContextSubstStatement', 'CharacterStatement', 'ConditionsetStatement', 'CursivePosStatement', 'ElidedFallbackName', 'ElidedFallbackNameID', 'Expression', 'FeatureNameStatement', 'FeatureReferenceStatement', 'FontRevisionStatement', 'HheaField', 'IgnorePosStatement', 'IgnoreSubstStatement', 'IncludeStatement', 'LanguageStatement', 'LanguageSystemStatement', 'LigatureCaretByIndexStatement', 'LigatureCaretByPosStatement', 'LigatureSubstStatement', 'LookupFlagStatement', 'LookupReferenceStatement', 'MarkBasePosStatement', 'MarkLigPosStatement', 'MarkMarkPosStatement', 'MultipleSubstStatement', 'NameRecord', 'OS2Field', 'PairPosStatement', 'ReverseChainSingleSubstStatement', 'ScriptStatement', 'SinglePosStatement', 'SingleSubstStatement', 'SizeParameters', 'Statement', 'STATAxisValueStatement', 'STATDesignAxisStatement', 'STATNameStatement', 'SubtableStatement', 'TableBlock', 'ValueRecord', 'ValueRecordDefinition', 'VheaField']

class Element:
    '''A base class representing "something" in a feature file.'''
    location: Incomplete
    def __init__(self, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = '') -> None:
        """Returns this element as a string of feature code. For block-type
        elements (such as :class:`FeatureBlock`), the `indent` string is
        added to the start of each line in the output."""

class Statement(Element): ...
class Expression(Element): ...

class Comment(Element):
    """A comment in a feature file."""
    text: Incomplete
    def __init__(self, text, location: Incomplete | None = None) -> None: ...
    def asFea(self, indent: str = ''): ...

class NullGlyph(Expression):
    """The NULL glyph, used in glyph deletion substitutions."""
    def __init__(self, location: Incomplete | None = None) -> None: ...
    def glyphSet(self):
        """The glyphs in this class as a tuple of :class:`GlyphName` objects."""
    def asFea(self, indent: str = ''): ...

class GlyphName(Expression):
    """A single glyph name, such as ``cedilla``."""
    glyph: Incomplete
    def __init__(self, glyph, location: Incomplete | None = None) -> None: ...
    def glyphSet(self):
        """The glyphs in this class as a tuple of :class:`GlyphName` objects."""
    def asFea(self, indent: str = ''): ...

class GlyphClass(Expression):
    """A glyph class, such as ``[acute cedilla grave]``."""
    glyphs: Incomplete
    original: Incomplete
    curr: int
    def __init__(self, glyphs: Incomplete | None = None, location: Incomplete | None = None) -> None: ...
    def glyphSet(self):
        """The glyphs in this class as a tuple of :class:`GlyphName` objects."""
    def asFea(self, indent: str = ''): ...
    def extend(self, glyphs) -> None:
        """Add a list of :class:`GlyphName` objects to the class."""
    def append(self, glyph) -> None:
        """Add a single :class:`GlyphName` object to the class."""
    def add_range(self, start, end, glyphs) -> None:
        """Add a range (e.g. ``A-Z``) to the class. ``start`` and ``end``
        are either :class:`GlyphName` objects or strings representing the
        start and end glyphs in the class, and ``glyphs`` is the full list of
        :class:`GlyphName` objects in the range."""
    def add_cid_range(self, start, end, glyphs) -> None:
        """Add a range to the class by glyph ID. ``start`` and ``end`` are the
        initial and final IDs, and ``glyphs`` is the full list of
        :class:`GlyphName` objects in the range."""
    def add_class(self, gc) -> None:
        """Add glyphs from the given :class:`GlyphClassName` object to the
        class."""

class GlyphClassName(Expression):
    """A glyph class name, such as ``@FRENCH_MARKS``. This must be instantiated
    with a :class:`GlyphClassDefinition` object."""
    glyphclass: Incomplete
    def __init__(self, glyphclass, location: Incomplete | None = None) -> None: ...
    def glyphSet(self):
        """The glyphs in this class as a tuple of :class:`GlyphName` objects."""
    def asFea(self, indent: str = ''): ...

class MarkClassName(Expression):
    """A mark class name, such as ``@FRENCH_MARKS`` defined with ``markClass``.
    This must be instantiated with a :class:`MarkClass` object."""
    markClass: Incomplete
    def __init__(self, markClass, location: Incomplete | None = None) -> None: ...
    def glyphSet(self):
        """The glyphs in this class as a tuple of :class:`GlyphName` objects."""
    def asFea(self, indent: str = ''): ...

class AnonymousBlock(Statement):
    """An anonymous data block."""
    tag: Incomplete
    content: Incomplete
    def __init__(self, tag, content, location: Incomplete | None = None) -> None: ...
    def asFea(self, indent: str = ''): ...

class Block(Statement):
    """A block of statements: feature, lookup, etc."""
    statements: Incomplete
    def __init__(self, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """When handed a 'builder' object of comparable interface to
        :class:`fontTools.feaLib.builder`, walks the statements in this
        block, calling the builder callbacks."""
    def asFea(self, indent: str = ''): ...

class FeatureFile(Block):
    """The top-level element of the syntax tree, containing the whole feature
    file in its ``statements`` attribute."""
    markClasses: Incomplete
    def __init__(self) -> None: ...
    def asFea(self, indent: str = ''): ...

class FeatureBlock(Block):
    """A named feature block."""
    def __init__(self, name, use_extension: bool = False, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Call the ``start_feature`` callback on the builder object, visit
        all the statements in this feature, and then call ``end_feature``."""
    def asFea(self, indent: str = ''): ...

class NestedBlock(Block):
    """A block inside another block, for example when found inside a
    ``cvParameters`` block."""
    tag: Incomplete
    block_name: Incomplete
    def __init__(self, tag, block_name, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = ''): ...

class LookupBlock(Block):
    """A named lookup, containing ``statements``."""
    def __init__(self, name, use_extension: bool = False, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = ''): ...

class TableBlock(Block):
    """A ``table ... { }`` block."""
    name: Incomplete
    def __init__(self, name, location: Incomplete | None = None) -> None: ...
    def asFea(self, indent: str = ''): ...

class GlyphClassDefinition(Statement):
    """Example: ``@UPPERCASE = [A-Z];``."""
    name: Incomplete
    glyphs: Incomplete
    def __init__(self, name, glyphs, location: Incomplete | None = None) -> None: ...
    def glyphSet(self):
        """The glyphs in this class as a tuple of :class:`GlyphName` objects."""
    def asFea(self, indent: str = ''): ...

class GlyphClassDefStatement(Statement):
    """Example: ``GlyphClassDef @UPPERCASE, [B], [C], [D];``. The parameters
    must be either :class:`GlyphClass` or :class:`GlyphClassName` objects, or
    ``None``."""
    ligatureGlyphs: Incomplete
    componentGlyphs: Incomplete
    def __init__(self, baseGlyphs, markGlyphs, ligatureGlyphs, componentGlyphs, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder's ``add_glyphClassDef`` callback."""
    def asFea(self, indent: str = ''): ...

class MarkClass:
    """One `or more` ``markClass`` statements for the same mark class.

    While glyph classes can be defined only once, the feature file format
    allows expanding mark classes with multiple definitions, each using
    different glyphs and anchors. The following are two ``MarkClassDefinitions``
    for the same ``MarkClass``::

        markClass [acute grave] <anchor 350 800> @FRENCH_ACCENTS;
        markClass [cedilla] <anchor 350 -200> @FRENCH_ACCENTS;

    The ``MarkClass`` object is therefore just a container for a list of
    :class:`MarkClassDefinition` statements.
    """
    name: Incomplete
    definitions: Incomplete
    glyphs: Incomplete
    def __init__(self, name) -> None: ...
    def addDefinition(self, definition) -> None:
        """Add a :class:`MarkClassDefinition` statement to this mark class."""
    def glyphSet(self):
        """The glyphs in this class as a tuple of :class:`GlyphName` objects."""
    def asFea(self, indent: str = ''): ...

class MarkClassDefinition(Statement):
    '''A single ``markClass`` statement. The ``markClass`` should be a
    :class:`MarkClass` object, the ``anchor`` an :class:`Anchor` object,
    and the ``glyphs`` parameter should be a `glyph-containing object`_ .

    Example:

        .. code:: python

            mc = MarkClass("FRENCH_ACCENTS")
            mc.addDefinition( MarkClassDefinition(mc, Anchor(350, 800),
                GlyphClass([ GlyphName("acute"), GlyphName("grave") ])
            ) )
            mc.addDefinition( MarkClassDefinition(mc, Anchor(350, -200),
                GlyphClass([ GlyphName("cedilla") ])
            ) )

            mc.asFea()
            # markClass [acute grave] <anchor 350 800> @FRENCH_ACCENTS;
            # markClass [cedilla] <anchor 350 -200> @FRENCH_ACCENTS;

    '''
    def __init__(self, markClass, anchor, glyphs, location: Incomplete | None = None) -> None: ...
    def glyphSet(self):
        """The glyphs in this class as a tuple of :class:`GlyphName` objects."""
    def asFea(self, indent: str = ''): ...

class AlternateSubstStatement(Statement):
    """A ``sub ... from ...`` statement.

    ``prefix``, ``glyph``, ``suffix`` and ``replacement`` should be lists of
    `glyph-containing objects`_. ``glyph`` should be a `one element list`."""
    replacement: Incomplete
    def __init__(self, prefix, glyph, suffix, replacement, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder's ``add_alternate_subst`` callback."""
    def asFea(self, indent: str = ''): ...

class Anchor(Expression):
    """An ``Anchor`` element, used inside a ``pos`` rule.

    If a ``name`` is given, this will be used in preference to the coordinates.
    Other values should be integer.
    """
    name: Incomplete
    def __init__(self, x, y, name: Incomplete | None = None, contourpoint: Incomplete | None = None, xDeviceTable: Incomplete | None = None, yDeviceTable: Incomplete | None = None, location: Incomplete | None = None) -> None: ...
    def asFea(self, indent: str = ''): ...

class AnchorDefinition(Statement):
    """A named anchor definition. (2.e.viii). ``name`` should be a string."""
    def __init__(self, name, x, y, contourpoint: Incomplete | None = None, location: Incomplete | None = None) -> None: ...
    def asFea(self, indent: str = ''): ...

class AttachStatement(Statement):
    """A ``GDEF`` table ``Attach`` statement."""
    glyphs: Incomplete
    contourPoints: Incomplete
    def __init__(self, glyphs, contourPoints, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder's ``add_attach_points`` callback."""
    def asFea(self, indent: str = ''): ...

class ChainContextPosStatement(Statement):
    """A chained contextual positioning statement.

    ``prefix``, ``glyphs``, and ``suffix`` should be lists of
    `glyph-containing objects`_ .

    ``lookups`` should be a list of elements representing what lookups
    to apply at each glyph position. Each element should be a
    :class:`LookupBlock` to apply a single chaining lookup at the given
    position, a list of :class:`LookupBlock`\\ s to apply multiple
    lookups, or ``None`` to apply no lookup. The length of the outer
    list should equal the length of ``glyphs``; the inner lists can be
    of variable length."""
    lookups: Incomplete
    def __init__(self, prefix, glyphs, suffix, lookups, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder's ``add_chain_context_pos`` callback."""
    def asFea(self, indent: str = ''): ...

class ChainContextSubstStatement(Statement):
    """A chained contextual substitution statement.

    ``prefix``, ``glyphs``, and ``suffix`` should be lists of
    `glyph-containing objects`_ .

    ``lookups`` should be a list of elements representing what lookups
    to apply at each glyph position. Each element should be a
    :class:`LookupBlock` to apply a single chaining lookup at the given
    position, a list of :class:`LookupBlock`\\ s to apply multiple
    lookups, or ``None`` to apply no lookup. The length of the outer
    list should equal the length of ``glyphs``; the inner lists can be
    of variable length."""
    lookups: Incomplete
    def __init__(self, prefix, glyphs, suffix, lookups, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder's ``add_chain_context_subst`` callback."""
    def asFea(self, indent: str = ''): ...

class CursivePosStatement(Statement):
    """A cursive positioning statement. Entry and exit anchors can either
    be :class:`Anchor` objects or ``None``."""
    glyphclass: Incomplete
    def __init__(self, glyphclass, entryAnchor, exitAnchor, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_cursive_pos`` callback."""
    def asFea(self, indent: str = ''): ...

class FeatureReferenceStatement(Statement):
    """Example: ``feature salt;``"""
    def __init__(self, featureName, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_feature_reference`` callback."""
    def asFea(self, indent: str = ''): ...

class IgnorePosStatement(Statement):
    """An ``ignore pos`` statement, containing `one or more` contexts to ignore.

    ``chainContexts`` should be a list of ``(prefix, glyphs, suffix)`` tuples,
    with each of ``prefix``, ``glyphs`` and ``suffix`` being
    `glyph-containing objects`_ ."""
    chainContexts: Incomplete
    def __init__(self, chainContexts, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_chain_context_pos`` callback on each
        rule context."""
    def asFea(self, indent: str = ''): ...

class IgnoreSubstStatement(Statement):
    """An ``ignore sub`` statement, containing `one or more` contexts to ignore.

    ``chainContexts`` should be a list of ``(prefix, glyphs, suffix)`` tuples,
    with each of ``prefix``, ``glyphs`` and ``suffix`` being
    `glyph-containing objects`_ ."""
    chainContexts: Incomplete
    def __init__(self, chainContexts, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_chain_context_subst`` callback on
        each rule context."""
    def asFea(self, indent: str = ''): ...

class IncludeStatement(Statement):
    """An ``include()`` statement."""
    filename: Incomplete
    def __init__(self, filename, location: Incomplete | None = None) -> None: ...
    def build(self) -> None: ...
    def asFea(self, indent: str = ''): ...

class LanguageStatement(Statement):
    """A ``language`` statement within a feature."""
    language: Incomplete
    include_default: Incomplete
    required: Incomplete
    def __init__(self, language, include_default: bool = True, required: bool = False, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Call the builder object's ``set_language`` callback."""
    def asFea(self, indent: str = ''): ...

class LanguageSystemStatement(Statement):
    """A top-level ``languagesystem`` statement."""
    def __init__(self, script, language, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_language_system`` callback."""
    def asFea(self, indent: str = ''): ...

class FontRevisionStatement(Statement):
    """A ``head`` table ``FontRevision`` statement. ``revision`` should be a
    number, and will be formatted to three significant decimal places."""
    revision: Incomplete
    def __init__(self, revision, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = ''): ...

class LigatureCaretByIndexStatement(Statement):
    """A ``GDEF`` table ``LigatureCaretByIndex`` statement. ``glyphs`` should be
    a `glyph-containing object`_, and ``carets`` should be a list of integers."""
    def __init__(self, glyphs, carets, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_ligatureCaretByIndex_`` callback."""
    def asFea(self, indent: str = ''): ...

class LigatureCaretByPosStatement(Statement):
    """A ``GDEF`` table ``LigatureCaretByPos`` statement. ``glyphs`` should be
    a `glyph-containing object`_, and ``carets`` should be a list of integers."""
    def __init__(self, glyphs, carets, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_ligatureCaretByPos_`` callback."""
    def asFea(self, indent: str = ''): ...

class LigatureSubstStatement(Statement):
    """A chained contextual substitution statement.

    ``prefix``, ``glyphs``, and ``suffix`` should be lists of
    `glyph-containing objects`_; ``replacement`` should be a single
    `glyph-containing object`_.

    If ``forceChain`` is True, this is expressed as a chaining rule
    (e.g. ``sub f' i' by f_i``) even when no context is given."""
    def __init__(self, prefix, glyphs, suffix, replacement, forceChain, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = ''): ...

class LookupFlagStatement(Statement):
    """A ``lookupflag`` statement. The ``value`` should be an integer value
    representing the flags in use, but not including the ``markAttachment``
    class and ``markFilteringSet`` values, which must be specified as
    glyph-containing objects."""
    value: Incomplete
    markAttachment: Incomplete
    markFilteringSet: Incomplete
    def __init__(self, value: int = 0, markAttachment: Incomplete | None = None, markFilteringSet: Incomplete | None = None, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``set_lookup_flag`` callback."""
    def asFea(self, indent: str = ''): ...

class LookupReferenceStatement(Statement):
    """Represents a ``lookup ...;`` statement to include a lookup in a feature.

    The ``lookup`` should be a :class:`LookupBlock` object."""
    def __init__(self, lookup, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_lookup_call`` callback."""
    def asFea(self, indent: str = ''): ...

class MarkBasePosStatement(Statement):
    """A mark-to-base positioning rule. The ``base`` should be a
    `glyph-containing object`_. The ``marks`` should be a list of
    (:class:`Anchor`, :class:`MarkClass`) tuples."""
    def __init__(self, base, marks, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_mark_base_pos`` callback."""
    def asFea(self, indent: str = ''): ...

class MarkLigPosStatement(Statement):
    '''A mark-to-ligature positioning rule. The ``ligatures`` must be a
    `glyph-containing object`_. The ``marks`` should be a list of lists: each
    element in the top-level list represents a component glyph, and is made
    up of a list of (:class:`Anchor`, :class:`MarkClass`) tuples representing
    mark attachment points for that position.

    Example::

        m1 = MarkClass("TOP_MARKS")
        m2 = MarkClass("BOTTOM_MARKS")
        # ... add definitions to mark classes...

        glyph = GlyphName("lam_meem_jeem")
        marks = [
            [ (Anchor(625,1800), m1) ], # Attachments on 1st component (lam)
            [ (Anchor(376,-378), m2) ], # Attachments on 2nd component (meem)
            [ ]                         # No attachments on the jeem
        ]
        mlp = MarkLigPosStatement(glyph, marks)

        mlp.asFea()
        # pos ligature lam_meem_jeem <anchor 625 1800> mark @TOP_MARKS
        # ligComponent <anchor 376 -378> mark @BOTTOM_MARKS;

    '''
    def __init__(self, ligatures, marks, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_mark_lig_pos`` callback."""
    def asFea(self, indent: str = ''): ...

class MarkMarkPosStatement(Statement):
    """A mark-to-mark positioning rule. The ``baseMarks`` must be a
    `glyph-containing object`_. The ``marks`` should be a list of
    (:class:`Anchor`, :class:`MarkClass`) tuples."""
    def __init__(self, baseMarks, marks, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_mark_mark_pos`` callback."""
    def asFea(self, indent: str = ''): ...

class MultipleSubstStatement(Statement):
    """A multiple substitution statement.

    Args:
        prefix: a list of `glyph-containing objects`_.
        glyph: a single glyph-containing object.
        suffix: a list of glyph-containing objects.
        replacement: a list of glyph-containing objects.
        forceChain: If true, the statement is expressed as a chaining rule
            (e.g. ``sub f' i' by f_i``) even when no context is given.
    """
    replacement: Incomplete
    forceChain: Incomplete
    def __init__(self, prefix, glyph, suffix, replacement, forceChain: bool = False, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_multiple_subst`` callback."""
    def asFea(self, indent: str = ''): ...

class PairPosStatement(Statement):
    """A pair positioning statement.

    ``glyphs1`` and ``glyphs2`` should be `glyph-containing objects`_.
    ``valuerecord1`` should be a :class:`ValueRecord` object;
    ``valuerecord2`` should be either a :class:`ValueRecord` object or ``None``.
    If ``enumerated`` is true, then this is expressed as an
    `enumerated pair <https://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html#6.b.ii>`_.
    """
    enumerated: Incomplete
    def __init__(self, glyphs1, valuerecord1, glyphs2, valuerecord2, enumerated: bool = False, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls a callback on the builder object:

        * If the rule is enumerated, calls ``add_specific_pair_pos`` on each
          combination of first and second glyphs.
        * If the glyphs are both single :class:`GlyphName` objects, calls
          ``add_specific_pair_pos``.
        * Else, calls ``add_class_pair_pos``.
        """
    def asFea(self, indent: str = ''): ...

class ReverseChainSingleSubstStatement(Statement):
    """A reverse chaining substitution statement. You don't see those every day.

    Note the unusual argument order: ``suffix`` comes `before` ``glyphs``.
    ``old_prefix``, ``old_suffix``, ``glyphs`` and ``replacements`` should be
    lists of `glyph-containing objects`_. ``glyphs`` and ``replacements`` should
    be one-item lists.
    """
    glyphs: Incomplete
    replacements: Incomplete
    def __init__(self, old_prefix, old_suffix, glyphs, replacements, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = ''): ...

class SingleSubstStatement(Statement):
    """A single substitution statement.

    Note the unusual argument order: ``prefix`` and suffix come `after`
    the replacement ``glyphs``. ``prefix``, ``suffix``, ``glyphs`` and
    ``replace`` should be lists of `glyph-containing objects`_. ``glyphs`` and
    ``replace`` should be one-item lists.
    """
    forceChain: Incomplete
    glyphs: Incomplete
    replacements: Incomplete
    def __init__(self, glyphs, replace, prefix, suffix, forceChain, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_single_subst`` callback."""
    def asFea(self, indent: str = ''): ...

class ScriptStatement(Statement):
    """A ``script`` statement."""
    script: Incomplete
    def __init__(self, script, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder's ``set_script`` callback."""
    def asFea(self, indent: str = ''): ...

class SinglePosStatement(Statement):
    """A single position statement. ``prefix`` and ``suffix`` should be
    lists of `glyph-containing objects`_.

    ``pos`` should be a one-element list containing a (`glyph-containing object`_,
    :class:`ValueRecord`) tuple."""
    forceChain: Incomplete
    def __init__(self, pos, prefix, suffix, forceChain, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_single_pos`` callback."""
    def asFea(self, indent: str = ''): ...

class SubtableStatement(Statement):
    """Represents a subtable break."""
    def __init__(self, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder objects's ``add_subtable_break`` callback."""
    def asFea(self, indent: str = ''): ...

class ValueRecord(Expression):
    """Represents a value record."""
    vertical: Incomplete
    def __init__(self, xPlacement: Incomplete | None = None, yPlacement: Incomplete | None = None, xAdvance: Incomplete | None = None, yAdvance: Incomplete | None = None, xPlaDevice: Incomplete | None = None, yPlaDevice: Incomplete | None = None, xAdvDevice: Incomplete | None = None, yAdvDevice: Incomplete | None = None, vertical: bool = False, location: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def asFea(self, indent: str = ''): ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__

class ValueRecordDefinition(Statement):
    """Represents a named value record definition."""
    name: Incomplete
    value: Incomplete
    def __init__(self, name, value, location: Incomplete | None = None) -> None: ...
    def asFea(self, indent: str = ''): ...

class NameRecord(Statement):
    """Represents a name record. (`Section 9.e. <https://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html#9.e>`_)"""
    nameID: Incomplete
    platformID: Incomplete
    platEncID: Incomplete
    langID: Incomplete
    string: Incomplete
    def __init__(self, nameID, platformID, platEncID, langID, string, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_name_record`` callback."""
    def asFea(self, indent: str = ''): ...

class FeatureNameStatement(NameRecord):
    """Represents a ``sizemenuname`` or ``name`` statement."""
    def build(self, builder) -> None:
        """Calls the builder object's ``add_featureName`` callback."""
    def asFea(self, indent: str = ''): ...

class STATNameStatement(NameRecord):
    """Represents a STAT table ``name`` statement."""
    def asFea(self, indent: str = ''): ...

class SizeParameters(Statement):
    """A ``parameters`` statement."""
    DesignSize: Incomplete
    SubfamilyID: Incomplete
    RangeStart: Incomplete
    RangeEnd: Incomplete
    def __init__(self, DesignSize, SubfamilyID, RangeStart, RangeEnd, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``set_size_parameters`` callback."""
    def asFea(self, indent: str = ''): ...

class CVParametersNameStatement(NameRecord):
    """Represent a name statement inside a ``cvParameters`` block."""
    block_name: Incomplete
    def __init__(self, nameID, platformID, platEncID, langID, string, block_name, location: Incomplete | None = None) -> None: ...
    nameID: Incomplete
    def build(self, builder) -> None:
        """Calls the builder object's ``add_cv_parameter`` callback."""
    def asFea(self, indent: str = ''): ...

class CharacterStatement(Statement):
    """
    Statement used in cvParameters blocks of Character Variant features (cvXX).
    The Unicode value may be written with either decimal or hexadecimal
    notation. The value must be preceded by '0x' if it is a hexadecimal value.
    The largest Unicode value allowed is 0xFFFFFF.
    """
    character: Incomplete
    tag: Incomplete
    def __init__(self, character, tag, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_cv_character`` callback."""
    def asFea(self, indent: str = ''): ...

class BaseAxis(Statement):
    """An axis definition, being either a ``VertAxis.BaseTagList/BaseScriptList``
    pair or a ``HorizAxis.BaseTagList/BaseScriptList`` pair."""
    bases: Incomplete
    scripts: Incomplete
    vertical: Incomplete
    def __init__(self, bases, scripts, vertical, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``set_base_axis`` callback."""
    def asFea(self, indent: str = ''): ...

class OS2Field(Statement):
    """An entry in the ``OS/2`` table. Most ``values`` should be numbers or
    strings, apart from when the key is ``UnicodeRange``, ``CodePageRange``
    or ``Panose``, in which case it should be an array of integers."""
    key: Incomplete
    value: Incomplete
    def __init__(self, key, value, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_os2_field`` callback."""
    def asFea(self, indent: str = ''): ...

class HheaField(Statement):
    """An entry in the ``hhea`` table."""
    key: Incomplete
    value: Incomplete
    def __init__(self, key, value, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_hhea_field`` callback."""
    def asFea(self, indent: str = ''): ...

class VheaField(Statement):
    """An entry in the ``vhea`` table."""
    key: Incomplete
    value: Incomplete
    def __init__(self, key, value, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Calls the builder object's ``add_vhea_field`` callback."""
    def asFea(self, indent: str = ''): ...

class STATDesignAxisStatement(Statement):
    """A STAT table Design Axis

    Args:
        tag (str): a 4 letter axis tag
        axisOrder (int): an int
        names (list): a list of :class:`STATNameStatement` objects
    """
    tag: Incomplete
    axisOrder: Incomplete
    names: Incomplete
    location: Incomplete
    def __init__(self, tag, axisOrder, names, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = ''): ...

class ElidedFallbackName(Statement):
    """STAT table ElidedFallbackName

    Args:
        names: a list of :class:`STATNameStatement` objects
    """
    names: Incomplete
    location: Incomplete
    def __init__(self, names, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = ''): ...

class ElidedFallbackNameID(Statement):
    """STAT table ElidedFallbackNameID

    Args:
        value: an int pointing to an existing name table name ID
    """
    value: Incomplete
    location: Incomplete
    def __init__(self, value, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = ''): ...

class STATAxisValueStatement(Statement):
    """A STAT table Axis Value Record

    Args:
        names (list): a list of :class:`STATNameStatement` objects
        locations (list): a list of :class:`AxisValueLocationStatement` objects
        flags (int): an int
    """
    names: Incomplete
    locations: Incomplete
    flags: Incomplete
    def __init__(self, names, locations, flags, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, indent: str = ''): ...

class AxisValueLocationStatement(Statement):
    """
    A STAT table Axis Value Location

    Args:
        tag (str): a 4 letter axis tag
        values (list): a list of ints and/or floats
    """
    tag: Incomplete
    values: Incomplete
    def __init__(self, tag, values, location: Incomplete | None = None) -> None: ...
    def asFea(self, res: str = ''): ...

class ConditionsetStatement(Statement):
    """
    A variable layout conditionset

    Args:
        name (str): the name of this conditionset
        conditions (dict): a dictionary mapping axis tags to a
            tuple of (min,max) userspace coordinates.
    """
    name: Incomplete
    conditions: Incomplete
    def __init__(self, name, conditions, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None: ...
    def asFea(self, res: str = '', indent: str = ''): ...

class VariationBlock(Block):
    """A variation feature block, applicable in a given set of conditions."""
    def __init__(self, name, conditionset, use_extension: bool = False, location: Incomplete | None = None) -> None: ...
    def build(self, builder) -> None:
        """Call the ``start_feature`` callback on the builder object, visit
        all the statements in this feature, and then call ``end_feature``."""
    def asFea(self, indent: str = ''): ...
