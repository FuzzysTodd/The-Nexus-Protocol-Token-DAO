from .containers import WindowRenderInfo
from .controls import UIContent
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import StyleAndTextTuples
from typing import Callable

__all__ = ['Margin', 'NumberedMargin', 'ScrollbarMargin', 'ConditionalMargin', 'PromptMargin']

class Margin(metaclass=ABCMeta):
    """
    Base interface for a margin.
    """
    @abstractmethod
    def get_width(self, get_ui_content: Callable[[], UIContent]) -> int:
        """
        Return the width that this margin is going to consume.

        :param get_ui_content: Callable that asks the user control to create
            a :class:`.UIContent` instance. This can be used for instance to
            obtain the number of lines.
        """
    @abstractmethod
    def create_margin(self, window_render_info: WindowRenderInfo, width: int, height: int) -> StyleAndTextTuples:
        """
        Creates a margin.
        This should return a list of (style_str, text) tuples.

        :param window_render_info:
            :class:`~prompt_toolkit.layout.containers.WindowRenderInfo`
            instance, generated after rendering and copying the visible part of
            the :class:`~prompt_toolkit.layout.controls.UIControl` into the
            :class:`~prompt_toolkit.layout.containers.Window`.
        :param width: The width that's available for this margin. (As reported
            by :meth:`.get_width`.)
        :param height: The height that's available for this margin. (The height
            of the :class:`~prompt_toolkit.layout.containers.Window`.)
        """

class NumberedMargin(Margin):
    """
    Margin that displays the line numbers.

    :param relative: Number relative to the cursor position. Similar to the Vi
                     'relativenumber' option.
    :param display_tildes: Display tildes after the end of the document, just
        like Vi does.
    """
    relative: Incomplete
    display_tildes: Incomplete
    def __init__(self, relative: FilterOrBool = False, display_tildes: FilterOrBool = False) -> None: ...
    def get_width(self, get_ui_content: Callable[[], UIContent]) -> int: ...
    def create_margin(self, window_render_info: WindowRenderInfo, width: int, height: int) -> StyleAndTextTuples: ...

class ConditionalMargin(Margin):
    """
    Wrapper around other :class:`.Margin` classes to show/hide them.
    """
    margin: Incomplete
    filter: Incomplete
    def __init__(self, margin: Margin, filter: FilterOrBool) -> None: ...
    def get_width(self, get_ui_content: Callable[[], UIContent]) -> int: ...
    def create_margin(self, window_render_info: WindowRenderInfo, width: int, height: int) -> StyleAndTextTuples: ...

class ScrollbarMargin(Margin):
    """
    Margin displaying a scrollbar.

    :param display_arrows: Display scroll up/down arrows.
    """
    display_arrows: Incomplete
    up_arrow_symbol: Incomplete
    down_arrow_symbol: Incomplete
    def __init__(self, display_arrows: FilterOrBool = False, up_arrow_symbol: str = '^', down_arrow_symbol: str = 'v') -> None: ...
    def get_width(self, get_ui_content: Callable[[], UIContent]) -> int: ...
    def create_margin(self, window_render_info: WindowRenderInfo, width: int, height: int) -> StyleAndTextTuples: ...

class PromptMargin(Margin):
    """
    [Deprecated]

    Create margin that displays a prompt.
    This can display one prompt at the first line, and a continuation prompt
    (e.g, just dots) on all the following lines.

    This `PromptMargin` implementation has been largely superseded in favor of
    the `get_line_prefix` attribute of `Window`. The reason is that a margin is
    always a fixed width, while `get_line_prefix` can return a variable width
    prefix in front of every line, making it more powerful, especially for line
    continuations.

    :param get_prompt: Callable returns formatted text or a list of
        `(style_str, type)` tuples to be shown as the prompt at the first line.
    :param get_continuation: Callable that takes three inputs. The width (int),
        line_number (int), and is_soft_wrap (bool). It should return formatted
        text or a list of `(style_str, type)` tuples for the next lines of the
        input.
    """
    get_prompt: Incomplete
    get_continuation: Incomplete
    def __init__(self, get_prompt: Callable[[], StyleAndTextTuples], get_continuation: None | Callable[[int, int, bool], StyleAndTextTuples] = None) -> None: ...
    def get_width(self, get_ui_content: Callable[[], UIContent]) -> int:
        """Width to report to the `Window`."""
    def create_margin(self, window_render_info: WindowRenderInfo, width: int, height: int) -> StyleAndTextTuples: ...
