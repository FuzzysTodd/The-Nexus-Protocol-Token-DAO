from .arc import EllipticalArc as EllipticalArc
from _typeshed import Incomplete

COMMANDS: Incomplete
ARC_COMMANDS: Incomplete
UPPERCASE: Incomplete
COMMAND_RE: Incomplete
FLOAT_RE: Incomplete
BOOL_RE: Incomplete
SEPARATOR_RE: Incomplete
ARC_ARGUMENT_TYPES: Incomplete

def parse_path(pathdef, pen, current_pos=(0, 0), arc_class=...) -> None:
    '''Parse SVG path definition (i.e. "d" attribute of <path> elements)
    and call a \'pen\' object\'s moveTo, lineTo, curveTo, qCurveTo and closePath
    methods.

    If \'current_pos\' (2-float tuple) is provided, the initial moveTo will
    be relative to that instead being absolute.

    If the pen has an "arcTo" method, it is called with the original values
    of the elliptical arc curve commands:

        pen.arcTo(rx, ry, rotation, arc_large, arc_sweep, (x, y))

    Otherwise, the arcs are approximated by series of cubic Bezier segments
    ("curveTo"), one every 90 degrees.
    '''
