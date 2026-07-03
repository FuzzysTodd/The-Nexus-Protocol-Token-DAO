from _typeshed import Incomplete
from statsmodels.base.model import LikelihoodModelResults as LikelihoodModelResults

class BayesGaussMI:
    """
    Bayesian Imputation using a Gaussian model.

    The approach is Bayesian.  The goal is to sample from the joint
    distribution of the mean vector, covariance matrix, and missing
    data values given the observed data values.  Conjugate priors for
    the population mean and covariance matrix are used.  Gibbs
    sampling is used to update the mean vector, covariance matrix, and
    missing data values in turn.  After burn-in, the imputed complete
    data sets from the Gibbs chain can be used in multiple imputation
    analyses (MI).

    Parameters
    ----------
    data : ndarray
        The array of data to be imputed.  Values in the array equal to
        NaN are imputed.
    mean_prior : ndarray, optional
        The covariance matrix of the Gaussian prior distribution for
        the mean vector.  If not provided, the identity matrix is
        used.
    cov_prior : ndarray, optional
        The center matrix for the inverse Wishart prior distribution
        for the covariance matrix.  If not provided, the identity
        matrix is used.
    cov_prior_df : positive float
        The degrees of freedom of the inverse Wishart prior
        distribution for the covariance matrix.  Defaults to 1.

    Examples
    --------
    A basic example with OLS. Data is generated assuming 10% is missing at
    random.

    >>> import numpy as np
    >>> x = np.random.standard_normal((1000, 2))
    >>> x.flat[np.random.sample(2000) < 0.1] = np.nan

    The imputer is used with ``MI``.

    >>> import statsmodels.api as sm
    >>> def model_args_fn(x):
    ...     # Return endog, exog from x
    ...    return x[:, 0], x[:, 1:]
    >>> imp = sm.BayesGaussMI(x)
    >>> mi = sm.MI(imp, sm.OLS, model_args_fn)
    """
    exog_names: Incomplete
    data: Incomplete
    mask: Incomplete
    nobs: Incomplete
    nvar: Incomplete
    patterns: Incomplete
    cov: Incomplete
    mean: Incomplete
    mean_prior: Incomplete
    cov_prior: Incomplete
    cov_prior_df: Incomplete
    def __init__(self, data, mean_prior: Incomplete | None = None, cov_prior: Incomplete | None = None, cov_prior_df: int = 1) -> None: ...
    def update(self) -> None:
        """
        Cycle through all Gibbs updates.
        """
    def update_data(self) -> None:
        """
        Gibbs update of the missing data values.
        """
    def update_mean(self) -> None:
        """
        Gibbs update of the mean vector.

        Do not call until update_data has been called once.
        """
    def update_cov(self) -> None:
        """
        Gibbs update of the covariance matrix.

        Do not call until update_data has been called once.
        """

class MI:
    """
    MI performs multiple imputation using a provided imputer object.

    Parameters
    ----------
    imp : object
        An imputer class, such as BayesGaussMI.
    model : model class
        Any statsmodels model class.
    model_args_fn : function
        A function taking an imputed dataset as input and returning
        endog, exog.  If the model is fit using a formula, returns
        a DataFrame used to build the model.  Optional when a formula
        is used.
    model_kwds_fn : function, optional
        A function taking an imputed dataset as input and returning
        a dictionary of model keyword arguments.
    formula : str, optional
        If provided, the model is constructed using the `from_formula`
        class method, otherwise the `__init__` method is used.
    fit_args : list-like, optional
        List of arguments to be passed to the fit method
    fit_kwds : dict-like, optional
        Keyword arguments to be passed to the fit method
    xfunc : function mapping ndarray to ndarray
        A function that is applied to the complete data matrix
        prior to fitting the model
    burn : int
        Number of burn-in iterations
    nrep : int
        Number of imputed data sets to use in the analysis
    skip : int
        Number of Gibbs iterations to skip between successive
        multiple imputation fits.

    Notes
    -----
    The imputer object must have an 'update' method, and a 'data'
    attribute that contains the current imputed dataset.

    xfunc can be used to introduce domain constraints, e.g. when
    imputing binary data the imputed continuous values can be rounded
    to 0/1.
    """
    imp: Incomplete
    skip: Incomplete
    model: Incomplete
    formula: Incomplete
    model_args_fn: Incomplete
    model_kwds_fn: Incomplete
    fit_args: Incomplete
    fit_kwds: Incomplete
    xfunc: Incomplete
    nrep: Incomplete
    def __init__(self, imp, model, model_args_fn: Incomplete | None = None, model_kwds_fn: Incomplete | None = None, formula: Incomplete | None = None, fit_args: Incomplete | None = None, fit_kwds: Incomplete | None = None, xfunc: Incomplete | None = None, burn: int = 100, nrep: int = 20, skip: int = 10) -> None: ...
    def fit(self, results_cb: Incomplete | None = None):
        """
        Impute datasets, fit models, and pool results.

        Parameters
        ----------
        results_cb : function, optional
            If provided, each results instance r is passed through `results_cb`,
            then appended to the `results` attribute of the MIResults object.
            To save complete results, use `results_cb=lambda x: x`.  The default
            behavior is to save no results.

        Returns
        -------
        A MIResults object.
        """

class MIResults(LikelihoodModelResults):
    """
    A results class for multiple imputation (MI).

    Parameters
    ----------
    mi : MI instance
        The MI object that produced the results
    model : instance of statsmodels model class
        This can be any instance from the multiple imputation runs.
        It is used to get class information, the specific parameter
        and data values are not used.
    params : array_like
        The overall multiple imputation parameter estimates.
    normalized_cov_params : array_like (2d)
        The overall variance covariance matrix of the estimates.
    """
    mi: Incomplete
    def __init__(self, mi, model, params, normalized_cov_params) -> None: ...
    def summary(self, title: Incomplete | None = None, alpha: float = 0.05):
        """
        Summarize the results of running multiple imputation.

        Parameters
        ----------
        title : str, optional
            Title for the top table. If not None, then this replaces
            the default title
        alpha : float
            Significance level for the confidence intervals

        Returns
        -------
        smry : Summary instance
            This holds the summary tables and text, which can be
            printed or converted to various output formats.
        """
