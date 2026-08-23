from ..base import BaseEstimator as BaseEstimator, MultiOutputMixin as MultiOutputMixin, RegressorMixin as RegressorMixin, clone as clone
from ..utils import check_random_state as check_random_state
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from .kernels import Kernel as Kernel, RBF as RBF
from _typeshed import Incomplete

GPR_CHOLESKY_LOWER: bool

class GaussianProcessRegressor(MultiOutputMixin, RegressorMixin, BaseEstimator):
    '''Gaussian process regression (GPR).

    The implementation is based on Algorithm 2.1 of [RW2006]_.

    In addition to standard scikit-learn estimator API,
    :class:`GaussianProcessRegressor`:

       * allows prediction without prior fitting (based on the GP prior)
       * provides an additional method `sample_y(X)`, which evaluates samples
         drawn from the GPR (prior or posterior) at given inputs
       * exposes a method `log_marginal_likelihood(theta)`, which can be used
         externally for other ways of selecting hyperparameters, e.g., via
         Markov chain Monte Carlo.

    Read more in the :ref:`User Guide <gaussian_process>`.

    .. versionadded:: 0.18

    Parameters
    ----------
    kernel : kernel instance, default=None
        The kernel specifying the covariance function of the GP. If None is
        passed, the kernel ``ConstantKernel(1.0, constant_value_bounds="fixed")
        * RBF(1.0, length_scale_bounds="fixed")`` is used as default. Note that
        the kernel hyperparameters are optimized during fitting unless the
        bounds are marked as "fixed".

    alpha : float or ndarray of shape (n_samples,), default=1e-10
        Value added to the diagonal of the kernel matrix during fitting.
        This can prevent a potential numerical issue during fitting, by
        ensuring that the calculated values form a positive definite matrix.
        It can also be interpreted as the variance of additional Gaussian
        measurement noise on the training observations. Note that this is
        different from using a `WhiteKernel`. If an array is passed, it must
        have the same number of entries as the data used for fitting and is
        used as datapoint-dependent noise level. Allowing to specify the
        noise level directly as a parameter is mainly for convenience and
        for consistency with :class:`~sklearn.linear_model.Ridge`.

    optimizer : "fmin_l_bfgs_b", callable or None, default="fmin_l_bfgs_b"
        Can either be one of the internally supported optimizers for optimizing
        the kernel\'s parameters, specified by a string, or an externally
        defined optimizer passed as a callable. If a callable is passed, it
        must have the signature::

            def optimizer(obj_func, initial_theta, bounds):
                # * \'obj_func\': the objective function to be minimized, which
                #   takes the hyperparameters theta as a parameter and an
                #   optional flag eval_gradient, which determines if the
                #   gradient is returned additionally to the function value
                # * \'initial_theta\': the initial value for theta, which can be
                #   used by local optimizers
                # * \'bounds\': the bounds on the values of theta
                ....
                # Returned are the best found hyperparameters theta and
                # the corresponding value of the target function.
                return theta_opt, func_min

        Per default, the L-BFGS-B algorithm from `scipy.optimize.minimize`
        is used. If None is passed, the kernel\'s parameters are kept fixed.
        Available internal optimizers are: `{\'fmin_l_bfgs_b\'}`.

    n_restarts_optimizer : int, default=0
        The number of restarts of the optimizer for finding the kernel\'s
        parameters which maximize the log-marginal likelihood. The first run
        of the optimizer is performed from the kernel\'s initial parameters,
        the remaining ones (if any) from thetas sampled log-uniform randomly
        from the space of allowed theta-values. If greater than 0, all bounds
        must be finite. Note that `n_restarts_optimizer == 0` implies that one
        run is performed.

    normalize_y : bool, default=False
        Whether or not to normalize the target values `y` by removing the mean
        and scaling to unit-variance. This is recommended for cases where
        zero-mean, unit-variance priors are used. Note that, in this
        implementation, the normalisation is reversed before the GP predictions
        are reported.

        .. versionchanged:: 0.23

    copy_X_train : bool, default=True
        If True, a persistent copy of the training data is stored in the
        object. Otherwise, just a reference to the training data is stored,
        which might cause predictions to change if the data is modified
        externally.

    n_targets : int, default=None
        The number of dimensions of the target values. Used to decide the number
        of outputs when sampling from the prior distributions (i.e. calling
        :meth:`sample_y` before :meth:`fit`). This parameter is ignored once
        :meth:`fit` has been called.

        .. versionadded:: 1.3

    random_state : int, RandomState instance or None, default=None
        Determines random number generation used to initialize the centers.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Attributes
    ----------
    X_train_ : array-like of shape (n_samples, n_features) or list of object
        Feature vectors or other representations of training data (also
        required for prediction).

    y_train_ : array-like of shape (n_samples,) or (n_samples, n_targets)
        Target values in training data (also required for prediction).

    kernel_ : kernel instance
        The kernel used for prediction. The structure of the kernel is the
        same as the one passed as parameter but with optimized hyperparameters.

    L_ : array-like of shape (n_samples, n_samples)
        Lower-triangular Cholesky decomposition of the kernel in ``X_train_``.

    alpha_ : array-like of shape (n_samples,)
        Dual coefficients of training data points in kernel space.

    log_marginal_likelihood_value_ : float
        The log-marginal-likelihood of ``self.kernel_.theta``.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    GaussianProcessClassifier : Gaussian process classification (GPC)
        based on Laplace approximation.

    References
    ----------
    .. [RW2006] `Carl E. Rasmussen and Christopher K.I. Williams,
       "Gaussian Processes for Machine Learning",
       MIT Press 2006 <https://www.gaussianprocess.org/gpml/chapters/RW.pdf>`_

    Examples
    --------
    >>> from sklearn.datasets import make_friedman2
    >>> from sklearn.gaussian_process import GaussianProcessRegressor
    >>> from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
    >>> X, y = make_friedman2(n_samples=500, noise=0, random_state=0)
    >>> kernel = DotProduct() + WhiteKernel()
    >>> gpr = GaussianProcessRegressor(kernel=kernel,
    ...         random_state=0).fit(X, y)
    >>> gpr.score(X, y)
    0.3680...
    >>> gpr.predict(X[:2,:], return_std=True)
    (array([653.0..., 592.1...]), array([316.6..., 316.6...]))
    '''
    kernel: Incomplete
    alpha: Incomplete
    optimizer: Incomplete
    n_restarts_optimizer: Incomplete
    normalize_y: Incomplete
    copy_X_train: Incomplete
    n_targets: Incomplete
    random_state: Incomplete
    def __init__(self, kernel: Incomplete | None = None, *, alpha: float = 1e-10, optimizer: str = 'fmin_l_bfgs_b', n_restarts_optimizer: int = 0, normalize_y: bool = False, copy_X_train: bool = True, n_targets: Incomplete | None = None, random_state: Incomplete | None = None) -> None: ...
    kernel_: Incomplete
    X_train_: Incomplete
    y_train_: Incomplete
    log_marginal_likelihood_value_: Incomplete
    L_: Incomplete
    alpha_: Incomplete
    def fit(self, X, y):
        """Fit Gaussian process regression model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or list of object
            Feature vectors or other representations of training data.

        y : array-like of shape (n_samples,) or (n_samples, n_targets)
            Target values.

        Returns
        -------
        self : object
            GaussianProcessRegressor class instance.
        """
    def predict(self, X, return_std: bool = False, return_cov: bool = False):
        """Predict using the Gaussian process regression model.

        We can also predict based on an unfitted model by using the GP prior.
        In addition to the mean of the predictive distribution, optionally also
        returns its standard deviation (`return_std=True`) or covariance
        (`return_cov=True`). Note that at most one of the two can be requested.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or list of object
            Query points where the GP is evaluated.

        return_std : bool, default=False
            If True, the standard-deviation of the predictive distribution at
            the query points is returned along with the mean.

        return_cov : bool, default=False
            If True, the covariance of the joint predictive distribution at
            the query points is returned along with the mean.

        Returns
        -------
        y_mean : ndarray of shape (n_samples,) or (n_samples, n_targets)
            Mean of predictive distribution a query points.

        y_std : ndarray of shape (n_samples,) or (n_samples, n_targets), optional
            Standard deviation of predictive distribution at query points.
            Only returned when `return_std` is True.

        y_cov : ndarray of shape (n_samples, n_samples) or                 (n_samples, n_samples, n_targets), optional
            Covariance of joint predictive distribution a query points.
            Only returned when `return_cov` is True.
        """
    def sample_y(self, X, n_samples: int = 1, random_state: int = 0):
        """Draw samples from Gaussian process and evaluate at X.

        Parameters
        ----------
        X : array-like of shape (n_samples_X, n_features) or list of object
            Query points where the GP is evaluated.

        n_samples : int, default=1
            Number of samples drawn from the Gaussian process per query point.

        random_state : int, RandomState instance or None, default=0
            Determines random number generation to randomly draw samples.
            Pass an int for reproducible results across multiple function
            calls.
            See :term:`Glossary <random_state>`.

        Returns
        -------
        y_samples : ndarray of shape (n_samples_X, n_samples), or             (n_samples_X, n_targets, n_samples)
            Values of n_samples samples drawn from Gaussian process and
            evaluated at query points.
        """
    def log_marginal_likelihood(self, theta: Incomplete | None = None, eval_gradient: bool = False, clone_kernel: bool = True):
        """Return log-marginal likelihood of theta for training data.

        Parameters
        ----------
        theta : array-like of shape (n_kernel_params,) default=None
            Kernel hyperparameters for which the log-marginal likelihood is
            evaluated. If None, the precomputed log_marginal_likelihood
            of ``self.kernel_.theta`` is returned.

        eval_gradient : bool, default=False
            If True, the gradient of the log-marginal likelihood with respect
            to the kernel hyperparameters at position theta is returned
            additionally. If True, theta must not be None.

        clone_kernel : bool, default=True
            If True, the kernel attribute is copied. If False, the kernel
            attribute is modified, but may result in a performance improvement.

        Returns
        -------
        log_likelihood : float
            Log-marginal likelihood of theta for training data.

        log_likelihood_gradient : ndarray of shape (n_kernel_params,), optional
            Gradient of the log-marginal likelihood with respect to the kernel
            hyperparameters at position theta.
            Only returned when eval_gradient is True.
        """
