__all__ = ['to_cupy', 'build_expression', 'evaluate_constants']

def to_cupy(array): ...
def build_expression(_, expr):
    """Build a cupy function based on ``arrays`` and ``expr``.
    """
def evaluate_constants(const_arrays, expr):
    """Convert constant arguments to cupy arrays, and perform any possible
    constant contractions.
    """
