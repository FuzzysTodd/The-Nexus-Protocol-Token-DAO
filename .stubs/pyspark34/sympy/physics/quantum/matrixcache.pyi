from _typeshed import Incomplete
from sympy.core.numbers import I as I, Rational as Rational, pi as pi
from sympy.core.power import Pow as Pow
from sympy.functions.elementary.exponential import exp as exp
from sympy.matrices.dense import Matrix as Matrix
from sympy.physics.quantum.matrixutils import to_numpy as to_numpy, to_scipy_sparse as to_scipy_sparse, to_sympy as to_sympy

class MatrixCache:
    """A cache for small matrices in different formats.

    This class takes small matrices in the standard ``sympy.Matrix`` format,
    and then converts these to both ``numpy.matrix`` and
    ``scipy.sparse.csr_matrix`` matrices. These matrices are then stored for
    future recovery.
    """
    dtype: Incomplete
    def __init__(self, dtype: str = 'complex') -> None: ...
    def cache_matrix(self, name, m) -> None:
        '''Cache a matrix by its name.

        Parameters
        ----------
        name : str
            A descriptive name for the matrix, like "identity2".
        m : list of lists
            The raw matrix data as a SymPy Matrix.
        '''
    def get_matrix(self, name, format):
        '''Get a cached matrix by name and format.

        Parameters
        ----------
        name : str
            A descriptive name for the matrix, like "identity2".
        format : str
            The format desired (\'sympy\', \'numpy\', \'scipy.sparse\')
        '''

sqrt2_inv: Incomplete
matrix_cache: Incomplete
