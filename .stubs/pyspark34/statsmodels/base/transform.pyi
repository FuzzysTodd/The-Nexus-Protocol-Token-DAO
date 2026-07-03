from _typeshed import Incomplete
from statsmodels.robust import mad as mad

class BoxCox:
    """
    Mixin class to allow for a Box-Cox transformation.
    """
    def transform_boxcox(self, x, lmbda: Incomplete | None = None, method: str = 'guerrero', **kwargs):
        '''
        Performs a Box-Cox transformation on the data array x. If lmbda is None,
        the indicated method is used to estimate a suitable lambda parameter.

        Parameters
        ----------
        x : array_like
        lmbda : float
            The lambda parameter for the Box-Cox transform. If None, a value
            will be estimated by means of the specified method.
        method : {\'guerrero\', \'loglik\'}
            The method to estimate the lambda parameter. Will only be used if
            lmbda is None, and defaults to \'guerrero\', detailed in Guerrero
            (1993). \'loglik\' maximizes the profile likelihood.
        **kwargs
            Options for the specified method.
            * For \'guerrero\', this entails window_length, the grouping
              parameter, scale, the dispersion measure, and options, to be
              passed to the optimizer.
            * For \'loglik\': options, to be passed to the optimizer.

        Returns
        -------
        y : array_like
            The transformed series.
        lmbda : float
            The lmbda parameter used to transform the series.

        References
        ----------
        Guerrero, Victor M. 1993. "Time-series analysis supported by power
        transformations". `Journal of Forecasting`. 12 (1): 37-48.

        Guerrero, Victor M. and Perera, Rafael. 2004. "Variance Stabilizing
        Power Transformation for Time Series," `Journal of Modern Applied
        Statistical Methods`. 3 (2): 357-369.

        Box, G. E. P., and D. R. Cox. 1964. "An Analysis of Transformations".
        `Journal of the Royal Statistical Society`. 26 (2): 211-252.
        '''
    def untransform_boxcox(self, x, lmbda, method: str = 'naive'):
        """
        Back-transforms the Box-Cox transformed data array, by means of the
        indicated method. The provided argument lmbda should be the lambda
        parameter that was used to initially transform the data.

        Parameters
        ----------
        x : array_like
            The transformed series.
        lmbda : float
            The lambda parameter that was used to transform the series.
        method : {'naive'}
            Indicates the method to be used in the untransformation. Defaults
            to 'naive', which reverses the transformation.

            NOTE: 'naive' is implemented natively, while other methods may be
            available in subclasses!

        Returns
        -------
        y : array_like
            The untransformed series.
        """
