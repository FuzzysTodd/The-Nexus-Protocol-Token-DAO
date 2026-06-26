from . import DefaultTable as DefaultTable
from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.arrayTools import intRect as intRect, unionRect as unionRect
from fontTools.misc.fixedTools import floatToFixedToStr as floatToFixedToStr, strToFixedToFloat as strToFixedToFloat
from fontTools.misc.textTools import binary2num as binary2num, num2binary as num2binary, safeEval as safeEval
from fontTools.misc.timeTools import timestampFromString as timestampFromString, timestampNow as timestampNow, timestampToString as timestampToString

log: Incomplete
headFormat: str

class table__h_e_a_d(DefaultTable.DefaultTable):
    dependencies: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    modified: Incomplete
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
