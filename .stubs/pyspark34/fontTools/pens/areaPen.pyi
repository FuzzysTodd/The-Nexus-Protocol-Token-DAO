from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen

__all__ = ['AreaPen']

class AreaPen(BasePen):
    value: int
    def __init__(self, glyphset: Incomplete | None = None) -> None: ...
