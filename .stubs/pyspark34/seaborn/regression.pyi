from _typeshed import Incomplete

__all__ = ['lmplot', 'regplot', 'residplot']

class _LinearPlotter:
    """Base class for plotting relational data in tidy format.

    To get anything useful done you'll have to inherit from this, but setup
    code that can be abstracted out should be put here.

    """
    data: Incomplete
    def establish_variables(self, data, **kws) -> None:
        """Extract variables from data or use directly."""
    def dropna(self, *vars) -> None:
        """Remove observations with missing data."""
    def plot(self, ax) -> None: ...

class _RegressionPlotter(_LinearPlotter):
    """Plotter for numeric independent variables with regression model.

    This does the computations and drawing for the `regplot` function, and
    is thus also used indirectly by `lmplot`.
    """
    x_estimator: Incomplete
    ci: Incomplete
    x_ci: Incomplete
    n_boot: Incomplete
    seed: Incomplete
    scatter: Incomplete
    fit_reg: Incomplete
    order: Incomplete
    logistic: Incomplete
    lowess: Incomplete
    robust: Incomplete
    logx: Incomplete
    truncate: Incomplete
    x_jitter: Incomplete
    y_jitter: Incomplete
    color: Incomplete
    label: Incomplete
    x: Incomplete
    y: Incomplete
    x_discrete: Incomplete
    x_range: Incomplete
    def __init__(self, x, y, data: Incomplete | None = None, x_estimator: Incomplete | None = None, x_bins: Incomplete | None = None, x_ci: str = 'ci', scatter: bool = True, fit_reg: bool = True, ci: int = 95, n_boot: int = 1000, units: Incomplete | None = None, seed: Incomplete | None = None, order: int = 1, logistic: bool = False, lowess: bool = False, robust: bool = False, logx: bool = False, x_partial: Incomplete | None = None, y_partial: Incomplete | None = None, truncate: bool = False, dropna: bool = True, x_jitter: Incomplete | None = None, y_jitter: Incomplete | None = None, color: Incomplete | None = None, label: Incomplete | None = None) -> None: ...
    @property
    def scatter_data(self):
        """Data where each observation is a point."""
    @property
    def estimate_data(self):
        """Data with a point estimate and CI for each discrete x value."""
    def fit_regression(self, ax: Incomplete | None = None, x_range: Incomplete | None = None, grid: Incomplete | None = None):
        """Fit the regression model."""
    def fit_fast(self, grid):
        """Low-level regression and prediction using linear algebra."""
    def fit_poly(self, grid, order):
        """Regression using numpy polyfit for higher-order trends."""
    def fit_statsmodels(self, grid, model, **kwargs):
        """More general regression function using statsmodels objects."""
    def fit_lowess(self):
        """Fit a locally-weighted regression, which returns its own grid."""
    def fit_logx(self, grid):
        """Fit the model in log-space."""
    def bin_predictor(self, bins):
        """Discretize a predictor by assigning value to closest bin."""
    def regress_out(self, a, b):
        """Regress b from a keeping a's original mean."""
    def plot(self, ax, scatter_kws, line_kws) -> None:
        """Draw the full plot."""
    def scatterplot(self, ax, kws) -> None:
        """Draw the data."""
    def lineplot(self, ax, kws) -> None:
        """Draw the model."""

def lmplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, col: Incomplete | None = None, row: Incomplete | None = None, palette: Incomplete | None = None, col_wrap: Incomplete | None = None, height: int = 5, aspect: int = 1, markers: str = 'o', sharex: Incomplete | None = None, sharey: Incomplete | None = None, hue_order: Incomplete | None = None, col_order: Incomplete | None = None, row_order: Incomplete | None = None, legend: bool = True, legend_out: Incomplete | None = None, x_estimator: Incomplete | None = None, x_bins: Incomplete | None = None, x_ci: str = 'ci', scatter: bool = True, fit_reg: bool = True, ci: int = 95, n_boot: int = 1000, units: Incomplete | None = None, seed: Incomplete | None = None, order: int = 1, logistic: bool = False, lowess: bool = False, robust: bool = False, logx: bool = False, x_partial: Incomplete | None = None, y_partial: Incomplete | None = None, truncate: bool = True, x_jitter: Incomplete | None = None, y_jitter: Incomplete | None = None, scatter_kws: Incomplete | None = None, line_kws: Incomplete | None = None, facet_kws: Incomplete | None = None): ...
def regplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, x_estimator: Incomplete | None = None, x_bins: Incomplete | None = None, x_ci: str = 'ci', scatter: bool = True, fit_reg: bool = True, ci: int = 95, n_boot: int = 1000, units: Incomplete | None = None, seed: Incomplete | None = None, order: int = 1, logistic: bool = False, lowess: bool = False, robust: bool = False, logx: bool = False, x_partial: Incomplete | None = None, y_partial: Incomplete | None = None, truncate: bool = True, dropna: bool = True, x_jitter: Incomplete | None = None, y_jitter: Incomplete | None = None, label: Incomplete | None = None, color: Incomplete | None = None, marker: str = 'o', scatter_kws: Incomplete | None = None, line_kws: Incomplete | None = None, ax: Incomplete | None = None): ...
def residplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, x_partial: Incomplete | None = None, y_partial: Incomplete | None = None, lowess: bool = False, order: int = 1, robust: bool = False, dropna: bool = True, label: Incomplete | None = None, color: Incomplete | None = None, scatter_kws: Incomplete | None = None, line_kws: Incomplete | None = None, ax: Incomplete | None = None):
    '''Plot the residuals of a linear regression.

    This function will regress y on x (possibly as a robust or polynomial
    regression) and then draw a scatterplot of the residuals. You can
    optionally fit a lowess smoother to the residual plot, which can
    help in determining if there is structure to the residuals.

    Parameters
    ----------
    data : DataFrame, optional
        DataFrame to use if `x` and `y` are column names.
    x : vector or string
        Data or column name in `data` for the predictor variable.
    y : vector or string
        Data or column name in `data` for the response variable.
    {x, y}_partial : vectors or string(s) , optional
        These variables are treated as confounding and are removed from
        the `x` or `y` variables before plotting.
    lowess : boolean, optional
        Fit a lowess smoother to the residual scatterplot.
    order : int, optional
        Order of the polynomial to fit when calculating the residuals.
    robust : boolean, optional
        Fit a robust linear regression when calculating the residuals.
    dropna : boolean, optional
        If True, ignore observations with missing data when fitting and
        plotting.
    label : string, optional
        Label that will be used in any plot legends.
    color : matplotlib color, optional
        Color to use for all elements of the plot.
    {scatter, line}_kws : dictionaries, optional
        Additional keyword arguments passed to scatter() and plot() for drawing
        the components of the plot.
    ax : matplotlib axis, optional
        Plot into this axis, otherwise grab the current axis or make a new
        one if not existing.

    Returns
    -------
    ax: matplotlib axes
        Axes with the regression plot.

    See Also
    --------
    regplot : Plot a simple linear regression model.
    jointplot : Draw a :func:`residplot` with univariate marginal distributions
                (when used with ``kind="resid"``).

    Examples
    --------

    .. include:: ../docstrings/residplot.rst

    '''
