from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen

__all__ = ['CocoaPen']

class CocoaPen(BasePen):
    path: Incomplete
    def __init__(self, glyphSet, path: Incomplete | None = None) -> None: ...
