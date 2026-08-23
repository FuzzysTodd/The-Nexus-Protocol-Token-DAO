__all__ = ['to_tensorflow', 'build_expression', 'evaluate_constants']

def to_tensorflow(array, constant: bool = False):
    """Convert a numpy array to a ``tensorflow.placeholder`` instance.
    """
def build_expression(arrays, expr): ...
def evaluate_constants(const_arrays, expr): ...
