from .containers import Container, ScrollOffsets
from .dimension import AnyDimension, Dimension
from .mouse_handlers import MouseHandlers
from .screen import Screen, WritePosition
from _typeshed import Incomplete
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.key_binding import KeyBindingsBase

__all__ = ['ScrollablePane']

class ScrollablePane(Container):
    """
    Container widget that exposes a larger virtual screen to its content and
    displays it in a vertical scrollbale region.

    Typically this is wrapped in a large `HSplit` container. Make sure in that
    case to not specify a `height` dimension of the `HSplit`, so that it will
    scale according to the content.

    .. note::

        If you want to display a completion menu for widgets in this
        `ScrollablePane`, then it's still a good practice to use a
        `FloatContainer` with a `CompletionsMenu` in a `Float` at the top-level
        of the layout hierarchy, rather then nesting a `FloatContainer` in this
        `ScrollablePane`. (Otherwise, it's possible that the completion menu
        is clipped.)

    :param content: The content container.
    :param scrolloffset: Try to keep the cursor within this distance from the
        top/bottom (left/right offset is not used).
    :param keep_cursor_visible: When `True`, automatically scroll the pane so
        that the cursor (of the focused window) is always visible.
    :param keep_focused_window_visible: When `True`, automatically scroll the
        pane so that the focused window is visible, or as much visible as
        possible if it doesn't completely fit the screen.
    :param max_available_height: Always constraint the height to this amount
        for performance reasons.
    :param width: When given, use this width instead of looking at the children.
    :param height: When given, use this height instead of looking at the children.
    :param show_scrollbar: When `True` display a scrollbar on the right.
    """
    content: Incomplete
    scroll_offsets: Incomplete
    keep_cursor_visible: Incomplete
    keep_focused_window_visible: Incomplete
    max_available_height: Incomplete
    width: Incomplete
    height: Incomplete
    show_scrollbar: Incomplete
    display_arrows: Incomplete
    up_arrow_symbol: Incomplete
    down_arrow_symbol: Incomplete
    vertical_scroll: int
    def __init__(self, content: Container, scroll_offsets: ScrollOffsets | None = None, keep_cursor_visible: FilterOrBool = True, keep_focused_window_visible: FilterOrBool = True, max_available_height: int = ..., width: AnyDimension = None, height: AnyDimension = None, show_scrollbar: FilterOrBool = True, display_arrows: FilterOrBool = True, up_arrow_symbol: str = '^', down_arrow_symbol: str = 'v') -> None: ...
    def reset(self) -> None: ...
    def preferred_width(self, max_available_width: int) -> Dimension: ...
    def preferred_height(self, width: int, max_available_height: int) -> Dimension: ...
    def write_to_screen(self, screen: Screen, mouse_handlers: MouseHandlers, write_position: WritePosition, parent_style: str, erase_bg: bool, z_index: int | None) -> None:
        """
        Render scrollable pane content.

        This works by rendering on an off-screen canvas, and copying over the
        visible region.
        """
    def is_modal(self) -> bool: ...
    def get_key_bindings(self) -> KeyBindingsBase | None: ...
    def get_children(self) -> list[Container]: ...
