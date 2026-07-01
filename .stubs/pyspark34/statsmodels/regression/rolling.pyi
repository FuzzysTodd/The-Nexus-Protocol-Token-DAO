from _typeshed import Incomplete
from statsmodels.base import model as model
from statsmodels.base.model import LikelihoodModelResults as LikelihoodModelResults, Model as Model
from statsmodels.compat.numpy import lstsq as lstsq
from statsmodels.compat.pandas import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly, call_cached_func as call_cached_func, get_cached_doc as get_cached_doc
from statsmodels.regression.linear_model import RegressionModel as RegressionModel, RegressionResults as RegressionResults
from statsmodels.tools.validation import array_like as array_like, int_like as int_like, string_like as string_like
from typing import NamedTuple

def strip4(line): ...

class RollingStore(NamedTuple):
    params: Incomplete
    ssr: Incomplete
    llf: Incomplete
    nobs: Incomplete
    s2: Incomplete
    xpxi: Incomplete
    xeex: Incomplete
    centered_tss: Incomplete
    uncentered_tss: Incomplete

common_params: Incomplete
window_parameters: str
weight_parameters: str
extra_base: Incomplete
extra_parameters: Incomplete

class RollingWLS:
    k_constant: Incomplete
    const_idx: Incomplete
    def __init__(self, endog, exog, window: Incomplete | None = None, *, weights: Incomplete | None = None, min_nobs: Incomplete | None = None, missing: str = 'drop', expanding: bool = False) -> None: ...
    def fit(self, method: str = 'inv', cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, reset: Incomplete | None = None, use_t: bool = False, params_only: bool = False):
        """
        Estimate model parameters.

        Parameters
        ----------
        method : {'inv', 'lstsq', 'pinv'}
            Method to use when computing the the model parameters.

            * 'inv' - use moving windows inner-products and matrix inversion.
              This method is the fastest, but may be less accurate than the
              other methods.
            * 'lstsq' - Use numpy.linalg.lstsq
            * 'pinv' - Use numpy.linalg.pinv. This method matches the default
              estimator in non-moving regression estimators.
        cov_type : {'nonrobust', 'HCCM', 'HC0'}
            Covariance estimator:

            * nonrobust - The classic OLS covariance estimator
            * HCCM, HC0 - White heteroskedasticity robust covariance
        cov_kwds : dict
            Unused
        reset : int, optional
            Interval to recompute the moving window inner products used to
            estimate the model parameters. Smaller values improve accuracy,
            although in practice this setting is not required to be set.
        use_t : bool, optional
            Flag indicating to use the Student's t distribution when computing
            p-values.
        params_only : bool, optional
            Flag indicating that only parameters should be computed. Avoids
            calculating all other statistics or performing inference.

        Returns
        -------
        RollingRegressionResults
            Estimation results where all pre-sample values are nan-filled.
        """
    @classmethod
    def from_formula(cls, formula, data, window, weights: Incomplete | None = None, subset: Incomplete | None = None, *args, **kwargs): ...

class RollingOLS(RollingWLS):
    def __init__(self, endog, exog, window: Incomplete | None = None, *, min_nobs: Incomplete | None = None, missing: str = 'drop', expanding: bool = False) -> None: ...

class RollingRegressionResults:
    """
    Results from rolling regressions

    Parameters
    ----------
    model : RollingWLS
        Model instance
    store : RollingStore
        Container for raw moving window results
    k_constant : bool
        Flag indicating that the model contains a constant
    use_t : bool
        Flag indicating to use the Student's t distribution when computing
        p-values.
    cov_type : str
        Name of covariance estimator
    """
    model: Incomplete
    def __init__(self, model, store: RollingStore, k_constant, use_t, cov_type) -> None: ...
    def aic(self): ...
    def bic(self): ...
    def info_criteria(self, crit, dk_params: int = 0): ...
    def params(self):
        """Estimated model parameters"""
    def ssr(self): ...
    def llf(self): ...
    def df_model(self): ...
    def k_constant(self):
        """Flag indicating whether the model contains a constant"""
    def centered_tss(self): ...
    def uncentered_tss(self): ...
    def rsquared(self): ...
    def rsquared_adj(self): ...
    def nobs(self): ...
    def df_resid(self): ...
    def use_t(self): ...
    def ess(self): ...
    def mse_model(self): ...
    def mse_resid(self): ...
    def mse_total(self): ...
    def cov_params(self):
        """
        Estimated parameter covariance

        Returns
        -------
        array_like
            The estimated model covariances. If the original input is a numpy
            array, the returned covariance is a 3-d array with shape
            (nobs, nvar, nvar). If the original inputs are pandas types, then
            the returned covariance is a DataFrame with a MultiIndex with
            key (observation, variable), so that the covariance for
            observation with index i is cov.loc[i].
        """
    def f_pvalue(self): ...
    def fvalue(self): ...
    def bse(self): ...
    def tvalues(self): ...
    def pvalues(self): ...
    def conf_int(self, alpha: float = 0.05, cols: Incomplete | None = None): ...
    @property
    def cov_type(self):
        """Name of covariance estimator"""
    @classmethod
    def load(cls, fname): ...
    remove_data: Incomplete
    def save(self, fname, remove_data: bool = False): ...
    def plot_recursive_coefficient(self, variables: Incomplete | None = None, alpha: float = 0.05, legend_loc: str = 'upper left', fig: Incomplete | None = None, figsize: Incomplete | None = None):
        """
        Plot the recursively estimated coefficients on a given variable

        Parameters
        ----------
        variables : {int, str, Iterable[int], Iterable[str], None}, optional
            Integer index or string name of the variables whose coefficients
            to plot. Can also be an iterable of integers or strings. Default
            plots all coefficients.
        alpha : float, optional
            The confidence intervals for the coefficient are (1 - alpha)%. Set
            to None to exclude confidence intervals.
        legend_loc : str, optional
            The location of the legend in the plot. Default is upper left.
        fig : Figure, optional
            If given, subplots are created in this figure instead of in a new
            figure. Note that the grid will be created in the provided
            figure using `fig.add_subplot()`.
        figsize : tuple, optional
            If a figure is created, this argument allows specifying a size.
            The tuple is (width, height).

        Returns
        -------
        Figure
            The matplotlib Figure object.
        """
