from .base import Attrs, BaseStyle
from _typeshed import Incomplete
from enum import Enum
from typing import Hashable

__all__ = ['Style', 'parse_color', 'Priority', 'merge_styles']

def parse_color(text: str) -> str:
    """
    Parse/validate color format.

    Like in Pygments, but also support the ANSI color names.
    (These will map to the colors of the 16 color palette.)
    """

class Priority(Enum):
    """
    The priority of the rules, when a style is created from a dictionary.

    In a `Style`, rules that are defined later will always override previous
    defined rules, however in a dictionary, the key order was arbitrary before
    Python 3.6. This means that the style could change at random between rules.

    We have two options:

    - `DICT_KEY_ORDER`: This means, iterate through the dictionary, and take
       the key/value pairs in order as they come. This is a good option if you
       have Python >3.6. Rules at the end will override rules at the beginning.
    - `MOST_PRECISE`: keys that are defined with most precision will get higher
      priority. (More precise means: more elements.)
    """
    DICT_KEY_ORDER: str
    MOST_PRECISE: str

class Style(BaseStyle):
    """
    Create a ``Style`` instance from a list of style rules.

    The `style_rules` is supposed to be a list of ('classnames', 'style') tuples.
    The classnames are a whitespace separated string of class names and the
    style string is just like a Pygments style definition, but with a few
    additions: it supports 'reverse' and 'blink'.

    Later rules always override previous rules.

    Usage::

        Style([
            ('title', '#ff0000 bold underline'),
            ('something-else', 'reverse'),
            ('class1 class2', 'reverse'),
        ])

    The ``from_dict`` classmethod is similar, but takes a dictionary as input.
    """
    class_names_and_attrs: Incomplete
    def __init__(self, style_rules: list[tuple[str, str]]) -> None: ...
    @property
    def style_rules(self) -> list[tuple[str, str]]: ...
    @classmethod
    def from_dict(cls, style_dict: dict[str, str], priority: Priority = ...) -> Style:
        """
        :param style_dict: Style dictionary.
        :param priority: `Priority` value.
        """
    def get_attrs_for_style_str(self, style_str: str, default: Attrs = ...) -> Attrs:
        """
        Get `Attrs` for the given style string.
        """
    def invalidation_hash(self) -> Hashable: ...

def merge_styles(styles: list[BaseStyle]) -> _MergedStyle:
    """
    Merge multiple `Style` objects.
    """

class _MergedStyle(BaseStyle):
    """
    Merge multiple `Style` objects into one.
    This is supposed to ensure consistency: if any of the given styles changes,
    then this style will be updated.
    """
    styles: Incomplete
    def __init__(self, styles: list[BaseStyle]) -> None: ...
    @property
    def style_rules(self) -> list[tuple[str, str]]: ...
    def get_attrs_for_style_str(self, style_str: str, default: Attrs = ...) -> Attrs: ...
    def invalidation_hash(self) -> Hashable: ...
