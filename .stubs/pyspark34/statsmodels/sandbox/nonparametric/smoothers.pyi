from . import kernels as kernels
from _typeshed import Incomplete

class KernelSmoother:
    """
    1D Kernel Density Regression/Kernel Smoother

    Requires:
    x - array_like of x values
    y - array_like of y values
    Kernel - Kernel object, Default is Gaussian.
    """
    Kernel: Incomplete
    x: Incomplete
    y: Incomplete
    def __init__(self, x, y, Kernel: Incomplete | None = None) -> None: ...
    def fit(self) -> None: ...
    def __call__(self, x): ...
    def predict(self, x):
        """
        Returns the kernel smoothed prediction at x

        If x is a real number then a single value is returned.

        Otherwise an attempt is made to cast x to numpy.ndarray and an array of
        corresponding y-points is returned.
        """
    def conf(self, x):
        """
        Returns the fitted curve and 1-sigma upper and lower point-wise
        confidence.
        These bounds are based on variance only, and do not include the bias.
        If the bandwidth is much larger than the curvature of the underlying
        function then the bias could be large.

        x is the points on which you want to evaluate the fit and the errors.

        Alternatively if x is specified as a positive integer, then the fit and
        confidence bands points will be returned after every
        xth sample point - so they are closer together where the data
        is denser.
        """
    def var(self, x): ...
    def std(self, x): ...

class PolySmoother:
    """
    Polynomial smoother up to a given order.
    Fit based on weighted least squares.

    The x values can be specified at instantiation or when called.

    This is a 3 liner with OLS or WLS, see test.
    It's here as a test smoother for GAM
    """
    order: Incomplete
    coef: Incomplete
    X: Incomplete
    def __init__(self, order, x: Incomplete | None = None) -> None: ...
    def df_fit(self):
        """alias of df_model for backwards compatibility
        """
    def df_model(self):
        """
        Degrees of freedom used in the fit.
        """
    def gram(self, d: Incomplete | None = None) -> None: ...
    def smooth(self, *args, **kwds):
        """alias for fit,  for backwards compatibility,

        do we need it with different behavior than fit?

        """
    def df_resid(self):
        """
        Residual degrees of freedom from last fit.
        """
    def __call__(self, x: Incomplete | None = None): ...
    def predict(self, x: Incomplete | None = None): ...
    N: Incomplete
    params: Incomplete
    def fit(self, y, x: Incomplete | None = None, weights: Incomplete | None = None) -> None: ...
