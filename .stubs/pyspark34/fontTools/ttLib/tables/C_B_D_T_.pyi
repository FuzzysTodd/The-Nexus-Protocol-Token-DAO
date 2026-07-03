from . import E_B_D_T_ as E_B_D_T_
from .BitmapGlyphMetrics import BigGlyphMetrics as BigGlyphMetrics, SmallGlyphMetrics as SmallGlyphMetrics, bigGlyphMetricsFormat as bigGlyphMetricsFormat, smallGlyphMetricsFormat as smallGlyphMetricsFormat
from .E_B_D_T_ import BitmapGlyph as BitmapGlyph, BitmapPlusBigMetricsMixin as BitmapPlusBigMetricsMixin, BitmapPlusSmallMetricsMixin as BitmapPlusSmallMetricsMixin
from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.textTools import bytesjoin as bytesjoin

class table_C_B_D_T_(E_B_D_T_.table_E_B_D_T_):
    locatorName: str
    def getImageFormatClass(self, imageFormat): ...

class ColorBitmapGlyph(BitmapGlyph):
    fileExtension: str
    xmlDataFunctions: Incomplete

class cbdt_bitmap_format_17(BitmapPlusSmallMetricsMixin, ColorBitmapGlyph):
    metrics: Incomplete
    imageData: Incomplete
    def decompile(self) -> None: ...
    def compile(self, ttFont): ...

class cbdt_bitmap_format_18(BitmapPlusBigMetricsMixin, ColorBitmapGlyph):
    metrics: Incomplete
    imageData: Incomplete
    def decompile(self) -> None: ...
    def compile(self, ttFont): ...

class cbdt_bitmap_format_19(ColorBitmapGlyph):
    imageData: Incomplete
    def decompile(self) -> None: ...
    def compile(self, ttFont): ...

cbdt_bitmap_classes: Incomplete
