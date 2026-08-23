from .base import Attrs
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.utils import AnyFloat
from typing import Callable, Hashable, Sequence

__all__ = ['StyleTransformation', 'SwapLightAndDarkStyleTransformation', 'ReverseStyleTransformation', 'SetDefaultColorStyleTransformation', 'AdjustBrightnessStyleTransformation', 'DummyStyleTransformation', 'ConditionalStyleTransformation', 'DynamicStyleTransformation', 'merge_style_transformations']

class StyleTransformation(metaclass=ABCMeta):
    """
    Base class for any style transformation.
    """
    @abstractmethod
    def transform_attrs(self, attrs: Attrs) -> Attrs:
        '''
        Take an `Attrs` object and return a new `Attrs` object.

        Remember that the color formats can be either "ansi..." or a 6 digit
        lowercase hexadecimal color (without \'#\' prefix).
        '''
    def invalidation_hash(self) -> Hashable:
        """
        When this changes, the cache should be invalidated.
        """

class SwapLightAndDarkStyleTransformation(StyleTransformation):
    '''
    Turn dark colors into light colors and the other way around.

    This is meant to make color schemes that work on a dark background usable
    on a light background (and the other way around).

    Notice that this doesn\'t swap foreground and background like "reverse"
    does. It turns light green into dark green and the other way around.
    Foreground and background colors are considered individually.

    Also notice that when <reverse> is used somewhere and no colors are given
    in particular (like what is the default for the bottom toolbar), then this
    doesn\'t change anything. This is what makes sense, because when the
    \'default\' color is chosen, it\'s what works best for the terminal, and
    reverse works good with that.
    '''
    def transform_attrs(self, attrs: Attrs) -> Attrs:
        """
        Return the `Attrs` used when opposite luminosity should be used.
        """

class ReverseStyleTransformation(StyleTransformation):
    """
    Swap the 'reverse' attribute.

    (This is still experimental.)
    """
    def transform_attrs(self, attrs: Attrs) -> Attrs: ...

class SetDefaultColorStyleTransformation(StyleTransformation):
    """
    Set default foreground/background color for output that doesn't specify
    anything. This is useful for overriding the terminal default colors.

    :param fg: Color string or callable that returns a color string for the
        foreground.
    :param bg: Like `fg`, but for the background.
    """
    fg: Incomplete
    bg: Incomplete
    def __init__(self, fg: str | Callable[[], str], bg: str | Callable[[], str]) -> None: ...
    def transform_attrs(self, attrs: Attrs) -> Attrs: ...
    def invalidation_hash(self) -> Hashable: ...

class AdjustBrightnessStyleTransformation(StyleTransformation):
    """
    Adjust the brightness to improve the rendering on either dark or light
    backgrounds.

    For dark backgrounds, it's best to increase `min_brightness`. For light
    backgrounds it's best to decrease `max_brightness`. Usually, only one
    setting is adjusted.

    This will only change the brightness for text that has a foreground color
    defined, but no background color. It works best for 256 or true color
    output.

    .. note:: Notice that there is no universal way to detect whether the
              application is running in a light or dark terminal. As a
              developer of an command line application, you'll have to make
              this configurable for the user.

    :param min_brightness: Float between 0.0 and 1.0 or a callable that returns
        a float.
    :param max_brightness: Float between 0.0 and 1.0 or a callable that returns
        a float.
    """
    min_brightness: Incomplete
    max_brightness: Incomplete
    def __init__(self, min_brightness: AnyFloat = 0.0, max_brightness: AnyFloat = 1.0) -> None: ...
    def transform_attrs(self, attrs: Attrs) -> Attrs: ...
    def invalidation_hash(self) -> Hashable: ...

class DummyStyleTransformation(StyleTransformation):
    """
    Don't transform anything at all.
    """
    def transform_attrs(self, attrs: Attrs) -> Attrs: ...
    def invalidation_hash(self) -> Hashable: ...

class DynamicStyleTransformation(StyleTransformation):
    """
    StyleTransformation class that can dynamically returns any
    `StyleTransformation`.

    :param get_style_transformation: Callable that returns a
        :class:`.StyleTransformation` instance.
    """
    get_style_transformation: Incomplete
    def __init__(self, get_style_transformation: Callable[[], StyleTransformation | None]) -> None: ...
    def transform_attrs(self, attrs: Attrs) -> Attrs: ...
    def invalidation_hash(self) -> Hashable: ...

class ConditionalStyleTransformation(StyleTransformation):
    """
    Apply the style transformation depending on a condition.
    """
    style_transformation: Incomplete
    filter: Incomplete
    def __init__(self, style_transformation: StyleTransformation, filter: FilterOrBool) -> None: ...
    def transform_attrs(self, attrs: Attrs) -> Attrs: ...
    def invalidation_hash(self) -> Hashable: ...

class _MergedStyleTransformation(StyleTransformation):
    style_transformations: Incomplete
    def __init__(self, style_transformations: Sequence[StyleTransformation]) -> None: ...
    def transform_attrs(self, attrs: Attrs) -> Attrs: ...
    def invalidation_hash(self) -> Hashable: ...

def merge_style_transformations(style_transformations: Sequence[StyleTransformation]) -> StyleTransformation:
    """
    Merge multiple transformations together.
    """
