from _typeshed import Incomplete
from fontTools.misc.roundTools import otRound as otRound

class Circle:
    centre: Incomplete
    radius: Incomplete
    def __init__(self, centre, radius) -> None: ...
    def round(self): ...
    def inside(self, outer_circle, tolerance=...): ...
    def concentric(self, other): ...
    def move(self, dx, dy) -> None: ...

def round_start_circle_stable_containment(c0, r0, c1, r1):
    """Round start circle so that it stays inside/outside end circle after rounding.

    The rounding of circle coordinates to integers may cause an abrupt change
    if the start circle c0 is so close to the end circle c1's perimiter that
    it ends up falling outside (or inside) as a result of the rounding.
    To keep the gradient unchanged, we nudge it in the right direction.

    See:
    https://github.com/googlefonts/colr-gradients-spec/issues/204
    https://github.com/googlefonts/picosvg/issues/158
    """
