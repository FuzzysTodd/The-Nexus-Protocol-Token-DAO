from _typeshed import Incomplete
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.statespace import initialization as initialization, mlemodel as mlemodel
from statsmodels.tsa.statespace.kalman_smoother import SMOOTHER_STATE as SMOOTHER_STATE, SMOOTHER_STATE_AUTOCOV as SMOOTHER_STATE_AUTOCOV, SMOOTHER_STATE_COV as SMOOTHER_STATE_COV
from statsmodels.tsa.statespace.tools import constrain_stationary_univariate as constrain_stationary_univariate, unconstrain_stationary_univariate as unconstrain_stationary_univariate

class QuarterlyAR1(mlemodel.MLEModel):
    """
    AR(1) model for monthly growth rates aggregated to quarterly frequency

    Parameters
    ----------
    endog : array_like
        The observed time-series process :math:`y`

    Notes
    -----
    This model is internal, used to estimate starting parameters for the
    DynamicFactorMQ class. The model is:

    .. math::

        y_t & = \\begin{bmatrix} 1 & 2 & 3 & 2 & 1 \\end{bmatrix} \\alpha_t \\\\\n        \\alpha_t & = \\begin{bmatrix}
            \\phi & 0 & 0 & 0 & 0 \\\\\n               1 & 0 & 0 & 0 & 0 \\\\\n               0 & 1 & 0 & 0 & 0 \\\\\n               0 & 0 & 1 & 0 & 0 \\\\\n               0 & 0 & 0 & 1 & 0 \\\\\n        \\end{bmatrix} +
        \\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\end{bmatrix} \\varepsilon_t

    The two parameters to be estimated are :math:`\\phi` and :math:`\\sigma^2`.

    It supports fitting via the usual quasi-Newton methods, as well as using
    the EM algorithm.

    """
    def __init__(self, endog) -> None: ...
    @property
    def param_names(self): ...
    @property
    def start_params(self): ...
    def fit(self, *args, **kwargs): ...
    def fit_em(self, start_params: Incomplete | None = None, transformed: bool = True, cov_type: str = 'none', cov_kwds: Incomplete | None = None, maxiter: int = 500, tolerance: float = 1e-06, em_initialization: bool = True, mstep_method: Incomplete | None = None, full_output: bool = True, return_params: bool = False, low_memory: bool = False): ...
    def transform_params(self, unconstrained): ...
    def untransform_params(self, constrained): ...
    def update(self, params, **kwargs) -> None: ...
