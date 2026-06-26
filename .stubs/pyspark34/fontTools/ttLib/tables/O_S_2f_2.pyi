from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.roundTools import otRound as otRound
from fontTools.misc.textTools import binary2num as binary2num, num2binary as num2binary, safeEval as safeEval
from fontTools.ttLib.tables import DefaultTable as DefaultTable

log: Incomplete
panoseFormat: str

class Panose:
    def __init__(self, **kwargs) -> None: ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

OS2_format_0: str
OS2_format_1_addition: str
OS2_format_2_addition: Incomplete
OS2_format_5_addition: Incomplete
bigendian: str
OS2_format_1: Incomplete
OS2_format_2: Incomplete
OS2_format_5: Incomplete

class table_O_S_2f_2(DefaultTable.DefaultTable):
    """the OS/2 table"""
    dependencies: Incomplete
    panose: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    usFirstCharIndex: Incomplete
    usLastCharIndex: Incomplete
    def updateFirstAndLastCharIndex(self, ttFont) -> None: ...
    @property
    def usMaxContex(self): ...
    usMaxContext: Incomplete
    @usMaxContex.setter
    def usMaxContex(self, value) -> None: ...
    @property
    def fsFirstCharIndex(self): ...
    @fsFirstCharIndex.setter
    def fsFirstCharIndex(self, value) -> None: ...
    @property
    def fsLastCharIndex(self): ...
    @fsLastCharIndex.setter
    def fsLastCharIndex(self, value) -> None: ...
    def getUnicodeRanges(self):
        """Return the set of 'ulUnicodeRange*' bits currently enabled."""
    def setUnicodeRanges(self, bits) -> None:
        """Set the 'ulUnicodeRange*' fields to the specified 'bits'."""
    def recalcUnicodeRanges(self, ttFont, pruneOnly: bool = False):
        """Intersect the codepoints in the font's Unicode cmap subtables with
        the Unicode block ranges defined in the OpenType specification (v1.7),
        and set the respective 'ulUnicodeRange*' bits if there is at least ONE
        intersection.
        If 'pruneOnly' is True, only clear unused bits with NO intersection.
        """
    def getCodePageRanges(self):
        """Return the set of 'ulCodePageRange*' bits currently enabled."""
    version: int
    def setCodePageRanges(self, bits) -> None:
        """Set the 'ulCodePageRange*' fields to the specified 'bits'."""
    def recalcCodePageRanges(self, ttFont, pruneOnly: bool = False): ...
    xAvgCharWidth: Incomplete
    def recalcAvgCharWidth(self, ttFont):
        """Recalculate xAvgCharWidth using metrics from ttFont's 'hmtx' table.

        Set it to 0 if the unlikely event 'hmtx' table is not found.
        """

OS2_UNICODE_RANGES: Incomplete

def intersectUnicodeRanges(unicodes, inverse: bool = False):
    """Intersect a sequence of (int) Unicode codepoints with the Unicode block
    ranges defined in the OpenType specification v1.7, and return the set of
    'ulUnicodeRanges' bits for which there is at least ONE intersection.
    If 'inverse' is True, return the the bits for which there is NO intersection.

    >>> intersectUnicodeRanges([0x0410]) == {9}
    True
    >>> intersectUnicodeRanges([0x0410, 0x1F000]) == {9, 57, 122}
    True
    >>> intersectUnicodeRanges([0x0410, 0x1F000], inverse=True) == (
    ...     set(range(len(OS2_UNICODE_RANGES))) - {9, 57, 122})
    True
    """
def calcCodePageRanges(unicodes):
    """Given a set of Unicode codepoints (integers), calculate the
    corresponding OS/2 CodePage range bits.
    This is a direct translation of FontForge implementation:
    https://github.com/fontforge/fontforge/blob/7b2c074/fontforge/tottf.c#L3158
    """
