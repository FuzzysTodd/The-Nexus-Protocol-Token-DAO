from . import check_random_state as check_random_state
from ._array_api import get_namespace as get_namespace
from .sparsefuncs_fast import csr_row_norms as csr_row_norms
from .validation import check_array as check_array
from _typeshed import Incomplete

def squared_norm(x):
    """Squared Euclidean or Frobenius norm of x.

    Faster than norm(x) ** 2.

    Parameters
    ----------
    x : array-like
        The input array which could be either be a vector or a 2 dimensional array.

    Returns
    -------
    float
        The Euclidean norm when x is a vector, the Frobenius norm when x
        is a matrix (2-d array).
    """
def row_norms(X, squared: bool = False):
    """Row-wise (squared) Euclidean norm of X.

    Equivalent to np.sqrt((X * X).sum(axis=1)), but also supports sparse
    matrices and does not create an X.shape-sized temporary.

    Performs no input validation.

    Parameters
    ----------
    X : array-like
        The input array.
    squared : bool, default=False
        If True, return squared norms.

    Returns
    -------
    array-like
        The row-wise (squared) Euclidean norm of X.
    """
def fast_logdet(A):
    """Compute logarithm of determinant of a square matrix.

    The (natural) logarithm of the determinant of a square matrix
    is returned if det(A) is non-negative and well defined.
    If the determinant is zero or negative returns -Inf.

    Equivalent to : np.log(np.det(A)) but more robust.

    Parameters
    ----------
    A : array_like of shape (n, n)
        The square matrix.

    Returns
    -------
    logdet : float
        When det(A) is strictly positive, log(det(A)) is returned.
        When det(A) is non-positive or not defined, then -inf is returned.

    See Also
    --------
    numpy.linalg.slogdet : Compute the sign and (natural) logarithm of the determinant
        of an array.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.utils.extmath import fast_logdet
    >>> a = np.array([[5, 1], [2, 8]])
    >>> fast_logdet(a)
    3.6375861597263857
    """
def density(w, **kwargs):
    """Compute density of a sparse vector.

    Parameters
    ----------
    w : array-like
        The sparse vector.
    **kwargs : keyword arguments
        Ignored.

        .. deprecated:: 1.2
            ``**kwargs`` were deprecated in version 1.2 and will be removed in
            1.4.

    Returns
    -------
    float
        The density of w, between 0 and 1.
    """
def safe_sparse_dot(a, b, *, dense_output: bool = False):
    """Dot product that handle the sparse matrix case correctly.

    Parameters
    ----------
    a : {ndarray, sparse matrix}
    b : {ndarray, sparse matrix}
    dense_output : bool, default=False
        When False, ``a`` and ``b`` both being sparse will yield sparse output.
        When True, output will always be a dense array.

    Returns
    -------
    dot_product : {ndarray, sparse matrix}
        Sparse if ``a`` and ``b`` are sparse and ``dense_output=False``.
    """
def randomized_range_finder(A, *, size, n_iter, power_iteration_normalizer: str = 'auto', random_state: Incomplete | None = None):
    '''Compute an orthonormal matrix whose range approximates the range of A.

    Parameters
    ----------
    A : 2D array
        The input data matrix.

    size : int
        Size of the return array.

    n_iter : int
        Number of power iterations used to stabilize the result.

    power_iteration_normalizer : {\'auto\', \'QR\', \'LU\', \'none\'}, default=\'auto\'
        Whether the power iterations are normalized with step-by-step
        QR factorization (the slowest but most accurate), \'none\'
        (the fastest but numerically unstable when `n_iter` is large, e.g.
        typically 5 or larger), or \'LU\' factorization (numerically stable
        but can lose slightly in accuracy). The \'auto\' mode applies no
        normalization if `n_iter` <= 2 and switches to LU otherwise.

        .. versionadded:: 0.18

    random_state : int, RandomState instance or None, default=None
        The seed of the pseudo random number generator to use when shuffling
        the data, i.e. getting the random vectors to initialize the algorithm.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    Q : ndarray
        A (size x size) projection matrix, the range of which
        approximates well the range of the input matrix A.

    Notes
    -----

    Follows Algorithm 4.3 of
    :arxiv:`"Finding structure with randomness:
    Stochastic algorithms for constructing approximate matrix decompositions"
    <0909.4061>`
    Halko, et al. (2009)

    An implementation of a randomized algorithm for principal component
    analysis
    A. Szlam et al. 2014
    '''
def randomized_svd(M, n_components, *, n_oversamples: int = 10, n_iter: str = 'auto', power_iteration_normalizer: str = 'auto', transpose: str = 'auto', flip_sign: bool = True, random_state: Incomplete | None = None, svd_lapack_driver: str = 'gesdd'):
    '''Compute a truncated randomized SVD.

    This method solves the fixed-rank approximation problem described in [1]_
    (problem (1.5), p5).

    Parameters
    ----------
    M : {ndarray, sparse matrix}
        Matrix to decompose.

    n_components : int
        Number of singular values and vectors to extract.

    n_oversamples : int, default=10
        Additional number of random vectors to sample the range of M so as
        to ensure proper conditioning. The total number of random vectors
        used to find the range of M is n_components + n_oversamples. Smaller
        number can improve speed but can negatively impact the quality of
        approximation of singular vectors and singular values. Users might wish
        to increase this parameter up to `2*k - n_components` where k is the
        effective rank, for large matrices, noisy problems, matrices with
        slowly decaying spectrums, or to increase precision accuracy. See [1]_
        (pages 5, 23 and 26).

    n_iter : int or \'auto\', default=\'auto\'
        Number of power iterations. It can be used to deal with very noisy
        problems. When \'auto\', it is set to 4, unless `n_components` is small
        (< .1 * min(X.shape)) in which case `n_iter` is set to 7.
        This improves precision with few components. Note that in general
        users should rather increase `n_oversamples` before increasing `n_iter`
        as the principle of the randomized method is to avoid usage of these
        more costly power iterations steps. When `n_components` is equal
        or greater to the effective matrix rank and the spectrum does not
        present a slow decay, `n_iter=0` or `1` should even work fine in theory
        (see [1]_ page 9).

        .. versionchanged:: 0.18

    power_iteration_normalizer : {\'auto\', \'QR\', \'LU\', \'none\'}, default=\'auto\'
        Whether the power iterations are normalized with step-by-step
        QR factorization (the slowest but most accurate), \'none\'
        (the fastest but numerically unstable when `n_iter` is large, e.g.
        typically 5 or larger), or \'LU\' factorization (numerically stable
        but can lose slightly in accuracy). The \'auto\' mode applies no
        normalization if `n_iter` <= 2 and switches to LU otherwise.

        .. versionadded:: 0.18

    transpose : bool or \'auto\', default=\'auto\'
        Whether the algorithm should be applied to M.T instead of M. The
        result should approximately be the same. The \'auto\' mode will
        trigger the transposition if M.shape[1] > M.shape[0] since this
        implementation of randomized SVD tend to be a little faster in that
        case.

        .. versionchanged:: 0.18

    flip_sign : bool, default=True
        The output of a singular value decomposition is only unique up to a
        permutation of the signs of the singular vectors. If `flip_sign` is
        set to `True`, the sign ambiguity is resolved by making the largest
        loadings for each component in the left singular vectors positive.

    random_state : int, RandomState instance or None, default=\'warn\'
        The seed of the pseudo random number generator to use when
        shuffling the data, i.e. getting the random vectors to initialize
        the algorithm. Pass an int for reproducible results across multiple
        function calls. See :term:`Glossary <random_state>`.

        .. versionchanged:: 1.2
            The default value changed from 0 to None.

    svd_lapack_driver : {"gesdd", "gesvd"}, default="gesdd"
        Whether to use the more efficient divide-and-conquer approach
        (`"gesdd"`) or more general rectangular approach (`"gesvd"`) to compute
        the SVD of the matrix B, which is the projection of M into a low
        dimensional subspace, as described in [1]_.

        .. versionadded:: 1.2

    Returns
    -------
    u : ndarray of shape (n_samples, n_components)
        Unitary matrix having left singular vectors with signs flipped as columns.
    s : ndarray of shape (n_components,)
        The singular values, sorted in non-increasing order.
    vh : ndarray of shape (n_components, n_features)
        Unitary matrix having right singular vectors with signs flipped as rows.

    Notes
    -----
    This algorithm finds a (usually very good) approximate truncated
    singular value decomposition using randomization to speed up the
    computations. It is particularly fast on large matrices on which
    you wish to extract only a small number of components. In order to
    obtain further speed up, `n_iter` can be set <=2 (at the cost of
    loss of precision). To increase the precision it is recommended to
    increase `n_oversamples`, up to `2*k-n_components` where k is the
    effective rank. Usually, `n_components` is chosen to be greater than k
    so increasing `n_oversamples` up to `n_components` should be enough.

    References
    ----------
    .. [1] :arxiv:`"Finding structure with randomness:
      Stochastic algorithms for constructing approximate matrix decompositions"
      <0909.4061>`
      Halko, et al. (2009)

    .. [2] A randomized algorithm for the decomposition of matrices
      Per-Gunnar Martinsson, Vladimir Rokhlin and Mark Tygert

    .. [3] An implementation of a randomized algorithm for principal component
      analysis A. Szlam et al. 2014

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.utils.extmath import randomized_svd
    >>> a = np.array([[1, 2, 3, 5],
    ...               [3, 4, 5, 6],
    ...               [7, 8, 9, 10]])
    >>> U, s, Vh = randomized_svd(a, n_components=2, random_state=0)
    >>> U.shape, s.shape, Vh.shape
    ((3, 2), (2,), (2, 4))
    '''
def weighted_mode(a, w, *, axis: int = 0):
    """Return an array of the weighted modal (most common) value in the passed array.

    If there is more than one such value, only the first is returned.
    The bin-count for the modal bins is also returned.

    This is an extension of the algorithm in scipy.stats.mode.

    Parameters
    ----------
    a : array-like of shape (n_samples,)
        Array of which values to find mode(s).
    w : array-like of shape (n_samples,)
        Array of weights for each value.
    axis : int, default=0
        Axis along which to operate. Default is 0, i.e. the first axis.

    Returns
    -------
    vals : ndarray
        Array of modal values.
    score : ndarray
        Array of weighted counts for each mode.

    See Also
    --------
    scipy.stats.mode: Calculates the Modal (most common) value of array elements
        along specified axis.

    Examples
    --------
    >>> from sklearn.utils.extmath import weighted_mode
    >>> x = [4, 1, 4, 2, 4, 2]
    >>> weights = [1, 1, 1, 1, 1, 1]
    >>> weighted_mode(x, weights)
    (array([4.]), array([3.]))

    The value 4 appears three times: with uniform weights, the result is
    simply the mode of the distribution.

    >>> weights = [1, 3, 0.5, 1.5, 1, 2]  # deweight the 4's
    >>> weighted_mode(x, weights)
    (array([2.]), array([3.5]))

    The value 2 has the highest score: it appears twice with weights of
    1.5 and 2: the sum of these is 3.5.
    """
def cartesian(arrays, out: Incomplete | None = None):
    """Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray of shape (M, len(arrays)), default=None
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray of shape (M, len(arrays))
        Array containing the cartesian products formed of input arrays.
        If not provided, the `dtype` of the output array is set to the most
        permissive `dtype` of the input arrays, according to NumPy type
        promotion.

        .. versionadded:: 1.2
           Add support for arrays of different types.

    Notes
    -----
    This function may not be used on more than 32 arrays
    because the underlying numpy functions do not support it.

    Examples
    --------
    >>> from sklearn.utils.extmath import cartesian
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])
    """
def svd_flip(u, v, u_based_decision: bool = True):
    """Sign correction to ensure deterministic output from SVD.

    Adjusts the columns of u and the rows of v such that the loadings in the
    columns in u that are largest in absolute value are always positive.

    Parameters
    ----------
    u : ndarray
        Parameters u and v are the output of `linalg.svd` or
        :func:`~sklearn.utils.extmath.randomized_svd`, with matching inner
        dimensions so one can compute `np.dot(u * s, v)`.

    v : ndarray
        Parameters u and v are the output of `linalg.svd` or
        :func:`~sklearn.utils.extmath.randomized_svd`, with matching inner
        dimensions so one can compute `np.dot(u * s, v)`.
        The input v should really be called vt to be consistent with scipy's
        output.

    u_based_decision : bool, default=True
        If True, use the columns of u as the basis for sign flipping.
        Otherwise, use the rows of v. The choice of which variable to base the
        decision on is generally algorithm dependent.

    Returns
    -------
    u_adjusted : ndarray
        Array u with adjusted columns and the same dimensions as u.

    v_adjusted : ndarray
        Array v with adjusted rows and the same dimensions as v.
    """
def log_logistic(X, out: Incomplete | None = None):
    """Compute the log of the logistic function, ``log(1 / (1 + e ** -x))``.

    This implementation is numerically stable because it splits positive and
    negative values::

        -log(1 + exp(-x_i))     if x_i > 0
        x_i - log(1 + exp(x_i)) if x_i <= 0

    For the ordinary logistic function, use ``scipy.special.expit``.

    Parameters
    ----------
    X : array-like of shape (M, N) or (M,)
        Argument to the logistic function.

    out : array-like of shape (M, N) or (M,), default=None
        Preallocated output array.

    Returns
    -------
    out : ndarray of shape (M, N) or (M,)
        Log of the logistic function evaluated at every point in x.

    Notes
    -----
    See the blog post describing this implementation:
    http://fa.bianp.net/blog/2013/numerical-optimizers-for-logistic-regression/
    """
def softmax(X, copy: bool = True):
    """
    Calculate the softmax function.

    The softmax function is calculated by
    np.exp(X) / np.sum(np.exp(X), axis=1)

    This will cause overflow when large values are exponentiated.
    Hence the largest value in each row is subtracted from each data
    point to prevent this.

    Parameters
    ----------
    X : array-like of float of shape (M, N)
        Argument to the logistic function.

    copy : bool, default=True
        Copy X or not.

    Returns
    -------
    out : ndarray of shape (M, N)
        Softmax function evaluated at every point in x.
    """
def make_nonnegative(X, min_value: int = 0):
    """Ensure `X.min()` >= `min_value`.

    Parameters
    ----------
    X : array-like
        The matrix to make non-negative.
    min_value : float, default=0
        The threshold value.

    Returns
    -------
    array-like
        The thresholded array.

    Raises
    ------
    ValueError
        When X is sparse.
    """
def stable_cumsum(arr, axis: Incomplete | None = None, rtol: float = 1e-05, atol: float = 1e-08):
    """Use high precision for cumsum and check that final value matches sum.

    Warns if the final cumulative sum does not match the sum (up to the chosen
    tolerance).

    Parameters
    ----------
    arr : array-like
        To be cumulatively summed as flat.
    axis : int, default=None
        Axis along which the cumulative sum is computed.
        The default (None) is to compute the cumsum over the flattened array.
    rtol : float, default=1e-05
        Relative tolerance, see ``np.allclose``.
    atol : float, default=1e-08
        Absolute tolerance, see ``np.allclose``.

    Returns
    -------
    out : ndarray
        Array with the cumulative sums along the chosen axis.
    """
