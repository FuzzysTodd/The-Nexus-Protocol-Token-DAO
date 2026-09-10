from . import DefaultTable as DefaultTable, grUtils as grUtils
from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.fixedTools import floatToFixedToStr as floatToFixedToStr
from fontTools.misc.textTools import safeEval as safeEval

Feat_hdr_format: str

class table_F__e_a_t(DefaultTable.DefaultTable):
    """The ``Feat`` table is used exclusively by the Graphite shaping engine
    to store features and possible settings specified in GDL. Graphite features
    determine what rules are applied to transform a glyph stream.

    Not to be confused with ``feat``, or the OpenType Layout tables
    ``GSUB``/``GPOS``."""
    features: Incomplete
    def __init__(self, tag: Incomplete | None = None) -> None: ...
    version: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont): ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...

class Feature: ...
