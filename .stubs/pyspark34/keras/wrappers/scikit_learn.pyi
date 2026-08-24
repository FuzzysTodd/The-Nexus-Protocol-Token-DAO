from _typeshed import Incomplete
from keras import losses as losses
from keras.models import Sequential as Sequential
from keras.utils.generic_utils import has_arg as has_arg
from keras.utils.np_utils import to_categorical as to_categorical

class BaseWrapper:
    """Base class for the Keras scikit-learn wrapper.

    Warning: This class should not be used directly.
    Use descendant classes instead.

    Args:
        build_fn: callable function or class instance
        **sk_params: model parameters & fitting parameters

    The `build_fn` should construct, compile and return a Keras model, which
    will then be used to fit/predict. One of the following
    three values could be passed to `build_fn`:
    1. A function
    2. An instance of a class that implements the `__call__` method
    3. None. This means you implement a class that inherits from either
    `KerasClassifier` or `KerasRegressor`. The `__call__` method of the
    present class will then be treated as the default `build_fn`.

    `sk_params` takes both model parameters and fitting parameters. Legal model
    parameters are the arguments of `build_fn`. Note that like all other
    estimators in scikit-learn, `build_fn` should provide default values for
    its arguments, so that you could create the estimator without passing any
    values to `sk_params`.

    `sk_params` could also accept parameters for calling `fit`, `predict`,
    `predict_proba`, and `score` methods (e.g., `epochs`, `batch_size`).
    fitting (predicting) parameters are selected in the following order:

    1. Values passed to the dictionary arguments of
    `fit`, `predict`, `predict_proba`, and `score` methods
    2. Values passed to `sk_params`
    3. The default values of the `keras.models.Sequential`
    `fit`, `predict` methods.

    When using scikit-learn's `grid_search` API, legal tunable parameters are
    those you could pass to `sk_params`, including fitting parameters.
    In other words, you could use `grid_search` to search for the best
    `batch_size` or `epochs` as well as the model parameters.
    """
    build_fn: Incomplete
    sk_params: Incomplete
    def __init__(self, build_fn: Incomplete | None = None, **sk_params) -> None: ...
    def check_params(self, params) -> None:
        """Checks for user typos in `params`.

        Args:
            params: dictionary; the parameters to be checked

        Raises:
            ValueError: if any member of `params` is not a valid argument.
        """
    def get_params(self, **params):
        """Gets parameters for this estimator.

        Args:
            **params: ignored (exists for API compatibility).

        Returns:
            Dictionary of parameter names mapped to their values.
        """
    def set_params(self, **params):
        """Sets the parameters of this estimator.

        Args:
            **params: Dictionary of parameter names mapped to their values.

        Returns:
            self
        """
    model: Incomplete
    def fit(self, x, y, **kwargs):
        """Constructs a new model with `build_fn` & fit the model to `(x, y)`.

        Args:
            x : array-like, shape `(n_samples, n_features)`
                Training samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            y : array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
                True labels for `x`.
            **kwargs: dictionary arguments
                Legal arguments are the arguments of `Sequential.fit`

        Returns:
            history : object
                details about the training history at each epoch.
        """
    def filter_sk_params(self, fn, override: Incomplete | None = None):
        """Filters `sk_params` and returns those in `fn`'s arguments.

        Args:
            fn : arbitrary function
            override: dictionary, values to override `sk_params`

        Returns:
            res : dictionary containing variables
                in both `sk_params` and `fn`'s arguments.
        """

class KerasClassifier(BaseWrapper):
    """Implementation of the scikit-learn classifier API for Keras.

    DEPRECATED. Use [Sci-Keras](https://github.com/adriangb/scikeras) instead.
    See https://www.adriangb.com/scikeras/stable/migration.html
    for help migrating.
    """
    def __init__(self, build_fn: Incomplete | None = None, **sk_params) -> None: ...
    classes_: Incomplete
    n_classes_: Incomplete
    def fit(self, x, y, **kwargs):
        """Constructs a new model with `build_fn` & fit the model to `(x, y)`.

        Args:
            x : array-like, shape `(n_samples, n_features)`
                Training samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            y : array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
                True labels for `x`.
            **kwargs: dictionary arguments
                Legal arguments are the arguments of `Sequential.fit`

        Returns:
            history : object
                details about the training history at each epoch.

        Raises:
            ValueError: In case of invalid shape for `y` argument.
        """
    def predict(self, x, **kwargs):
        """Returns the class predictions for the given test data.

        Args:
            x: array-like, shape `(n_samples, n_features)`
                Test samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            **kwargs: dictionary arguments
                Legal arguments are the arguments
                of `Sequential.predict`.

        Returns:
            preds: array-like, shape `(n_samples,)`
                Class predictions.
        """
    def predict_proba(self, x, **kwargs):
        """Returns class probability estimates for the given test data.

        Args:
            x: array-like, shape `(n_samples, n_features)`
                Test samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            **kwargs: dictionary arguments
                Legal arguments are the arguments
                of `Sequential.predict`.

        Returns:
            proba: array-like, shape `(n_samples, n_outputs)`
                Class probability estimates.
                In the case of binary classification,
                to match the scikit-learn API,
                will return an array of shape `(n_samples, 2)`
                (instead of `(n_sample, 1)` as in Keras).
        """
    def score(self, x, y, **kwargs):
        '''Returns the mean accuracy on the given test data and labels.

        Args:
            x: array-like, shape `(n_samples, n_features)`
                Test samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            y: array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
                True labels for `x`.
            **kwargs: dictionary arguments
                Legal arguments are the arguments of `Sequential.evaluate`.

        Returns:
            score: float
                Mean accuracy of predictions on `x` wrt. `y`.

        Raises:
            ValueError: If the underlying model isn\'t configured to
                compute accuracy. You should pass `metrics=["accuracy"]` to
                the `.compile()` method of the model.
        '''

class KerasRegressor(BaseWrapper):
    """Implementation of the scikit-learn regressor API for Keras.

    DEPRECATED. Use [Sci-Keras](https://github.com/adriangb/scikeras) instead.
    See https://www.adriangb.com/scikeras/stable/migration.html
    for help migrating.
    """
    def __init__(self, build_fn: Incomplete | None = None, **sk_params) -> None: ...
    def predict(self, x, **kwargs):
        """Returns predictions for the given test data.

        Args:
            x: array-like, shape `(n_samples, n_features)`
                Test samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            **kwargs: dictionary arguments
                Legal arguments are the arguments of `Sequential.predict`.

        Returns:
            preds: array-like, shape `(n_samples,)`
                Predictions.
        """
    def score(self, x, y, **kwargs):
        """Returns the mean loss on the given test data and labels.

        Args:
            x: array-like, shape `(n_samples, n_features)`
                Test samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            y: array-like, shape `(n_samples,)`
                True labels for `x`.
            **kwargs: dictionary arguments
                Legal arguments are the arguments of `Sequential.evaluate`.

        Returns:
            score: float
                Mean accuracy of predictions on `x` wrt. `y`.
        """
