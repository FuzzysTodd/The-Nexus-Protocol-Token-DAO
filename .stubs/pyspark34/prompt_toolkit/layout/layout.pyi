from .containers import AnyContainer, Container, Window
from .controls import BufferControl, UIControl
from _typeshed import Incomplete
from prompt_toolkit.buffer import Buffer
from typing import Generator, Iterable

__all__ = ['Layout', 'InvalidLayoutError', 'walk']

FocusableElement = str | Buffer | UIControl | AnyContainer

class Layout:
    '''
    The layout for a prompt_toolkit
    :class:`~prompt_toolkit.application.Application`.
    This also keeps track of which user control is focused.

    :param container: The "root" container for the layout.
    :param focused_element: element to be focused initially. (Can be anything
        the `focus` function accepts.)
    '''
    container: Incomplete
    search_links: Incomplete
    visible_windows: Incomplete
    def __init__(self, container: AnyContainer, focused_element: FocusableElement | None = None) -> None: ...
    def find_all_windows(self) -> Generator[Window, None, None]:
        """
        Find all the :class:`.UIControl` objects in this layout.
        """
    def find_all_controls(self) -> Iterable[UIControl]: ...
    def focus(self, value: FocusableElement) -> None:
        """
        Focus the given UI element.

        `value` can be either:

        - a :class:`.UIControl`
        - a :class:`.Buffer` instance or the name of a :class:`.Buffer`
        - a :class:`.Window`
        - Any container object. In this case we will focus the :class:`.Window`
          from this container that was focused most recent, or the very first
          focusable :class:`.Window` of the container.
        """
    def has_focus(self, value: FocusableElement) -> bool:
        """
        Check whether the given control has the focus.
        :param value: :class:`.UIControl` or :class:`.Window` instance.
        """
    @property
    def current_control(self) -> UIControl:
        """
        Get the :class:`.UIControl` to currently has the focus.
        """
    @current_control.setter
    def current_control(self, control: UIControl) -> None:
        """
        Set the :class:`.UIControl` to receive the focus.
        """
    @property
    def current_window(self) -> Window:
        """Return the :class:`.Window` object that is currently focused."""
    @current_window.setter
    def current_window(self, value: Window) -> None:
        """Set the :class:`.Window` object to be currently focused."""
    @property
    def is_searching(self) -> bool:
        """True if we are searching right now."""
    @property
    def search_target_buffer_control(self) -> BufferControl | None:
        """
        Return the :class:`.BufferControl` in which we are searching or `None`.
        """
    def get_focusable_windows(self) -> Iterable[Window]:
        """
        Return all the :class:`.Window` objects which are focusable (in the
        'modal' area).
        """
    def get_visible_focusable_windows(self) -> list[Window]:
        """
        Return a list of :class:`.Window` objects that are focusable.
        """
    @property
    def current_buffer(self) -> Buffer | None:
        """
        The currently focused :class:`~.Buffer` or `None`.
        """
    def get_buffer_by_name(self, buffer_name: str) -> Buffer | None:
        """
        Look in the layout for a buffer with the given name.
        Return `None` when nothing was found.
        """
    @property
    def buffer_has_focus(self) -> bool:
        """
        Return `True` if the currently focused control is a
        :class:`.BufferControl`. (For instance, used to determine whether the
        default key bindings should be active or not.)
        """
    @property
    def previous_control(self) -> UIControl:
        """
        Get the :class:`.UIControl` to previously had the focus.
        """
    def focus_last(self) -> None:
        """
        Give the focus to the last focused control.
        """
    def focus_next(self) -> None:
        """
        Focus the next visible/focusable Window.
        """
    def focus_previous(self) -> None:
        """
        Focus the previous visible/focusable Window.
        """
    def walk(self) -> Iterable[Container]:
        """
        Walk through all the layout nodes (and their children) and yield them.
        """
    def walk_through_modal_area(self) -> Iterable[Container]:
        """
        Walk through all the containers which are in the current 'modal' part
        of the layout.
        """
    def update_parents_relations(self) -> None:
        """
        Update child->parent relationships mapping.
        """
    def reset(self) -> None: ...
    def get_parent(self, container: Container) -> Container | None:
        """
        Return the parent container for the given container, or ``None``, if it
        wasn't found.
        """

class InvalidLayoutError(Exception): ...

def walk(container: Container, skip_hidden: bool = False) -> Iterable[Container]:
    """
    Walk through layout, starting at this container.
    """
