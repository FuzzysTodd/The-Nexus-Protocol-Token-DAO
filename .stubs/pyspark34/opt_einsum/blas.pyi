from _typeshed import Incomplete

__all__ = ['can_blas', 'tensor_blas']

def can_blas(inputs, result, idx_removed, shapes: Incomplete | None = None):
    '''
    Checks if we can use a BLAS call.

    Parameters
    ----------
    inputs : list of str
        Specifies the subscripts for summation.
    result : str
        Resulting summation.
    idx_removed : set
        Indices that are removed in the summation
    shapes : sequence of tuple[int], optional
        If given, check also that none of the indices are broadcast dimensions.

    Returns
    -------
    type : str or bool
        The type of BLAS call to be used or False if none.

    Notes
    -----
    We assume several operations are not efficient such as a transposed
    DDOT, therefore \'ijk,jki->\' should prefer einsum. These return the blas
    type appended with "/EINSUM" to differentiate when they can still be done
    with tensordot if required, e.g. when a backend has no einsum.

    Examples
    --------
    >>> can_blas([\'ij\', \'jk\'], \'ik\', set(\'j\'))
    \'GEMM\'

    >>> can_blas([\'ijj\', \'jk\'], \'ik\', set(\'j\'))
    False

    >>> can_blas([\'ab\', \'cd\'], \'abcd\', set())
    \'OUTER/EINSUM\'

    >>> # looks like GEMM but actually \'j\' is broadcast:
    >>> can_blas([\'ij\', \'jk\'], \'ik\', set(\'j\'), shapes=[(4, 1), (5, 6)])
    False
    '''
def tensor_blas(view_left, input_left, view_right, input_right, index_result, idx_removed):
    """
    Computes the dot product between two tensors, attempts to use np.dot and
    then tensordot if that fails.

    Parameters
    ----------
    view_left : array_like
        The left hand view
    input_left : str
        Indices of the left view
    view_right : array_like
        The right hand view
    input_right : str
        Indices of the right view
    index_result : str
        The resulting indices
    idx_removed : set
        Indices removed in the contraction

    Returns
    -------
    type : array
        The resulting BLAS operation.

    Notes
    -----
    Interior function for tensor BLAS.

    This function will attempt to use `np.dot` by the iterating through the
    four possible transpose cases. If this fails all inner and matrix-vector
    operations will be handed off to einsum while all matrix-matrix operations will
    first copy the data, perform the DGEMM, and then copy the data to the required
    order.

    Examples
    --------

    >>> a = np.random.rand(4, 4)
    >>> b = np.random.rand(4, 4)
    >>> tmp = tensor_blas(a, 'ij', b, 'jk', 'ik', set('j'))
    >>> np.allclose(tmp, np.dot(a, b))

    """
