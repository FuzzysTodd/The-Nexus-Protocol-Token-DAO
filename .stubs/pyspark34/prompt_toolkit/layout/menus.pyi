from .containers import ConditionalContainer, HSplit
from .controls import GetLinePrefixCallable, UIContent, UIControl
from _typeshed import Incomplete
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.key_binding.key_bindings import KeyBindings, NotImplementedOrNone
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.mouse_events import MouseEvent
from typing import Callable

__all__ = ['CompletionsMenu', 'MultiColumnCompletionsMenu']

E = KeyPressEvent

class CompletionsMenuControl(UIControl):
    """
    Helper for drawing the complete menu to the screen.

    :param scroll_offset: Number (integer) representing the preferred amount of
        completions to be displayed before and after the current one. When this
        is a very high number, the current completion will be shown in the
        middle most of the time.
    """
    MIN_WIDTH: int
    def has_focus(self) -> bool: ...
    def preferred_width(self, max_available_width: int) -> int | None: ...
    def preferred_height(self, width: int, max_available_height: int, wrap_lines: bool, get_line_prefix: GetLinePrefixCallable | None) -> int | None: ...
    def create_content(self, width: int, height: int) -> UIContent:
        """
        Create a UIContent object for this control.
        """
    def mouse_handler(self, mouse_event: MouseEvent) -> NotImplementedOrNone:
        """
        Handle mouse events: clicking and scrolling.
        """

class CompletionsMenu(ConditionalContainer):
    def __init__(self, max_height: int | None = None, scroll_offset: int | Callable[[], int] = 0, extra_filter: FilterOrBool = True, display_arrows: FilterOrBool = False, z_index: int = ...) -> None: ...

class MultiColumnCompletionMenuControl(UIControl):
    """
    Completion menu that displays all the completions in several columns.
    When there are more completions than space for them to be displayed, an
    arrow is shown on the left or right side.

    `min_rows` indicates how many rows will be available in any possible case.
    When this is larger than one, it will try to use less columns and more
    rows until this value is reached.
    Be careful passing in a too big value, if less than the given amount of
    rows are available, more columns would have been required, but
    `preferred_width` doesn't know about that and reports a too small value.
    This results in less completions displayed and additional scrolling.
    (It's a limitation of how the layout engine currently works: first the
    widths are calculated, then the heights.)

    :param suggested_max_column_width: The suggested max width of a column.
        The column can still be bigger than this, but if there is place for two
        columns of this width, we will display two columns. This to avoid that
        if there is one very wide completion, that it doesn't significantly
        reduce the amount of columns.
    """
    min_rows: Incomplete
    suggested_max_column_width: Incomplete
    scroll: int
    def __init__(self, min_rows: int = 3, suggested_max_column_width: int = 30) -> None: ...
    def reset(self) -> None: ...
    def has_focus(self) -> bool: ...
    def preferred_width(self, max_available_width: int) -> int | None:
        """
        Preferred width: prefer to use at least min_rows, but otherwise as much
        as possible horizontally.
        """
    def preferred_height(self, width: int, max_available_height: int, wrap_lines: bool, get_line_prefix: GetLinePrefixCallable | None) -> int | None:
        """
        Preferred height: as much as needed in order to display all the completions.
        """
    def create_content(self, width: int, height: int) -> UIContent:
        """
        Create a UIContent object for this menu.
        """
    def mouse_handler(self, mouse_event: MouseEvent) -> NotImplementedOrNone:
        """
        Handle scroll and click events.
        """
    def get_key_bindings(self) -> KeyBindings:
        """
        Expose key bindings that handle the left/right arrow keys when the menu
        is displayed.
        """

class MultiColumnCompletionsMenu(HSplit):
    """
    Container that displays the completions in several columns.
    When `show_meta` (a :class:`~prompt_toolkit.filters.Filter`) evaluates
    to True, it shows the meta information at the bottom.
    """
    def __init__(self, min_rows: int = 3, suggested_max_column_width: int = 30, show_meta: FilterOrBool = True, extra_filter: FilterOrBool = True, z_index: int = ...) -> None: ...

class _SelectedCompletionMetaControl(UIControl):
    """
    Control that shows the meta information of the selected completion.
    """
    def preferred_width(self, max_available_width: int) -> int | None:
        """
        Report the width of the longest meta text as the preferred width of this control.

        It could be that we use less width, but this way, we're sure that the
        layout doesn't change when we select another completion (E.g. that
        completions are suddenly shown in more or fewer columns.)
        """
    def preferred_height(self, width: int, max_available_height: int, wrap_lines: bool, get_line_prefix: GetLinePrefixCallable | None) -> int | None: ...
    def create_content(self, width: int, height: int) -> UIContent: ...
