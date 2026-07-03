from _typeshed import Incomplete
from typing import Callable, Sequence, Tuple

__all__ = ['Munkres', 'make_cost_matrix', 'DISALLOWED']

class DISALLOWED_OBJ: ...

DISALLOWED: Incomplete

class UnsolvableMatrix(Exception):
    """
    Exception raised for unsolvable matrices
    """

class Munkres:
    """
    Calculate the Munkres solution to the classical assignment problem.
    See the module documentation for usage.
    """
    C: Incomplete
    row_covered: Incomplete
    col_covered: Incomplete
    n: int
    Z0_r: int
    Z0_c: int
    marked: Incomplete
    path: Incomplete
    def __init__(self) -> None:
        """Create a new instance"""
    def pad_matrix(self, matrix: Matrix, pad_value: int = 0) -> Matrix:
        """
        Pad a possibly non-square matrix to make it square.

        **Parameters**

        - `matrix` (list of lists of numbers): matrix to pad
        - `pad_value` (`int`): value to use to pad the matrix

        **Returns**

        a new, possibly padded, matrix
        """
    original_length: Incomplete
    original_width: Incomplete
    def compute(self, cost_matrix: Matrix) -> Sequence[Tuple[int, int]]:
        """
        Compute the indexes for the lowest-cost pairings between rows and
        columns in the database. Returns a list of `(row, column)` tuples
        that can be used to traverse the matrix.

        **WARNING**: This code handles square and rectangular matrices. It
        does *not* handle irregular matrices.

        **Parameters**

        - `cost_matrix` (list of lists of numbers): The cost matrix. If this
          cost matrix is not square, it will be padded with zeros, via a call
          to `pad_matrix()`. (This method does *not* modify the caller's
          matrix. It operates on a copy of the matrix.)


        **Returns**

        A list of `(row, column)` tuples that describe the lowest cost path
        through the matrix
        """

def make_cost_matrix(profit_matrix: Matrix, inversion_function: Callable[[AnyNum], AnyNum] | None = None) -> Matrix:
    """
    Create a cost matrix from a profit matrix by calling `inversion_function()`
    to invert each value. The inversion function must take one numeric argument
    (of any type) and return another numeric argument which is presumed to be
    the cost inverse of the original profit value. If the inversion function
    is not provided, a given cell's inverted value is calculated as
    `max(matrix) - value`.

    This is a static method. Call it like this:

        from munkres import Munkres
        cost_matrix = Munkres.make_cost_matrix(matrix, inversion_func)

    For example:

        from munkres import Munkres
        cost_matrix = Munkres.make_cost_matrix(matrix, lambda x : sys.maxsize - x)

    **Parameters**

    - `profit_matrix` (list of lists of numbers): The matrix to convert from
       profit to cost values.
    - `inversion_function` (`function`): The function to use to invert each
       entry in the profit matrix.

    **Returns**

    A new matrix representing the inversion of `profix_matrix`.
    """
