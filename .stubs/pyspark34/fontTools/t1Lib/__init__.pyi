from _typeshed import Incomplete
from fontTools.encodings.StandardEncoding import StandardEncoding as StandardEncoding
from fontTools.misc import eexec as eexec
from fontTools.misc.macCreatorType import getMacCreatorAndType as getMacCreatorAndType
from fontTools.misc.textTools import bytechr as bytechr, byteord as byteord, bytesjoin as bytesjoin, tobytes as tobytes

__version__: str
DEBUG: int
haveMacSupport: int

class T1Error(Exception): ...

class T1Font:
    """Type 1 font class.

    Uses a minimal interpeter that supports just about enough PS to parse
    Type 1 fonts.
    """
    data: Incomplete
    encoding: Incomplete
    def __init__(self, path, encoding: str = 'ascii', kind: Incomplete | None = None) -> None: ...
    def saveAs(self, path, type, dohex: bool = False) -> None: ...
    def getData(self): ...
    def getGlyphSet(self):
        """Return a generic GlyphSet, which is a dict-like object
        mapping glyph names to glyph objects. The returned glyph objects
        have a .draw() method that supports the Pen protocol, and will
        have an attribute named 'width', but only *after* the .draw() method
        has been called.

        In the case of Type 1, the GlyphSet is simply the CharStrings dict.
        """
    def __getitem__(self, key): ...
    font: Incomplete
    def parse(self) -> None: ...
    def createData(self): ...
    def encode_eexec(self, eexec_dict): ...

def read(path, onlyHeader: bool = False):
    """reads any Type 1 font file, returns raw data"""
def write(path, data, kind: str = 'OTHER', dohex: bool = False) -> None: ...

LWFNCHUNKSIZE: int
HEXLINELENGTH: int

def readLWFN(path, onlyHeader: bool = False):
    """reads an LWFN font file, returns raw data"""
def readPFB(path, onlyHeader: bool = False):
    """reads a PFB font file, returns raw data"""
def readOther(path):
    """reads any (font) file, returns raw data"""
def writeLWFN(path, data) -> None: ...
def writePFB(path, data) -> None: ...
def writeOther(path, data, dohex: bool = False) -> None: ...

EEXECBEGIN: bytes
EEXECEND: Incomplete
EEXECINTERNALEND: bytes
EEXECBEGINMARKER: bytes
EEXECENDMARKER: bytes

def isHex(text): ...
def decryptType1(data): ...
def findEncryptedChunks(data): ...
def deHexString(hexstring): ...
def assertType1(data): ...
def longToString(long): ...
def stringToLong(s): ...

font_dictionary_keys: Incomplete
FontInfo_dictionary_keys: Incomplete
Private_dictionary_keys: Incomplete
hintothers: str
std_subrs: Incomplete
eexec_IV: bytes
char_IV: bytes
RD_value: Incomplete
ND_values: Incomplete
PD_values: Incomplete
