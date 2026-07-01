from tensorflow.python.framework import composite_tensor as composite_tensor
from tensorflow.python.util import nest as nest

def flatten_with_variables(inputs):
    """Flattens `inputs` but don't expand `ResourceVariable`s."""
