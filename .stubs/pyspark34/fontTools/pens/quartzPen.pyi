from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen

__all__ = ['QuartzPen']

class QuartzPen(BasePen):
    """A pen that creates a CGPath

    Parameters
    - path: an optional CGPath to add to
    - xform: an optional CGAffineTransform to apply to the path
    """
    path: Incomplete
    xform: Incomplete
    def __init__(self, glyphSet, path: Incomplete | None = None, xform: Incomplete | None = None) -> None: ...
