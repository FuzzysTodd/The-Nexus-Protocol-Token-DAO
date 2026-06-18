from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen

__all__ = ['ReportLabPen']

class ReportLabPen(BasePen):
    """A pen for drawing onto a ``reportlab.graphics.shapes.Path`` object."""
    path: Incomplete
    def __init__(self, glyphSet, path: Incomplete | None = None) -> None: ...
