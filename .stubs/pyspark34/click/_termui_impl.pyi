import typing as t
from ._compat import CYGWIN as CYGWIN, WIN as WIN, get_best_encoding as get_best_encoding, isatty as isatty, open_stream as open_stream, strip_ansi as strip_ansi, term_len as term_len
from .exceptions import ClickException as ClickException
from .utils import echo as echo
from _typeshed import Incomplete
from types import TracebackType

V = t.TypeVar('V')
BEFORE_BAR: str
AFTER_BAR: str

class ProgressBar(t.Generic[V]):
    fill_char: Incomplete
    empty_char: Incomplete
    bar_template: Incomplete
    info_sep: Incomplete
    show_eta: Incomplete
    show_percent: Incomplete
    show_pos: Incomplete
    item_show_func: Incomplete
    label: Incomplete
    file: Incomplete
    color: Incomplete
    update_min_steps: Incomplete
    width: Incomplete
    autowidth: Incomplete
    iter: Incomplete
    length: Incomplete
    pos: int
    avg: Incomplete
    last_eta: Incomplete
    start: Incomplete
    eta_known: bool
    finished: bool
    max_width: Incomplete
    entered: bool
    current_item: Incomplete
    is_hidden: Incomplete
    def __init__(self, iterable: t.Iterable[V] | None, length: int | None = None, fill_char: str = '#', empty_char: str = ' ', bar_template: str = '%(bar)s', info_sep: str = '  ', show_eta: bool = True, show_percent: bool | None = None, show_pos: bool = False, item_show_func: t.Callable[[V | None], str | None] | None = None, label: str | None = None, file: t.TextIO | None = None, color: bool | None = None, update_min_steps: int = 1, width: int = 30) -> None: ...
    def __enter__(self) -> ProgressBar[V]: ...
    def __exit__(self, exc_type: t.Type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None: ...
    def __iter__(self) -> t.Iterator[V]: ...
    def __next__(self) -> V: ...
    def render_finish(self) -> None: ...
    @property
    def pct(self) -> float: ...
    @property
    def time_per_iteration(self) -> float: ...
    @property
    def eta(self) -> float: ...
    def format_eta(self) -> str: ...
    def format_pos(self) -> str: ...
    def format_pct(self) -> str: ...
    def format_bar(self) -> str: ...
    def format_progress_line(self) -> str: ...
    def render_progress(self) -> None: ...
    def make_step(self, n_steps: int) -> None: ...
    def update(self, n_steps: int, current_item: V | None = None) -> None:
        """Update the progress bar by advancing a specified number of
        steps, and optionally set the ``current_item`` for this new
        position.

        :param n_steps: Number of steps to advance.
        :param current_item: Optional item to set as ``current_item``
            for the updated position.

        .. versionchanged:: 8.0
            Added the ``current_item`` optional parameter.

        .. versionchanged:: 8.0
            Only render when the number of steps meets the
            ``update_min_steps`` threshold.
        """
    def finish(self) -> None: ...
    def generator(self) -> t.Iterator[V]:
        """Return a generator which yields the items added to the bar
        during construction, and updates the progress bar *after* the
        yielded block returns.
        """

def pager(generator: t.Iterable[str], color: bool | None = None) -> None:
    """Decide what method to use for paging through text."""

class Editor:
    editor: Incomplete
    env: Incomplete
    require_save: Incomplete
    extension: Incomplete
    def __init__(self, editor: str | None = None, env: t.Mapping[str, str] | None = None, require_save: bool = True, extension: str = '.txt') -> None: ...
    def get_editor(self) -> str: ...
    def edit_file(self, filename: str) -> None: ...
    def edit(self, text: t.AnyStr | None) -> t.AnyStr | None: ...

def open_url(url: str, wait: bool = False, locate: bool = False) -> int: ...
def raw_terminal() -> t.Iterator[int]: ...
def getchar(echo: bool) -> str: ...
