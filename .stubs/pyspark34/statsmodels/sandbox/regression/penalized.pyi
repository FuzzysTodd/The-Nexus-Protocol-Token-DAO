from _typeshed import Incomplete
from statsmodels.compat.python import lrange as lrange
from statsmodels.regression.feasible_gls import atleast_2dcols as atleast_2dcols
from statsmodels.regression.linear_model import GLS as GLS, OLS as OLS, RegressionResults as RegressionResults
from statsmodels.tools.decorators import cache_readonly as cache_readonly

class TheilGLS(GLS):
    """GLS with stochastic restrictions

    TheilGLS estimates the following linear model

    .. math:: y = X \\beta + u

    using additional information given by a stochastic constraint

    .. math:: q = R \\beta + v

    :math:`E(u) = 0`, :math:`cov(u) = \\Sigma`
    :math:`cov(u, v) = \\Sigma_p`, with full rank.

    u and v are assumed to be independent of each other.
    If :math:`E(v) = 0`, then the estimator is unbiased.

    Note: The explanatory variables are not rescaled, the parameter estimates
    not scale equivariant and fitted values are not scale invariant since
    scaling changes the relative penalization weights (for given \\Sigma_p).

    Note: GLS is not tested yet, only Sigma is identity is tested

    Notes
    -----

    The parameter estimates solves the moment equation:

    .. math:: (X' \\Sigma X + \\lambda R' \\sigma^2 \\Sigma_p^{-1} R) b = X' \\Sigma y + \\lambda R' \\Sigma_p^{-1} q

    :math:`\\lambda` is the penalization weight similar to Ridge regression.

    If lambda is zero, then the parameter estimate is the same as OLS. If
    lambda goes to infinity, then the restriction is imposed with equality.
    In the model `pen_weight` is used as name instead of $\\lambda$

    R does not have to be square. The number of rows of R can be smaller
    than the number of parameters. In this case not all linear combination
    of parameters are penalized.

    The stochastic constraint can be interpreted in several different ways:

     - The prior information represents parameter estimates from independent
       prior samples.
     - We can consider it just as linear restrictions that we do not want
       to impose without uncertainty.
     - With a full rank square restriction matrix R, the parameter estimate
       is the same as a Bayesian posterior mean for the case of an informative
       normal prior, normal likelihood and known error variance Sigma. If R
       is less than full rank, then it defines a partial prior.

    References
    ----------
    Theil Goldberger

    Baum, Christopher slides for tgmixed in Stata

    (I do not remember what I used when I first wrote the code.)

    Parameters
    ----------
    endog : array_like, 1-D
        dependent or endogenous variable
    exog : array_like, 1D or 2D
        array of explanatory or exogenous variables
    r_matrix : None or array_like, 2D
        array of linear restrictions for stochastic constraint.
        default is identity matrix that does not penalize constant, if constant
        is detected to be in `exog`.
    q_matrix : None or array_like
        mean of the linear restrictions. If None, the it is set to zeros.
    sigma_prior : None or array_like
        A fully specified sigma_prior is a square matrix with the same number
        of rows and columns as there are constraints (number of rows of r_matrix).
        If sigma_prior is None, a scalar or one-dimensional, then a diagonal matrix
        is created.
    sigma : None or array_like
        Sigma is the covariance matrix of the error term that is used in the same
        way as in GLS.
    """
    r_matrix: Incomplete
    q_matrix: Incomplete
    sigma_prior: Incomplete
    sigma_prior_inv: Incomplete
    def __init__(self, endog, exog, r_matrix: Incomplete | None = None, q_matrix: Incomplete | None = None, sigma_prior: Incomplete | None = None, sigma: Incomplete | None = None) -> None: ...
    res_gls: Incomplete
    normalized_cov_params: Incomplete
    xpxi: Incomplete
    sigma2_e: Incomplete
    def fit(self, pen_weight: float = 1.0, cov_type: str = 'sandwich', use_t: bool = True):
        """Estimate parameters and return results instance

        Parameters
        ----------
        pen_weight : float
            penalization factor for the restriction, default is 1.
        cov_type : str, 'data-prior' or 'sandwich'
            'data-prior' assumes that the stochastic restriction reflects a
            previous sample. The covariance matrix of the parameter estimate
            is in this case the same form as the one of GLS.
            The covariance matrix for cov_type='sandwich' treats the stochastic
            restriction (R and q) as fixed and has a sandwich form analogously
            to M-estimators.

        Returns
        -------
        results : TheilRegressionResults instance

        Notes
        -----
        cov_params for cov_type data-prior, is calculated as

        .. math:: \\sigma^2 A^{-1}

        cov_params for cov_type sandwich, is calculated as

        .. math:: \\sigma^2 A^{-1} (X'X) A^{-1}

        where :math:`A = X' \\Sigma X + \\lambda \\sigma^2 R' \\Simga_p^{-1} R`

        :math:`\\sigma^2` is an estimate of the error variance.
        :math:`\\sigma^2` inside A is replaced by the estimate from the initial
        GLS estimate. :math:`\\sigma^2` in cov_params is obtained from the
        residuals of the final estimate.

        The sandwich form of the covariance estimator is not robust to
        misspecified heteroscedasticity or autocorrelation.
        """
    def select_pen_weight(self, method: str = 'aicc', start_params: float = 1.0, optim_args: Incomplete | None = None):
        """find penalization factor that minimizes gcv or an information criterion

        Parameters
        ----------
        method : str
            the name of an attribute of the results class. Currently the following
            are available aic, aicc, bic, gc and gcv.
        start_params : float
            starting values for the minimization to find the penalization factor
            `lambd`. Not since there can be local minima, it is best to try
            different starting values.
        optim_args : None or dict
            optimization keyword arguments used with `scipy.optimize.fmin`

        Returns
        -------
        min_pen_weight : float
            The penalization factor at which the target criterion is (locally)
            minimized.

        Notes
        -----
        This uses `scipy.optimize.fmin` as optimizer.
        """

class TheilRegressionResults(RegressionResults):
    df_model: Incomplete
    df_resid: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def hatmatrix_diag(self):
        """diagonal of hat matrix

        diag(X' xpxi X)

        where xpxi = (X'X + sigma2_e * lambd * sigma_prior)^{-1}

        Notes
        -----

        uses wexog, so this includes weights or sigma - check this case

        not clear whether I need to multiply by sigmahalf, i.e.

        (W^{-0.5} X) (X' W X)^{-1} (W^{-0.5} X)'  or
        (W X) (X' W X)^{-1} (W X)'

        projection y_hat = H y    or in terms of transformed variables (W^{-0.5} y)

        might be wrong for WLS and GLS case
        """
    def hatmatrix_trace(self):
        """trace of hat matrix
        """
    def gcv(self): ...
    def cv(self): ...
    def aicc(self): ...
    def test_compatibility(self):
        """Hypothesis test for the compatibility of prior mean with data
        """
    def share_data(self):
        """a measure for the fraction of the data in the estimation result

        The share of the prior information is `1 - share_data`.

        Returns
        -------
        share : float between 0 and 1
            share of data defined as the ration between effective degrees of
            freedom of the model and the number (TODO should be rank) of the
            explanatory variables.
        """

def coef_restriction_meandiff(n_coeffs, n_vars: Incomplete | None = None, position: int = 0): ...
def coef_restriction_diffbase(n_coeffs, n_vars: Incomplete | None = None, position: int = 0, base_idx: int = 0): ...
def next_odd(d): ...
def coef_restriction_diffseq(n_coeffs, degree: int = 1, n_vars: Incomplete | None = None, position: int = 0, base_idx: int = 0): ...
