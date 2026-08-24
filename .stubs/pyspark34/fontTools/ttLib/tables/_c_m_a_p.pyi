from . import DefaultTable as DefaultTable
from _typeshed import Incomplete
from fontTools.misc.encodingTools import getEncoding as getEncoding
from fontTools.misc.textTools import bytesjoin as bytesjoin, readHex as readHex, safeEval as safeEval
from fontTools.ttLib import getSearchRange as getSearchRange
from fontTools.unicode import Unicode as Unicode

log: Incomplete

class table__c_m_a_p(DefaultTable.DefaultTable):
    '''Character to Glyph Index Mapping Table

    This class represents the `cmap <https://docs.microsoft.com/en-us/typography/opentype/spec/cmap>`_
    table, which maps between input characters (in Unicode or other system encodings)
    and glyphs within the font. The ``cmap`` table contains one or more subtables
    which determine the mapping of of characters to glyphs across different platforms
    and encoding systems.

    ``table__c_m_a_p`` objects expose an accessor ``.tables`` which provides access
    to the subtables, although it is normally easier to retrieve individual subtables
    through the utility methods described below. To add new subtables to a font,
    first determine the subtable format (if in doubt use format 4 for glyphs within
    the BMP, format 12 for glyphs outside the BMP, and format 14 for Unicode Variation
    Sequences) construct subtable objects with ``CmapSubtable.newSubtable(format)``,
    and append them to the ``.tables`` list.

    Within a subtable, the mapping of characters to glyphs is provided by the ``.cmap``
    attribute.

    Example::

            cmap4_0_3 = CmapSubtable.newSubtable(4)
            cmap4_0_3.platformID = 0
            cmap4_0_3.platEncID = 3
            cmap4_0_3.language = 0
            cmap4_0_3.cmap = { 0xC1: "Aacute" }

            cmap = newTable("cmap")
            cmap.tableVersion = 0
            cmap.tables = [cmap4_0_3]
    '''
    def getcmap(self, platformID, platEncID):
        """Returns the first subtable which matches the given platform and encoding.

        Args:
                platformID (int): The platform ID. Use 0 for Unicode, 1 for Macintosh
                        (deprecated for new fonts), 2 for ISO (deprecated) and 3 for Windows.
                encodingID (int): Encoding ID. Interpretation depends on the platform ID.
                        See the OpenType specification for details.

        Returns:
                An object which is a subclass of :py:class:`CmapSubtable` if a matching
                subtable is found within the font, or ``None`` otherwise.
        """
    def getBestCmap(self, cmapPreferences=((3, 10), (0, 6), (0, 4), (3, 1), (0, 3), (0, 2), (0, 1), (0, 0))):
        """Returns the 'best' Unicode cmap dictionary available in the font
        or ``None``, if no Unicode cmap subtable is available.

        By default it will search for the following (platformID, platEncID)
        pairs in order::

                        (3, 10), # Windows Unicode full repertoire
                        (0, 6),  # Unicode full repertoire (format 13 subtable)
                        (0, 4),  # Unicode 2.0 full repertoire
                        (3, 1),  # Windows Unicode BMP
                        (0, 3),  # Unicode 2.0 BMP
                        (0, 2),  # Unicode ISO/IEC 10646
                        (0, 1),  # Unicode 1.1
                        (0, 0)   # Unicode 1.0

        This particular order matches what HarfBuzz uses to choose what
        subtable to use by default. This order prefers the largest-repertoire
        subtable, and among those, prefers the Windows-platform over the
        Unicode-platform as the former has wider support.

        This order can be customized via the ``cmapPreferences`` argument.
        """
    def buildReversed(self):
        """Builds a reverse mapping dictionary

        Iterates over all Unicode cmap tables and returns a dictionary mapping
        glyphs to sets of codepoints, such as::

                {
                        'one': {0x31}
                        'A': {0x41,0x391}
                }

        The values are sets of Unicode codepoints because
        some fonts map different codepoints to the same glyph.
        For example, ``U+0041 LATIN CAPITAL LETTER A`` and ``U+0391
        GREEK CAPITAL LETTER ALPHA`` are sometimes the same glyph.
        """
    tableVersion: Incomplete
    tables: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def ensureDecompiled(self, recurse: bool = False) -> None: ...
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

class CmapSubtable:
    """Base class for all cmap subtable formats.

    Subclasses which handle the individual subtable formats are named
    ``cmap_format_0``, ``cmap_format_2`` etc. Use :py:meth:`getSubtableClass`
    to retrieve the concrete subclass, or :py:meth:`newSubtable` to get a
    new subtable object for a given format.

    The object exposes a ``.cmap`` attribute, which contains a dictionary mapping
    character codepoints to glyph names.
    """
    @staticmethod
    def getSubtableClass(format):
        """Return the subtable class for a format."""
    @staticmethod
    def newSubtable(format):
        """Return a new instance of a subtable for the given format
        ."""
    format: Incomplete
    data: Incomplete
    ttFont: Incomplete
    platformID: Incomplete
    platEncID: Incomplete
    language: Incomplete
    def __init__(self, format) -> None: ...
    def ensureDecompiled(self, recurse: bool = False) -> None: ...
    def __getattr__(self, attr): ...
    length: Incomplete
    def decompileHeader(self, data, ttFont) -> None: ...
    def toXML(self, writer, ttFont) -> None: ...
    def getEncoding(self, default: Incomplete | None = None):
        '''Returns the Python encoding name for this cmap subtable based on its platformID,
        platEncID, and language.  If encoding for these values is not known, by default
        ``None`` is returned.  That can be overridden by passing a value to the ``default``
        argument.

        Note that if you want to choose a "preferred" cmap subtable, most of the time
        ``self.isUnicode()`` is what you want as that one only returns true for the modern,
        commonly used, Unicode-compatible triplets, not the legacy ones.
        '''
    def isUnicode(self):
        """Returns true if the characters are interpreted as Unicode codepoints."""
    def isSymbol(self):
        """Returns true if the subtable is for the Symbol encoding (3,0)"""
    def __lt__(self, other): ...

class cmap_format_0(CmapSubtable):
    cmap: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    language: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

subHeaderFormat: str

class SubHeader:
    firstCode: Incomplete
    entryCount: Incomplete
    idDelta: Incomplete
    idRangeOffset: Incomplete
    glyphIndexArray: Incomplete
    def __init__(self) -> None: ...

class cmap_format_2(CmapSubtable):
    def setIDDelta(self, subHeader) -> None: ...
    data: bytes
    cmap: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    language: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

cmap_format_4_format: str

def splitRange(startCode, endCode, cmap): ...

class cmap_format_4(CmapSubtable):
    data: Incomplete
    cmap: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    language: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

class cmap_format_6(CmapSubtable):
    data: Incomplete
    cmap: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    language: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

class cmap_format_12_or_13(CmapSubtable):
    format: Incomplete
    reserved: int
    data: Incomplete
    ttFont: Incomplete
    def __init__(self, format) -> None: ...
    length: Incomplete
    language: Incomplete
    nGroups: Incomplete
    def decompileHeader(self, data, ttFont) -> None: ...
    cmap: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

class cmap_format_12(cmap_format_12_or_13):
    def __init__(self, format: int = 12) -> None: ...

class cmap_format_13(cmap_format_12_or_13):
    def __init__(self, format: int = 13) -> None: ...

def cvtToUVS(threeByteString): ...
def cvtFromUVS(val): ...

class cmap_format_14(CmapSubtable):
    data: Incomplete
    length: Incomplete
    numVarSelectorRecords: Incomplete
    ttFont: Incomplete
    language: int
    def decompileHeader(self, data, ttFont) -> None: ...
    cmap: Incomplete
    uvsDict: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def toXML(self, writer, ttFont): ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    def compile(self, ttFont): ...

class cmap_format_unknown(CmapSubtable):
    def toXML(self, writer, ttFont) -> None: ...
    data: Incomplete
    cmap: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    language: int
    def decompileHeader(self, data, ttFont) -> None: ...
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...

cmap_classes: Incomplete
