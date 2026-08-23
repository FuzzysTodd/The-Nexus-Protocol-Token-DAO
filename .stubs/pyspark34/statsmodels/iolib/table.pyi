from _typeshed import Incomplete
from statsmodels.compat.python import lmap as lmap, lrange as lrange

def csv2st(csvfile, headers: bool = False, stubs: bool = False, title: Incomplete | None = None):
    """Return SimpleTable instance,
    created from the data in `csvfile`,
    which is in comma separated values format.
    The first row may contain headers: set headers=True.
    The first column may contain stubs: set stubs=True.
    Can also supply headers and stubs as tuples of strings.
    """

class SimpleTable(list):
    '''Produce a simple ASCII, CSV, HTML, or LaTeX table from a
    *rectangular* (2d!) array of data, not necessarily numerical.
    Directly supports at most one header row,
    which should be the length of data[0].
    Directly supports at most one stubs column,
    which must be the length of data.
    (But see `insert_stubs` method.)
    See globals `default_txt_fmt`, `default_csv_fmt`, `default_html_fmt`,
    and `default_latex_fmt` for formatting options.

    Sample uses::

        mydata = [[11,12],[21,22]]  # data MUST be 2-dimensional
        myheaders = [ "Column 1", "Column 2" ]
        mystubs = [ "Row 1", "Row 2" ]
        tbl = text.SimpleTable(mydata, myheaders, mystubs, title="Title")
        print( tbl )
        print( tbl.as_html() )
        # set column specific data formatting
        tbl = text.SimpleTable(mydata, myheaders, mystubs,
            data_fmts=["%3.2f","%d"])
        print( tbl.as_csv() )
        with open(\'c:/temp/temp.tex\',\'w\') as fh:
            fh.write( tbl.as_latex_tabular() )
    '''
    title: Incomplete
    output_formats: Incomplete
    def __init__(self, data, headers: Incomplete | None = None, stubs: Incomplete | None = None, title: str = '', datatypes: Incomplete | None = None, csv_fmt: Incomplete | None = None, txt_fmt: Incomplete | None = None, ltx_fmt: Incomplete | None = None, html_fmt: Incomplete | None = None, celltype: Incomplete | None = None, rowtype: Incomplete | None = None, **fmt_dict) -> None:
        """
        Parameters
        ----------
        data : list of lists or 2d array (not matrix!)
            R rows by K columns of table elements
        headers : list (or tuple) of str
            sequence of K strings, one per header
        stubs : list (or tuple) of str
            sequence of R strings, one per stub
        title : str
            title of the table
        datatypes : list of int
            indexes to `data_fmts`
        txt_fmt : dict
            text formatting options
        ltx_fmt : dict
            latex formatting options
        csv_fmt : dict
            csv formatting options
        hmtl_fmt : dict
            hmtl formatting options
        celltype : class
            the cell class for the table (default: Cell)
        rowtype : class
            the row class for the table (default: Row)
        fmt_dict : dict
            general formatting options
        """
    def insert(self, idx, row, datatype: Incomplete | None = None) -> None:
        """Return None.  Insert a row into a table.
        """
    def insert_header_row(self, rownum, headers, dec_below: str = 'header_dec_below') -> None:
        """Return None.  Insert a row of headers,
        where ``headers`` is a sequence of strings.
        (The strings may contain newlines, to indicated multiline headers.)
        """
    def insert_stubs(self, loc, stubs) -> None:
        """Return None.  Insert column of stubs at column `loc`.
        If there is a header row, it gets an empty cell.
        So ``len(stubs)`` should equal the number of non-header rows.
        """
    def pad(self, s, width, align):
        """DEPRECATED: just use the pad function"""
    def get_colwidths(self, output_format, **fmt_dict):
        """Return list, the widths of each column."""
    def as_csv(self, **fmt_dict):
        """Return string, the table in CSV format.
        Currently only supports comma separator."""
    def as_text(self, **fmt_dict):
        """Return string, the table as text."""
    def as_html(self, **fmt_dict):
        """Return string.
        This is the default formatter for HTML tables.
        An HTML table formatter must accept as arguments
        a table and a format dictionary.
        """
    def as_latex_tabular(self, center: bool = True, **fmt_dict):
        """Return string, the table as a LaTeX tabular environment.
        Note: will require the booktabs package."""
    def extend_right(self, table) -> None:
        """Return None.
        Extend each row of `self` with corresponding row of `table`.
        Does **not** import formatting from ``table``.
        This generally makes sense only if the two tables have
        the same number of rows, but that is not enforced.
        :note: To extend append a table below, just use `extend`,
        which is the ordinary list method.  This generally makes sense
        only if the two tables have the same number of columns,
        but that is not enforced.
        """
    def label_cells(self, func) -> None:
        """Return None.  Labels cells based on `func`.
        If ``func(cell) is None`` then its datatype is
        not changed; otherwise it is set to ``func(cell)``.
        """
    @property
    def data(self): ...

def pad(s, width, align):
    """Return string padded with spaces,
    based on alignment parameter."""

class Row(list):
    """Provides a table row as a list of cells.
    A row can belong to a SimpleTable, but does not have to.
    """
    datatype: Incomplete
    table: Incomplete
    special_fmts: Incomplete
    dec_below: Incomplete
    def __init__(self, seq, datatype: str = 'data', table: Incomplete | None = None, celltype: Incomplete | None = None, dec_below: str = 'row_dec_below', **fmt_dict) -> None:
        """
        Parameters
        ----------
        seq : sequence of data or cells
        table : SimpleTable
        datatype : str ('data' or 'header')
        dec_below : str
          (e.g., 'header_dec_below' or 'row_dec_below')
          decoration tag, identifies the decoration to go below the row.
          (Decoration is repeated as needed for text formats.)
        """
    def add_format(self, output_format, **fmt_dict) -> None:
        """
        Return None. Adds row-instance specific formatting
        for the specified output format.
        Example: myrow.add_format('txt', row_dec_below='+-')
        """
    def insert_stub(self, loc, stub) -> None:
        """Return None.  Inserts a stub cell
        in the row at `loc`.
        """
    def get_aligns(self, output_format, **fmt_dict):
        """Return string, sequence of column alignments.
        Ensure comformable data_aligns in `fmt_dict`."""
    def as_string(self, output_format: str = 'txt', **fmt_dict):
        """Return string: the formatted row.
        This is the default formatter for rows.
        Override this to get different formatting.
        A row formatter must accept as arguments
        a row (self) and an output format,
        one of ('html', 'txt', 'csv', 'latex').
        """
    @property
    def data(self): ...

class Cell:
    """Provides a table cell.
    A cell can belong to a Row, but does not have to.
    """
    data: Incomplete
    row: Incomplete
    def __init__(self, data: str = '', datatype: Incomplete | None = None, row: Incomplete | None = None, **fmt_dict) -> None: ...
    def alignment(self, output_format, **fmt_dict): ...
    def format(self, width, output_format: str = 'txt', **fmt_dict):
        """Return string.
        This is the default formatter for cells.
        Override this to get different formating.
        A cell formatter must accept as arguments
        a cell (self) and an output format,
        one of ('html', 'txt', 'csv', 'latex').
        It will generally respond to the datatype,
        one of (int, 'header', 'stub').
        """
    def get_datatype(self): ...
    def set_datatype(self, val) -> None: ...
    datatype: Incomplete

default_txt_fmt: Incomplete
default_csv_fmt: Incomplete
default_html_fmt: Incomplete
default_latex_fmt: Incomplete
default_fmts: Incomplete
output_format_translations: Incomplete

def get_output_format(output_format): ...
