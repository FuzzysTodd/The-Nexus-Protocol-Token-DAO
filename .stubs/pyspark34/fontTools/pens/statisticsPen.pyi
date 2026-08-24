from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen
from fontTools.pens.momentsPen import MomentsPen

__all__ = ['StatisticsPen', 'StatisticsControlPen']

class StatisticsBase:
    def __init__(self) -> None: ...

class StatisticsPen(StatisticsBase, MomentsPen):
    """Pen calculating area, center of mass, variance and
    standard-deviation, covariance and correlation, and slant,
    of glyph shapes.

    Note that if the glyph shape is self-intersecting, the values
    are not correct (but well-defined). Moreover, area will be
    negative if contour directions are clockwise."""
    def __init__(self, glyphset: Incomplete | None = None) -> None: ...

class StatisticsControlPen(StatisticsBase, BasePen):
    """Pen calculating area, center of mass, variance and
    standard-deviation, covariance and correlation, and slant,
    of glyph shapes, using the control polygon only.

    Note that if the glyph shape is self-intersecting, the values
    are not correct (but well-defined). Moreover, area will be
    negative if contour directions are clockwise."""
    def __init__(self, glyphset: Incomplete | None = None) -> None: ...
