from . import DefaultTable as DefaultTable
from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.textTools import safeEval as safeEval

maxpFormat_0_5: str
maxpFormat_1_0_add: str

class table__m_a_x_p(DefaultTable.DefaultTable):
    dependencies: Incomplete
    numGlyphs: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    tableVersion: int
    def compile(self, ttFont): ...
    maxPoints: Incomplete
    maxContours: Incomplete
    maxCompositePoints: Incomplete
    maxCompositeContours: Incomplete
    maxComponentElements: Incomplete
    maxComponentDepth: Incomplete
    def recalc(self, ttFont) -> None:
        """Recalculate the font bounding box, and most other maxp values except
        for the TT instructions values. Also recalculate the value of bit 1
        of the flags field and the font bounding box of the 'head' table.
        """
    def testrepr(self) -> None: ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
