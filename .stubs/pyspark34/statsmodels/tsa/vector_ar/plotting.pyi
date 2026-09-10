from _typeshed import Incomplete
from statsmodels.compat.python import lrange as lrange

class MPLConfigurator:
    def __init__(self) -> None: ...
    def revert(self) -> None: ...
    def set_fontsize(self, size) -> None: ...

def plot_mts(Y, names: Incomplete | None = None, index: Incomplete | None = None):
    """
    Plot multiple time series
    """
def plot_var_forc(prior, forc, err_upper, err_lower, index: Incomplete | None = None, names: Incomplete | None = None, plot_stderr: bool = True, legend_options: Incomplete | None = None): ...
def plot_with_error(y, error, x: Incomplete | None = None, axes: Incomplete | None = None, value_fmt: str = 'k', error_fmt: str = 'k--', alpha: float = 0.05, stderr_type: str = 'asym'):
    """
    Make plot with optional error bars

    Parameters
    ----------
    y :
    error : array or None
    """
def plot_full_acorr(acorr, fontsize: int = 8, linewidth: int = 8, xlabel: Incomplete | None = None, err_bound: Incomplete | None = None):
    """

    Parameters
    ----------
    """
def acorr_plot(acorr, linewidth: int = 8, xlabel: Incomplete | None = None, ax: Incomplete | None = None) -> None: ...
def plot_acorr_with_error() -> None: ...
def adjust_subplots(**kwds) -> None: ...
def irf_grid_plot(values, stderr, impcol, rescol, names, title, signif: float = 0.05, hlines: Incomplete | None = None, subplot_params: Incomplete | None = None, plot_params: Incomplete | None = None, figsize=(10, 10), stderr_type: str = 'asym'):
    """
    Reusable function to make flexible grid plots of impulse responses and
    comulative effects

    values : (T + 1) x k x k
    stderr : T x k x k
    hlines : k x k
    """
