from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen

__all__ = ['CairoPen']

class CairoPen(BasePen):
    """Pen to draw to a Cairo graphics library context."""
    context: Incomplete
    def __init__(self, glyphSet, context) -> None: ...
