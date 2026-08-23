from statsmodels.tools.tools import Bunch as Bunch

def partial_project(endog, exog):
    """helper function to get linear projection or partialling out of variables

    endog variables are projected on exog variables

    Parameters
    ----------
    endog : ndarray
        array of variables where the effect of exog is partialled out.
    exog : ndarray
        array of variables on which the endog variables are projected.

    Returns
    -------
    res : instance of Bunch with

        - params : OLS parameter estimates from projection of endog on exog
        - fittedvalues : predicted values of endog given exog
        - resid : residual of the regression, values of endog with effect of
          exog partialled out

    Notes
    -----
    This is no-frills mainly for internal calculations, no error checking or
    array conversion is performed, at least for now.

    """
def cancorr(x1, x2, demean: bool = True, standardize: bool = False):
    """canonical correlation coefficient beween 2 arrays

    Parameters
    ----------
    x1, x2 : ndarrays, 2_D
        two 2-dimensional data arrays, observations in rows, variables in columns
    demean : bool
         If demean is true, then the mean is subtracted from each variable
    standardize : bool
         If standardize is true, then each variable is demeaned and divided by
         its standard deviation. Rescaling does not change the canonical
         correlation coefficients.

    Returns
    -------
    ccorr : ndarray, 1d
        canonical correlation coefficients, sorted from largest to smallest.
        Note, that these are the square root of the eigenvalues.

    Notes
    -----
    This is a helper function for other statistical functions. It only
    calculates the canonical correlation coefficients and does not do a full
    canoncial correlation analysis

    The canonical correlation coefficient is calculated with the generalized
    matrix inverse and does not raise an exception if one of the data arrays
    have less than full column rank.

    See Also
    --------
    cc_ranktest
    cc_stats
    CCA not yet

    """
def cc_ranktest(x1, x2, demean: bool = True, fullrank: bool = False):
    """rank tests based on smallest canonical correlation coefficients

    Anderson canonical correlations test (LM test) and
    Cragg-Donald test (Wald test)
    Assumes homoskedasticity and independent observations, overrejects if
    there is heteroscedasticity or autocorrelation.

    The Null Hypothesis is that the rank is k - 1, the alternative hypothesis
    is that the rank is at least k.


    Parameters
    ----------
    x1, x2 : ndarrays, 2_D
        two 2-dimensional data arrays, observations in rows, variables in columns
    demean : bool
         If demean is true, then the mean is subtracted from each variable.
    fullrank : bool
         If true, then only the test that the matrix has full rank is returned.
         If false, the test for all possible ranks are returned. However, no
         the p-values are not corrected for the multiplicity of tests.

    Returns
    -------
    value : float
        value of the test statistic
    p-value : float
        p-value for the test Null Hypothesis tha the smallest canonical
        correlation coefficient is zero. based on chi-square distribution
    df : int
        degrees of freedom for thechi-square distribution in the hypothesis test
    ccorr : ndarray, 1d
        All canonical correlation coefficients sorted from largest to smallest.

    Notes
    -----
    Degrees of freedom for the distribution of the test statistic are based on
    number of columns of x1 and x2 and not on their matrix rank.
    (I'm not sure yet what the interpretation of the test is if x1 or x2 are of
    reduced rank.)

    See Also
    --------
    cancorr
    cc_stats

    """
def cc_stats(x1, x2, demean: bool = True):
    """MANOVA statistics based on canonical correlation coefficient

    Calculates Pillai's Trace, Wilk's Lambda, Hotelling's Trace and
    Roy's Largest Root.

    Parameters
    ----------
    x1, x2 : ndarrays, 2_D
        two 2-dimensional data arrays, observations in rows, variables in columns
    demean : bool
         If demean is true, then the mean is subtracted from each variable.

    Returns
    -------
    res : dict
        Dictionary containing the test statistics.

    Notes
    -----

    same as `canon` in Stata

    missing: F-statistics and p-values

    TODO: should return a results class instead
    produces nans sometimes, singular, perfect correlation of x1, x2 ?

    """
