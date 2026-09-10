from _typeshed import Incomplete
from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.tools.decorators import cache_readonly as cache_readonly

def dispersion_poisson(results):
    """Score/LM type tests for Poisson variance assumptions

    .. deprecated:: 0.14

       dispersion_poisson moved to discrete._diagnostic_count

    Null Hypothesis is

    H0: var(y) = E(y) and assuming E(y) is correctly specified
    H1: var(y) ~= E(y)

    The tests are based on the constrained model, i.e. the Poisson model.
    The tests differ in their assumed alternatives, and in their maintained
    assumptions.

    Parameters
    ----------
    results : Poisson results instance
        This can be a results instance for either a discrete Poisson or a GLM
        with family Poisson.

    Returns
    -------
    res : ndarray, shape (7, 2)
       each row contains the test statistic and p-value for one of the 7 tests
       computed here.
    description : 2-D list of strings
       Each test has two strings a descriptive name and a string for the
       alternative hypothesis.
    """
def dispersion_poisson_generic(results, exog_new_test, exog_new_control: Incomplete | None = None, include_score: bool = False, use_endog: bool = True, cov_type: str = 'HC3', cov_kwds: Incomplete | None = None, use_t: bool = False):
    """A variable addition test for the variance function

    .. deprecated:: 0.14

       dispersion_poisson_generic moved to discrete._diagnostic_count

    This uses an artificial regression to calculate a variant of an LM or
    generalized score test for the specification of the variance assumption
    in a Poisson model. The performed test is a Wald test on the coefficients
    of the `exog_new_test`.

    Warning: insufficiently tested, especially for options
    """

class ResultsGeneric:
    def __init__(self, **kwds) -> None: ...

class TestResults(ResultsGeneric):
    def summary(self): ...

def lm_test_glm(result, exog_extra, mean_deriv: Incomplete | None = None):
    """score/lagrange multiplier test for GLM

    Wooldridge procedure for test of mean function in GLM

    Parameters
    ----------
    results : GLMResults instance
        results instance with the constrained model
    exog_extra : ndarray or None
        additional exogenous variables for variable addition test
        This can be set to None if mean_deriv is provided.
    mean_deriv : None or ndarray
        Extra moment condition that correspond to the partial derivative of
        a mean function with respect to some parameters.

    Returns
    -------
    test_results : Results instance
        The results instance has the following attributes which are score
        statistic and p-value for 3 versions of the score test.

        c1, pval1 : nonrobust score_test results
        c2, pval2 : score test results robust to over or under dispersion
        c3, pval3 : score test results fully robust to any heteroscedasticity

        The test results instance also has a simple summary method.

    Notes
    -----
    TODO: add `df` to results and make df detection more robust

    This implements the auxiliary regression procedure of Wooldridge,
    implemented based on the presentation in chapter 8 in Handbook of
    Applied Econometrics 2.

    References
    ----------
    Wooldridge, Jeffrey M. 1997. “Quasi-Likelihood Methods for Count Data.”
    Handbook of Applied Econometrics 2: 352–406.

    and other articles and text book by Wooldridge

    """
def cm_test_robust(resid, resid_deriv, instruments, weights: int = 1):
    """score/lagrange multiplier of Wooldridge

    generic version of Wooldridge procedure for test of conditional moments

    Limitation: This version allows only for one unconditional moment
    restriction, i.e. resid is scalar for each observation.
    Another limitation is that it assumes independent observations, no
    correlation in residuals and weights cannot be replaced by cross-observation
    whitening.

    Parameters
    ----------
    resid : ndarray, (nobs, )
        conditional moment restriction, E(r | x, params) = 0
    resid_deriv : ndarray, (nobs, k_params)
        derivative of conditional moment restriction with respect to parameters
    instruments : ndarray, (nobs, k_instruments)
        indicator variables of Wooldridge, multiplies the conditional momen
        restriction
    weights : ndarray
        This is a weights function as used in WLS. The moment
        restrictions are multiplied by weights. This corresponds to the
        inverse of the variance in a heteroskedastic model.

    Returns
    -------
    test_results : Results instance
        ???  TODO

    Notes
    -----
    This implements the auxiliary regression procedure of Wooldridge,
    implemented based on procedure 2.1 in Wooldridge 1990.

    Wooldridge allows for multivariate conditional moments (`resid`)
    TODO: check dimensions for multivariate case for extension

    References
    ----------
    Wooldridge
    Wooldridge
    and more Wooldridge

    """
def lm_robust(score, constraint_matrix, score_deriv_inv, cov_score, cov_params: Incomplete | None = None):
    """general formula for score/LM test

    generalized score or lagrange multiplier test for implicit constraints

    `r(params) = 0`, with gradient `R = d r / d params`

    linear constraints are given by `R params - q = 0`

    It is assumed that all arrays are evaluated at the constrained estimates.

    Parameters
    ----------
    score : ndarray, 1-D
        derivative of objective function at estimated parameters
        of constrained model
    constraint_matrix R : ndarray
        Linear restriction matrix or Jacobian of nonlinear constraints
    hessian_inv, Ainv : ndarray, symmetric, square
        inverse of second derivative of objective function
        TODO: could be OPG or any other estimator if information matrix
        equality holds
    cov_score B :  ndarray, symmetric, square
        covariance matrix of the score. This is the inner part of a sandwich
        estimator.
    cov_params V :  ndarray, symmetric, square
        covariance of full parameter vector evaluated at constrained parameter
        estimate. This can be specified instead of cov_score B.

    Returns
    -------
    lm_stat : float
        score/lagrange multiplier statistic

    Notes
    -----

    """
def lm_robust_subset(score, k_constraints, score_deriv_inv, cov_score):
    """general formula for score/LM test

    generalized score or lagrange multiplier test for constraints on a subset
    of parameters

    `params_1 = value`, where params_1 is a subset of the unconstrained
    parameter vector.

    It is assumed that all arrays are evaluated at the constrained estimates.

    Parameters
    ----------
    score : ndarray, 1-D
        derivative of objective function at estimated parameters
        of constrained model
    k_constraint : int
        number of constraints
    score_deriv_inv : ndarray, symmetric, square
        inverse of second derivative of objective function
        TODO: could be OPG or any other estimator if information matrix
        equality holds
    cov_score B :  ndarray, symmetric, square
        covariance matrix of the score. This is the inner part of a sandwich
        estimator.
    not cov_params V :  ndarray, symmetric, square
        covariance of full parameter vector evaluated at constrained parameter
        estimate. This can be specified instead of cov_score B.

    Returns
    -------
    lm_stat : float
        score/lagrange multiplier statistic
    p-value : float
        p-value of the LM test based on chisquare distribution

    Notes
    -----
    The implementation is based on Boos 1992 section 4.1. The same derivation
    is also in other articles and in text books.

    """
def lm_robust_subset_parts(score, k_constraints, score_deriv_uu, score_deriv_cu, cov_score_cc, cov_score_cu, cov_score_uu):
    """robust generalized score tests on subset of parameters

    This is the same as lm_robust_subset with arguments in parts of
    partitioned matrices.
    This can be useful, when we have the parts based on different estimation
    procedures, i.e. when we do not have the full unconstrained model.

    Calculates mainly the covariance of the constraint part of the score.

    Parameters
    ----------
    score : ndarray, 1-D
        derivative of objective function at estimated parameters
        of constrained model. These is the score component for the restricted
        part under hypothesis. The unconstrained part of the score is assumed
        to be zero.
    k_constraint : int
        number of constraints
    score_deriv_uu : ndarray, symmetric, square
        first derivative of moment equation or second derivative of objective
        function for the unconstrained part
        TODO: could be OPG or any other estimator if information matrix
        equality holds
    score_deriv_cu : ndarray
        first cross derivative of moment equation or second cross
        derivative of objective function between.
    cov_score_cc :  ndarray
        covariance matrix of the score for the unconstrained part.
        This is the inner part of a sandwich estimator.
    cov_score_cu :  ndarray
        covariance matrix of the score for the off-diagonal block, i.e.
        covariance between constrained and unconstrained part.
    cov_score_uu :  ndarray
        covariance matrix of the score for the unconstrained part.

    Returns
    -------
    lm_stat : float
        score/lagrange multiplier statistic
    p-value : float
        p-value of the LM test based on chisquare distribution

    Notes
    -----
    TODO: these function should just return the covariance of the score
    instead of calculating the score/lm test.

    Implementation similar to lm_robust_subset and is based on Boos 1992,
    section 4.1 in the form attributed to Breslow (1990). It does not use the
    computation attributed to Kent (1982) and Engle (1984).
    """
def lm_robust_reparameterized(score, params_deriv, score_deriv, cov_score):
    """robust generalized score test for transformed parameters

    The parameters are given by a nonlinear transformation of the estimated
    reduced parameters

    `params = g(params_reduced)`  with jacobian `G = d g / d params_reduced`

    score and other arrays are for full parameter space `params`

    Parameters
    ----------
    score : ndarray, 1-D
        derivative of objective function at estimated parameters
        of constrained model
    params_deriv : ndarray
        Jacobian G of the parameter trasnformation
    score_deriv : ndarray, symmetric, square
        second derivative of objective function
        TODO: could be OPG or any other estimator if information matrix
        equality holds
    cov_score B :  ndarray, symmetric, square
        covariance matrix of the score. This is the inner part of a sandwich
        estimator.

    Returns
    -------
    lm_stat : float
        score/lagrange multiplier statistic
    p-value : float
        p-value of the LM test based on chisquare distribution

    Notes
    -----
    Boos 1992, section 4.3, expression for T_{GS} just before example 6
    """
def conditional_moment_test_generic(mom_test, mom_test_deriv, mom_incl, mom_incl_deriv, var_mom_all: Incomplete | None = None, cov_type: str = 'OPG', cov_kwds: Incomplete | None = None):
    """generic conditional moment test

    This is mainly intended as internal function in support of diagnostic
    and specification tests. It has no conversion and checking of correct
    arguments.

    Parameters
    ----------
    mom_test : ndarray, 2-D (nobs, k_constraints)
        moment conditions that will be tested to be zero
    mom_test_deriv : ndarray, 2-D, square (k_constraints, k_constraints)
        derivative of moment conditions under test with respect to the
        parameters of the model summed over observations.
    mom_incl : ndarray, 2-D (nobs, k_params)
        moment conditions that where use in estimation, assumed to be zero
        This is score_obs in the case of (Q)MLE
    mom_incl_deriv : ndarray, 2-D, square (k_params, k_params)
        derivative of moment conditions of estimator summed over observations
        This is the information matrix or Hessian in the case of (Q)MLE.
    var_mom_all : None, or ndarray, 2-D, (k, k) with k = k_constraints + k_params
        Expected product or variance of the joint (column_stacked) moment
        conditions. The stacking should have the variance of the moment
        conditions under test in the first k_constraint rows and columns.
        If it is not None, then it will be estimated based on cov_type.
        I think: This is the Hessian of the extended or alternative model
        under full MLE and score test assuming information matrix identity
        holds.

    Returns
    -------
    results

    Notes
    -----
    TODO: cov_type other than OPG is missing
    initial implementation based on Cameron Trived countbook 1998 p.48, p.56

    also included: mom_incl can be None if expected mom_test_deriv is zero.

    References
    ----------
    Cameron and Trivedi 1998 count book
    Wooldridge ???
    Pagan and Vella 1989
    """
def conditional_moment_test_regression(mom_test, mom_test_deriv: Incomplete | None = None, mom_incl: Incomplete | None = None, mom_incl_deriv: Incomplete | None = None, var_mom_all: Incomplete | None = None, demean: bool = False, cov_type: str = 'OPG', cov_kwds: Incomplete | None = None):
    """generic conditional moment test based artificial regression

    this is very experimental, no options implemented yet

    so far
    OPG regression, or
    artificial regression with Robust Wald test

    The latter is (as far as I can see) the same as an overidentifying test
    in GMM where the test statistic is the value of the GMM objective function
    and it is assumed that parameters were estimated with optimial GMM, i.e.
    the weight matrix equal to the expectation of the score variance.
    """

class CMTNewey:
    """generic moment test for GMM

    This is a class to calculate and hold the various results

    This is based on Newey 1985 on GMM.
    Lemma 1:
    Theorem 1

    The main method is `chisquare` which returns the result of the
    conditional moment test.

    Warning: name of class and methods will likely be changed

    Parameters
    ----------
    moments : ndarray, 1-D
        moments that are tested to be zero. They do not need to be derived
        from a likelihood function.
    moments_deriv : ndarray
        derivative of the moment function with respect to the parameters that
        are estimated
    cov_moments : ndarray
        An estimate for the joint (expected) covariance of all moments. This
        can be a heteroscedasticity or correlation robust covariance estimate,
        i.e. the inner part of a sandwich covariance.
    weights : ndarray
        Weights used in the GMM estimation.
    transf_mt : ndarray
        This defines the test moments where `transf_mt` is the matrix that
        defines a Linear combination of moments that have expected value equal
        to zero under the Null hypothesis.

    Notes
    -----
    The one letter names in Newey 1985 are

    moments, g :
    cov_moments, V :
    moments_deriv, H :
    weights, W :
    transf_mt, L :
        linear transformation to get the test condition from the moments

    not used, add as argument to methods or __init__?
    K cov for misspecification
    or mispecification_deriv

    This follows the GMM version in Newey 1985a, not the MLE version in
    Newey 1985b. Newey uses the generalized information matrix equality in the
    MLE version Newey (1985b).

    Newey 1985b Lemma 1 does not impose correctly specified likelihood, but
    assumes it in the following. Lemma 1 in both articles are essentially the
    same assuming D = H' W.

    References
    ----------
    - Newey 1985a, Generalized Method of Moment specification testing,
      Journal of Econometrics
    - Newey 1985b, Maximum Likelihood Specification Testing and Conditional
      Moment Tests, Econometrica
    """
    moments: Incomplete
    cov_moments: Incomplete
    moments_deriv: Incomplete
    weights: Incomplete
    transf_mt: Incomplete
    moments_constraint: Incomplete
    htw: Incomplete
    k_moments: Incomplete
    k_constraints: Incomplete
    def __init__(self, moments, cov_moments, moments_deriv, weights, transf_mt) -> None: ...
    def asy_transf_params(self): ...
    def project_w(self): ...
    def asy_transform_mom_constraints(self): ...
    def asy_cov_moments(self):
        """

        `sqrt(T) * g_T(b_0) asy N(K delta, V)`

        mean is not implemented,
        V is the same as cov_moments in __init__ argument
        """
    def cov_mom_constraints(self): ...
    def rank_cov_mom_constraints(self): ...
    def ztest(self):
        """statistic, p-value and degrees of freedom of separate moment test

        currently two sided test only

        TODO: This can use generic ztest/ttest features and return
        ContrastResults
        """
    def chisquare(self):
        """statistic, p-value and degrees of freedom of joint moment test
        """

class CMTTauchen:
    """generic moment tests or conditional moment tests for Quasi-MLE

    This is a generic class based on Tauchen 1985

    The main method is `chisquare` which returns the result of the
    conditional moment test.

    Warning: name of class and of methods will likely be changed

    Parameters
    ----------
    score : ndarray, 1-D
        moment condition used in estimation, score of log-likelihood function
    score_deriv : ndarray
        derivative of score function with respect to the parameters that are
        estimated. This is the Hessian in quasi-maximum likelihood
    moments : ndarray, 1-D
        moments that are tested to be zero. They do not need to be derived
        from a likelihood function.
    moments_deriv : ndarray
        derivative of the moment function with respect to the parameters that
        are estimated
    cov_moments : ndarray
        An estimate for the joint (expected) covariance of score and test
        moments. This can be a heteroscedasticity or correlation robust
        covariance estimate, i.e. the inner part of a sandwich covariance.
    """
    score: Incomplete
    score_deriv: Incomplete
    moments: Incomplete
    moments_deriv: Incomplete
    cov_moments_all: Incomplete
    k_moments_test: Incomplete
    k_params: Incomplete
    k_moments_all: Incomplete
    def __init__(self, score, score_deriv, moments, moments_deriv, cov_moments) -> None: ...
    def cov_params_all(self): ...
    def cov_mom_constraints(self): ...
    def rank_cov_mom_constraints(self): ...
    def ztest(self):
        """statistic, p-value and degrees of freedom of separate moment test

        currently two sided test only

        TODO: This can use generic ztest/ttest features and return
        ContrastResults
        """
    def chisquare(self):
        """statistic, p-value and degrees of freedom of joint moment test
        """
