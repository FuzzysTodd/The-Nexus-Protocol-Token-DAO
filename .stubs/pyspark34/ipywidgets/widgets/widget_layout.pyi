from .._version import __jupyter_widgets_base_version__ as __jupyter_widgets_base_version__
from .widget import Widget as Widget, register as register
from _typeshed import Incomplete
from traitlets import Instance, validate as validate

CSS_PROPERTIES: Incomplete

class Layout(Widget):
    """Layout specification

    Defines a layout that can be expressed using CSS.  Supports a subset of
    https://developer.mozilla.org/en-US/docs/Web/CSS/Reference

    When a property is also accessible via a shorthand property, we only
    expose the shorthand.

    For example:
    - ``flex-grow``, ``flex-shrink`` and ``flex-basis`` are bound to ``flex``.
    - ``flex-wrap`` and ``flex-direction`` are bound to ``flex-flow``.
    - ``margin-[top/bottom/left/right]`` values are bound to ``margin``, etc.
    """
    align_content: Incomplete
    align_items: Incomplete
    align_self: Incomplete
    border_top: Incomplete
    border_right: Incomplete
    border_bottom: Incomplete
    border_left: Incomplete
    bottom: Incomplete
    display: Incomplete
    flex: Incomplete
    flex_flow: Incomplete
    height: Incomplete
    justify_content: Incomplete
    justify_items: Incomplete
    left: Incomplete
    margin: Incomplete
    max_height: Incomplete
    max_width: Incomplete
    min_height: Incomplete
    min_width: Incomplete
    overflow: Incomplete
    order: Incomplete
    padding: Incomplete
    right: Incomplete
    top: Incomplete
    visibility: Incomplete
    width: Incomplete
    object_fit: Incomplete
    object_position: Incomplete
    grid_auto_columns: Incomplete
    grid_auto_flow: Incomplete
    grid_auto_rows: Incomplete
    grid_gap: Incomplete
    grid_template_rows: Incomplete
    grid_template_columns: Incomplete
    grid_template_areas: Incomplete
    grid_row: Incomplete
    grid_column: Incomplete
    grid_area: Incomplete
    def __init__(self, **kwargs) -> None: ...
    border: Incomplete

class LayoutTraitType(Instance):
    klass = Layout
    def validate(self, obj, value): ...
