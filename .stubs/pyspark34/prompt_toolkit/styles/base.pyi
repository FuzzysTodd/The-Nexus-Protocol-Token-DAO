import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from typing import Callable, Hashable, NamedTuple

__all__ = ['Attrs', 'DEFAULT_ATTRS', 'ANSI_COLOR_NAMES', 'ANSI_COLOR_NAMES_ALIASES', 'BaseStyle', 'DummyStyle', 'DynamicStyle']

class Attrs(NamedTuple):
    color: str | None
    bgcolor: str | None
    bold: bool | None
    underline: bool | None
    strike: bool | None
    italic: bool | None
    blink: bool | None
    reverse: bool | None
    hidden: bool | None

DEFAULT_ATTRS: Incomplete
ANSI_COLOR_NAMES: Incomplete
ANSI_COLOR_NAMES_ALIASES: dict[str, str]

class BaseStyle(metaclass=ABCMeta):
    """
    Abstract base class for prompt_toolkit styles.
    """
    @abstractmethod
    def get_attrs_for_style_str(self, style_str: str, default: Attrs = ...) -> Attrs:
        '''
        Return :class:`.Attrs` for the given style string.

        :param style_str: The style string. This can contain inline styling as
            well as classnames (e.g. "class:title").
        :param default: `Attrs` to be used if no styling was defined.
        '''
    @property
    @abc.abstractmethod
    def style_rules(self) -> list[tuple[str, str]]:
        """
        The list of style rules, used to create this style.
        (Required for `DynamicStyle` and `_MergedStyle` to work.)
        """
    @abstractmethod
    def invalidation_hash(self) -> Hashable:
        """
        Invalidation hash for the style. When this changes over time, the
        renderer knows that something in the style changed, and that everything
        has to be redrawn.
        """

class DummyStyle(BaseStyle):
    """
    A style that doesn't style anything.
    """
    def get_attrs_for_style_str(self, style_str: str, default: Attrs = ...) -> Attrs: ...
    def invalidation_hash(self) -> Hashable: ...
    @property
    def style_rules(self) -> list[tuple[str, str]]: ...

class DynamicStyle(BaseStyle):
    """
    Style class that can dynamically returns an other Style.

    :param get_style: Callable that returns a :class:`.Style` instance.
    """
    get_style: Incomplete
    def __init__(self, get_style: Callable[[], BaseStyle | None]) -> None: ...
    def get_attrs_for_style_str(self, style_str: str, default: Attrs = ...) -> Attrs: ...
    def invalidation_hash(self) -> Hashable: ...
    @property
    def style_rules(self) -> list[tuple[str, str]]: ...
