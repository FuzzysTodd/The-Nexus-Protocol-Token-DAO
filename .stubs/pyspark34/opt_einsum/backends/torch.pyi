__all__ = ['transpose', 'einsum', 'tensordot', 'to_torch', 'build_expression', 'evaluate_constants']

def transpose(a, axes):
    """Normal torch transpose is only valid for 2D matrices.
    """
def einsum(equation, *operands):
    """Variadic version of torch.einsum to match numpy api.
    """
def tensordot(x, y, axes: int = 2):
    """Simple translation of tensordot syntax to einsum.
    """
def to_torch(array): ...
def build_expression(_, expr):
    """Build a torch function based on ``arrays`` and ``expr``.
    """
def evaluate_constants(const_arrays, expr):
    """Convert constant arguments to torch, and perform any possible constant
    contractions.
    """
