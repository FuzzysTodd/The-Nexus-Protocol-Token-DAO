import fontTools.ttLib.tables.TupleVariation as tv
from . import DefaultTable as DefaultTable
from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.lazyTools import LazyDict as LazyDict
from fontTools.misc.textTools import safeEval as safeEval
from functools import partial as partial

log: Incomplete
TupleVariation = tv.TupleVariation
GVAR_HEADER_FORMAT: str
GVAR_HEADER_SIZE: Incomplete

class table__g_v_a_r(DefaultTable.DefaultTable):
    dependencies: Incomplete
    variations: Incomplete
    def __init__(self, tag: Incomplete | None = None) -> None: ...
    def compile(self, ttFont): ...
    def compileGlyphs_(self, ttFont, axisTags, sharedCoordIndices): ...
    def decompile(self, data, ttFont): ...
    def ensureDecompiled(self, recurse: bool = False) -> None: ...
    @staticmethod
    def decompileOffsets_(data, tableFormat, glyphCount): ...
    @staticmethod
    def compileOffsets_(offsets):
        """Packs a list of offsets into a 'gvar' offset table.

        Returns a pair (bytestring, tableFormat). Bytestring is the
        packed offset table. Format indicates whether the table
        uses short (tableFormat=0) or long (tableFormat=1) integers.
        The returned tableFormat should get packed into the flags field
        of the 'gvar' header.
        """
    def toXML(self, writer, ttFont) -> None: ...
    version: Incomplete
    reserved: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    @staticmethod
    def getNumPoints_(glyph): ...

def compileGlyph_(variations, pointCount, axisTags, sharedCoordIndices): ...
def decompileGlyph_(pointCount, sharedTuples, axisTags, data): ...
