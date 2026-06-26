from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.textTools import readHex as readHex, safeEval as safeEval

sbixGlyphHeaderFormat: str
sbixGlyphHeaderFormatSize: Incomplete

class Glyph:
    gid: Incomplete
    glyphName: Incomplete
    referenceGlyphName: Incomplete
    originOffsetX: Incomplete
    originOffsetY: Incomplete
    rawdata: Incomplete
    graphicType: Incomplete
    imageData: Incomplete
    def __init__(self, glyphName: Incomplete | None = None, referenceGlyphName: Incomplete | None = None, originOffsetX: int = 0, originOffsetY: int = 0, graphicType: Incomplete | None = None, imageData: Incomplete | None = None, rawdata: Incomplete | None = None, gid: int = 0) -> None: ...
    def is_reference_type(self):
        """Returns True if this glyph is a reference to another glyph's image data."""
    def decompile(self, ttFont) -> None: ...
    def compile(self, ttFont) -> None: ...
    def toXML(self, xmlWriter, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
