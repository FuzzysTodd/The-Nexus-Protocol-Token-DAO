from ..base import BaseEstimator, RegressorMixin
from _typeshed import Incomplete

__all__ = ['TransformedTargetRegressor']

class TransformedTargetRegressor(RegressorMixin, BaseEstimator):
    """Meta-estimator to regress on a transformed target.

    Useful for applying a non-linear transformation to the target `y` in
    regression problems. This transformation can be given as a Transformer
    such as the :class:`~sklearn.preprocessing.QuantileTransformer` or as a
    function and its inverse such as `np.log` and `np.exp`.

    The computation during :meth:`fit` is::

        regressor.fit(X, func(y))

    or::

        regressor.fit(X, transformer.transform(y))

    The computation during :meth:`predict` is::

        inverse_func(regressor.predict(X))

    or::

        transformer.inverse_transform(regressor.predict(X))

    Read more in the :ref:`User Guide <transformed_target_regressor>`.

    .. versionadded:: 0.20

    Parameters
    ----------
    regressor : object, default=None
        Regressor object such as derived from
        :class:`~sklearn.base.RegressorMixin`. This regressor will
        automatically be cloned each time prior to fitting. If `regressor is
        None`, :class:`~sklearn.linear_model.LinearRegression` is created and used.

    transformer : object, default=None
        Estimator object such as derived from
        :class:`~sklearn.base.TransformerMixin`. Cannot be set at the same time
        as `func` and `inverse_func`. If `transformer is None` as well as
        `func` and `inverse_func`, the transformer will be an identity
        transformer. Note that the transformer will be cloned during fitting.
        Also, the transformer is restricting `y` to be a numpy array.

    func : function, default=None
        Function to apply to `y` before passing to :meth:`fit`. Cannot be set
        at the same time as `transformer`. The function needs to return a
        2-dimensional array. If `func is None`, the function used will be the
        identity function.

    inverse_func : function, default=None
        Function to apply to the prediction of the regressor. Cannot be set at
        the same time as `transformer`. The function needs to return a
        2-dimensional array. The inverse function is used to return
        predictions to the same space of the original training labels.

    check_inverse : bool, default=True
        Whether to check that `transform` followed by `inverse_transform`
        or `func` followed by `inverse_func` leads to the original targets.

    Attributes
    ----------
    regressor_ : object
        Fitted regressor.

    transformer_ : object
        Transformer used in :meth:`fit` and :meth:`predict`.

    n_features_in_ : int
        Number of features seen during :term:`fit`. Only defined if the
        underlying regressor exposes such an attribute when fit.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    sklearn.preprocessing.FunctionTransformer : Construct a transformer from an
        arbitrary callable.

    Notes
    -----
    Internally, the target `y` is always converted into a 2-dimensional array
    to be used by scikit-learn transformers. At the time of prediction, the
    output will be reshaped to a have the same number of dimensions as `y`.

    See :ref:`examples/compose/plot_transformed_target.py
    <sphx_glr_auto_examples_compose_plot_transformed_target.py>`.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.linear_model import LinearRegression
    >>> from sklearn.compose import TransformedTargetRegressor
    >>> tt = TransformedTargetRegressor(regressor=LinearRegression(),
    ...                                 func=np.log, inverse_func=np.exp)
    >>> X = np.arange(4).reshape(-1, 1)
    >>> y = np.exp(2 * X).ravel()
    >>> tt.fit(X, y)
    TransformedTargetRegressor(...)
    >>> tt.score(X, y)
    1.0
    >>> tt.regressor_.coef_
    array([2.])
    """
    regressor: Incomplete
    transformer: Incomplete
    func: Incomplete
    inverse_func: Incomplete
    check_inverse: Incomplete
    def __init__(self, regressor: Incomplete | None = None, *, transformer: Incomplete | None = None, func: Incomplete | None = None, inverse_func: Incomplete | None = None, check_inverse: bool = True) -> None: ...
    regressor_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y, **fit_params):
        """Fit the model according to the given training data.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples and
            `n_features` is the number of features.

        y : array-like of shape (n_samples,)
            Target values.

        **fit_params : dict
            Parameters passed to the `fit` method of the underlying
            regressor.

        Returns
        -------
        self : object
            Fitted estimator.
        """
    def predict(self, X, **predict_params):
        """Predict using the base regressor, applying inverse.

        The regressor is used to predict and the `inverse_func` or
        `inverse_transform` is applied before returning the prediction.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Samples.

        **predict_params : dict of str -> object
            Parameters passed to the `predict` method of the underlying
            regressor.

        Returns
        -------
        y_hat : ndarray of shape (n_samples,)
            Predicted values.
        """
    @property
    def n_features_in_(self):
        """Number of features seen during :term:`fit`."""
