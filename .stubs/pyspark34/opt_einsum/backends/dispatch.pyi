from _typeshed import Incomplete

__all__ = ['get_func', 'has_einsum', 'has_tensordot', 'build_expression', 'evaluate_constants', 'has_backend']

def get_func(func, backend: str = 'numpy', default: Incomplete | None = None):
    """Return ``{backend}.{func}``, e.g. ``numpy.einsum``,
    or a default func if provided. Cache result.
    """
def has_einsum(backend):
    """Check if ``{backend}.einsum`` exists, cache result for performance.
    """
def has_tensordot(backend):
    """Check if ``{backend}.tensordot`` exists, cache result for performance.
    """
def build_expression(backend, arrays, expr):
    """Build an expression, based on ``expr`` and initial arrays ``arrays``,
    that evaluates using backend ``backend``.
    """
def evaluate_constants(backend, arrays, expr):
    """Convert constant arrays to the correct backend, and perform as much of
    the contraction of ``expr`` with these as possible.
    """
def has_backend(backend):
    """Checks if the backend is known.
    """
