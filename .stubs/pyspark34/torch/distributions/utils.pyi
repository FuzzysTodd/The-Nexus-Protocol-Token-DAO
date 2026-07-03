from _typeshed import Incomplete

__all__ = ['broadcast_all', 'logits_to_probs', 'clamp_probs', 'probs_to_logits', 'lazy_property', 'tril_matrix_to_vec', 'vec_to_tril_matrix']

def broadcast_all(*values):
    """
    Given a list of values (possibly containing numbers), returns a list where each
    value is broadcasted based on the following rules:
      - `torch.*Tensor` instances are broadcasted as per :ref:`_broadcasting-semantics`.
      - numbers.Number instances (scalars) are upcast to tensors having
        the same size and type as the first tensor passed to `values`.  If all the
        values are scalars, then they are upcasted to scalar Tensors.

    Args:
        values (list of `numbers.Number`, `torch.*Tensor` or objects implementing __torch_function__)

    Raises:
        ValueError: if any of the values is not a `numbers.Number` instance,
            a `torch.*Tensor` instance, or an instance implementing __torch_function__
    """
def logits_to_probs(logits, is_binary: bool = False):
    """
    Converts a tensor of logits into probabilities. Note that for the
    binary case, each value denotes log odds, whereas for the
    multi-dimensional case, the values along the last dimension denote
    the log probabilities (possibly unnormalized) of the events.
    """
def clamp_probs(probs): ...
def probs_to_logits(probs, is_binary: bool = False):
    """
    Converts a tensor of probabilities into logits. For the binary case,
    this denotes the probability of occurrence of the event indexed by `1`.
    For the multi-dimensional case, the values along the last dimension
    denote the probabilities of occurrence of each of the events.
    """

class lazy_property:
    """
    Used as a decorator for lazy loading of class attributes. This uses a
    non-data descriptor that calls the wrapped method to compute the property on
    first call; thereafter replacing the wrapped method into an instance
    attribute.
    """
    wrapped: Incomplete
    def __init__(self, wrapped) -> None: ...
    def __get__(self, instance, obj_type: Incomplete | None = None): ...

class _lazy_property_and_property(lazy_property, property):
    """We want lazy properties to look like multiple things.

    * property when Sphinx autodoc looks
    * lazy_property when Distribution validate_args looks
    """
    def __init__(self, wrapped) -> None: ...

def tril_matrix_to_vec(mat, diag: int = 0):
    """
    Convert a `D x D` matrix or a batch of matrices into a (batched) vector
    which comprises of lower triangular elements from the matrix in row order.
    """
def vec_to_tril_matrix(vec, diag: int = 0):
    """
    Convert a vector or a batch of vectors into a batched `D x D`
    lower triangular matrix containing elements from the vector in row order.
    """
