from . import DefaultTable as DefaultTable
from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.textTools import safeEval as safeEval, tobytes as tobytes, tostr as tostr

GMAPFormat: str
GMAPRecordFormat1: str

class GMAPRecord:
    UV: Incomplete
    cid: Incomplete
    gid: Incomplete
    ggid: Incomplete
    name: Incomplete
    def __init__(self, uv: int = 0, cid: int = 0, gid: int = 0, ggid: int = 0, name: str = '') -> None: ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    def compile(self, ttFont): ...

class table_G_M_A_P_(DefaultTable.DefaultTable):
    dependencies: Incomplete
    psFontName: Incomplete
    gmapRecords: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    recordsCount: Incomplete
    fontNameLength: Incomplete
    recordsOffset: Incomplete
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
