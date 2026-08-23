import abc
from .controls import GetLinePrefixCallable, UIContent, UIControl
from .dimension import AnyDimension, Dimension
from .margins import Margin
from .mouse_handlers import MouseHandlers
from .screen import Screen, WritePosition
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from enum import Enum
from prompt_toolkit.data_structures import Point
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.key_binding import KeyBindingsBase
from typing import Callable, Sequence
from typing_extensions import Protocol, TypeGuard

__all__ = ['AnyContainer', 'Container', 'HorizontalAlign', 'VerticalAlign', 'HSplit', 'VSplit', 'FloatContainer', 'Float', 'WindowAlign', 'Window', 'WindowRenderInfo', 'ConditionalContainer', 'ScrollOffsets', 'ColorColumn', 'to_container', 'to_window', 'is_container', 'DynamicContainer']

class Container(metaclass=ABCMeta):
    """
    Base class for user interface layout.
    """
    @abstractmethod
    def reset(self) -> None:
        """
        Reset the state of this container and all the children.
        (E.g. reset scroll offsets, etc...)
        """
    @abstractmethod
    def preferred_width(self, max_available_width: int) -> Dimension:
        """
        Return a :class:`~prompt_toolkit.layout.Dimension` that represents the
        desired width for this container.
        """
    @abstractmethod
    def preferred_height(self, width: int, max_available_height: int) -> Dimension:
        """
        Return a :class:`~prompt_toolkit.layout.Dimension` that represents the
        desired height for this container.
        """
    @abstractmethod
    def write_to_screen(self, screen: Screen, mouse_handlers: MouseHandlers, write_position: WritePosition, parent_style: str, erase_bg: bool, z_index: int | None) -> None:
        """
        Write the actual content to the screen.

        :param screen: :class:`~prompt_toolkit.layout.screen.Screen`
        :param mouse_handlers: :class:`~prompt_toolkit.layout.mouse_handlers.MouseHandlers`.
        :param parent_style: Style string to pass to the :class:`.Window`
            object. This will be applied to all content of the windows.
            :class:`.VSplit` and :class:`.HSplit` can use it to pass their
            style down to the windows that they contain.
        :param z_index: Used for propagating z_index from parent to child.
        """
    def is_modal(self) -> bool:
        """
        When this container is modal, key bindings from parent containers are
        not taken into account if a user control in this container is focused.
        """
    def get_key_bindings(self) -> KeyBindingsBase | None:
        """
        Returns a :class:`.KeyBindings` object. These bindings become active when any
        user control in this container has the focus, except if any containers
        between this container and the focused user control is modal.
        """
    @abstractmethod
    def get_children(self) -> list[Container]:
        """
        Return the list of child :class:`.Container` objects.
        """

class MagicContainer(Protocol):
    """
        Any object that implements ``__pt_container__`` represents a container.
        """
    def __pt_container__(self) -> AnyContainer: ...

AnyContainer: Incomplete

class VerticalAlign(Enum):
    """Alignment for `HSplit`."""
    TOP: str
    CENTER: str
    BOTTOM: str
    JUSTIFY: str

class HorizontalAlign(Enum):
    """Alignment for `VSplit`."""
    LEFT: str
    CENTER: str
    RIGHT: str
    JUSTIFY: str

class _Split(Container, metaclass=abc.ABCMeta):
    """
    The common parts of `VSplit` and `HSplit`.
    """
    children: Incomplete
    window_too_small: Incomplete
    padding: Incomplete
    padding_char: Incomplete
    padding_style: Incomplete
    width: Incomplete
    height: Incomplete
    z_index: Incomplete
    modal: Incomplete
    key_bindings: Incomplete
    style: Incomplete
    def __init__(self, children: Sequence[AnyContainer], window_too_small: Container | None = None, padding: AnyDimension = ..., padding_char: str | None = None, padding_style: str = '', width: AnyDimension = None, height: AnyDimension = None, z_index: int | None = None, modal: bool = False, key_bindings: KeyBindingsBase | None = None, style: str | Callable[[], str] = '') -> None: ...
    def is_modal(self) -> bool: ...
    def get_key_bindings(self) -> KeyBindingsBase | None: ...
    def get_children(self) -> list[Container]: ...

class HSplit(_Split):
    '''
    Several layouts, one stacked above/under the other. ::

        +--------------------+
        |                    |
        +--------------------+
        |                    |
        +--------------------+

    By default, this doesn\'t display a horizontal line between the children,
    but if this is something you need, then create a HSplit as follows::

        HSplit(children=[ ... ], padding_char=\'-\',
               padding=1, padding_style=\'#ffff00\')

    :param children: List of child :class:`.Container` objects.
    :param window_too_small: A :class:`.Container` object that is displayed if
        there is not enough space for all the children. By default, this is a
        "Window too small" message.
    :param align: `VerticalAlign` value.
    :param width: When given, use this width instead of looking at the children.
    :param height: When given, use this height instead of looking at the children.
    :param z_index: (int or None) When specified, this can be used to bring
        element in front of floating elements.  `None` means: inherit from parent.
    :param style: A style string.
    :param modal: ``True`` or ``False``.
    :param key_bindings: ``None`` or a :class:`.KeyBindings` object.

    :param padding: (`Dimension` or int), size to be used for the padding.
    :param padding_char: Character to be used for filling in the padding.
    :param padding_style: Style to applied to the padding.
    '''
    align: Incomplete
    def __init__(self, children: Sequence[AnyContainer], window_too_small: Container | None = None, align: VerticalAlign = ..., padding: AnyDimension = 0, padding_char: str | None = None, padding_style: str = '', width: AnyDimension = None, height: AnyDimension = None, z_index: int | None = None, modal: bool = False, key_bindings: KeyBindingsBase | None = None, style: str | Callable[[], str] = '') -> None: ...
    def preferred_width(self, max_available_width: int) -> Dimension: ...
    def preferred_height(self, width: int, max_available_height: int) -> Dimension: ...
    def reset(self) -> None: ...
    def write_to_screen(self, screen: Screen, mouse_handlers: MouseHandlers, write_position: WritePosition, parent_style: str, erase_bg: bool, z_index: int | None) -> None:
        """
        Render the prompt to a `Screen` instance.

        :param screen: The :class:`~prompt_toolkit.layout.screen.Screen` class
            to which the output has to be written.
        """

class VSplit(_Split):
    '''
    Several layouts, one stacked left/right of the other. ::

        +---------+----------+
        |         |          |
        |         |          |
        +---------+----------+

    By default, this doesn\'t display a vertical line between the children, but
    if this is something you need, then create a HSplit as follows::

        VSplit(children=[ ... ], padding_char=\'|\',
               padding=1, padding_style=\'#ffff00\')

    :param children: List of child :class:`.Container` objects.
    :param window_too_small: A :class:`.Container` object that is displayed if
        there is not enough space for all the children. By default, this is a
        "Window too small" message.
    :param align: `HorizontalAlign` value.
    :param width: When given, use this width instead of looking at the children.
    :param height: When given, use this height instead of looking at the children.
    :param z_index: (int or None) When specified, this can be used to bring
        element in front of floating elements.  `None` means: inherit from parent.
    :param style: A style string.
    :param modal: ``True`` or ``False``.
    :param key_bindings: ``None`` or a :class:`.KeyBindings` object.

    :param padding: (`Dimension` or int), size to be used for the padding.
    :param padding_char: Character to be used for filling in the padding.
    :param padding_style: Style to applied to the padding.
    '''
    align: Incomplete
    def __init__(self, children: Sequence[AnyContainer], window_too_small: Container | None = None, align: HorizontalAlign = ..., padding: AnyDimension = 0, padding_char: str | None = None, padding_style: str = '', width: AnyDimension = None, height: AnyDimension = None, z_index: int | None = None, modal: bool = False, key_bindings: KeyBindingsBase | None = None, style: str | Callable[[], str] = '') -> None: ...
    def preferred_width(self, max_available_width: int) -> Dimension: ...
    def preferred_height(self, width: int, max_available_height: int) -> Dimension: ...
    def reset(self) -> None: ...
    def write_to_screen(self, screen: Screen, mouse_handlers: MouseHandlers, write_position: WritePosition, parent_style: str, erase_bg: bool, z_index: int | None) -> None:
        """
        Render the prompt to a `Screen` instance.

        :param screen: The :class:`~prompt_toolkit.layout.screen.Screen` class
            to which the output has to be written.
        """

class FloatContainer(Container):
    """
    Container which can contain another container for the background, as well
    as a list of floating containers on top of it.

    Example Usage::

        FloatContainer(content=Window(...),
                       floats=[
                           Float(xcursor=True,
                                ycursor=True,
                                content=CompletionsMenu(...))
                       ])

    :param z_index: (int or None) When specified, this can be used to bring
        element in front of floating elements.  `None` means: inherit from parent.
        This is the z_index for the whole `Float` container as a whole.
    """
    content: Incomplete
    floats: Incomplete
    modal: Incomplete
    key_bindings: Incomplete
    style: Incomplete
    z_index: Incomplete
    def __init__(self, content: AnyContainer, floats: list[Float], modal: bool = False, key_bindings: KeyBindingsBase | None = None, style: str | Callable[[], str] = '', z_index: int | None = None) -> None: ...
    def reset(self) -> None: ...
    def preferred_width(self, max_available_width: int) -> Dimension: ...
    def preferred_height(self, width: int, max_available_height: int) -> Dimension:
        """
        Return the preferred height of the float container.
        (We don't care about the height of the floats, they should always fit
        into the dimensions provided by the container.)
        """
    def write_to_screen(self, screen: Screen, mouse_handlers: MouseHandlers, write_position: WritePosition, parent_style: str, erase_bg: bool, z_index: int | None) -> None: ...
    def is_modal(self) -> bool: ...
    def get_key_bindings(self) -> KeyBindingsBase | None: ...
    def get_children(self) -> list[Container]: ...

class Float:
    """
    Float for use in a :class:`.FloatContainer`.
    Except for the `content` parameter, all other options are optional.

    :param content: :class:`.Container` instance.

    :param width: :class:`.Dimension` or callable which returns a :class:`.Dimension`.
    :param height: :class:`.Dimension` or callable which returns a :class:`.Dimension`.

    :param left: Distance to the left edge of the :class:`.FloatContainer`.
    :param right: Distance to the right edge of the :class:`.FloatContainer`.
    :param top: Distance to the top of the :class:`.FloatContainer`.
    :param bottom: Distance to the bottom of the :class:`.FloatContainer`.

    :param attach_to_window: Attach to the cursor from this window, instead of
        the current window.
    :param hide_when_covering_content: Hide the float when it covers content underneath.
    :param allow_cover_cursor: When `False`, make sure to display the float
        below the cursor. Not on top of the indicated position.
    :param z_index: Z-index position. For a Float, this needs to be at least
        one. It is relative to the z_index of the parent container.
    :param transparent: :class:`.Filter` indicating whether this float needs to be
        drawn transparently.
    """
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    width: Incomplete
    height: Incomplete
    xcursor: Incomplete
    ycursor: Incomplete
    attach_to_window: Incomplete
    content: Incomplete
    hide_when_covering_content: Incomplete
    allow_cover_cursor: Incomplete
    z_index: Incomplete
    transparent: Incomplete
    def __init__(self, content: AnyContainer, top: int | None = None, right: int | None = None, bottom: int | None = None, left: int | None = None, width: int | Callable[[], int] | None = None, height: int | Callable[[], int] | None = None, xcursor: bool = False, ycursor: bool = False, attach_to_window: AnyContainer | None = None, hide_when_covering_content: bool = False, allow_cover_cursor: bool = False, z_index: int = 1, transparent: bool = False) -> None: ...
    def get_width(self) -> int | None: ...
    def get_height(self) -> int | None: ...

class WindowRenderInfo:
    """
    Render information for the last render time of this control.
    It stores mapping information between the input buffers (in case of a
    :class:`~prompt_toolkit.layout.controls.BufferControl`) and the actual
    render position on the output screen.

    (Could be used for implementation of the Vi 'H' and 'L' key bindings as
    well as implementing mouse support.)

    :param ui_content: The original :class:`.UIContent` instance that contains
        the whole input, without clipping. (ui_content)
    :param horizontal_scroll: The horizontal scroll of the :class:`.Window` instance.
    :param vertical_scroll: The vertical scroll of the :class:`.Window` instance.
    :param window_width: The width of the window that displays the content,
        without the margins.
    :param window_height: The height of the window that displays the content.
    :param configured_scroll_offsets: The scroll offsets as configured for the
        :class:`Window` instance.
    :param visible_line_to_row_col: Mapping that maps the row numbers on the
        displayed screen (starting from zero for the first visible line) to
        (row, col) tuples pointing to the row and column of the :class:`.UIContent`.
    :param rowcol_to_yx: Mapping that maps (row, column) tuples representing
        coordinates of the :class:`UIContent` to (y, x) absolute coordinates at
        the rendered screen.
    """
    window: Incomplete
    ui_content: Incomplete
    vertical_scroll: Incomplete
    window_width: Incomplete
    window_height: Incomplete
    configured_scroll_offsets: Incomplete
    visible_line_to_row_col: Incomplete
    wrap_lines: Incomplete
    def __init__(self, window: Window, ui_content: UIContent, horizontal_scroll: int, vertical_scroll: int, window_width: int, window_height: int, configured_scroll_offsets: ScrollOffsets, visible_line_to_row_col: dict[int, tuple[int, int]], rowcol_to_yx: dict[tuple[int, int], tuple[int, int]], x_offset: int, y_offset: int, wrap_lines: bool) -> None: ...
    @property
    def visible_line_to_input_line(self) -> dict[int, int]: ...
    @property
    def cursor_position(self) -> Point:
        """
        Return the cursor position coordinates, relative to the left/top corner
        of the rendered screen.
        """
    @property
    def applied_scroll_offsets(self) -> ScrollOffsets:
        """
        Return a :class:`.ScrollOffsets` instance that indicates the actual
        offset. This can be less than or equal to what's configured. E.g, when
        the cursor is completely at the top, the top offset will be zero rather
        than what's configured.
        """
    @property
    def displayed_lines(self) -> list[int]:
        """
        List of all the visible rows. (Line numbers of the input buffer.)
        The last line may not be entirely visible.
        """
    @property
    def input_line_to_visible_line(self) -> dict[int, int]:
        """
        Return the dictionary mapping the line numbers of the input buffer to
        the lines of the screen. When a line spans several rows at the screen,
        the first row appears in the dictionary.
        """
    def first_visible_line(self, after_scroll_offset: bool = False) -> int:
        """
        Return the line number (0 based) of the input document that corresponds
        with the first visible line.
        """
    def last_visible_line(self, before_scroll_offset: bool = False) -> int:
        """
        Like `first_visible_line`, but for the last visible line.
        """
    def center_visible_line(self, before_scroll_offset: bool = False, after_scroll_offset: bool = False) -> int:
        """
        Like `first_visible_line`, but for the center visible line.
        """
    @property
    def content_height(self) -> int:
        """
        The full height of the user control.
        """
    @property
    def full_height_visible(self) -> bool:
        """
        True when the full height is visible (There is no vertical scroll.)
        """
    @property
    def top_visible(self) -> bool:
        """
        True when the top of the buffer is visible.
        """
    @property
    def bottom_visible(self) -> bool:
        """
        True when the bottom of the buffer is visible.
        """
    @property
    def vertical_scroll_percentage(self) -> int:
        """
        Vertical scroll as a percentage. (0 means: the top is visible,
        100 means: the bottom is visible.)
        """
    def get_height_for_line(self, lineno: int) -> int:
        """
        Return the height of the given line.
        (The height that it would take, if this line became visible.)
        """

class ScrollOffsets:
    """
    Scroll offsets for the :class:`.Window` class.

    Note that left/right offsets only make sense if line wrapping is disabled.
    """
    def __init__(self, top: int | Callable[[], int] = 0, bottom: int | Callable[[], int] = 0, left: int | Callable[[], int] = 0, right: int | Callable[[], int] = 0) -> None: ...
    @property
    def top(self) -> int: ...
    @property
    def bottom(self) -> int: ...
    @property
    def left(self) -> int: ...
    @property
    def right(self) -> int: ...

class ColorColumn:
    """
    Column for a :class:`.Window` to be colored.
    """
    position: Incomplete
    style: Incomplete
    def __init__(self, position: int, style: str = 'class:color-column') -> None: ...

class WindowAlign(Enum):
    """
    Alignment of the Window content.

    Note that this is different from `HorizontalAlign` and `VerticalAlign`,
    which are used for the alignment of the child containers in respectively
    `VSplit` and `HSplit`.
    """
    LEFT: str
    RIGHT: str
    CENTER: str

class Window(Container):
    '''
    Container that holds a control.

    :param content: :class:`.UIControl` instance.
    :param width: :class:`.Dimension` instance or callable.
    :param height: :class:`.Dimension` instance or callable.
    :param z_index: When specified, this can be used to bring element in front
        of floating elements.
    :param dont_extend_width: When `True`, don\'t take up more width then the
                              preferred width reported by the control.
    :param dont_extend_height: When `True`, don\'t take up more width then the
                               preferred height reported by the control.
    :param ignore_content_width: A `bool` or :class:`.Filter` instance. Ignore
        the :class:`.UIContent` width when calculating the dimensions.
    :param ignore_content_height: A `bool` or :class:`.Filter` instance. Ignore
        the :class:`.UIContent` height when calculating the dimensions.
    :param left_margins: A list of :class:`.Margin` instance to be displayed on
        the left. For instance: :class:`~prompt_toolkit.layout.NumberedMargin`
        can be one of them in order to show line numbers.
    :param right_margins: Like `left_margins`, but on the other side.
    :param scroll_offsets: :class:`.ScrollOffsets` instance, representing the
        preferred amount of lines/columns to be always visible before/after the
        cursor. When both top and bottom are a very high number, the cursor
        will be centered vertically most of the time.
    :param allow_scroll_beyond_bottom: A `bool` or
        :class:`.Filter` instance. When True, allow scrolling so far, that the
        top part of the content is not visible anymore, while there is still
        empty space available at the bottom of the window. In the Vi editor for
        instance, this is possible. You will see tildes while the top part of
        the body is hidden.
    :param wrap_lines: A `bool` or :class:`.Filter` instance. When True, don\'t
        scroll horizontally, but wrap lines instead.
    :param get_vertical_scroll: Callable that takes this window
        instance as input and returns a preferred vertical scroll.
        (When this is `None`, the scroll is only determined by the last and
        current cursor position.)
    :param get_horizontal_scroll: Callable that takes this window
        instance as input and returns a preferred vertical scroll.
    :param always_hide_cursor: A `bool` or
        :class:`.Filter` instance. When True, never display the cursor, even
        when the user control specifies a cursor position.
    :param cursorline: A `bool` or :class:`.Filter` instance. When True,
        display a cursorline.
    :param cursorcolumn: A `bool` or :class:`.Filter` instance. When True,
        display a cursorcolumn.
    :param colorcolumns: A list of :class:`.ColorColumn` instances that
        describe the columns to be highlighted, or a callable that returns such
        a list.
    :param align: :class:`.WindowAlign` value or callable that returns an
        :class:`.WindowAlign` value. alignment of content.
    :param style: A style string. Style to be applied to all the cells in this
        window. (This can be a callable that returns a string.)
    :param char: (string) Character to be used for filling the background. This
        can also be a callable that returns a character.
    :param get_line_prefix: None or a callable that returns formatted text to
        be inserted before a line. It takes a line number (int) and a
        wrap_count and returns formatted text. This can be used for
        implementation of line continuations, things like Vim "breakindent" and
        so on.
    '''
    allow_scroll_beyond_bottom: Incomplete
    always_hide_cursor: Incomplete
    wrap_lines: Incomplete
    cursorline: Incomplete
    cursorcolumn: Incomplete
    content: Incomplete
    dont_extend_width: Incomplete
    dont_extend_height: Incomplete
    ignore_content_width: Incomplete
    ignore_content_height: Incomplete
    left_margins: Incomplete
    right_margins: Incomplete
    scroll_offsets: Incomplete
    get_vertical_scroll: Incomplete
    get_horizontal_scroll: Incomplete
    colorcolumns: Incomplete
    align: Incomplete
    style: Incomplete
    char: Incomplete
    get_line_prefix: Incomplete
    width: Incomplete
    height: Incomplete
    z_index: Incomplete
    def __init__(self, content: UIControl | None = None, width: AnyDimension = None, height: AnyDimension = None, z_index: int | None = None, dont_extend_width: FilterOrBool = False, dont_extend_height: FilterOrBool = False, ignore_content_width: FilterOrBool = False, ignore_content_height: FilterOrBool = False, left_margins: Sequence[Margin] | None = None, right_margins: Sequence[Margin] | None = None, scroll_offsets: ScrollOffsets | None = None, allow_scroll_beyond_bottom: FilterOrBool = False, wrap_lines: FilterOrBool = False, get_vertical_scroll: Callable[[Window], int] | None = None, get_horizontal_scroll: Callable[[Window], int] | None = None, always_hide_cursor: FilterOrBool = False, cursorline: FilterOrBool = False, cursorcolumn: FilterOrBool = False, colorcolumns: None | list[ColorColumn] | Callable[[], list[ColorColumn]] = None, align: WindowAlign | Callable[[], WindowAlign] = ..., style: str | Callable[[], str] = '', char: None | str | Callable[[], str] = None, get_line_prefix: GetLinePrefixCallable | None = None) -> None: ...
    vertical_scroll: int
    horizontal_scroll: int
    vertical_scroll_2: int
    render_info: Incomplete
    def reset(self) -> None: ...
    def preferred_width(self, max_available_width: int) -> Dimension:
        """
        Calculate the preferred width for this window.
        """
    def preferred_height(self, width: int, max_available_height: int) -> Dimension:
        """
        Calculate the preferred height for this window.
        """
    def write_to_screen(self, screen: Screen, mouse_handlers: MouseHandlers, write_position: WritePosition, parent_style: str, erase_bg: bool, z_index: int | None) -> None:
        """
        Write window to screen. This renders the user control, the margins and
        copies everything over to the absolute position at the given screen.
        """
    def get_key_bindings(self) -> KeyBindingsBase | None: ...
    def get_children(self) -> list[Container]: ...

class ConditionalContainer(Container):
    """
    Wrapper around any other container that can change the visibility. The
    received `filter` determines whether the given container should be
    displayed or not.

    :param content: :class:`.Container` instance.
    :param filter: :class:`.Filter` instance.
    """
    content: Incomplete
    filter: Incomplete
    def __init__(self, content: AnyContainer, filter: FilterOrBool) -> None: ...
    def reset(self) -> None: ...
    def preferred_width(self, max_available_width: int) -> Dimension: ...
    def preferred_height(self, width: int, max_available_height: int) -> Dimension: ...
    def write_to_screen(self, screen: Screen, mouse_handlers: MouseHandlers, write_position: WritePosition, parent_style: str, erase_bg: bool, z_index: int | None) -> None: ...
    def get_children(self) -> list[Container]: ...

class DynamicContainer(Container):
    """
    Container class that dynamically returns any Container.

    :param get_container: Callable that returns a :class:`.Container` instance
        or any widget with a ``__pt_container__`` method.
    """
    get_container: Incomplete
    def __init__(self, get_container: Callable[[], AnyContainer]) -> None: ...
    def reset(self) -> None: ...
    def preferred_width(self, max_available_width: int) -> Dimension: ...
    def preferred_height(self, width: int, max_available_height: int) -> Dimension: ...
    def write_to_screen(self, screen: Screen, mouse_handlers: MouseHandlers, write_position: WritePosition, parent_style: str, erase_bg: bool, z_index: int | None) -> None: ...
    def is_modal(self) -> bool: ...
    def get_key_bindings(self) -> KeyBindingsBase | None: ...
    def get_children(self) -> list[Container]: ...

def to_container(container: AnyContainer) -> Container:
    """
    Make sure that the given object is a :class:`.Container`.
    """
def to_window(container: AnyContainer) -> Window:
    """
    Make sure that the given argument is a :class:`.Window`.
    """
def is_container(value: object) -> TypeGuard[AnyContainer]:
    """
    Checks whether the given value is a container object
    (for use in assert statements).
    """
