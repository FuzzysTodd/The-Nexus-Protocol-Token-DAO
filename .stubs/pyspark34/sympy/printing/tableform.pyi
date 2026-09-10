from sympy.core.containers import Tuple as Tuple
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import SympifyError as SympifyError

class TableForm:
    """
    Create a nice table representation of data.

    Examples
    ========

    >>> from sympy import TableForm
    >>> t = TableForm([[5, 7], [4, 2], [10, 3]])
    >>> print(t)
    5  7
    4  2
    10 3

    You can use the SymPy's printing system to produce tables in any
    format (ascii, latex, html, ...).

    >>> print(t.as_latex())
    \\begin{tabular}{l l}
    $5$ & $7$ \\\\\n    $4$ & $2$ \\\\\n    $10$ & $3$ \\\\\n    \\end{tabular}

    """
    def __init__(self, data, **kwarg) -> None:
        '''
        Creates a TableForm.

        Parameters:

            data ...
                            2D data to be put into the table; data can be
                            given as a Matrix

            headings ...
                            gives the labels for rows and columns:

                            Can be a single argument that applies to both
                            dimensions:

                                - None ... no labels
                                - "automatic" ... labels are 1, 2, 3, ...

                            Can be a list of labels for rows and columns:
                            The labels for each dimension can be given
                            as None, "automatic", or [l1, l2, ...] e.g.
                            ["automatic", None] will number the rows

                            [default: None]

            alignments ...
                            alignment of the columns with:

                                - "left" or "<"
                                - "center" or "^"
                                - "right" or ">"

                            When given as a single value, the value is used for
                            all columns. The row headings (if given) will be
                            right justified unless an explicit alignment is
                            given for it and all other columns.

                            [default: "left"]

            formats ...
                            a list of format strings or functions that accept
                            3 arguments (entry, row number, col number) and
                            return a string for the table entry. (If a function
                            returns None then the _print method will be used.)

            wipe_zeros ...
                            Do not show zeros in the table.

                            [default: True]

            pad ...
                            the string to use to indicate a missing value (e.g.
                            elements that are None or those that are missing
                            from the end of a row (i.e. any row that is shorter
                            than the rest is assumed to have missing values).
                            When None, nothing will be shown for values that
                            are missing from the end of a row; values that are
                            None, however, will be shown.

                            [default: None]

        Examples
        ========

        >>> from sympy import TableForm, Symbol
        >>> TableForm([[5, 7], [4, 2], [10, 3]])
        5  7
        4  2
        10 3
        >>> TableForm([list(\'.\'*i) for i in range(1, 4)], headings=\'automatic\')
          | 1 2 3
        ---------
        1 | .
        2 | . .
        3 | . . .
        >>> TableForm([[Symbol(\'.\'*(j if not i%2 else 1)) for i in range(3)]
        ...            for j in range(4)], alignments=\'rcl\')
            .
          . . .
         .. . ..
        ... . ...
        '''
    def as_matrix(self):
        """Returns the data of the table in Matrix form.

        Examples
        ========

        >>> from sympy import TableForm
        >>> t = TableForm([[5, 7], [4, 2], [10, 3]], headings='automatic')
        >>> t
          | 1  2
        --------
        1 | 5  7
        2 | 4  2
        3 | 10 3
        >>> t.as_matrix()
        Matrix([
        [ 5, 7],
        [ 4, 2],
        [10, 3]])
        """
    def as_str(self): ...
    def as_latex(self): ...
