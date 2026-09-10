from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen

__all__ = ['PerimeterPen']

class PerimeterPen(BasePen):
    value: int
    tolerance: Incomplete
    def __init__(self, glyphset: Incomplete | None = None, tolerance: float = 0.005) -> None: ...
