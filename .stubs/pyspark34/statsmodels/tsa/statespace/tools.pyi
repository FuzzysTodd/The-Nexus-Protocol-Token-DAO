from _typeshed import Incomplete
from statsmodels.compat.pandas import Appender as Appender

compatibility_mode: bool
has_trmm: bool
prefix_dtype_map: Incomplete
prefix_initialization_map: Incomplete
prefix_statespace_map: Incomplete
prefix_kalman_filter_map: Incomplete
prefix_kalman_smoother_map: Incomplete
prefix_simulation_smoother_map: Incomplete
prefix_cfa_simulation_smoother_map: Incomplete
prefix_pacf_map: Incomplete
prefix_sv_map: Incomplete
prefix_reorder_missing_matrix_map: Incomplete
prefix_reorder_missing_vector_map: Incomplete
prefix_copy_missing_matrix_map: Incomplete
prefix_copy_missing_vector_map: Incomplete
prefix_copy_index_matrix_map: Incomplete
prefix_copy_index_vector_map: Incomplete
prefix_compute_smoothed_state_weights_map: Incomplete

def set_mode(compatibility: Incomplete | None = None) -> None: ...
def companion_matrix(polynomial):
    """
    Create a companion matrix

    Parameters
    ----------
    polynomial : array_like or list
        If an iterable, interpreted as the coefficients of the polynomial from
        which to form the companion matrix. Polynomial coefficients are in
        order of increasing degree, and may be either scalars (as in an AR(p)
        model) or coefficient matrices (as in a VAR(p) model). If an integer,
        it is interpreted as the size of a companion matrix of a scalar
        polynomial, where the polynomial coefficients are initialized to zeros.
        If a matrix polynomial is passed, :math:`C_0` may be set to the scalar
        value 1 to indicate an identity matrix (doing so will improve the speed
        of the companion matrix creation).

    Returns
    -------
    companion_matrix : ndarray

    Notes
    -----
    Given coefficients of a lag polynomial of the form:

    .. math::

        c(L) = c_0 + c_1 L + \\dots + c_p L^p

    returns a matrix of the form

    .. math::
        \\begin{bmatrix}
            \\phi_1 & 1      & 0 & \\cdots & 0 \\\\\n            \\phi_2 & 0      & 1 &        & 0 \\\\\n            \\vdots &        &   & \\ddots & 0 \\\\\n                   &        &   &        & 1 \\\\\n            \\phi_n & 0      & 0 & \\cdots & 0 \\\\\n        \\end{bmatrix}

    where some or all of the :math:`\\phi_i` may be non-zero (if `polynomial` is
    None, then all are equal to zero).

    If the coefficients provided are scalars :math:`(c_0, c_1, \\dots, c_p)`,
    then the companion matrix is an :math:`n \\times n` matrix formed with the
    elements in the first column defined as
    :math:`\\phi_i = -\\frac{c_i}{c_0}, i \\in 1, \\dots, p`.

    If the coefficients provided are matrices :math:`(C_0, C_1, \\dots, C_p)`,
    each of shape :math:`(m, m)`, then the companion matrix is an
    :math:`nm \\times nm` matrix formed with the elements in the first column
    defined as :math:`\\phi_i = -C_0^{-1} C_i', i \\in 1, \\dots, p`.

    It is important to understand the expected signs of the coefficients. A
    typical AR(p) model is written as:

    .. math::
        y_t = a_1 y_{t-1} + \\dots + a_p y_{t-p} + \\varepsilon_t

    This can be rewritten as:

    .. math::
        (1 - a_1 L - \\dots - a_p L^p )y_t = \\varepsilon_t \\\\\n        (1 + c_1 L + \\dots + c_p L^p )y_t = \\varepsilon_t \\\\\n        c(L) y_t = \\varepsilon_t

    The coefficients from this form are defined to be :math:`c_i = - a_i`, and
    it is the :math:`c_i` coefficients that this function expects to be
    provided.
    """
def diff(series, k_diff: int = 1, k_seasonal_diff: Incomplete | None = None, seasonal_periods: int = 1):
    """
    Difference a series simply and/or seasonally along the zero-th axis.

    Given a series (denoted :math:`y_t`), performs the differencing operation

    .. math::

        \\Delta^d \\Delta_s^D y_t

    where :math:`d =` `diff`, :math:`s =` `seasonal_periods`,
    :math:`D =` `seasonal\\_diff`, and :math:`\\Delta` is the difference
    operator.

    Parameters
    ----------
    series : array_like
        The series to be differenced.
    k_diff : int, optional
        The number of simple differences to perform. Default is 1.
    k_seasonal_diff : int or None, optional
        The number of seasonal differences to perform. Default is no seasonal
        differencing.
    seasonal_periods : int, optional
        The seasonal lag. Default is 1. Unused if there is no seasonal
        differencing.

    Returns
    -------
    differenced : ndarray
        The differenced array.
    """
def concat(series, axis: int = 0, allow_mix: bool = False):
    """
    Concatenate a set of series.

    Parameters
    ----------
    series : iterable
        An iterable of series to be concatenated
    axis : int, optional
        The axis along which to concatenate. Default is 1 (columns).
    allow_mix : bool
        Whether or not to allow a mix of pandas and non-pandas objects. Default
        is False. If true, the returned object is an ndarray, and additional
        pandas metadata (e.g. column names, indices, etc) is lost.

    Returns
    -------
    concatenated : array or pd.DataFrame
        The concatenated array. Will be a DataFrame if series are pandas
        objects.
    """
def is_invertible(polynomial, threshold=...):
    """
    Determine if a polynomial is invertible.

    Requires all roots of the polynomial lie inside the unit circle.

    Parameters
    ----------
    polynomial : array_like or tuple, list
        Coefficients of a polynomial, in order of increasing degree.
        For example, `polynomial=[1, -0.5]` corresponds to the polynomial
        :math:`1 - 0.5x` which has root :math:`2`. If it is a matrix
        polynomial (in which case the coefficients are coefficient matrices),
        a tuple or list of matrices should be passed.
    threshold : number
        Allowed threshold for `is_invertible` to return True. Default is 1.

    See Also
    --------
    companion_matrix

    Notes
    -----

    If the coefficients provided are scalars :math:`(c_0, c_1, \\dots, c_n)`,
    then the corresponding polynomial is :math:`c_0 + c_1 L + \\dots + c_n L^n`.


    If the coefficients provided are matrices :math:`(C_0, C_1, \\dots, C_n)`,
    then the corresponding polynomial is :math:`C_0 + C_1 L + \\dots + C_n L^n`.

    There are three equivalent methods of determining if the polynomial
    represented by the coefficients is invertible:

    The first method factorizes the polynomial into:

    .. math::

        C(L) & = c_0 + c_1 L + \\dots + c_n L^n \\\\\n             & = constant (1 - \\lambda_1 L)
                 (1 - \\lambda_2 L) \\dots (1 - \\lambda_n L)

    In order for :math:`C(L)` to be invertible, it must be that each factor
    :math:`(1 - \\lambda_i L)` is invertible; the condition is then that
    :math:`|\\lambda_i| < 1`, where :math:`\\lambda_i` is a root of the
    polynomial.

    The second method factorizes the polynomial into:

    .. math::

        C(L) & = c_0 + c_1 L + \\dots + c_n L^n \\\\\n             & = constant (L - \\zeta_1) (L - \\zeta_2) \\dots (L - \\zeta_3)

    The condition is now :math:`|\\zeta_i| > 1`, where :math:`\\zeta_i` is a root
    of the polynomial with reversed coefficients and
    :math:`\\lambda_i = \\frac{1}{\\zeta_i}`.

    Finally, a companion matrix can be formed using the coefficients of the
    polynomial. Then the eigenvalues of that matrix give the roots of the
    polynomial. This last method is the one actually used.
    """
def solve_discrete_lyapunov(a, q, complex_step: bool = False):
    """
    Solves the discrete Lyapunov equation using a bilinear transformation.

    Notes
    -----
    This is a modification of the version in Scipy (see
    https://github.com/scipy/scipy/blob/master/scipy/linalg/_solvers.py)
    which allows passing through the complex numbers in the matrix a
    (usually the transition matrix) in order to allow complex step
    differentiation.
    """
def constrain_stationary_univariate(unconstrained):
    '''
    Transform unconstrained parameters used by the optimizer to constrained
    parameters used in likelihood evaluation

    Parameters
    ----------
    unconstrained : ndarray
        Unconstrained parameters used by the optimizer, to be transformed to
        stationary coefficients of, e.g., an autoregressive or moving average
        component.

    Returns
    -------
    constrained : ndarray
        Constrained parameters of, e.g., an autoregressive or moving average
        component, to be transformed to arbitrary parameters used by the
        optimizer.

    References
    ----------
    .. [*] Monahan, John F. 1984.
       "A Note on Enforcing Stationarity in
       Autoregressive-moving Average Models."
       Biometrika 71 (2) (August 1): 403-404.
    '''
def unconstrain_stationary_univariate(constrained):
    '''
    Transform constrained parameters used in likelihood evaluation
    to unconstrained parameters used by the optimizer

    Parameters
    ----------
    constrained : ndarray
        Constrained parameters of, e.g., an autoregressive or moving average
        component, to be transformed to arbitrary parameters used by the
        optimizer.

    Returns
    -------
    unconstrained : ndarray
        Unconstrained parameters used by the optimizer, to be transformed to
        stationary coefficients of, e.g., an autoregressive or moving average
        component.

    References
    ----------
    .. [*] Monahan, John F. 1984.
       "A Note on Enforcing Stationarity in
       Autoregressive-moving Average Models."
       Biometrika 71 (2) (August 1): 403-404.
    '''
def constrain_stationary_multivariate_python(unconstrained, error_variance, transform_variance: bool = False, prefix: Incomplete | None = None):
    '''
    Transform unconstrained parameters used by the optimizer to constrained
    parameters used in likelihood evaluation for a vector autoregression.

    Parameters
    ----------
    unconstrained : array or list
        Arbitrary matrices to be transformed to stationary coefficient matrices
        of the VAR. If a list, should be a list of length `order`, where each
        element is an array sized `k_endog` x `k_endog`. If an array, should be
        the matrices horizontally concatenated and sized
        `k_endog` x `k_endog * order`.
    error_variance : ndarray
        The variance / covariance matrix of the error term. Should be sized
        `k_endog` x `k_endog`. This is used as input in the algorithm even if
        is not transformed by it (when `transform_variance` is False). The
        error term variance is required input when transformation is used
        either to force an autoregressive component to be stationary or to
        force a moving average component to be invertible.
    transform_variance : bool, optional
        Whether or not to transform the error variance term. This option is
        not typically used, and the default is False.
    prefix : {\'s\',\'d\',\'c\',\'z\'}, optional
        The appropriate BLAS prefix to use for the passed datatypes. Only
        use if absolutely sure that the prefix is correct or an error will
        result.

    Returns
    -------
    constrained : array or list
        Transformed coefficient matrices leading to a stationary VAR
        representation. Will match the type of the passed `unconstrained`
        variable (so if a list was passed, a list will be returned).

    Notes
    -----
    In the notation of [1]_, the arguments `(variance, unconstrained)` are
    written as :math:`(\\Sigma, A_1, \\dots, A_p)`, where :math:`p` is the order
    of the vector autoregression, and is here determined by the length of
    the `unconstrained` argument.

    There are two steps in the constraining algorithm.

    First, :math:`(A_1, \\dots, A_p)` are transformed into
    :math:`(P_1, \\dots, P_p)` via Lemma 2.2 of [1]_.

    Second, :math:`(\\Sigma, P_1, \\dots, P_p)` are transformed into
    :math:`(\\Sigma, \\phi_1, \\dots, \\phi_p)` via Lemmas 2.1 and 2.3 of [1]_.

    If `transform_variance=True`, then only Lemma 2.1 is applied in the second
    step.

    While this function can be used even in the univariate case, it is much
    slower, so in that case `constrain_stationary_univariate` is preferred.

    References
    ----------
    .. [1] Ansley, Craig F., and Robert Kohn. 1986.
       "A Note on Reparameterizing a Vector Autoregressive Moving Average Model
       to Enforce Stationarity."
       Journal of Statistical Computation and Simulation 24 (2): 99-106.
    .. [*] Ansley, Craig F, and Paul Newbold. 1979.
       "Multivariate Partial Autocorrelations."
       In Proceedings of the Business and Economic Statistics Section, 349-53.
       American Statistical Association
    '''
def constrain_stationary_multivariate(unconstrained, variance, transform_variance: bool = False, prefix: Incomplete | None = None): ...
def unconstrain_stationary_multivariate(constrained, error_variance):
    '''
    Transform constrained parameters used in likelihood evaluation
    to unconstrained parameters used by the optimizer

    Parameters
    ----------
    constrained : array or list
        Constrained parameters of, e.g., an autoregressive or moving average
        component, to be transformed to arbitrary parameters used by the
        optimizer. If a list, should be a list of length `order`, where each
        element is an array sized `k_endog` x `k_endog`. If an array, should be
        the coefficient matrices horizontally concatenated and sized
        `k_endog` x `k_endog * order`.
    error_variance : ndarray
        The variance / covariance matrix of the error term. Should be sized
        `k_endog` x `k_endog`. This is used as input in the algorithm even if
        is not transformed by it (when `transform_variance` is False).

    Returns
    -------
    unconstrained : ndarray
        Unconstrained parameters used by the optimizer, to be transformed to
        stationary coefficients of, e.g., an autoregressive or moving average
        component. Will match the type of the passed `constrained`
        variable (so if a list was passed, a list will be returned).

    Notes
    -----
    Uses the list representation internally, even if an array is passed.

    References
    ----------
    .. [*] Ansley, Craig F., and Robert Kohn. 1986.
       "A Note on Reparameterizing a Vector Autoregressive Moving Average Model
       to Enforce Stationarity."
       Journal of Statistical Computation and Simulation 24 (2): 99-106.
    '''
def validate_matrix_shape(name, shape, nrows, ncols, nobs) -> None:
    """
    Validate the shape of a possibly time-varying matrix, or raise an exception

    Parameters
    ----------
    name : str
        The name of the matrix being validated (used in exception messages)
    shape : array_like
        The shape of the matrix to be validated. May be of size 2 or (if
        the matrix is time-varying) 3.
    nrows : int
        The expected number of rows.
    ncols : int
        The expected number of columns.
    nobs : int
        The number of observations (used to validate the last dimension of a
        time-varying matrix)

    Raises
    ------
    ValueError
        If the matrix is not of the desired shape.
    """
def validate_vector_shape(name, shape, nrows, nobs) -> None:
    """
    Validate the shape of a possibly time-varying vector, or raise an exception

    Parameters
    ----------
    name : str
        The name of the vector being validated (used in exception messages)
    shape : array_like
        The shape of the vector to be validated. May be of size 1 or (if
        the vector is time-varying) 2.
    nrows : int
        The expected number of rows (elements of the vector).
    nobs : int
        The number of observations (used to validate the last dimension of a
        time-varying vector)

    Raises
    ------
    ValueError
        If the vector is not of the desired shape.
    """
def reorder_missing_matrix(matrix, missing, reorder_rows: bool = False, reorder_cols: bool = False, is_diagonal: bool = False, inplace: bool = False, prefix: Incomplete | None = None):
    """
    Reorder the rows or columns of a time-varying matrix where all non-missing
    values are in the upper left corner of the matrix.

    Parameters
    ----------
    matrix : array_like
        The matrix to be reordered. Must have shape (n, m, nobs).
    missing : array_like of bool
        The vector of missing indices. Must have shape (k, nobs) where `k = n`
        if `reorder_rows is True` and `k = m` if `reorder_cols is True`.
    reorder_rows : bool, optional
        Whether or not the rows of the matrix should be re-ordered. Default
        is False.
    reorder_cols : bool, optional
        Whether or not the columns of the matrix should be re-ordered. Default
        is False.
    is_diagonal : bool, optional
        Whether or not the matrix is diagonal. If this is True, must also have
        `n = m`. Default is False.
    inplace : bool, optional
        Whether or not to reorder the matrix in-place.
    prefix : {'s', 'd', 'c', 'z'}, optional
        The Fortran prefix of the vector. Default is to automatically detect
        the dtype. This parameter should only be used with caution.

    Returns
    -------
    reordered_matrix : array_like
        The reordered matrix.
    """
def reorder_missing_vector(vector, missing, inplace: bool = False, prefix: Incomplete | None = None):
    """
    Reorder the elements of a time-varying vector where all non-missing
    values are in the first elements of the vector.

    Parameters
    ----------
    vector : array_like
        The vector to be reordered. Must have shape (n, nobs).
    missing : array_like of bool
        The vector of missing indices. Must have shape (n, nobs).
    inplace : bool, optional
        Whether or not to reorder the matrix in-place. Default is False.
    prefix : {'s', 'd', 'c', 'z'}, optional
        The Fortran prefix of the vector. Default is to automatically detect
        the dtype. This parameter should only be used with caution.

    Returns
    -------
    reordered_vector : array_like
        The reordered vector.
    """
def copy_missing_matrix(A, B, missing, missing_rows: bool = False, missing_cols: bool = False, is_diagonal: bool = False, inplace: bool = False, prefix: Incomplete | None = None):
    """
    Copy the rows or columns of a time-varying matrix where all non-missing
    values are in the upper left corner of the matrix.

    Parameters
    ----------
    A : array_like
        The matrix from which to copy. Must have shape (n, m, nobs) or
        (n, m, 1).
    B : array_like
        The matrix to copy to. Must have shape (n, m, nobs).
    missing : array_like of bool
        The vector of missing indices. Must have shape (k, nobs) where `k = n`
        if `reorder_rows is True` and `k = m` if `reorder_cols is True`.
    missing_rows : bool, optional
        Whether or not the rows of the matrix are a missing dimension. Default
        is False.
    missing_cols : bool, optional
        Whether or not the columns of the matrix are a missing dimension.
        Default is False.
    is_diagonal : bool, optional
        Whether or not the matrix is diagonal. If this is True, must also have
        `n = m`. Default is False.
    inplace : bool, optional
        Whether or not to copy to B in-place. Default is False.
    prefix : {'s', 'd', 'c', 'z'}, optional
        The Fortran prefix of the vector. Default is to automatically detect
        the dtype. This parameter should only be used with caution.

    Returns
    -------
    copied_matrix : array_like
        The matrix B with the non-missing submatrix of A copied onto it.
    """
def copy_missing_vector(a, b, missing, inplace: bool = False, prefix: Incomplete | None = None):
    """
    Reorder the elements of a time-varying vector where all non-missing
    values are in the first elements of the vector.

    Parameters
    ----------
    a : array_like
        The vector from which to copy. Must have shape (n, nobs) or (n, 1).
    b : array_like
        The vector to copy to. Must have shape (n, nobs).
    missing : array_like of bool
        The vector of missing indices. Must have shape (n, nobs).
    inplace : bool, optional
        Whether or not to copy to b in-place. Default is False.
    prefix : {'s', 'd', 'c', 'z'}, optional
        The Fortran prefix of the vector. Default is to automatically detect
        the dtype. This parameter should only be used with caution.

    Returns
    -------
    copied_vector : array_like
        The vector b with the non-missing subvector of b copied onto it.
    """
def copy_index_matrix(A, B, index, index_rows: bool = False, index_cols: bool = False, is_diagonal: bool = False, inplace: bool = False, prefix: Incomplete | None = None):
    """
    Copy the rows or columns of a time-varying matrix where all non-index
    values are in the upper left corner of the matrix.

    Parameters
    ----------
    A : array_like
        The matrix from which to copy. Must have shape (n, m, nobs) or
        (n, m, 1).
    B : array_like
        The matrix to copy to. Must have shape (n, m, nobs).
    index : array_like of bool
        The vector of index indices. Must have shape (k, nobs) where `k = n`
        if `reorder_rows is True` and `k = m` if `reorder_cols is True`.
    index_rows : bool, optional
        Whether or not the rows of the matrix are a index dimension. Default
        is False.
    index_cols : bool, optional
        Whether or not the columns of the matrix are a index dimension.
        Default is False.
    is_diagonal : bool, optional
        Whether or not the matrix is diagonal. If this is True, must also have
        `n = m`. Default is False.
    inplace : bool, optional
        Whether or not to copy to B in-place. Default is False.
    prefix : {'s', 'd', 'c', 'z'}, optional
        The Fortran prefix of the vector. Default is to automatically detect
        the dtype. This parameter should only be used with caution.

    Returns
    -------
    copied_matrix : array_like
        The matrix B with the non-index submatrix of A copied onto it.
    """
def copy_index_vector(a, b, index, inplace: bool = False, prefix: Incomplete | None = None):
    """
    Reorder the elements of a time-varying vector where all non-index
    values are in the first elements of the vector.

    Parameters
    ----------
    a : array_like
        The vector from which to copy. Must have shape (n, nobs) or (n, 1).
    b : array_like
        The vector to copy to. Must have shape (n, nobs).
    index : array_like of bool
        The vector of index indices. Must have shape (n, nobs).
    inplace : bool, optional
        Whether or not to copy to b in-place. Default is False.
    prefix : {'s', 'd', 'c', 'z'}, optional
        The Fortran prefix of the vector. Default is to automatically detect
        the dtype. This parameter should only be used with caution.

    Returns
    -------
    copied_vector : array_like
        The vector b with the non-index subvector of b copied onto it.
    """
def prepare_exog(exog): ...
def prepare_trend_spec(trend): ...
def prepare_trend_data(polynomial_trend, k_trend, nobs, offset: int = 1): ...
def compute_smoothed_state_weights(results, compute_t: Incomplete | None = None, compute_j: Incomplete | None = None, compute_prior_weights: Incomplete | None = None, resmooth: Incomplete | None = None):
    '''
    Construct the weights of observations and the prior on the smoothed state

    Parameters
    ----------
    results : MLEResults object
        Results object from fitting a state space model.
    compute_t : array_like, optional
        An explicit list of periods `t` of the smoothed state vector to compute
        weights for (see the Returns section for more details about the
        dimension `t`). Default is to compute weights for all periods `t`.
        However, if weights for only a few time points are desired, then
        performance can be improved by specifying this argument.
    compute_j : array_like, optional
        An explicit list of periods `j` of observations to compute
        weights for (see the Returns section for more details about the
        dimension `j`). Default is to compute weights for all periods `j`.
        However, if weights for only a few time points are desired, then
        performance can be improved by specifying this argument.
    compute_prior_weights : bool, optional
        Whether or not to compute the weight matrices associated with the prior
        mean (also called the "initial state"). Note that doing so requires
        that period 0 is in the periods defined in `compute_j`. Default is True
        if 0 is in `compute_j` (or if the `compute_j` argument is not passed)
        and False otherwise.
    resmooth : bool, optional
        Whether or not to re-perform filtering and smoothing prior to
        constructing the weights. Default is to resmooth if the smoothed_state
        vector is different between the given results object and the
        underlying smoother. Caution is adviced when changing this setting.
        See the Notes section below for more details.

    Returns
    -------
    weights : array_like
        Weight matrices that can be used to construct the smoothed state from
        the observations. The returned matrix is always shaped
        `(nobs, nobs, k_states, k_endog)`, and entries that are not computed
        are set to NaNs. (Entries will not be computed if they are not
        included in `compute_t` and `compute_j`, or if they correspond to
        missing observations, or if they are for periods in which the exact
        diffuse Kalman filter is operative). The `(t, j, m, p)`-th element of
        this matrix contains the weight of the `p`-th element of the
        observation vector at time `j` in constructing the `m`-th element of
        the smoothed state vector at time `t`.
    prior_weights : array_like
        Weight matrices that describe the impact of the prior (also called the
        initialization) on the smoothed state vector. The returned matrix is
        always shaped `(nobs, k_states, k_states)`. If prior weights are not
        computed, then all entries will be set to NaNs. The `(t, m, l)`-th
        element of this matrix contains the weight of the `l`-th element of the
        prior mean (also called the "initial state") in constructing the
        `m`-th element of the smoothed state vector at time `t`.

    Notes
    -----
    In [1]_, Chapter 4.8, it is shown how the smoothed state vector can be
    written as a weighted vector sum of observations:

    .. math::

        \\hat \\alpha_t = \\sum_{j=1}^n \\omega_{jt}^{\\hat \\alpha} y_j

    One output of this function is the weights
    :math:`\\omega_{jt}^{\\hat \\alpha}`. Note that the description in [1]_
    assumes that the prior mean (or "initial state") is fixed to be zero. More
    generally, the smoothed state vector will also depend partly on the prior.
    The second output of this function are the weights of the prior mean.

    There are two important technical notes about the computations used here:

    1. In the univariate approach to multivariate filtering (see e.g.
       Chapter 6.4 of [1]_), all observations are introduced one at a time,
       including those from the same time period. As a result, the weight of
       each observation can be different than when all observations from the
       same time point are introduced together, as in the typical multivariate
       filtering approach. Here, we always compute weights as in the
       multivariate filtering approach, and we handle singular forecast error
       covariance matrices by using a pseudo-inverse.
    2. Constructing observation weights for periods in which the exact diffuse
       filter (see e.g. Chapter 5 of [1]_) is operative is not done here, and
       so the corresponding entries in the returned weight matrices will always
       be set equal to zeros. While handling these periods may be implemented
       in the future, one option for constructing these weights is to use an
       approximate (instead of exact) diffuse initialization for this purpose.

    Finally, one note about implementation: to compute the weights, we use
    attributes of the underlying filtering and smoothing Cython objects
    directly. However, these objects are not frozen with the result
    computation, and we cannot guarantee that their attributes have not
    changed since `res` was created. As a result, by default we re-run the
    filter and smoother to ensure that the attributes there actually correspond
    to the `res` object. This can be overridden by the user for a small
    performance boost if they are sure that the attributes have not changed;
    see the `resmooth` argument.

    References
    ----------
    .. [1] Durbin, James, and Siem Jan Koopman. 2012.
            Time Series Analysis by State Space Methods: Second Edition.
            Oxford University Press.
    '''
def get_impact_dates(previous_model, updated_model, impact_date: Incomplete | None = None, start: Incomplete | None = None, end: Incomplete | None = None, periods: Incomplete | None = None):
    """
    Compute start/end periods and an index, often for impacts of data updates

    Parameters
    ----------
    previous_model : MLEModel
        Model used to compute default start/end periods if None are given.
        In the case of computing impacts of data updates, this would be the
        model estimated with the previous dataset. Otherwise, can be the same
        as `updated_model`.
    updated_model : MLEModel
        Model used to compute the index. In the case of computing impacts of
        data updates, this would be the model estimated with the updated
        dataset. Otherwise, can be the same as `previous_model`.
    impact_date : {int, str, datetime}, optional
        Specific individual impact date. Cannot be used in combination with
        `start`, `end`, or `periods`.
    start : {int, str, datetime}, optional
        Starting point of the impact dates. If given, one of `end` or `periods`
        must also be given. If a negative integer, will be computed relative to
        the dates in the `updated_model` index. Cannot be used in combination
        with `impact_date`.
    end : {int, str, datetime}, optional
        Ending point of the impact dates. If given, one of `start` or `periods`
        must also be given. If a negative integer, will be computed relative to
        the dates in the `updated_model` index. Cannot be used in combination
        with `impact_date`.
    periods : int, optional
        Number of impact date periods. If given, one of `start` or `end`
        must also be given. Cannot be used in combination with `impact_date`.

    Returns
    -------
    start : int
        Integer location of the first included impact dates.
    end : int
        Integer location of the last included impact dates (i.e. this integer
        location is included in the returned `index`).
    index : pd.Index
        Index associated with `start` and `end`, as computed from the
        `updated_model`'s index.

    Notes
    -----
    This function is typically used as a helper for standardizing start and
    end periods for a date range where the most sensible default values are
    based on some initial dataset (here contained in the `previous_model`),
    while index-related operations (especially relative start/end dates given
    via negative integers) are most sensibly computed from an updated dataset
    (here contained in the `updated_model`).

    """
