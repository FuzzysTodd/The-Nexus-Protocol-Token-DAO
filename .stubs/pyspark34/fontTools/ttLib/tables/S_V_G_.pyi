from . import DefaultTable as DefaultTable
from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from fontTools.misc import sstruct as sstruct
from fontTools.misc.textTools import bytesjoin as bytesjoin, safeEval as safeEval, strjoin as strjoin, tobytes as tobytes, tostr as tostr

log: Incomplete
SVG_format_0: str
SVG_format_0Size: Incomplete
doc_index_entry_format_0: str
doc_index_entry_format_0Size: Incomplete

class table_S_V_G_(DefaultTable.DefaultTable):
    docList: Incomplete
    numEntries: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

class DocumentIndexEntry:
    startGlyphID: Incomplete
    endGlyphID: Incomplete
    svgDocOffset: Incomplete
    svgDocLength: Incomplete
    def __init__(self) -> None: ...

@dataclass
class SVGDocument(Sequence):
    data: str
    startGlyphID: int
    endGlyphID: int
    compressed: bool = ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...
    def __init__(self, data, startGlyphID, endGlyphID, compressed) -> None: ...
