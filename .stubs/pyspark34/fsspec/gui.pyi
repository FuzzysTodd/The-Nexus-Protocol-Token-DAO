from .core import OpenFile as OpenFile, get_filesystem_class as get_filesystem_class, split_protocol as split_protocol
from .registry import known_implementations as known_implementations
from _typeshed import Incomplete
from collections.abc import Generator
from typing import ClassVar, Sequence

logger: Incomplete

class SigSlot:
    """Signal-slot mixin, for Panel event passing

    Include this class in a widget manager's superclasses to be able to
    register events and callbacks on Panel widgets managed by that class.

    The method ``_register`` should be called as widgets are added, and external
    code should call ``connect`` to associate callbacks.

    By default, all signals emit a DEBUG logging statement.
    """
    signals: ClassVar[Sequence[str]]
    slots: ClassVar[Sequence[str]]
    def __init__(self) -> None: ...
    def connect(self, signal, slot) -> None:
        '''Associate call back with given event

        The callback must be a function which takes the "new" value of the
        watched attribute as the only parameter. If the callback return False,
        this cancels any further processing of the given event.

        Alternatively, the callback can be a string, in which case it means
        emitting the correspondingly-named event (i.e., connect to self)
        '''
    def ignore_events(self) -> Generator[None, None, None]:
        """Temporarily turn off events processing in this instance

        (does not propagate to children)
        """
    def show(self, threads: bool = False):
        """Open a new browser tab and display this instance's interface"""

class SingleSelect(SigSlot):
    """A multiselect which only allows you to select one item for an event"""
    signals: Incomplete
    slots: Incomplete
    kwargs: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def select_one(self, *_) -> None: ...
    def set_options(self, options) -> None: ...
    def clear(self) -> None: ...
    @property
    def value(self): ...
    def set_selection(self, selection) -> None: ...

class FileSelector(SigSlot):
    """Panel-based graphical file selector widget

    Instances of this widget are interactive and can be displayed in jupyter by having
    them as the output of a cell,  or in a separate browser tab using ``.show()``.
    """
    signals: Incomplete
    slots: Incomplete
    init_url: Incomplete
    init_kwargs: Incomplete
    filters: Incomplete
    ignore: Incomplete
    def __init__(self, url: Incomplete | None = None, filters: Incomplete | None = None, ignore: Incomplete | None = None, kwargs: Incomplete | None = None) -> None:
        '''

        Parameters
        ----------
        url : str (optional)
            Initial value of the URL to populate the dialog; should include protocol
        filters : list(str) (optional)
            File endings to include in the listings. If not included, all files are
            allowed. Does not affect directories.
            If given, the endings will appear as checkboxes in the interface
        ignore : list(str) (optional)
            Regex(s) of file basename patterns to ignore, e.g., "\\." for typical
            hidden files on posix
        kwargs : dict (optional)
            To pass to file system instance
        '''
    def set_filters(self, filters: Incomplete | None = None) -> None: ...
    @property
    def storage_options(self):
        """Value of the kwargs box as a dictionary"""
    @property
    def fs(self):
        """Current filesystem instance"""
    @property
    def urlpath(self):
        """URL of currently selected item"""
    def open_file(self, mode: str = 'rb', compression: Incomplete | None = None, encoding: Incomplete | None = None):
        """Create OpenFile instance for the currently selected item

        For example, in a notebook you might do something like

        .. code-block::

            [ ]: sel = FileSelector(); sel

            # user selects their file

            [ ]: with sel.open_file('rb') as f:
            ...      out = f.read()

        Parameters
        ----------
        mode: str (optional)
            Open mode for the file.
        compression: str (optional)
            The interact with the file as compressed. Set to 'infer' to guess
            compression from the file ending
        encoding: str (optional)
            If using text mode, use this encoding; defaults to UTF8.
        """
    def filters_changed(self, values) -> None: ...
    def selection_changed(self, *_) -> None: ...
    prev_protocol: Incomplete
    prev_kwargs: Incomplete
    def go_clicked(self, *_): ...
    def protocol_changed(self, *_) -> None: ...
    def home_clicked(self, *_) -> None: ...
    def up_clicked(self, *_) -> None: ...
