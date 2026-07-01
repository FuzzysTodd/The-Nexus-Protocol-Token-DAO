from .._config import config_context as config_context
from ..base import BaseEstimator as BaseEstimator, ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin, TransformerMixin as TransformerMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_array as check_array, check_random_state as check_random_state, gen_batches as gen_batches, metadata_routing as metadata_routing
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions, validate_params as validate_params
from ..utils.extmath import randomized_svd as randomized_svd, safe_sparse_dot as safe_sparse_dot, squared_norm as squared_norm
from ..utils.validation import check_is_fitted as check_is_fitted, check_non_negative as check_non_negative
from _typeshed import Incomplete
from abc import ABC

EPSILON: Incomplete

def norm(x):
    """Dot product-based Euclidean norm implementation.

    See: http://fa.bianp.net/blog/2011/computing-the-vector-norm/

    Parameters
    ----------
    x : array-like
        Vector for which to compute the norm.
    """
def trace_dot(X, Y):
    """Trace of np.dot(X, Y.T).

    Parameters
    ----------
    X : array-like
        First matrix.
    Y : array-like
        Second matrix.
    """
def non_negative_factorization(X, W: Incomplete | None = None, H: Incomplete | None = None, n_components: Incomplete | None = None, *, init: Incomplete | None = None, update_H: bool = True, solver: str = 'cd', beta_loss: str = 'frobenius', tol: float = 0.0001, max_iter: int = 200, alpha_W: float = 0.0, alpha_H: str = 'same', l1_ratio: float = 0.0, random_state: Incomplete | None = None, verbose: int = 0, shuffle: bool = False):
    '''Compute Non-negative Matrix Factorization (NMF).

    Find two non-negative matrices (W, H) whose product approximates the non-
    negative matrix X. This factorization can be used for example for
    dimensionality reduction, source separation or topic extraction.

    The objective function is:

        .. math::

            L(W, H) &= 0.5 * ||X - WH||_{loss}^2

            &+ alpha\\_W * l1\\_ratio * n\\_features * ||vec(W)||_1

            &+ alpha\\_H * l1\\_ratio * n\\_samples * ||vec(H)||_1

            &+ 0.5 * alpha\\_W * (1 - l1\\_ratio) * n\\_features * ||W||_{Fro}^2

            &+ 0.5 * alpha\\_H * (1 - l1\\_ratio) * n\\_samples * ||H||_{Fro}^2

    Where:

    :math:`||A||_{Fro}^2 = \\sum_{i,j} A_{ij}^2` (Frobenius norm)

    :math:`||vec(A)||_1 = \\sum_{i,j} abs(A_{ij})` (Elementwise L1 norm)

    The generic norm :math:`||X - WH||_{loss}^2` may represent
    the Frobenius norm or another supported beta-divergence loss.
    The choice between options is controlled by the `beta_loss` parameter.

    The regularization terms are scaled by `n_features` for `W` and by `n_samples` for
    `H` to keep their impact balanced with respect to one another and to the data fit
    term as independent as possible of the size `n_samples` of the training set.

    The objective function is minimized with an alternating minimization of W
    and H. If H is given and update_H=False, it solves for W only.

    Note that the transformed data is named W and the components matrix is named H. In
    the NMF literature, the naming convention is usually the opposite since the data
    matrix X is transposed.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Constant matrix.

    W : array-like of shape (n_samples, n_components), default=None
        If `init=\'custom\'`, it is used as initial guess for the solution.
        If `update_H=False`, it is initialised as an array of zeros, unless
        `solver=\'mu\'`, then it is filled with values calculated by
        `np.sqrt(X.mean() / self._n_components)`.
        If `None`, uses the initialisation method specified in `init`.

    H : array-like of shape (n_components, n_features), default=None
        If `init=\'custom\'`, it is used as initial guess for the solution.
        If `update_H=False`, it is used as a constant, to solve for W only.
        If `None`, uses the initialisation method specified in `init`.

    n_components : int, default=None
        Number of components, if n_components is not set all features
        are kept.

    init : {\'random\', \'nndsvd\', \'nndsvda\', \'nndsvdar\', \'custom\'}, default=None
        Method used to initialize the procedure.

        Valid options:

        - None: \'nndsvda\' if n_components < n_features, otherwise \'random\'.
        - \'random\': non-negative random matrices, scaled with:
          `sqrt(X.mean() / n_components)`
        - \'nndsvd\': Nonnegative Double Singular Value Decomposition (NNDSVD)
          initialization (better for sparseness)
        - \'nndsvda\': NNDSVD with zeros filled with the average of X
          (better when sparsity is not desired)
        - \'nndsvdar\': NNDSVD with zeros filled with small random values
          (generally faster, less accurate alternative to NNDSVDa
          for when sparsity is not desired)
        - \'custom\': If `update_H=True`, use custom matrices W and H which must both
          be provided. If `update_H=False`, then only custom matrix H is used.

        .. versionchanged:: 0.23
            The default value of `init` changed from \'random\' to None in 0.23.

        .. versionchanged:: 1.1
            When `init=None` and n_components is less than n_samples and n_features
            defaults to `nndsvda` instead of `nndsvd`.

    update_H : bool, default=True
        Set to True, both W and H will be estimated from initial guesses.
        Set to False, only W will be estimated.

    solver : {\'cd\', \'mu\'}, default=\'cd\'
        Numerical solver to use:

        - \'cd\' is a Coordinate Descent solver that uses Fast Hierarchical
          Alternating Least Squares (Fast HALS).
        - \'mu\' is a Multiplicative Update solver.

        .. versionadded:: 0.17
           Coordinate Descent solver.

        .. versionadded:: 0.19
           Multiplicative Update solver.

    beta_loss : float or {\'frobenius\', \'kullback-leibler\',             \'itakura-saito\'}, default=\'frobenius\'
        Beta divergence to be minimized, measuring the distance between X
        and the dot product WH. Note that values different from \'frobenius\'
        (or 2) and \'kullback-leibler\' (or 1) lead to significantly slower
        fits. Note that for beta_loss <= 0 (or \'itakura-saito\'), the input
        matrix X cannot contain zeros. Used only in \'mu\' solver.

        .. versionadded:: 0.19

    tol : float, default=1e-4
        Tolerance of the stopping condition.

    max_iter : int, default=200
        Maximum number of iterations before timing out.

    alpha_W : float, default=0.0
        Constant that multiplies the regularization terms of `W`. Set it to zero
        (default) to have no regularization on `W`.

        .. versionadded:: 1.0

    alpha_H : float or "same", default="same"
        Constant that multiplies the regularization terms of `H`. Set it to zero to
        have no regularization on `H`. If "same" (default), it takes the same value as
        `alpha_W`.

        .. versionadded:: 1.0

    l1_ratio : float, default=0.0
        The regularization mixing parameter, with 0 <= l1_ratio <= 1.
        For l1_ratio = 0 the penalty is an elementwise L2 penalty
        (aka Frobenius Norm).
        For l1_ratio = 1 it is an elementwise L1 penalty.
        For 0 < l1_ratio < 1, the penalty is a combination of L1 and L2.

    random_state : int, RandomState instance or None, default=None
        Used for NMF initialisation (when ``init`` == \'nndsvdar\' or
        \'random\'), and in Coordinate Descent. Pass an int for reproducible
        results across multiple function calls.
        See :term:`Glossary <random_state>`.

    verbose : int, default=0
        The verbosity level.

    shuffle : bool, default=False
        If true, randomize the order of coordinates in the CD solver.

    Returns
    -------
    W : ndarray of shape (n_samples, n_components)
        Solution to the non-negative least squares problem.

    H : ndarray of shape (n_components, n_features)
        Solution to the non-negative least squares problem.

    n_iter : int
        Actual number of iterations.

    References
    ----------
    .. [1] :doi:`"Fast local algorithms for large scale nonnegative matrix and tensor
       factorizations" <10.1587/transfun.E92.A.708>`
       Cichocki, Andrzej, and P. H. A. N. Anh-Huy. IEICE transactions on fundamentals
       of electronics, communications and computer sciences 92.3: 708-721, 2009.

    .. [2] :doi:`"Algorithms for nonnegative matrix factorization with the
       beta-divergence" <10.1162/NECO_a_00168>`
       Fevotte, C., & Idier, J. (2011). Neural Computation, 23(9).

    Examples
    --------
    >>> import numpy as np
    >>> X = np.array([[1,1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
    >>> from sklearn.decomposition import non_negative_factorization
    >>> W, H, n_iter = non_negative_factorization(
    ...     X, n_components=2, init=\'random\', random_state=0)
    '''

class _BaseNMF(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator, ABC):
    """Base class for NMF and MiniBatchNMF."""
    n_components: Incomplete
    init: Incomplete
    beta_loss: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    random_state: Incomplete
    alpha_W: Incomplete
    alpha_H: Incomplete
    l1_ratio: Incomplete
    verbose: Incomplete
    def __init__(self, n_components: Incomplete | None = None, *, init: Incomplete | None = None, beta_loss: str = 'frobenius', tol: float = 0.0001, max_iter: int = 200, random_state: Incomplete | None = None, alpha_W: float = 0.0, alpha_H: str = 'same', l1_ratio: float = 0.0, verbose: int = 0) -> None: ...
    def fit(self, X, y: Incomplete | None = None, **params):
        """Learn a NMF model for the data X.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : Ignored
            Not used, present for API consistency by convention.

        **params : kwargs
            Parameters (keyword arguments) and values passed to
            the fit_transform instance.

        Returns
        -------
        self : object
            Returns the instance itself.
        """
    def inverse_transform(self, Xt: Incomplete | None = None, W: Incomplete | None = None):
        """Transform data back to its original space.

        .. versionadded:: 0.18

        Parameters
        ----------
        Xt : {ndarray, sparse matrix} of shape (n_samples, n_components)
            Transformed data matrix.

        W : deprecated
            Use `Xt` instead.

            .. deprecated:: 1.3

        Returns
        -------
        X : {ndarray, sparse matrix} of shape (n_samples, n_features)
            Returns a data matrix of the original shape.
        """

class NMF(_BaseNMF):
    '''Non-Negative Matrix Factorization (NMF).

    Find two non-negative matrices, i.e. matrices with all non-negative elements, (W, H)
    whose product approximates the non-negative matrix X. This factorization can be used
    for example for dimensionality reduction, source separation or topic extraction.

    The objective function is:

        .. math::

            L(W, H) &= 0.5 * ||X - WH||_{loss}^2

            &+ alpha\\_W * l1\\_ratio * n\\_features * ||vec(W)||_1

            &+ alpha\\_H * l1\\_ratio * n\\_samples * ||vec(H)||_1

            &+ 0.5 * alpha\\_W * (1 - l1\\_ratio) * n\\_features * ||W||_{Fro}^2

            &+ 0.5 * alpha\\_H * (1 - l1\\_ratio) * n\\_samples * ||H||_{Fro}^2

    Where:

    :math:`||A||_{Fro}^2 = \\sum_{i,j} A_{ij}^2` (Frobenius norm)

    :math:`||vec(A)||_1 = \\sum_{i,j} abs(A_{ij})` (Elementwise L1 norm)

    The generic norm :math:`||X - WH||_{loss}` may represent
    the Frobenius norm or another supported beta-divergence loss.
    The choice between options is controlled by the `beta_loss` parameter.

    The regularization terms are scaled by `n_features` for `W` and by `n_samples` for
    `H` to keep their impact balanced with respect to one another and to the data fit
    term as independent as possible of the size `n_samples` of the training set.

    The objective function is minimized with an alternating minimization of W
    and H.

    Note that the transformed data is named W and the components matrix is named H. In
    the NMF literature, the naming convention is usually the opposite since the data
    matrix X is transposed.

    Read more in the :ref:`User Guide <NMF>`.

    Parameters
    ----------
    n_components : int, default=None
        Number of components, if n_components is not set all features
        are kept.

    init : {\'random\', \'nndsvd\', \'nndsvda\', \'nndsvdar\', \'custom\'}, default=None
        Method used to initialize the procedure.
        Valid options:

        - `None`: \'nndsvda\' if n_components <= min(n_samples, n_features),
          otherwise random.

        - `\'random\'`: non-negative random matrices, scaled with:
          `sqrt(X.mean() / n_components)`

        - `\'nndsvd\'`: Nonnegative Double Singular Value Decomposition (NNDSVD)
          initialization (better for sparseness)

        - `\'nndsvda\'`: NNDSVD with zeros filled with the average of X
          (better when sparsity is not desired)

        - `\'nndsvdar\'` NNDSVD with zeros filled with small random values
          (generally faster, less accurate alternative to NNDSVDa
          for when sparsity is not desired)

        - `\'custom\'`: Use custom matrices `W` and `H` which must both be provided.

        .. versionchanged:: 1.1
            When `init=None` and n_components is less than n_samples and n_features
            defaults to `nndsvda` instead of `nndsvd`.

    solver : {\'cd\', \'mu\'}, default=\'cd\'
        Numerical solver to use:

        - \'cd\' is a Coordinate Descent solver.
        - \'mu\' is a Multiplicative Update solver.

        .. versionadded:: 0.17
           Coordinate Descent solver.

        .. versionadded:: 0.19
           Multiplicative Update solver.

    beta_loss : float or {\'frobenius\', \'kullback-leibler\',             \'itakura-saito\'}, default=\'frobenius\'
        Beta divergence to be minimized, measuring the distance between X
        and the dot product WH. Note that values different from \'frobenius\'
        (or 2) and \'kullback-leibler\' (or 1) lead to significantly slower
        fits. Note that for beta_loss <= 0 (or \'itakura-saito\'), the input
        matrix X cannot contain zeros. Used only in \'mu\' solver.

        .. versionadded:: 0.19

    tol : float, default=1e-4
        Tolerance of the stopping condition.

    max_iter : int, default=200
        Maximum number of iterations before timing out.

    random_state : int, RandomState instance or None, default=None
        Used for initialisation (when ``init`` == \'nndsvdar\' or
        \'random\'), and in Coordinate Descent. Pass an int for reproducible
        results across multiple function calls.
        See :term:`Glossary <random_state>`.

    alpha_W : float, default=0.0
        Constant that multiplies the regularization terms of `W`. Set it to zero
        (default) to have no regularization on `W`.

        .. versionadded:: 1.0

    alpha_H : float or "same", default="same"
        Constant that multiplies the regularization terms of `H`. Set it to zero to
        have no regularization on `H`. If "same" (default), it takes the same value as
        `alpha_W`.

        .. versionadded:: 1.0

    l1_ratio : float, default=0.0
        The regularization mixing parameter, with 0 <= l1_ratio <= 1.
        For l1_ratio = 0 the penalty is an elementwise L2 penalty
        (aka Frobenius Norm).
        For l1_ratio = 1 it is an elementwise L1 penalty.
        For 0 < l1_ratio < 1, the penalty is a combination of L1 and L2.

        .. versionadded:: 0.17
           Regularization parameter *l1_ratio* used in the Coordinate Descent
           solver.

    verbose : int, default=0
        Whether to be verbose.

    shuffle : bool, default=False
        If true, randomize the order of coordinates in the CD solver.

        .. versionadded:: 0.17
           *shuffle* parameter used in the Coordinate Descent solver.

    Attributes
    ----------
    components_ : ndarray of shape (n_components, n_features)
        Factorization matrix, sometimes called \'dictionary\'.

    n_components_ : int
        The number of components. It is same as the `n_components` parameter
        if it was given. Otherwise, it will be same as the number of
        features.

    reconstruction_err_ : float
        Frobenius norm of the matrix difference, or beta-divergence, between
        the training data ``X`` and the reconstructed data ``WH`` from
        the fitted model.

    n_iter_ : int
        Actual number of iterations.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    DictionaryLearning : Find a dictionary that sparsely encodes data.
    MiniBatchSparsePCA : Mini-batch Sparse Principal Components Analysis.
    PCA : Principal component analysis.
    SparseCoder : Find a sparse representation of data from a fixed,
        precomputed dictionary.
    SparsePCA : Sparse Principal Components Analysis.
    TruncatedSVD : Dimensionality reduction using truncated SVD.

    References
    ----------
    .. [1] :doi:`"Fast local algorithms for large scale nonnegative matrix and tensor
       factorizations" <10.1587/transfun.E92.A.708>`
       Cichocki, Andrzej, and P. H. A. N. Anh-Huy. IEICE transactions on fundamentals
       of electronics, communications and computer sciences 92.3: 708-721, 2009.

    .. [2] :doi:`"Algorithms for nonnegative matrix factorization with the
       beta-divergence" <10.1162/NECO_a_00168>`
       Fevotte, C., & Idier, J. (2011). Neural Computation, 23(9).

    Examples
    --------
    >>> import numpy as np
    >>> X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
    >>> from sklearn.decomposition import NMF
    >>> model = NMF(n_components=2, init=\'random\', random_state=0)
    >>> W = model.fit_transform(X)
    >>> H = model.components_
    '''
    solver: Incomplete
    shuffle: Incomplete
    def __init__(self, n_components: Incomplete | None = None, *, init: Incomplete | None = None, solver: str = 'cd', beta_loss: str = 'frobenius', tol: float = 0.0001, max_iter: int = 200, random_state: Incomplete | None = None, alpha_W: float = 0.0, alpha_H: str = 'same', l1_ratio: float = 0.0, verbose: int = 0, shuffle: bool = False) -> None: ...
    reconstruction_err_: Incomplete
    n_components_: Incomplete
    components_: Incomplete
    n_iter_: Incomplete
    def fit_transform(self, X, y: Incomplete | None = None, W: Incomplete | None = None, H: Incomplete | None = None):
        """Learn a NMF model for the data X and returns the transformed data.

        This is more efficient than calling fit followed by transform.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : Ignored
            Not used, present for API consistency by convention.

        W : array-like of shape (n_samples, n_components), default=None
            If `init='custom'`, it is used as initial guess for the solution.
            If `None`, uses the initialisation method specified in `init`.

        H : array-like of shape (n_components, n_features), default=None
            If `init='custom'`, it is used as initial guess for the solution.
            If `None`, uses the initialisation method specified in `init`.

        Returns
        -------
        W : ndarray of shape (n_samples, n_components)
            Transformed data.
        """
    def transform(self, X):
        """Transform the data X according to the fitted NMF model.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        Returns
        -------
        W : ndarray of shape (n_samples, n_components)
            Transformed data.
        """

class MiniBatchNMF(_BaseNMF):
    '''Mini-Batch Non-Negative Matrix Factorization (NMF).

    .. versionadded:: 1.1

    Find two non-negative matrices, i.e. matrices with all non-negative elements,
    (`W`, `H`) whose product approximates the non-negative matrix `X`. This
    factorization can be used for example for dimensionality reduction, source
    separation or topic extraction.

    The objective function is:

        .. math::

            L(W, H) &= 0.5 * ||X - WH||_{loss}^2

            &+ alpha\\_W * l1\\_ratio * n\\_features * ||vec(W)||_1

            &+ alpha\\_H * l1\\_ratio * n\\_samples * ||vec(H)||_1

            &+ 0.5 * alpha\\_W * (1 - l1\\_ratio) * n\\_features * ||W||_{Fro}^2

            &+ 0.5 * alpha\\_H * (1 - l1\\_ratio) * n\\_samples * ||H||_{Fro}^2

    Where:

    :math:`||A||_{Fro}^2 = \\sum_{i,j} A_{ij}^2` (Frobenius norm)

    :math:`||vec(A)||_1 = \\sum_{i,j} abs(A_{ij})` (Elementwise L1 norm)

    The generic norm :math:`||X - WH||_{loss}^2` may represent
    the Frobenius norm or another supported beta-divergence loss.
    The choice between options is controlled by the `beta_loss` parameter.

    The objective function is minimized with an alternating minimization of `W`
    and `H`.

    Note that the transformed data is named `W` and the components matrix is
    named `H`. In the NMF literature, the naming convention is usually the opposite
    since the data matrix `X` is transposed.

    Read more in the :ref:`User Guide <MiniBatchNMF>`.

    Parameters
    ----------
    n_components : int, default=None
        Number of components, if `n_components` is not set all features
        are kept.

    init : {\'random\', \'nndsvd\', \'nndsvda\', \'nndsvdar\', \'custom\'}, default=None
        Method used to initialize the procedure.
        Valid options:

        - `None`: \'nndsvda\' if `n_components <= min(n_samples, n_features)`,
          otherwise random.

        - `\'random\'`: non-negative random matrices, scaled with:
          `sqrt(X.mean() / n_components)`

        - `\'nndsvd\'`: Nonnegative Double Singular Value Decomposition (NNDSVD)
          initialization (better for sparseness).

        - `\'nndsvda\'`: NNDSVD with zeros filled with the average of X
          (better when sparsity is not desired).

        - `\'nndsvdar\'` NNDSVD with zeros filled with small random values
          (generally faster, less accurate alternative to NNDSVDa
          for when sparsity is not desired).

        - `\'custom\'`: Use custom matrices `W` and `H` which must both be provided.

    batch_size : int, default=1024
        Number of samples in each mini-batch. Large batch sizes
        give better long-term convergence at the cost of a slower start.

    beta_loss : float or {\'frobenius\', \'kullback-leibler\',             \'itakura-saito\'}, default=\'frobenius\'
        Beta divergence to be minimized, measuring the distance between `X`
        and the dot product `WH`. Note that values different from \'frobenius\'
        (or 2) and \'kullback-leibler\' (or 1) lead to significantly slower
        fits. Note that for `beta_loss <= 0` (or \'itakura-saito\'), the input
        matrix `X` cannot contain zeros.

    tol : float, default=1e-4
        Control early stopping based on the norm of the differences in `H`
        between 2 steps. To disable early stopping based on changes in `H`, set
        `tol` to 0.0.

    max_no_improvement : int, default=10
        Control early stopping based on the consecutive number of mini batches
        that does not yield an improvement on the smoothed cost function.
        To disable convergence detection based on cost function, set
        `max_no_improvement` to None.

    max_iter : int, default=200
        Maximum number of iterations over the complete dataset before
        timing out.

    alpha_W : float, default=0.0
        Constant that multiplies the regularization terms of `W`. Set it to zero
        (default) to have no regularization on `W`.

    alpha_H : float or "same", default="same"
        Constant that multiplies the regularization terms of `H`. Set it to zero to
        have no regularization on `H`. If "same" (default), it takes the same value as
        `alpha_W`.

    l1_ratio : float, default=0.0
        The regularization mixing parameter, with 0 <= l1_ratio <= 1.
        For l1_ratio = 0 the penalty is an elementwise L2 penalty
        (aka Frobenius Norm).
        For l1_ratio = 1 it is an elementwise L1 penalty.
        For 0 < l1_ratio < 1, the penalty is a combination of L1 and L2.

    forget_factor : float, default=0.7
        Amount of rescaling of past information. Its value could be 1 with
        finite datasets. Choosing values < 1 is recommended with online
        learning as more recent batches will weight more than past batches.

    fresh_restarts : bool, default=False
        Whether to completely solve for W at each step. Doing fresh restarts will likely
        lead to a better solution for a same number of iterations but it is much slower.

    fresh_restarts_max_iter : int, default=30
        Maximum number of iterations when solving for W at each step. Only used when
        doing fresh restarts. These iterations may be stopped early based on a small
        change of W controlled by `tol`.

    transform_max_iter : int, default=None
        Maximum number of iterations when solving for W at transform time.
        If None, it defaults to `max_iter`.

    random_state : int, RandomState instance or None, default=None
        Used for initialisation (when ``init`` == \'nndsvdar\' or
        \'random\'), and in Coordinate Descent. Pass an int for reproducible
        results across multiple function calls.
        See :term:`Glossary <random_state>`.

    verbose : bool, default=False
        Whether to be verbose.

    Attributes
    ----------
    components_ : ndarray of shape (n_components, n_features)
        Factorization matrix, sometimes called \'dictionary\'.

    n_components_ : int
        The number of components. It is same as the `n_components` parameter
        if it was given. Otherwise, it will be same as the number of
        features.

    reconstruction_err_ : float
        Frobenius norm of the matrix difference, or beta-divergence, between
        the training data `X` and the reconstructed data `WH` from
        the fitted model.

    n_iter_ : int
        Actual number of started iterations over the whole dataset.

    n_steps_ : int
        Number of mini-batches processed.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

    See Also
    --------
    NMF : Non-negative matrix factorization.
    MiniBatchDictionaryLearning : Finds a dictionary that can best be used to represent
        data using a sparse code.

    References
    ----------
    .. [1] :doi:`"Fast local algorithms for large scale nonnegative matrix and tensor
       factorizations" <10.1587/transfun.E92.A.708>`
       Cichocki, Andrzej, and P. H. A. N. Anh-Huy. IEICE transactions on fundamentals
       of electronics, communications and computer sciences 92.3: 708-721, 2009.

    .. [2] :doi:`"Algorithms for nonnegative matrix factorization with the
       beta-divergence" <10.1162/NECO_a_00168>`
       Fevotte, C., & Idier, J. (2011). Neural Computation, 23(9).

    .. [3] :doi:`"Online algorithms for nonnegative matrix factorization with the
       Itakura-Saito divergence" <10.1109/ASPAA.2011.6082314>`
       Lefevre, A., Bach, F., Fevotte, C. (2011). WASPA.

    Examples
    --------
    >>> import numpy as np
    >>> X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
    >>> from sklearn.decomposition import MiniBatchNMF
    >>> model = MiniBatchNMF(n_components=2, init=\'random\', random_state=0)
    >>> W = model.fit_transform(X)
    >>> H = model.components_
    '''
    max_no_improvement: Incomplete
    batch_size: Incomplete
    forget_factor: Incomplete
    fresh_restarts: Incomplete
    fresh_restarts_max_iter: Incomplete
    transform_max_iter: Incomplete
    def __init__(self, n_components: Incomplete | None = None, *, init: Incomplete | None = None, batch_size: int = 1024, beta_loss: str = 'frobenius', tol: float = 0.0001, max_no_improvement: int = 10, max_iter: int = 200, alpha_W: float = 0.0, alpha_H: str = 'same', l1_ratio: float = 0.0, forget_factor: float = 0.7, fresh_restarts: bool = False, fresh_restarts_max_iter: int = 30, transform_max_iter: Incomplete | None = None, random_state: Incomplete | None = None, verbose: int = 0) -> None: ...
    reconstruction_err_: Incomplete
    n_components_: Incomplete
    components_: Incomplete
    n_iter_: Incomplete
    n_steps_: Incomplete
    def fit_transform(self, X, y: Incomplete | None = None, W: Incomplete | None = None, H: Incomplete | None = None):
        """Learn a NMF model for the data X and returns the transformed data.

        This is more efficient than calling fit followed by transform.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data matrix to be decomposed.

        y : Ignored
            Not used, present here for API consistency by convention.

        W : array-like of shape (n_samples, n_components), default=None
            If `init='custom'`, it is used as initial guess for the solution.
            If `None`, uses the initialisation method specified in `init`.

        H : array-like of shape (n_components, n_features), default=None
            If `init='custom'`, it is used as initial guess for the solution.
            If `None`, uses the initialisation method specified in `init`.

        Returns
        -------
        W : ndarray of shape (n_samples, n_components)
            Transformed data.
        """
    def transform(self, X):
        """Transform the data X according to the fitted MiniBatchNMF model.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data matrix to be transformed by the model.

        Returns
        -------
        W : ndarray of shape (n_samples, n_components)
            Transformed data.
        """
    def partial_fit(self, X, y: Incomplete | None = None, W: Incomplete | None = None, H: Incomplete | None = None):
        """Update the model using the data in `X` as a mini-batch.

        This method is expected to be called several times consecutively
        on different chunks of a dataset so as to implement out-of-core
        or online learning.

        This is especially useful when the whole dataset is too big to fit in
        memory at once (see :ref:`scaling_strategies`).

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data matrix to be decomposed.

        y : Ignored
            Not used, present here for API consistency by convention.

        W : array-like of shape (n_samples, n_components), default=None
            If `init='custom'`, it is used as initial guess for the solution.
            Only used for the first call to `partial_fit`.

        H : array-like of shape (n_components, n_features), default=None
            If `init='custom'`, it is used as initial guess for the solution.
            Only used for the first call to `partial_fit`.

        Returns
        -------
        self
            Returns the instance itself.
        """
