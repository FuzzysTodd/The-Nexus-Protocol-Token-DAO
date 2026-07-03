from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.arrayTools import calcIntBounds as calcIntBounds
from fontTools.misc.textTools import Tag as Tag, bytechr as bytechr, byteord as byteord, bytesjoin as bytesjoin, pad as pad
from fontTools.ttLib import TTFont as TTFont, TTLibError as TTLibError, getSearchRange as getSearchRange, getTableClass as getTableClass, getTableModule as getTableModule
from fontTools.ttLib.sfnt import DirectoryEntry as DirectoryEntry, SFNTDirectoryEntry as SFNTDirectoryEntry, SFNTReader as SFNTReader, SFNTWriter as SFNTWriter, WOFFFlavorData as WOFFFlavorData, calcChecksum as calcChecksum, sfntDirectoryEntrySize as sfntDirectoryEntrySize, sfntDirectoryFormat as sfntDirectoryFormat, sfntDirectorySize as sfntDirectorySize
from fontTools.ttLib.tables import ttProgram as ttProgram

log: Incomplete
haveBrotli: bool

class WOFF2Reader(SFNTReader):
    flavor: str
    file: Incomplete
    DirectoryEntry: Incomplete
    tables: Incomplete
    transformBuffer: Incomplete
    flavorData: Incomplete
    ttFont: Incomplete
    def __init__(self, file, checkChecksums: int = 0, fontNumber: int = -1) -> None: ...
    def __getitem__(self, tag):
        """Fetch the raw table data. Reconstruct transformed tables."""
    def reconstructTable(self, tag):
        """Reconstruct table named 'tag' from transformed data."""

class WOFF2Writer(SFNTWriter):
    flavor: str
    file: Incomplete
    numTables: Incomplete
    sfntVersion: Incomplete
    flavorData: Incomplete
    directoryFormat: Incomplete
    directorySize: Incomplete
    DirectoryEntry: Incomplete
    signature: Incomplete
    nextTableOffset: int
    transformBuffer: Incomplete
    tables: Incomplete
    ttFont: Incomplete
    def __init__(self, file, numTables, sfntVersion: str = '\x00\x01\x00\x00', flavor: Incomplete | None = None, flavorData: Incomplete | None = None) -> None: ...
    def __setitem__(self, tag, data) -> None:
        """Associate new entry named 'tag' with raw table data."""
    totalSfntSize: Incomplete
    totalCompressedSize: Incomplete
    length: Incomplete
    reserved: int
    def close(self) -> None:
        """All tags must have been specified. Now write the table data and directory."""
    def transformTable(self, tag):
        """Return transformed table data, or None if some pre-conditions aren't
        met -- in which case, the non-transformed table data will be used.
        """
    def writeMasterChecksum(self) -> None:
        """Write checkSumAdjustment to the transformBuffer."""
    def reordersTables(self): ...

woff2DirectoryFormat: str
woff2DirectorySize: Incomplete
woff2KnownTags: Incomplete
woff2FlagsFormat: str
woff2FlagsSize: Incomplete
woff2UnknownTagFormat: str
woff2UnknownTagSize: Incomplete
woff2UnknownTagIndex: int
woff2Base128MaxSize: int
woff2DirectoryEntryMaxSize: Incomplete
woff2TransformedTableTags: Incomplete
woff2GlyfTableFormat: str
woff2GlyfTableFormatSize: Incomplete
bboxFormat: str
woff2OverlapSimpleBitmapFlag: int

def getKnownTagIndex(tag):
    """Return index of 'tag' in woff2KnownTags list. Return 63 if not found."""

class WOFF2DirectoryEntry(DirectoryEntry):
    def fromFile(self, file) -> None: ...
    tag: Incomplete
    length: Incomplete
    def fromString(self, data): ...
    def toString(self): ...
    @property
    def transformVersion(self):
        """Return bits 6-7 of table entry's flags, which indicate the preprocessing
        transformation version number (between 0 and 3).
        """
    @transformVersion.setter
    def transformVersion(self, value) -> None: ...
    @property
    def transformed(self):
        """Return True if the table has any transformation, else return False."""
    @transformed.setter
    def transformed(self, booleanValue) -> None: ...

class WOFF2LocaTable(Incomplete):
    """Same as parent class. The only difference is that it attempts to preserve
    the 'indexFormat' as encoded in the WOFF2 glyf table.
    """
    tableTag: Incomplete
    def __init__(self, tag: Incomplete | None = None) -> None: ...
    def compile(self, ttFont): ...

class WOFF2GlyfTable(Incomplete):
    """Decoder/Encoder for WOFF2 'glyf' table transform."""
    subStreams: Incomplete
    tableTag: Incomplete
    def __init__(self, tag: Incomplete | None = None) -> None: ...
    overlapSimpleBitmap: Incomplete
    bboxBitmap: Incomplete
    bboxStream: Incomplete
    nContourStream: Incomplete
    glyphOrder: Incomplete
    def reconstruct(self, data, ttFont) -> None:
        """Decompile transformed 'glyf' data."""
    numGlyphs: Incomplete
    indexFormat: Incomplete
    version: int
    optionFlags: int
    def transform(self, ttFont):
        """Return transformed 'glyf' data"""

class WOFF2HmtxTable(Incomplete):
    tableTag: Incomplete
    def __init__(self, tag: Incomplete | None = None) -> None: ...
    metrics: Incomplete
    def reconstruct(self, data, ttFont) -> None: ...
    def transform(self, ttFont): ...

class WOFF2FlavorData(WOFFFlavorData):
    Flavor: str
    majorVersion: Incomplete
    metaData: Incomplete
    privData: Incomplete
    transformedTables: Incomplete
    def __init__(self, reader: Incomplete | None = None, data: Incomplete | None = None, transformedTables: Incomplete | None = None) -> None:
        """Data class that holds the WOFF2 header major/minor version, any
        metadata or private data (as bytes strings), and the set of
        table tags that have transformations applied (if reader is not None),
        or will have once the WOFF2 font is compiled.

        Args:
                reader: an SFNTReader (or subclass) object to read flavor data from.
                data: another WOFFFlavorData object to initialise data from.
                transformedTables: set of strings containing table tags to be transformed.

        Raises:
                ImportError if the brotli module is not installed.

        NOTE: The 'reader' argument, on the one hand, and the 'data' and
        'transformedTables' arguments, on the other hand, are mutually exclusive.
        """

def unpackBase128(data):
    '''Read one to five bytes from UIntBase128-encoded input string, and return
    a tuple containing the decoded integer plus any leftover data.

    >>> unpackBase128(b\'\\x3f\\x00\\x00\') == (63, b"\\x00\\x00")
    True
    >>> unpackBase128(b\'\\x8f\\xff\\xff\\xff\\x7f\')[0] == 4294967295
    True
    >>> unpackBase128(b\'\\x80\\x80\\x3f\')  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    TTLibError: UIntBase128 value must not start with leading zeros
    >>> unpackBase128(b\'\\x8f\\xff\\xff\\xff\\xff\\x7f\')[0]  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    TTLibError: UIntBase128-encoded sequence is longer than 5 bytes
    >>> unpackBase128(b\'\\x90\\x80\\x80\\x80\\x00\')[0]  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    TTLibError: UIntBase128 value exceeds 2**32-1
    '''
def base128Size(n):
    """Return the length in bytes of a UIntBase128-encoded sequence with value n.

    >>> base128Size(0)
    1
    >>> base128Size(24567)
    3
    >>> base128Size(2**32-1)
    5
    """
def packBase128(n):
    '''Encode unsigned integer in range 0 to 2**32-1 (inclusive) to a string of
    bytes using UIntBase128 variable-length encoding. Produce the shortest possible
    encoding.

    >>> packBase128(63) == b"\\x3f"
    True
    >>> packBase128(2**32-1) == b\'\\x8f\\xff\\xff\\xff\\x7f\'
    True
    '''
def unpack255UShort(data):
    '''Read one to three bytes from 255UInt16-encoded input string, and return a
    tuple containing the decoded integer plus any leftover data.

    >>> unpack255UShort(bytechr(252))[0]
    252

    Note that some numbers (e.g. 506) can have multiple encodings:
    >>> unpack255UShort(struct.pack("BB", 254, 0))[0]
    506
    >>> unpack255UShort(struct.pack("BB", 255, 253))[0]
    506
    >>> unpack255UShort(struct.pack("BBB", 253, 1, 250))[0]
    506
    '''
def pack255UShort(value):
    """Encode unsigned integer in range 0 to 65535 (inclusive) to a bytestring
    using 255UInt16 variable-length encoding.

    >>> pack255UShort(252) == b'\\xfc'
    True
    >>> pack255UShort(506) == b'\\xfe\\x00'
    True
    >>> pack255UShort(762) == b'\\xfd\\x02\\xfa'
    True
    """
def compress(input_file, output_file, transform_tables: Incomplete | None = None) -> None:
    """Compress OpenType font to WOFF2.

    Args:
            input_file: a file path, file or file-like object (open in binary mode)
                    containing an OpenType font (either CFF- or TrueType-flavored).
            output_file: a file path, file or file-like object where to save the
                    compressed WOFF2 font.
            transform_tables: Optional[Iterable[str]]: a set of table tags for which
                    to enable preprocessing transformations. By default, only 'glyf'
                    and 'loca' tables are transformed. An empty set means disable all
                    transformations.
    """
def decompress(input_file, output_file) -> None:
    """Decompress WOFF2 font to OpenType font.

    Args:
            input_file: a file path, file or file-like object (open in binary mode)
                    containing a compressed WOFF2 font.
            output_file: a file path, file or file-like object where to save the
                    decompressed OpenType font.
    """
def main(args: Incomplete | None = None) -> None:
    """Compress and decompress WOFF2 fonts"""
