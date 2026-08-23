from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, MultiOutputMixin, RegressorMixin, TransformerMixin
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

__all__ = ['PLSCanonical', 'PLSRegression', 'PLSSVD']

class _PLS(ClassNamePrefixFeaturesOutMixin, TransformerMixin, RegressorMixin, MultiOutputMixin, BaseEstimator, metaclass=ABCMeta):
    """Partial Least Squares (PLS)

    This class implements the generic PLS algorithm.

    Main ref: Wegelin, a survey of Partial Least Squares (PLS) methods,
    with emphasis on the two-block case
    https://stat.uw.edu/sites/default/files/files/reports/2000/tr371.pdf
    """
    n_components: Incomplete
    deflation_mode: Incomplete
    mode: Incomplete
    scale: Incomplete
    algorithm: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    copy: Incomplete
    @abstractmethod
    def __init__(self, n_components: int = 2, *, scale: bool = True, deflation_mode: str = 'regression', mode: str = 'A', algorithm: str = 'nipals', max_iter: int = 500, tol: float = 1e-06, copy: bool = True): ...
    x_weights_: Incomplete
    y_weights_: Incomplete
    x_loadings_: Incomplete
    y_loadings_: Incomplete
    n_iter_: Incomplete
    x_rotations_: Incomplete
    y_rotations_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    def fit(self, X, Y):
        """Fit model to data.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vectors, where `n_samples` is the number of samples and
            `n_features` is the number of predictors.

        Y : array-like of shape (n_samples,) or (n_samples, n_targets)
            Target vectors, where `n_samples` is the number of samples and
            `n_targets` is the number of response variables.

        Returns
        -------
        self : object
            Fitted model.
        """
    def transform(self, X, Y: Incomplete | None = None, copy: bool = True):
        """Apply the dimension reduction.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Samples to transform.

        Y : array-like of shape (n_samples, n_targets), default=None
            Target vectors.

        copy : bool, default=True
            Whether to copy `X` and `Y`, or perform in-place normalization.

        Returns
        -------
        x_scores, y_scores : array-like or tuple of array-like
            Return `x_scores` if `Y` is not given, `(x_scores, y_scores)` otherwise.
        """
    def inverse_transform(self, X, Y: Incomplete | None = None):
        """Transform data back to its original space.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_components)
            New data, where `n_samples` is the number of samples
            and `n_components` is the number of pls components.

        Y : array-like of shape (n_samples, n_components)
            New target, where `n_samples` is the number of samples
            and `n_components` is the number of pls components.

        Returns
        -------
        X_reconstructed : ndarray of shape (n_samples, n_features)
            Return the reconstructed `X` data.

        Y_reconstructed : ndarray of shape (n_samples, n_targets)
            Return the reconstructed `X` target. Only returned when `Y` is given.

        Notes
        -----
        This transformation will only be exact if `n_components=n_features`.
        """
    def predict(self, X, copy: bool = True):
        """Predict targets of given samples.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Samples.

        copy : bool, default=True
            Whether to copy `X` and `Y`, or perform in-place normalization.

        Returns
        -------
        y_pred : ndarray of shape (n_samples,) or (n_samples, n_targets)
            Returns predicted values.

        Notes
        -----
        This call requires the estimation of a matrix of shape
        `(n_features, n_targets)`, which may be an issue in high dimensional
        space.
        """
    def fit_transform(self, X, y: Incomplete | None = None):
        """Learn and apply the dimension reduction on the train data.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vectors, where `n_samples` is the number of samples and
            `n_features` is the number of predictors.

        y : array-like of shape (n_samples, n_targets), default=None
            Target vectors, where `n_samples` is the number of samples and
            `n_targets` is the number of response variables.

        Returns
        -------
        self : ndarray of shape (n_samples, n_components)
            Return `x_scores` if `Y` is not given, `(x_scores, y_scores)` otherwise.
        """

class PLSRegression(_PLS):
    """PLS regression.

    PLSRegression is also known as PLS2 or PLS1, depending on the number of
    targets.

    Read more in the :ref:`User Guide <cross_decomposition>`.

    .. versionadded:: 0.8

    Parameters
    ----------
    n_components : int, default=2
        Number of components to keep. Should be in `[1, min(n_samples,
        n_features, n_targets)]`.

    scale : bool, default=True
        Whether to scale `X` and `Y`.

    max_iter : int, default=500
        The maximum number of iterations of the power method when
        `algorithm='nipals'`. Ignored otherwise.

    tol : float, default=1e-06
        The tolerance used as convergence criteria in the power method: the
        algorithm stops whenever the squared norm of `u_i - u_{i-1}` is less
        than `tol`, where `u` corresponds to the left singular vector.

    copy : bool, default=True
        Whether to copy `X` and `Y` in :term:`fit` before applying centering,
        and potentially scaling. If `False`, these operations will be done
        inplace, modifying both arrays.

    Attributes
    ----------
    x_weights_ : ndarray of shape (n_features, n_components)
        The left singular vectors of the cross-covariance matrices of each
        iteration.

    y_weights_ : ndarray of shape (n_targets, n_components)
        The right singular vectors of the cross-covariance matrices of each
        iteration.

    x_loadings_ : ndarray of shape (n_features, n_components)
        The loadings of `X`.

    y_loadings_ : ndarray of shape (n_targets, n_components)
        The loadings of `Y`.

    x_scores_ : ndarray of shape (n_samples, n_components)
        The transformed training samples.

    y_scores_ : ndarray of shape (n_samples, n_components)
        The transformed training targets.

    x_rotations_ : ndarray of shape (n_features, n_components)
        The projection matrix used to transform `X`.

    y_rotations_ : ndarray of shape (n_features, n_components)
        The projection matrix used to transform `Y`.

    coef_ : ndarray of shape (n_target, n_features)
        The coefficients of the linear model such that `Y` is approximated as
        `Y = X @ coef_.T + intercept_`.

    intercept_ : ndarray of shape (n_targets,)
        The intercepts of the linear model such that `Y` is approximated as
        `Y = X @ coef_.T + intercept_`.

        .. versionadded:: 1.1

    n_iter_ : list of shape (n_components,)
        Number of iterations of the power method, for each
        component.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    PLSCanonical : Partial Least Squares transformer and regressor.

    Examples
    --------
    >>> from sklearn.cross_decomposition import PLSRegression
    >>> X = [[0., 0., 1.], [1.,0.,0.], [2.,2.,2.], [2.,5.,4.]]
    >>> Y = [[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]]
    >>> pls2 = PLSRegression(n_components=2)
    >>> pls2.fit(X, Y)
    PLSRegression()
    >>> Y_pred = pls2.predict(X)
    """
    def __init__(self, n_components: int = 2, *, scale: bool = True, max_iter: int = 500, tol: float = 1e-06, copy: bool = True) -> None: ...
    x_scores_: Incomplete
    y_scores_: Incomplete
    def fit(self, X, Y):
        """Fit model to data.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vectors, where `n_samples` is the number of samples and
            `n_features` is the number of predictors.

        Y : array-like of shape (n_samples,) or (n_samples, n_targets)
            Target vectors, where `n_samples` is the number of samples and
            `n_targets` is the number of response variables.

        Returns
        -------
        self : object
            Fitted model.
        """

class PLSCanonical(_PLS):
    """Partial Least Squares transformer and regressor.

    Read more in the :ref:`User Guide <cross_decomposition>`.

    .. versionadded:: 0.8

    Parameters
    ----------
    n_components : int, default=2
        Number of components to keep. Should be in `[1, min(n_samples,
        n_features, n_targets)]`.

    scale : bool, default=True
        Whether to scale `X` and `Y`.

    algorithm : {'nipals', 'svd'}, default='nipals'
        The algorithm used to estimate the first singular vectors of the
        cross-covariance matrix. 'nipals' uses the power method while 'svd'
        will compute the whole SVD.

    max_iter : int, default=500
        The maximum number of iterations of the power method when
        `algorithm='nipals'`. Ignored otherwise.

    tol : float, default=1e-06
        The tolerance used as convergence criteria in the power method: the
        algorithm stops whenever the squared norm of `u_i - u_{i-1}` is less
        than `tol`, where `u` corresponds to the left singular vector.

    copy : bool, default=True
        Whether to copy `X` and `Y` in fit before applying centering, and
        potentially scaling. If False, these operations will be done inplace,
        modifying both arrays.

    Attributes
    ----------
    x_weights_ : ndarray of shape (n_features, n_components)
        The left singular vectors of the cross-covariance matrices of each
        iteration.

    y_weights_ : ndarray of shape (n_targets, n_components)
        The right singular vectors of the cross-covariance matrices of each
        iteration.

    x_loadings_ : ndarray of shape (n_features, n_components)
        The loadings of `X`.

    y_loadings_ : ndarray of shape (n_targets, n_components)
        The loadings of `Y`.

    x_rotations_ : ndarray of shape (n_features, n_components)
        The projection matrix used to transform `X`.

    y_rotations_ : ndarray of shape (n_features, n_components)
        The projection matrix used to transform `Y`.

    coef_ : ndarray of shape (n_targets, n_features)
        The coefficients of the linear model such that `Y` is approximated as
        `Y = X @ coef_.T + intercept_`.

    intercept_ : ndarray of shape (n_targets,)
        The intercepts of the linear model such that `Y` is approximated as
        `Y = X @ coef_.T + intercept_`.

        .. versionadded:: 1.1

    n_iter_ : list of shape (n_components,)
        Number of iterations of the power method, for each
        component. Empty if `algorithm='svd'`.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    CCA : Canonical Correlation Analysis.
    PLSSVD : Partial Least Square SVD.

    Examples
    --------
    >>> from sklearn.cross_decomposition import PLSCanonical
    >>> X = [[0., 0., 1.], [1.,0.,0.], [2.,2.,2.], [2.,5.,4.]]
    >>> Y = [[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]]
    >>> plsca = PLSCanonical(n_components=2)
    >>> plsca.fit(X, Y)
    PLSCanonical()
    >>> X_c, Y_c = plsca.transform(X, Y)
    """
    def __init__(self, n_components: int = 2, *, scale: bool = True, algorithm: str = 'nipals', max_iter: int = 500, tol: float = 1e-06, copy: bool = True) -> None: ...

class CCA(_PLS):
    '''Canonical Correlation Analysis, also known as "Mode B" PLS.

    Read more in the :ref:`User Guide <cross_decomposition>`.

    Parameters
    ----------
    n_components : int, default=2
        Number of components to keep. Should be in `[1, min(n_samples,
        n_features, n_targets)]`.

    scale : bool, default=True
        Whether to scale `X` and `Y`.

    max_iter : int, default=500
        The maximum number of iterations of the power method.

    tol : float, default=1e-06
        The tolerance used as convergence criteria in the power method: the
        algorithm stops whenever the squared norm of `u_i - u_{i-1}` is less
        than `tol`, where `u` corresponds to the left singular vector.

    copy : bool, default=True
        Whether to copy `X` and `Y` in fit before applying centering, and
        potentially scaling. If False, these operations will be done inplace,
        modifying both arrays.

    Attributes
    ----------
    x_weights_ : ndarray of shape (n_features, n_components)
        The left singular vectors of the cross-covariance matrices of each
        iteration.

    y_weights_ : ndarray of shape (n_targets, n_components)
        The right singular vectors of the cross-covariance matrices of each
        iteration.

    x_loadings_ : ndarray of shape (n_features, n_components)
        The loadings of `X`.

    y_loadings_ : ndarray of shape (n_targets, n_components)
        The loadings of `Y`.

    x_rotations_ : ndarray of shape (n_features, n_components)
        The projection matrix used to transform `X`.

    y_rotations_ : ndarray of shape (n_features, n_components)
        The projection matrix used to transform `Y`.

    coef_ : ndarray of shape (n_targets, n_features)
        The coefficients of the linear model such that `Y` is approximated as
        `Y = X @ coef_.T + intercept_`.

    intercept_ : ndarray of shape (n_targets,)
        The intercepts of the linear model such that `Y` is approximated as
        `Y = X @ coef_.T + intercept_`.

        .. versionadded:: 1.1

    n_iter_ : list of shape (n_components,)
        Number of iterations of the power method, for each
        component.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    PLSCanonical : Partial Least Squares transformer and regressor.
    PLSSVD : Partial Least Square SVD.

    Examples
    --------
    >>> from sklearn.cross_decomposition import CCA
    >>> X = [[0., 0., 1.], [1.,0.,0.], [2.,2.,2.], [3.,5.,4.]]
    >>> Y = [[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]]
    >>> cca = CCA(n_components=1)
    >>> cca.fit(X, Y)
    CCA(n_components=1)
    >>> X_c, Y_c = cca.transform(X, Y)
    '''
    def __init__(self, n_components: int = 2, *, scale: bool = True, max_iter: int = 500, tol: float = 1e-06, copy: bool = True) -> None: ...

class PLSSVD(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    """Partial Least Square SVD.

    This transformer simply performs a SVD on the cross-covariance matrix
    `X'Y`. It is able to project both the training data `X` and the targets
    `Y`. The training data `X` is projected on the left singular vectors, while
    the targets are projected on the right singular vectors.

    Read more in the :ref:`User Guide <cross_decomposition>`.

    .. versionadded:: 0.8

    Parameters
    ----------
    n_components : int, default=2
        The number of components to keep. Should be in `[1,
        min(n_samples, n_features, n_targets)]`.

    scale : bool, default=True
        Whether to scale `X` and `Y`.

    copy : bool, default=True
        Whether to copy `X` and `Y` in fit before applying centering, and
        potentially scaling. If `False`, these operations will be done inplace,
        modifying both arrays.

    Attributes
    ----------
    x_weights_ : ndarray of shape (n_features, n_components)
        The left singular vectors of the SVD of the cross-covariance matrix.
        Used to project `X` in :meth:`transform`.

    y_weights_ : ndarray of (n_targets, n_components)
        The right singular vectors of the SVD of the cross-covariance matrix.
        Used to project `X` in :meth:`transform`.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    PLSCanonical : Partial Least Squares transformer and regressor.
    CCA : Canonical Correlation Analysis.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.cross_decomposition import PLSSVD
    >>> X = np.array([[0., 0., 1.],
    ...               [1., 0., 0.],
    ...               [2., 2., 2.],
    ...               [2., 5., 4.]])
    >>> Y = np.array([[0.1, -0.2],
    ...               [0.9, 1.1],
    ...               [6.2, 5.9],
    ...               [11.9, 12.3]])
    >>> pls = PLSSVD(n_components=2).fit(X, Y)
    >>> X_c, Y_c = pls.transform(X, Y)
    >>> X_c.shape, Y_c.shape
    ((4, 2), (4, 2))
    """
    n_components: Incomplete
    scale: Incomplete
    copy: Incomplete
    def __init__(self, n_components: int = 2, *, scale: bool = True, copy: bool = True) -> None: ...
    x_weights_: Incomplete
    y_weights_: Incomplete
    def fit(self, X, Y):
        """Fit model to data.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training samples.

        Y : array-like of shape (n_samples,) or (n_samples, n_targets)
            Targets.

        Returns
        -------
        self : object
            Fitted estimator.
        """
    def transform(self, X, Y: Incomplete | None = None):
        """
        Apply the dimensionality reduction.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Samples to be transformed.

        Y : array-like of shape (n_samples,) or (n_samples, n_targets),                 default=None
            Targets.

        Returns
        -------
        x_scores : array-like or tuple of array-like
            The transformed data `X_transformed` if `Y is not None`,
            `(X_transformed, Y_transformed)` otherwise.
        """
    def fit_transform(self, X, y: Incomplete | None = None):
        """Learn and apply the dimensionality reduction.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training samples.

        y : array-like of shape (n_samples,) or (n_samples, n_targets),                 default=None
            Targets.

        Returns
        -------
        out : array-like or tuple of array-like
            The transformed data `X_transformed` if `Y is not None`,
            `(X_transformed, Y_transformed)` otherwise.
        """
