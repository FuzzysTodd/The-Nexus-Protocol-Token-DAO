import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete
from statsmodels.base.model import GenericLikelihoodModel as GenericLikelihoodModel, GenericLikelihoodModelResults as GenericLikelihoodModelResults, LikelihoodModel as LikelihoodModel, Model as Model
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.tools.decorators import cache_readonly as cache_readonly

class OrderedModel(GenericLikelihoodModel):
    """Ordinal Model based on logistic or normal distribution

    The parameterization corresponds to the proportional odds model in the
    logistic case.
    The model assumes that the endogenous variable is ordered but that the
    labels have no numeric interpretation besides the ordering.

    The model is based on a latent linear variable, where we observe only a
    discretization.

    y_latent = X beta + u

    The observed variable is defined by the interval

    y = {0 if y_latent <= cut_0
         1 of cut_0 < y_latent <= cut_1
         ...
         K if cut_K < y_latent

    The probability of observing y=k conditional on the explanatory variables
    X is given by

    prob(y = k | x) = Prob(cut_k < y_latent <= cut_k+1)
                    = Prob(cut_k - x beta < u <= cut_k+1 - x beta
                    = F(cut_k+1 - x beta) - F(cut_k - x beta)

    Where F is the cumulative distribution of u which is either the normal
    or the logistic distribution, but can be set to any other continuous
    distribution. We use standardized distributions to avoid identifiability
    problems.

    Parameters
    ----------
    endog : array_like
        Endogenous or dependent ordered categorical variable with k levels.
        Labels or values of endog will internally transformed to consecutive
        integers, 0, 1, 2, ...
        pd.Series with ordered Categorical as dtype should be preferred as it
        gives the order relation between the levels.
        If endog is not a pandas Categorical, then categories are
        sorted in lexicographic order (by numpy.unique).
    exog : array_like
        Exogenous, explanatory variables. This should not include an intercept.
        pd.DataFrame are also accepted.
        see Notes about constant when using formulas
    offset : array_like
        Offset is added to the linear prediction with coefficient equal to 1.
    distr : string 'probit' or 'logit', or a distribution instance
        The default is currently 'probit' which uses the normal distribution
        and corresponds to an ordered Probit model. The distribution is
        assumed to have the main methods of scipy.stats distributions, mainly
        cdf, pdf and ppf. The inverse cdf, ppf, is only use to calculate
        starting values.

    Notes
    -----
    Status: experimental, core results are verified, still subclasses
    `GenericLikelihoodModel` which will change in future versions.

    The parameterization of OrderedModel requires that there is no constant in
    the model, neither explicit nor implicit. The constant is equivalent to
    shifting all thresholds and is therefore not separately identified.

    Patsy's formula specification does not allow a design matrix without
    explicit or implicit constant if there are categorical variables (or maybe
    splines) among explanatory variables. As workaround, statsmodels removes an
    explicit intercept.

    Consequently, there are two valid cases to get a design matrix without
    intercept when using formulas:

    - specify a model without explicit and implicit intercept which is possible
      if there are only numerical variables in the model.
    - specify a model with an explicit intercept which statsmodels will remove.

    Models with an implicit intercept will be overparameterized, the parameter
    estimates will not be fully identified, cov_params will not be invertible
    and standard errors might contain nans. The computed results will be
    dominated by numerical imprecision coming mainly from convergence tolerance
    and numerical derivatives.

    The model will raise a ValueError if a remaining constant is detected.

    """
    distr: Incomplete
    offset: Incomplete
    endog: Incomplete
    k_extra: Incomplete
    df_model: Incomplete
    df_resid: Incomplete
    results_class: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, distr: str = 'probit', **kwds) -> None: ...
    @classmethod
    def from_formula(cls, formula, data, subset: Incomplete | None = None, drop_cols: Incomplete | None = None, *args, **kwargs): ...
    def cdf(self, x):
        """Cdf evaluated at x.

        Parameters
        ----------
        x : array_like
            Points at which cdf is evaluated. In the model `x` is the latent
            variable plus threshold constants.

        Returns
        -------
        Value of the cumulative distribution function of the underlying latent
        variable evaluated at x.
        """
    def pdf(self, x):
        """Pdf evaluated at x

        Parameters
        ----------
        x : array_like
            Points at which cdf is evaluated. In the model `x` is the latent
            variable plus threshold constants.

        Returns
        -------
        Value of the probability density function of the underlying latent
        variable evaluated at x.
        """
    def prob(self, low, upp):
        """Interval probability.

        Probability that value is in interval (low, upp], computed as

            prob = cdf(upp) - cdf(low)

        Parameters
        ----------
        low : array_like
            lower bound for interval
        upp : array_like
            upper bound for interval

        Returns
        -------
        float or ndarray
            Probability that value falls in interval (low, upp]

        """
    def transform_threshold_params(self, params):
        """transformation of the parameters in the optimization

        Parameters
        ----------
        params : nd_array
            Contains (exog_coef, transformed_thresholds) where exog_coef are
            the coefficient for the explanatory variables in the linear term,
            transformed threshold or cutoff points. The first, lowest threshold
            is unchanged, all other thresholds are in terms of exponentiated
            increments.

        Returns
        -------
        thresh : nd_array
            Thresh are the thresholds or cutoff constants for the intervals.

        """
    def transform_reverse_threshold_params(self, params):
        """obtain transformed thresholds from original thresholds or cutoffs

        Parameters
        ----------
        params : ndarray
            Threshold values, cutoff constants for choice intervals, which
            need to be monotonically increasing.

        Returns
        -------
        thresh_params : ndarrray
            Transformed threshold parameter.
            The first, lowest threshold is unchanged, all other thresholds are
            in terms of exponentiated increments.
            Transformed parameters can be any real number without restrictions.

        """
    def predict(self, params, exog: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'prob'):
        '''
        Predicted probabilities for each level of the ordinal endog.

        Parameters
        ----------
        params : ndarray
            Parameters for the Model, (exog_coef, transformed_thresholds).
        exog : array_like, optional
            Design / exogenous data. If exog is None, model exog is used.
        offset : array_like, optional
            Offset is added to the linear prediction with coefficient
            equal to 1. If offset is not provided and exog
            is None, uses the model\'s offset if present.  If not, uses
            0 as the default value.
        which : {"prob", "linpred", "cumprob"}
            Determines which statistic is predicted.

            - prob : predicted probabilities to be in each choice. 2-dim.
            - linear : 1-dim linear prediction of the latent variable
              ``x b + offset``
            - cumprob : predicted cumulative probability to be in choice k or
              lower

        Returns
        -------
        predicted values : ndarray
            If which is "prob", then 2-dim predicted probabilities with
            observations in rows and one column for each category or level of
            the categorical dependent variable.
            If which is "cumprob", then "prob" ar cumulatively added to get the
            cdf at k, i.e. probability of observing choice k or lower.
            If which is "linpred", then the conditional prediction of the
            latent variable is returned. In this case, the return is
            one-dimensional.
        '''
    def loglike(self, params): ...
    def loglikeobs(self, params):
        """
        Log-likelihood of OrderdModel for all observations.

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike_obs : array_like
            The log likelihood for each observation of the model evaluated
            at ``params``.
        """
    def score_obs_(self, params):
        """score, first derivative of loglike for each observations

        This currently only implements the derivative with respect to the
        exog parameters, but not with respect to threshold parameters.

        """
    @property
    def start_params(self):
        """Start parameters for the optimization corresponding to null model.

        The threshold are computed from the observed frequencies and
        transformed to the exponential increments parameterization.
        The parameters for explanatory variables are set to zero.
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'nm', maxiter: int = 500, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, retall: int = 0, **kwargs): ...

class OrderedResults(GenericLikelihoodModelResults):
    """Results class for OrderedModel

    This class inherits from GenericLikelihoodModelResults and not all
    inherited methods might be appropriate in this case.
    """
    def pred_table(self):
        """prediction table

        returns pandas DataFrame

        """
    def llnull(self):
        """
        Value of the loglikelihood of model without explanatory variables
        """
    def prsquared(self):
        """
        McFadden's pseudo-R-squared. `1 - (llf / llnull)`
        """
    def llr(self):
        """
        Likelihood ratio chi-squared statistic; `-2*(llnull - llf)`
        """
    def llr_pvalue(self):
        """
        The chi-squared probability of getting a log-likelihood ratio
        statistic greater than llr.  llr has a chi-squared distribution
        with degrees of freedom `df_model`.
        """
    def resid_prob(self):
        """probability residual

        Probability-scale residual is ``P(Y < y) − P(Y > y)`` where `Y` is the
        observed choice and ``y`` is a random variable corresponding to the
        predicted distribution.

        References
        ----------
        Shepherd BE, Li C, Liu Q (2016) Probability-scale residuals for
        continuous, discrete, and censored data.
        The Canadian Journal of Statistics. 44:463–476.

        Li C and Shepherd BE (2012) A new residual for ordinal outcomes.
        Biometrika. 99: 473–480

        """

class OrderedResultsWrapper(lm.RegressionResultsWrapper): ...
