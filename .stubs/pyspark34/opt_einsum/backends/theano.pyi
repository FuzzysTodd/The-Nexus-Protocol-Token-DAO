__all__ = ['to_theano', 'build_expression', 'evaluate_constants']

def to_theano(array, constant: bool = False):
    """Convert a numpy array to ``theano.tensor.TensorType`` instance.
    """
def build_expression(arrays, expr):
    """Build a theano function based on ``arrays`` and ``expr``.
    """
def evaluate_constants(const_arrays, expr): ...
