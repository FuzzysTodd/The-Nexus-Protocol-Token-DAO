from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen

__all__ = ['MomentsPen']

class MomentsPen(BasePen):
    area: int
    momentX: int
    momentY: int
    momentXX: int
    momentXY: int
    momentYY: int
    def __init__(self, glyphset: Incomplete | None = None) -> None: ...
