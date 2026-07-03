from _typeshed import Incomplete
from pandas import MultiIndex as MultiIndex, option_context as option_context
from pandas._config import get_option as get_option
from pandas._libs import lib as lib
from pandas.io.common import is_url as is_url
from pandas.io.formats.format import DataFrameFormatter as DataFrameFormatter, get_level_lengths as get_level_lengths
from pandas.io.formats.printing import pprint_thing as pprint_thing
from typing import Any, Final, Iterable

class HTMLFormatter:
    """
    Internal class for formatting output data in html.
    This class is intended for shared functionality between
    DataFrame.to_html() and DataFrame._repr_html_().
    Any logic in common with other output formatting methods
    should ideally be inherited from classes in format.py
    and this class responsible for only producing html markup.
    """
    indent_delta: Final[int]
    fmt: Incomplete
    classes: Incomplete
    frame: Incomplete
    columns: Incomplete
    elements: Incomplete
    bold_rows: Incomplete
    escape: Incomplete
    show_dimensions: Incomplete
    border: Incomplete
    table_id: Incomplete
    render_links: Incomplete
    col_space: Incomplete
    def __init__(self, formatter: DataFrameFormatter, classes: str | list[str] | tuple[str, ...] | None = None, border: int | bool | None = None, table_id: str | None = None, render_links: bool = False) -> None: ...
    def to_string(self) -> str: ...
    def render(self) -> list[str]: ...
    @property
    def should_show_dimensions(self) -> bool: ...
    @property
    def show_row_idx_names(self) -> bool: ...
    @property
    def show_col_idx_names(self) -> bool: ...
    @property
    def row_levels(self) -> int: ...
    @property
    def is_truncated(self) -> bool: ...
    @property
    def ncols(self) -> int: ...
    def write(self, s: Any, indent: int = 0) -> None: ...
    def write_th(self, s: Any, header: bool = False, indent: int = 0, tags: str | None = None) -> None:
        """
        Method for writing a formatted <th> cell.

        If col_space is set on the formatter then that is used for
        the value of min-width.

        Parameters
        ----------
        s : object
            The data to be written inside the cell.
        header : bool, default False
            Set to True if the <th> is for use inside <thead>.  This will
            cause min-width to be set if there is one.
        indent : int, default 0
            The indentation level of the cell.
        tags : str, default None
            Tags to include in the cell.

        Returns
        -------
        A written <th> cell.
        """
    def write_td(self, s: Any, indent: int = 0, tags: str | None = None) -> None: ...
    def write_tr(self, line: Iterable, indent: int = 0, indent_delta: int = 0, header: bool = False, align: str | None = None, tags: dict[int, str] | None = None, nindex_levels: int = 0) -> None: ...

class NotebookFormatter(HTMLFormatter):
    """
    Internal class for formatting output data in html for display in Jupyter
    Notebooks. This class is intended for functionality specific to
    DataFrame._repr_html_() and DataFrame.to_html(notebook=True)
    """
    def write_style(self) -> None: ...
    def render(self) -> list[str]: ...
