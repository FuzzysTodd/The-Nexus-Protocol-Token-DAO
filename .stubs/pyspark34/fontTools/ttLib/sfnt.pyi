from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.textTools import Tag as Tag
from fontTools.ttLib import TTLibError as TTLibError, TTLibFileIsCollectionError as TTLibFileIsCollectionError

log: Incomplete

class SFNTReader:
    def __new__(cls, *args, **kwargs):
        """Return an instance of the SFNTReader sub-class which is compatible
        with the input file type.
        """
    file: Incomplete
    checkChecksums: Incomplete
    flavor: Incomplete
    flavorData: Incomplete
    DirectoryEntry: Incomplete
    sfntVersion: Incomplete
    numFonts: Incomplete
    tables: Incomplete
    def __init__(self, file, checkChecksums: int = 0, fontNumber: int = -1) -> None: ...
    def has_key(self, tag): ...
    __contains__ = has_key
    def keys(self): ...
    def __getitem__(self, tag):
        """Fetch the raw table data."""
    def __delitem__(self, tag) -> None: ...
    def close(self) -> None: ...

ZLIB_COMPRESSION_LEVEL: int
USE_ZOPFLI: bool
ZOPFLI_LEVELS: Incomplete

def compress(data, level=...):
    """Compress 'data' to Zlib format. If 'USE_ZOPFLI' variable is True,
    zopfli is used instead of the zlib module.
    The compression 'level' must be between 0 and 9. 1 gives best speed,
    9 gives best compression (0 gives no compression at all).
    The default value is a compromise between speed and compression (6).
    """

class SFNTWriter:
    def __new__(cls, *args, **kwargs):
        """Return an instance of the SFNTWriter sub-class which is compatible
        with the specified 'flavor'.
        """
    file: Incomplete
    numTables: Incomplete
    sfntVersion: Incomplete
    flavor: Incomplete
    flavorData: Incomplete
    directoryFormat: Incomplete
    directorySize: Incomplete
    DirectoryEntry: Incomplete
    signature: str
    origNextTableOffset: Incomplete
    directoryOffset: Incomplete
    nextTableOffset: Incomplete
    tables: Incomplete
    def __init__(self, file, numTables, sfntVersion: str = '\x00\x01\x00\x00', flavor: Incomplete | None = None, flavorData: Incomplete | None = None) -> None: ...
    def setEntry(self, tag, entry) -> None: ...
    headTable: Incomplete
    def __setitem__(self, tag, data) -> None:
        """Write raw table data to disk."""
    def __getitem__(self, tag): ...
    reserved: int
    totalSfntSize: int
    majorVersion: Incomplete
    minorVersion: Incomplete
    metaOrigLength: Incomplete
    metaOffset: Incomplete
    metaLength: Incomplete
    privOffset: Incomplete
    privLength: Incomplete
    length: Incomplete
    def close(self) -> None:
        """All tables must have been written to disk. Now write the
        directory.
        """
    def writeMasterChecksum(self, directory) -> None: ...
    def reordersTables(self): ...

ttcHeaderFormat: str
ttcHeaderSize: Incomplete
sfntDirectoryFormat: str
sfntDirectorySize: Incomplete
sfntDirectoryEntryFormat: str
sfntDirectoryEntrySize: Incomplete
woffDirectoryFormat: str
woffDirectorySize: Incomplete
woffDirectoryEntryFormat: str
woffDirectoryEntrySize: Incomplete

class DirectoryEntry:
    uncompressed: bool
    def __init__(self) -> None: ...
    def fromFile(self, file) -> None: ...
    def fromString(self, str) -> None: ...
    def toString(self): ...
    def loadData(self, file): ...
    length: Incomplete
    def saveData(self, file, data) -> None: ...
    def decodeData(self, rawData): ...
    def encodeData(self, data): ...

class SFNTDirectoryEntry(DirectoryEntry):
    format = sfntDirectoryEntryFormat
    formatSize = sfntDirectoryEntrySize

class WOFFDirectoryEntry(DirectoryEntry):
    format = woffDirectoryEntryFormat
    formatSize = woffDirectoryEntrySize
    zlibCompressionLevel: Incomplete
    def __init__(self) -> None: ...
    def decodeData(self, rawData): ...
    origLength: Incomplete
    length: Incomplete
    def encodeData(self, data): ...

class WOFFFlavorData:
    Flavor: str
    majorVersion: Incomplete
    minorVersion: Incomplete
    metaData: Incomplete
    privData: Incomplete
    def __init__(self, reader: Incomplete | None = None) -> None: ...

def calcChecksum(data):
    '''Calculate the checksum for an arbitrary block of data.

    If the data length is not a multiple of four, it assumes
    it is to be padded with null byte.

            >>> print(calcChecksum(b"abcd"))
            1633837924
            >>> print(calcChecksum(b"abcdxyz"))
            3655064932
    '''
def readTTCHeader(file): ...
def writeTTCHeader(file, numFonts): ...
