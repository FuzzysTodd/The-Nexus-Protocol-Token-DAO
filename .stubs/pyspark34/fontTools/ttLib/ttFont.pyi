from _typeshed import Incomplete
from fontTools.config import Config as Config
from fontTools.misc import xmlWriter as xmlWriter
from fontTools.misc.configTools import AbstractConfig as AbstractConfig
from fontTools.misc.loggingTools import deprecateArgument as deprecateArgument
from fontTools.misc.textTools import Tag as Tag, byteord as byteord, tostr as tostr
from fontTools.ttLib import TTLibError as TTLibError
from fontTools.ttLib.sfnt import SFNTReader as SFNTReader, SFNTWriter as SFNTWriter

log: Incomplete

class TTFont:
    '''Represents a TrueType font.

    The object manages file input and output, and offers a convenient way of
    accessing tables. Tables will be only decompiled when necessary, ie. when
    they\'re actually accessed. This means that simple operations can be extremely fast.

    Example usage::

            >> from fontTools import ttLib
            >> tt = ttLib.TTFont("afont.ttf") # Load an existing font file
            >> tt[\'maxp\'].numGlyphs
            242
            >> tt[\'OS/2\'].achVendID
            \'B&H\x00\'
            >> tt[\'head\'].unitsPerEm
            2048

    For details of the objects returned when accessing each table, see :ref:`tables`.
    To add a table to the font, use the :py:func:`newTable` function::

            >> os2 = newTable("OS/2")
            >> os2.version = 4
            >> # set other attributes
            >> font["OS/2"] = os2

    TrueType fonts can also be serialized to and from XML format (see also the
    :ref:`ttx` binary)::

            >> tt.saveXML("afont.ttx")
            Dumping \'LTSH\' table...
            Dumping \'OS/2\' table...
            [...]

            >> tt2 = ttLib.TTFont() # Create a new font object
            >> tt2.importXML("afont.ttx")
            >> tt2[\'maxp\'].numGlyphs
            242

    The TTFont object may be used as a context manager; this will cause the file
    reader to be closed after the context ``with`` block is exited::

            with TTFont(filename) as f:
                    # Do stuff

    Args:
            file: When reading a font from disk, either a pathname pointing to a file,
                    or a readable file object.
            res_name_or_index: If running on a Macintosh, either a sfnt resource name or
                    an sfnt resource index number. If the index number is zero, TTLib will
                    autodetect whether the file is a flat file or a suitcase. (If it is a suitcase,
                    only the first \'sfnt\' resource will be read.)
            sfntVersion (str): When constructing a font object from scratch, sets the four-byte
                    sfnt magic number to be used. Defaults to ``\x00\x01\x00\x00`` (TrueType). To create
                    an OpenType file, use ``OTTO``.
            flavor (str): Set this to ``woff`` when creating a WOFF file or ``woff2`` for a WOFF2
                    file.
            checkChecksums (int): How checksum data should be treated. Default is 0
                    (no checking). Set to 1 to check and warn on wrong checksums; set to 2 to
                    raise an exception if any wrong checksums are found.
            recalcBBoxes (bool): If true (the default), recalculates ``glyf``, ``CFF ``,
                    ``head`` bounding box values and ``hhea``/``vhea`` min/max values on save.
                    Also compiles the glyphs on importing, which saves memory consumption and
                    time.
            ignoreDecompileErrors (bool): If true, exceptions raised during table decompilation
                    will be ignored, and the binary data will be returned for those tables instead.
            recalcTimestamp (bool): If true (the default), sets the ``modified`` timestamp in
                    the ``head`` table on save.
            fontNumber (int): The index of the font in a TrueType Collection file.
            lazy (bool): If lazy is set to True, many data structures are loaded lazily, upon
                    access only. If it is set to False, many data structures are loaded immediately.
                    The default is ``lazy=None`` which is somewhere in between.
    '''
    lazy: Incomplete
    recalcBBoxes: Incomplete
    recalcTimestamp: Incomplete
    tables: Incomplete
    reader: Incomplete
    cfg: Incomplete
    ignoreDecompileErrors: Incomplete
    sfntVersion: Incomplete
    flavor: Incomplete
    flavorData: Incomplete
    def __init__(self, file: Incomplete | None = None, res_name_or_index: Incomplete | None = None, sfntVersion: str = '\x00\x01\x00\x00', flavor: Incomplete | None = None, checkChecksums: int = 0, verbose: Incomplete | None = None, recalcBBoxes: bool = True, allowVID=..., ignoreDecompileErrors: bool = False, recalcTimestamp: bool = True, fontNumber: int = -1, lazy: Incomplete | None = None, quiet: Incomplete | None = None, _tableCache: Incomplete | None = None, cfg={}) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def close(self) -> None:
        """If we still have a reader object, close it."""
    def save(self, file, reorderTables: bool = True) -> None:
        """Save the font to disk.

        Args:
                file: Similarly to the constructor, can be either a pathname or a writable
                        file object.
                reorderTables (Option[bool]): If true (the default), reorder the tables,
                        sorting them by tag (recommended by the OpenType specification). If
                        false, retain the original font order. If None, reorder by table
                        dependency (fastest).
        """
    def saveXML(self, fileOrPath, newlinestr: str = '\n', **kwargs) -> None:
        """Export the font as TTX (an XML-based text file), or as a series of text
        files when splitTables is true. In the latter case, the 'fileOrPath'
        argument should be a path to a directory.
        The 'tables' argument must either be false (dump all tables) or a
        list of tables to dump. The 'skipTables' argument may be a list of tables
        to skip, but only when the 'tables' argument is false.
        """
    def importXML(self, fileOrPath, quiet: Incomplete | None = None) -> None:
        """Import a TTX file (an XML-based text format), so as to recreate
        a font object.
        """
    def isLoaded(self, tag):
        """Return true if the table identified by ``tag`` has been
        decompiled and loaded into memory."""
    def has_key(self, tag):
        """Test if the table identified by ``tag`` is present in the font.

        As well as this method, ``tag in font`` can also be used to determine the
        presence of the table."""
    __contains__ = has_key
    def keys(self):
        """Returns the list of tables in the font, along with the ``GlyphOrder`` pseudo-table."""
    def ensureDecompiled(self, recurse: Incomplete | None = None) -> None:
        """Decompile all the tables, even if a TTFont was opened in 'lazy' mode."""
    def __len__(self) -> int: ...
    def __getitem__(self, tag): ...
    def __setitem__(self, tag, table) -> None: ...
    def __delitem__(self, tag) -> None: ...
    def get(self, tag, default: Incomplete | None = None):
        """Returns the table if it exists or (optionally) a default if it doesn't."""
    glyphOrder: Incomplete
    def setGlyphOrder(self, glyphOrder) -> None:
        """Set the glyph order

        Args:
                glyphOrder ([str]): List of glyph names in order.
        """
    def getGlyphOrder(self):
        """Returns a list of glyph names ordered by their position in the font."""
    def getGlyphNames(self):
        """Get a list of glyph names, sorted alphabetically."""
    def getGlyphNames2(self):
        """Get a list of glyph names, sorted alphabetically,
        but not case sensitive.
        """
    def getGlyphName(self, glyphID):
        """Returns the name for the glyph with the given ID.

        If no name is available, synthesises one with the form ``glyphXXXXX``` where
        ```XXXXX`` is the zero-padded glyph ID.
        """
    def getGlyphNameMany(self, lst):
        """Converts a list of glyph IDs into a list of glyph names."""
    def getGlyphID(self, glyphName):
        """Returns the ID of the glyph with the given name."""
    def getGlyphIDMany(self, lst):
        """Converts a list of glyph names into a list of glyph IDs."""
    def getReverseGlyphMap(self, rebuild: bool = False):
        """Returns a mapping of glyph names to glyph IDs."""
    def getTableData(self, tag):
        """Returns the binary representation of a table.

        If the table is currently loaded and in memory, the data is compiled to
        binary and returned; if it is not currently loaded, the binary data is
        read from the font file and returned.
        """
    def getGlyphSet(self, preferCFF: bool = True, location: Incomplete | None = None, normalized: bool = False, recalcBounds: bool = True):
        """Return a generic GlyphSet, which is a dict-like object
        mapping glyph names to glyph objects. The returned glyph objects
        have a ``.draw()`` method that supports the Pen protocol, and will
        have an attribute named 'width'.

        If the font is CFF-based, the outlines will be taken from the ``CFF ``
        or ``CFF2`` tables. Otherwise the outlines will be taken from the
        ``glyf`` table.

        If the font contains both a ``CFF ``/``CFF2`` and a ``glyf`` table, you
        can use the ``preferCFF`` argument to specify which one should be taken.
        If the font contains both a ``CFF `` and a ``CFF2`` table, the latter is
        taken.

        If the ``location`` parameter is set, it should be a dictionary mapping
        four-letter variation tags to their float values, and the returned
        glyph-set will represent an instance of a variable font at that
        location.

        If the ``normalized`` variable is set to True, that location is
        interpreted as in the normalized (-1..+1) space, otherwise it is in the
        font's defined axes space.
        """
    def normalizeLocation(self, location):
        """Normalize a ``location`` from the font's defined axes space (also
        known as user space) into the normalized (-1..+1) space. It applies
        ``avar`` mapping if the font contains an ``avar`` table.

        The ``location`` parameter should be a dictionary mapping four-letter
        variation tags to their float values.

        Raises ``TTLibError`` if the font is not a variable font.
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
    def reorderGlyphs(self, new_glyph_order) -> None: ...

class GlyphOrder:
    """A pseudo table. The glyph order isn't in the font as a separate
    table, but it's nice to present it as such in the TTX format.
    """
    def __init__(self, tag: Incomplete | None = None) -> None: ...
    def toXML(self, writer, ttFont) -> None: ...
    glyphOrder: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

def getTableModule(tag):
    """Fetch the packer/unpacker module for a table.
    Return None when no module is found.
    """
def registerCustomTableClass(tag, moduleName, className: Incomplete | None = None) -> None:
    """Register a custom packer/unpacker class for a table.

    The 'moduleName' must be an importable module. If no 'className'
    is given, it is derived from the tag, for example it will be
    ``table_C_U_S_T_`` for a 'CUST' tag.

    The registered table class should be a subclass of
    :py:class:`fontTools.ttLib.tables.DefaultTable.DefaultTable`
    """
def unregisterCustomTableClass(tag) -> None:
    """Unregister the custom packer/unpacker class for a table."""
def getCustomTableClass(tag):
    """Return the custom table class for tag, if one has been registered
    with 'registerCustomTableClass()'. Else return None.
    """
def getTableClass(tag):
    """Fetch the packer/unpacker class for a table."""
def getClassTag(klass):
    """Fetch the table tag for a class object."""
def newTable(tag):
    """Return a new instance of a table."""
def tagToIdentifier(tag):
    """Convert a table tag to a valid (but UGLY) python identifier,
    as well as a filename that's guaranteed to be unique even on a
    caseless file system. Each character is mapped to two characters.
    Lowercase letters get an underscore before the letter, uppercase
    letters get an underscore after the letter. Trailing spaces are
    trimmed. Illegal characters are escaped as two hex bytes. If the
    result starts with a number (as the result of a hex escape), an
    extra underscore is prepended. Examples::

            >>> tagToIdentifier('glyf')
            '_g_l_y_f'
            >>> tagToIdentifier('cvt ')
            '_c_v_t'
            >>> tagToIdentifier('OS/2')
            'O_S_2f_2'
    """
def identifierToTag(ident):
    """the opposite of tagToIdentifier()"""
def tagToXML(tag):
    """Similarly to tagToIdentifier(), this converts a TT tag
    to a valid XML element name. Since XML element names are
    case sensitive, this is a fairly simple/readable translation.
    """
def xmlToTag(tag):
    """The opposite of tagToXML()"""

TTFTableOrder: Incomplete
OTFTableOrder: Incomplete

def sortedTagList(tagList, tableOrder: Incomplete | None = None):
    """Return a sorted copy of tagList, sorted according to the OpenType
    specification, or according to a custom tableOrder. If given and not
    None, tableOrder needs to be a list of tag names.
    """
def reorderFontTables(inFile, outFile, tableOrder: Incomplete | None = None, checkChecksums: bool = False) -> None:
    """Rewrite a font file, ordering the tables as recommended by the
    OpenType specification 1.4.
    """
def maxPowerOfTwo(x):
    """Return the highest exponent of two, so that
    (2 ** exponent) <= x.  Return 0 if x is 0.
    """
def getSearchRange(n, itemSize: int = 16):
    """Calculate searchRange, entrySelector, rangeShift."""
