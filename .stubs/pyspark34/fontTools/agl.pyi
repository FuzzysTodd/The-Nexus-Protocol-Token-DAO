from _typeshed import Incomplete
from fontTools.misc.textTools import tostr as tostr

class AGLError(Exception): ...

LEGACY_AGL2UV: Incomplete
AGL2UV: Incomplete
UV2AGL: Incomplete

def toUnicode(glyph, isZapfDingbats: bool = False):
    """Convert glyph names to Unicode, such as ``'longs_t.oldstyle'`` --> ``u'ſt'``

    If ``isZapfDingbats`` is ``True``, the implementation recognizes additional
    glyph names (as required by the AGL specification).
    """
