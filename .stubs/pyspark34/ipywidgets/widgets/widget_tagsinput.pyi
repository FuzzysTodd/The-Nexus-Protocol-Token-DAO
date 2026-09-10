from .trait_types import Color as Color, NumberFormat as NumberFormat
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionWidget as DescriptionWidget
from _typeshed import Incomplete

class TagsInputBase(DescriptionWidget, ValueWidget, CoreWidget):
    value: Incomplete
    placeholder: Incomplete
    allowed_tags: Incomplete
    allow_duplicates: Incomplete

class TagsInput(TagsInputBase):
    """
    List of string tags
    """
    value: Incomplete
    tag_style: Incomplete

class ColorsInput(TagsInputBase):
    """
    List of color tags
    """
    value: Incomplete

class NumbersInputBase(TagsInput):
    min: Incomplete
    max: Incomplete

class FloatsInput(NumbersInputBase):
    """
    List of float tags
    """
    value: Incomplete
    format: Incomplete

class IntsInput(NumbersInputBase):
    """
    List of int tags
    """
    value: Incomplete
    format: Incomplete
    min: Incomplete
    max: Incomplete
