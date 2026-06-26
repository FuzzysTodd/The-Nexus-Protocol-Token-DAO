from . import DefaultTable as DefaultTable
from _typeshed import Incomplete
from fontTools.misc.textTools import strjoin as strjoin, tobytes as tobytes, tostr as tostr

class asciiTable(DefaultTable.DefaultTable):
    def toXML(self, writer, ttFont) -> None: ...
    data: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
