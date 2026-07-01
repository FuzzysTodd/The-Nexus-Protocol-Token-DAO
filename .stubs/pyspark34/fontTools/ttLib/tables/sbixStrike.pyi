from .sbixGlyph import Glyph as Glyph
from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.textTools import safeEval as safeEval

sbixStrikeHeaderFormat: str
sbixGlyphDataOffsetFormat: str
sbixStrikeHeaderFormatSize: Incomplete
sbixGlyphDataOffsetFormatSize: Incomplete

class Strike:
    data: Incomplete
    ppem: Incomplete
    resolution: Incomplete
    glyphs: Incomplete
    def __init__(self, rawdata: Incomplete | None = None, ppem: int = 0, resolution: int = 72) -> None: ...
    numGlyphs: Incomplete
    glyphDataOffsets: Incomplete
    def decompile(self, ttFont) -> None: ...
    bitmapData: bytes
    def compile(self, ttFont) -> None: ...
    def toXML(self, xmlWriter, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
