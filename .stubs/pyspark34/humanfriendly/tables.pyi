from _typeshed import Incomplete

__all__ = ['format_pretty_table', 'format_robust_table', 'format_rst_table', 'format_smart_table']

def format_smart_table(data, column_names):
    """
    Render tabular data using the most appropriate representation.

    :param data: An iterable (e.g. a :func:`tuple` or :class:`list`)
                 containing the rows of the table, where each row is an
                 iterable containing the columns of the table (strings).
    :param column_names: An iterable of column names (strings).
    :returns: The rendered table (a string).

    If you want an easy way to render tabular data on a terminal in a human
    friendly format then this function is for you! It works as follows:

    - If the input data doesn't contain any line breaks the function
      :func:`format_pretty_table()` is used to render a pretty table. If the
      resulting table fits in the terminal without wrapping the rendered pretty
      table is returned.

    - If the input data does contain line breaks or if a pretty table would
      wrap (given the width of the terminal) then the function
      :func:`format_robust_table()` is used to render a more robust table that
      can deal with data containing line breaks and long text.
    """
def format_pretty_table(data, column_names: Incomplete | None = None, horizontal_bar: str = '-', vertical_bar: str = '|'):
    """
    Render a table using characters like dashes and vertical bars to emulate borders.

    :param data: An iterable (e.g. a :func:`tuple` or :class:`list`)
                 containing the rows of the table, where each row is an
                 iterable containing the columns of the table (strings).
    :param column_names: An iterable of column names (strings).
    :param horizontal_bar: The character used to represent a horizontal bar (a
                           string).
    :param vertical_bar: The character used to represent a vertical bar (a
                         string).
    :returns: The rendered table (a string).

    Here's an example:

    >>> from humanfriendly.tables import format_pretty_table
    >>> column_names = ['Version', 'Uploaded on', 'Downloads']
    >>> humanfriendly_releases = [
    ... ['1.23', '2015-05-25', '218'],
    ... ['1.23.1', '2015-05-26', '1354'],
    ... ['1.24', '2015-05-26', '223'],
    ... ['1.25', '2015-05-26', '4319'],
    ... ['1.25.1', '2015-06-02', '197'],
    ... ]
    >>> print(format_pretty_table(humanfriendly_releases, column_names))
    -------------------------------------
    | Version | Uploaded on | Downloads |
    -------------------------------------
    | 1.23    | 2015-05-25  |       218 |
    | 1.23.1  | 2015-05-26  |      1354 |
    | 1.24    | 2015-05-26  |       223 |
    | 1.25    | 2015-05-26  |      4319 |
    | 1.25.1  | 2015-06-02  |       197 |
    -------------------------------------

    Notes about the resulting table:

    - If a column contains numeric data (integer and/or floating point
      numbers) in all rows (ignoring column names of course) then the content
      of that column is right-aligned, as can be seen in the example above. The
      idea here is to make it easier to compare the numbers in different
      columns to each other.

    - The column names are highlighted in color so they stand out a bit more
      (see also :data:`.HIGHLIGHT_COLOR`). The following screen shot shows what
      that looks like (my terminals are always set to white text on a black
      background):

      .. image:: images/pretty-table.png
    """
def format_robust_table(data, column_names):
    """
    Render tabular data with one column per line (allowing columns with line breaks).

    :param data: An iterable (e.g. a :func:`tuple` or :class:`list`)
                 containing the rows of the table, where each row is an
                 iterable containing the columns of the table (strings).
    :param column_names: An iterable of column names (strings).
    :returns: The rendered table (a string).

    Here's an example:

    >>> from humanfriendly.tables import format_robust_table
    >>> column_names = ['Version', 'Uploaded on', 'Downloads']
    >>> humanfriendly_releases = [
    ... ['1.23', '2015-05-25', '218'],
    ... ['1.23.1', '2015-05-26', '1354'],
    ... ['1.24', '2015-05-26', '223'],
    ... ['1.25', '2015-05-26', '4319'],
    ... ['1.25.1', '2015-06-02', '197'],
    ... ]
    >>> print(format_robust_table(humanfriendly_releases, column_names))
    -----------------------
    Version: 1.23
    Uploaded on: 2015-05-25
    Downloads: 218
    -----------------------
    Version: 1.23.1
    Uploaded on: 2015-05-26
    Downloads: 1354
    -----------------------
    Version: 1.24
    Uploaded on: 2015-05-26
    Downloads: 223
    -----------------------
    Version: 1.25
    Uploaded on: 2015-05-26
    Downloads: 4319
    -----------------------
    Version: 1.25.1
    Uploaded on: 2015-06-02
    Downloads: 197
    -----------------------

    The column names are highlighted in bold font and color so they stand out a
    bit more (see :data:`.HIGHLIGHT_COLOR`).
    """
def format_rst_table(data, column_names: Incomplete | None = None):
    """
    Render a table in reStructuredText_ format.

    :param data: An iterable (e.g. a :func:`tuple` or :class:`list`)
                 containing the rows of the table, where each row is an
                 iterable containing the columns of the table (strings).
    :param column_names: An iterable of column names (strings).
    :returns: The rendered table (a string).

    Here's an example:

    >>> from humanfriendly.tables import format_rst_table
    >>> column_names = ['Version', 'Uploaded on', 'Downloads']
    >>> humanfriendly_releases = [
    ... ['1.23', '2015-05-25', '218'],
    ... ['1.23.1', '2015-05-26', '1354'],
    ... ['1.24', '2015-05-26', '223'],
    ... ['1.25', '2015-05-26', '4319'],
    ... ['1.25.1', '2015-06-02', '197'],
    ... ]
    >>> print(format_rst_table(humanfriendly_releases, column_names))
    =======  ===========  =========
    Version  Uploaded on  Downloads
    =======  ===========  =========
    1.23     2015-05-25   218
    1.23.1   2015-05-26   1354
    1.24     2015-05-26   223
    1.25     2015-05-26   4319
    1.25.1   2015-06-02   197
    =======  ===========  =========

    .. _reStructuredText: https://en.wikipedia.org/wiki/ReStructuredText
    """
