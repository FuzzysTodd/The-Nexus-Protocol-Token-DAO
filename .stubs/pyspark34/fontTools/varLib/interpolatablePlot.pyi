from .interpolatableHelpers import *
from _typeshed import Incomplete
from fontTools.pens.boundsPen import ControlBoundsPen as ControlBoundsPen
from fontTools.pens.cairoPen import CairoPen as CairoPen
from fontTools.pens.pointPen import PointToSegmentPen as PointToSegmentPen, ReverseContourPointPen as ReverseContourPointPen, SegmentToPointPen as SegmentToPointPen
from fontTools.pens.recordingPen import DecomposingRecordingPen as DecomposingRecordingPen, RecordingPen as RecordingPen, RecordingPointPen as RecordingPointPen
from fontTools.ttLib import TTFont as TTFont
from fontTools.ttLib.ttGlyphSet import LerpGlyphSet as LerpGlyphSet
from fontTools.varLib.interpolatableHelpers import PerContourOrComponentPen as PerContourOrComponentPen, SimpleRecordingPointPen as SimpleRecordingPointPen
from functools import wraps as wraps

log: Incomplete

class OverridingDict(dict):
    parent_dict: Incomplete
    def __init__(self, parent_dict) -> None: ...
    def __missing__(self, key): ...

class InterpolatablePlot:
    width: Incomplete
    height: Incomplete
    pad: Incomplete
    title_font_size: int
    font_size: int
    page_number: int
    head_color: Incomplete
    label_color: Incomplete
    border_color: Incomplete
    border_width: float
    fill_color: Incomplete
    stroke_color: Incomplete
    stroke_width: int
    oncurve_node_color: Incomplete
    oncurve_node_diameter: int
    offcurve_node_color: Incomplete
    offcurve_node_diameter: int
    handle_color: Incomplete
    handle_width: float
    corrected_start_point_color: Incomplete
    corrected_start_point_size: int
    wrong_start_point_color: Incomplete
    start_point_color: Incomplete
    start_arrow_length: int
    kink_point_size: int
    kink_point_color: Incomplete
    kink_circle_size: int
    kink_circle_stroke_width: int
    kink_circle_color: Incomplete
    contour_colors: Incomplete
    contour_alpha: float
    weight_issue_contour_color: Incomplete
    no_issues_label: str
    no_issues_label_color: Incomplete
    cupcake_color: Incomplete
    cupcake: str
    emoticon_color: Incomplete
    shrug: str
    underweight: str
    overweight: str
    yay: str
    out: Incomplete
    glyphsets: Incomplete
    names: Incomplete
    toc: Incomplete
    panel_width: Incomplete
    panel_height: Incomplete
    def __init__(self, out, glyphsets, names: Incomplete | None = None, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def show_page(self) -> None: ...
    def add_title_page(self, files, *, show_tolerance: bool = True, tolerance: Incomplete | None = None, kinkiness: Incomplete | None = None) -> None: ...
    def draw_legend(self, *, show_tolerance: bool = True, tolerance: Incomplete | None = None, kinkiness: Incomplete | None = None) -> None: ...
    def add_summary(self, problems): ...
    def add_table_of_contents(self) -> None: ...
    def add_index(self): ...
    def add_problems(self, problems, *, show_tolerance: bool = True, show_page_number: bool = True) -> None: ...
    def add_problem(self, glyphname, problems, *, show_tolerance: bool = True, show_page_number: bool = True) -> None: ...
    def draw_label(self, label, *, x: int = 0, y: int = 0, color=(0, 0, 0), align: int = 0, bold: bool = False, width: Incomplete | None = None, height: Incomplete | None = None, font_size: Incomplete | None = None) -> None: ...
    def draw_glyph(self, glyphset, glyphname, problems, which, *, x: int = 0, y: int = 0, scale: Incomplete | None = None): ...
    def draw_dot(self, cr, *, x: int = 0, y: int = 0, color=(0, 0, 0), diameter: int = 10) -> None: ...
    def draw_circle(self, cr, *, x: int = 0, y: int = 0, color=(0, 0, 0), diameter: int = 10, stroke_width: int = 1) -> None: ...
    def draw_arrow(self, cr, *, x: int = 0, y: int = 0, color=(0, 0, 0)) -> None: ...
    def draw_text(self, text, *, x: int = 0, y: int = 0, color=(0, 0, 0), width: Incomplete | None = None, height: Incomplete | None = None) -> None: ...
    def draw_cupcake(self) -> None: ...
    def draw_emoticon(self, emoticon, x: int = 0, y: int = 0) -> None: ...

class InterpolatablePostscriptLike(InterpolatablePlot):
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def show_page(self) -> None: ...

class InterpolatablePS(InterpolatablePostscriptLike):
    surface: Incomplete
    def __enter__(self): ...

class InterpolatablePDF(InterpolatablePostscriptLike):
    surface: Incomplete
    def __enter__(self): ...

class InterpolatableSVG(InterpolatablePlot):
    sink: Incomplete
    surface: Incomplete
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def show_page(self) -> None: ...
