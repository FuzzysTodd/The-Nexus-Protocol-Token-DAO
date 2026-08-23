from . import DefaultTable as DefaultTable
from _typeshed import Incomplete
from fontTools import ttLib as ttLib
from fontTools.misc import sstruct as sstruct
from fontTools.misc.encodingTools import getEncoding as getEncoding
from fontTools.misc.textTools import bytechr as bytechr, byteord as byteord, bytesjoin as bytesjoin, safeEval as safeEval, strjoin as strjoin, tobytes as tobytes, tostr as tostr
from fontTools.ttLib import newTable as newTable
from fontTools.ttLib.tables import C_P_A_L_ as C_P_A_L_
from fontTools.ttLib.ttVisitor import TTVisitor as TTVisitor

log: Incomplete
nameRecordFormat: str
nameRecordSize: Incomplete

class table__n_a_m_e(DefaultTable.DefaultTable):
    dependencies: Incomplete
    names: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    def getName(self, nameID, platformID, platEncID, langID: Incomplete | None = None): ...
    def getDebugName(self, nameID): ...
    def getFirstDebugName(self, nameIDs): ...
    def getBestFamilyName(self): ...
    def getBestSubFamilyName(self): ...
    def getBestFullName(self): ...
    def setName(self, string, nameID, platformID, platEncID, langID) -> None:
        """Set the 'string' for the name record identified by 'nameID', 'platformID',
        'platEncID' and 'langID'. If a record with that nameID doesn't exist, create it
        and append to the name table.

        'string' can be of type `str` (`unicode` in PY2) or `bytes`. In the latter case,
        it is assumed to be already encoded with the correct plaform-specific encoding
        identified by the (platformID, platEncID, langID) triplet. A warning is issued
        to prevent unexpected results.
        """
    def removeNames(self, nameID: Incomplete | None = None, platformID: Incomplete | None = None, platEncID: Incomplete | None = None, langID: Incomplete | None = None) -> None:
        """Remove any name records identified by the given combination of 'nameID',
        'platformID', 'platEncID' and 'langID'.
        """
    @staticmethod
    def removeUnusedNames(ttFont):
        """Remove any name records which are not in NameID range 0-255 and not utilized
        within the font itself."""
    def findMultilingualName(self, names, windows: bool = True, mac: bool = True, minNameID: int = 0, ttFont: Incomplete | None = None):
        """Return the name ID of an existing multilingual name that
        matches the 'names' dictionary, or None if not found.

        'names' is a dictionary with the name in multiple languages,
        such as {'en': 'Pale', 'de': 'Blaß', 'de-CH': 'Blass'}.
        The keys can be arbitrary IETF BCP 47 language codes;
        the values are Unicode strings.

        If 'windows' is True, the returned name ID is guaranteed
        exist for all requested languages for platformID=3 and
        platEncID=1.
        If 'mac' is True, the returned name ID is guaranteed to exist
        for all requested languages for platformID=1 and platEncID=0.

        The returned name ID will not be less than the 'minNameID'
        argument.
        """
    def addMultilingualName(self, names, ttFont: Incomplete | None = None, nameID: Incomplete | None = None, windows: bool = True, mac: bool = True, minNameID: int = 0):
        """Add a multilingual name, returning its name ID

        'names' is a dictionary with the name in multiple languages,
        such as {'en': 'Pale', 'de': 'Blaß', 'de-CH': 'Blass'}.
        The keys can be arbitrary IETF BCP 47 language codes;
        the values are Unicode strings.

        'ttFont' is the TTFont to which the names are added, or None.
        If present, the font's 'ltag' table can get populated
        to store exotic language codes, which allows encoding
        names that otherwise cannot get encoded at all.

        'nameID' is the name ID to be used, or None to let the library
        find an existing set of name records that match, or pick an
        unused name ID.

        If 'windows' is True, a platformID=3 name record will be added.
        If 'mac' is True, a platformID=1 name record will be added.

        If the 'nameID' argument is None, the created nameID will not
        be less than the 'minNameID' argument.
        """
    def addName(self, string, platforms=((1, 0, 0), (3, 1, 1033)), minNameID: int = 255):
        """Add a new name record containing 'string' for each (platformID, platEncID,
        langID) tuple specified in the 'platforms' list.

        The nameID is assigned in the range between 'minNameID'+1 and 32767 (inclusive),
        following the last nameID in the name table.
        If no 'platforms' are specified, two English name records are added, one for the
        Macintosh (platformID=0), and one for the Windows platform (3).

        The 'string' must be a Unicode string, so it can be encoded with different,
        platform-specific encodings.

        Return the new nameID.
        """

def makeName(string, nameID, platformID, platEncID, langID): ...

class NameRecord:
    def getEncoding(self, default: str = 'ascii'):
        """Returns the Python encoding name for this name entry based on its platformID,
        platEncID, and langID.  If encoding for these values is not known, by default
        'ascii' is returned.  That can be overriden by passing a value to the default
        argument.
        """
    def encodingIsUnicodeCompatible(self): ...
    def isUnicode(self): ...
    def toUnicode(self, errors: str = 'strict'):
        """
        If self.string is a Unicode string, return it; otherwise try decoding the
        bytes in self.string to a Unicode string using the encoding of this
        entry as returned by self.getEncoding(); Note that  self.getEncoding()
        returns 'ascii' if the encoding is unknown to the library.

        Certain heuristics are performed to recover data from bytes that are
        ill-formed in the chosen encoding, or that otherwise look misencoded
        (mostly around bad UTF-16BE encoded bytes, or bytes that look like UTF-16BE
        but marked otherwise).  If the bytes are ill-formed and the heuristics fail,
        the error is handled according to the errors parameter to this function, which is
        passed to the underlying decode() function; by default it throws a
        UnicodeDecodeError exception.

        Note: The mentioned heuristics mean that roundtripping a font to XML and back
        to binary might recover some misencoded data whereas just loading the font
        and saving it back will not change them.
        """
    def toBytes(self, errors: str = 'strict'):
        """If self.string is a bytes object, return it; otherwise try encoding
        the Unicode string in self.string to bytes using the encoding of this
        entry as returned by self.getEncoding(); Note that self.getEncoding()
        returns 'ascii' if the encoding is unknown to the library.

        If the Unicode string cannot be encoded to bytes in the chosen encoding,
        the error is handled according to the errors parameter to this function,
        which is passed to the underlying encode() function; by default it throws a
        UnicodeEncodeError exception.
        """
    toStr = toUnicode
    def toXML(self, writer, ttFont) -> None: ...
    nameID: Incomplete
    platformID: Incomplete
    platEncID: Incomplete
    langID: Incomplete
    string: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    def __lt__(self, other): ...

class NameRecordVisitor(TTVisitor):
    TABLES: Incomplete
    seen: Incomplete
    def __init__(self) -> None: ...
