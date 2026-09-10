__all__ = ['numpy_ndarray', 'scipy_sparse_matrix', 'sympy_to_numpy', 'sympy_to_scipy_sparse', 'numpy_to_sympy', 'scipy_sparse_to_sympy', 'flatten_scalar', 'matrix_dagger', 'to_sympy', 'to_numpy', 'to_scipy_sparse', 'matrix_tensor_product', 'matrix_zeros']

class numpy_ndarray: ...
class scipy_sparse_matrix: ...

def sympy_to_numpy(m, **options):
    """Convert a SymPy Matrix/complex number to a numpy matrix or scalar."""
def sympy_to_scipy_sparse(m, **options):
    """Convert a SymPy Matrix/complex number to a numpy matrix or scalar."""
def scipy_sparse_to_sympy(m, **options):
    """Convert a scipy.sparse matrix to a SymPy matrix."""
def numpy_to_sympy(m, **options):
    """Convert a numpy matrix to a SymPy matrix."""
def to_sympy(m, **options):
    """Convert a numpy/scipy.sparse matrix to a SymPy matrix."""
def to_numpy(m, **options):
    """Convert a sympy/scipy.sparse matrix to a numpy matrix."""
def to_scipy_sparse(m, **options):
    """Convert a sympy/numpy matrix to a scipy.sparse matrix."""
def flatten_scalar(e):
    """Flatten a 1x1 matrix to a scalar, return larger matrices unchanged."""
def matrix_dagger(e):
    """Return the dagger of a sympy/numpy/scipy.sparse matrix."""
def matrix_tensor_product(*product):
    """Compute the matrix tensor product of sympy/numpy/scipy.sparse matrices."""
def matrix_zeros(m, n, **options):
    '''"Get a zeros matrix for a given format.'''
