from _typeshed import Incomplete
from statsmodels.stats.base import HolderTuple as HolderTuple

class CombineResults:
    """Results from combined estimate of means or effect sizes

    This currently includes intermediate results that might be removed
    """
    df_resid: Incomplete
    sd_eff_w_fe_hksj: Incomplete
    sd_eff_w_re_hksj: Incomplete
    h2: Incomplete
    i2: Incomplete
    cache_ci: Incomplete
    def __init__(self, **kwds) -> None: ...
    ci_sample_distr: str
    def conf_int_samples(self, alpha: float = 0.05, use_t: Incomplete | None = None, nobs: Incomplete | None = None, ci_func: Incomplete | None = None):
        """confidence intervals for the effect size estimate of samples

        Additional information needs to be provided for confidence intervals
        that are not based on normal distribution using available variance.
        This is likely to change in future.

        Parameters
        ----------
        alpha : float in (0, 1)
            Significance level for confidence interval. Nominal coverage is
            ``1 - alpha``.
        use_t : None or bool
            If use_t is None, then the attribute `use_t` determines whether
            normal or t-distribution is used for confidence intervals.
            Specifying use_t overrides the attribute.
            If use_t is false, then confidence intervals are based on the
            normal distribution. If it is true, then the t-distribution is
            used.
        nobs : None or float
            Number of observations used for degrees of freedom computation.
            Only used if use_t is true.
        ci_func : None or callable
            User provided function to compute confidence intervals.
            This is not used yet and will allow using non-standard confidence
            intervals.

        Returns
        -------
        ci_eff : tuple of ndarrays
            Tuple (ci_low, ci_upp) with confidence interval computed for each
            sample.

        Notes
        -----
        CombineResults currently only has information from the combine_effects
        function, which does not provide details about individual samples.
        """
    def conf_int(self, alpha: float = 0.05, use_t: Incomplete | None = None):
        """confidence interval for the overall mean estimate

        Parameters
        ----------
        alpha : float in (0, 1)
            Significance level for confidence interval. Nominal coverage is
            ``1 - alpha``.
        use_t : None or bool
            If use_t is None, then the attribute `use_t` determines whether
            normal or t-distribution is used for confidence intervals.
            Specifying use_t overrides the attribute.
            If use_t is false, then confidence intervals are based on the
            normal distribution. If it is true, then the t-distribution is
            used.

        Returns
        -------
        ci_eff_fe : tuple of floats
            Confidence interval for mean effects size based on fixed effects
            model with scale=1.
        ci_eff_re : tuple of floats
            Confidence interval for mean effects size based on random effects
            model with scale=1
        ci_eff_fe_wls : tuple of floats
            Confidence interval for mean effects size based on fixed effects
            model with estimated scale corresponding to WLS, ie. HKSJ.
        ci_eff_re_wls : tuple of floats
            Confidence interval for mean effects size based on random effects
            model with estimated scale corresponding to WLS, ie. HKSJ.
            If random effects method is fully iterated, i.e. Paule-Mandel, then
            the estimated scale is 1.

        """
    def test_homogeneity(self):
        """Test whether the means of all samples are the same

        currently no options, test uses chisquare distribution
        default might change depending on `use_t`

        Returns
        -------
        res : HolderTuple instance
            The results include the following attributes:

            - statistic : float
                Test statistic, ``q`` in meta-analysis, this is the
                pearson_chi2 statistic for the fixed effects model.
            - pvalue : float
                P-value based on chisquare distribution.
            - df : float
                Degrees of freedom, equal to number of studies or samples
                minus 1.
        """
    def summary_array(self, alpha: float = 0.05, use_t: Incomplete | None = None):
        '''Create array with sample statistics and mean estimates

        Parameters
        ----------
        alpha : float in (0, 1)
            Significance level for confidence interval. Nominal coverage is
            ``1 - alpha``.
        use_t : None or bool
            If use_t is None, then the attribute `use_t` determines whether
            normal or t-distribution is used for confidence intervals.
            Specifying use_t overrides the attribute.
            If use_t is false, then confidence intervals are based on the
            normal distribution. If it is true, then the t-distribution is
            used.

        Returns
        -------
        res : ndarray
            Array with columns
            [\'eff\', "sd_eff", "ci_low", "ci_upp", "w_fe","w_re"].
            Rows include statistics for samples and estimates of overall mean.
        column_names : list of str
            The names for the columns, used when creating summary DataFrame.
        '''
    def summary_frame(self, alpha: float = 0.05, use_t: Incomplete | None = None):
        '''Create DataFrame with sample statistics and mean estimates

        Parameters
        ----------
        alpha : float in (0, 1)
            Significance level for confidence interval. Nominal coverage is
            ``1 - alpha``.
        use_t : None or bool
            If use_t is None, then the attribute `use_t` determines whether
            normal or t-distribution is used for confidence intervals.
            Specifying use_t overrides the attribute.
            If use_t is false, then confidence intervals are based on the
            normal distribution. If it is true, then the t-distribution is
            used.

        Returns
        -------
        res : DataFrame
            pandas DataFrame instance with columns
            [\'eff\', "sd_eff", "ci_low", "ci_upp", "w_fe","w_re"].
            Rows include statistics for samples and estimates of overall mean.

        '''
    def plot_forest(self, alpha: float = 0.05, use_t: Incomplete | None = None, use_exp: bool = False, ax: Incomplete | None = None, **kwds):
        """Forest plot with means and confidence intervals

        Parameters
        ----------
        ax : None or matplotlib axis instance
            If ax is provided, then the plot will be added to it.
        alpha : float in (0, 1)
            Significance level for confidence interval. Nominal coverage is
            ``1 - alpha``.
        use_t : None or bool
            If use_t is None, then the attribute `use_t` determines whether
            normal or t-distribution is used for confidence intervals.
            Specifying use_t overrides the attribute.
            If use_t is false, then confidence intervals are based on the
            normal distribution. If it is true, then the t-distribution is
            used.
        use_exp : bool
            If `use_exp` is True, then the effect size and confidence limits
            will be exponentiated. This transform log-odds-ration into
            odds-ratio, and similarly for risk-ratio.
        ax : AxesSubplot, optional
            If given, this axes is used to plot in instead of a new figure
            being created.
        kwds : optional keyword arguments
            Keywords are forwarded to the dot_plot function that creates the
            plot.

        Returns
        -------
        fig : Matplotlib figure instance

        See Also
        --------
        dot_plot

        """

def effectsize_smd(mean1, sd1, nobs1, mean2, sd2, nobs2):
    """effect sizes for mean difference for use in meta-analysis

    mean1, sd1, nobs1 are for treatment
    mean2, sd2, nobs2 are for control

    Effect sizes are computed for the mean difference ``mean1 - mean2``
    standardized by an estimate of the within variance.

    This does not have option yet.
    It uses standardized mean difference with bias correction as effect size.

    This currently does not use np.asarray, all computations are possible in
    pandas.

    Parameters
    ----------
    mean1 : array
        mean of second sample, treatment groups
    sd1 : array
        standard deviation of residuals in treatment groups, within
    nobs1 : array
        number of observations in treatment groups
    mean2, sd2, nobs2 : arrays
        mean, standard deviation and number of observations of control groups

    Returns
    -------
    smd_bc : array
        bias corrected estimate of standardized mean difference
    var_smdbc : array
        estimate of variance of smd_bc

    Notes
    -----
    Status: API will still change. This is currently intended for support of
    meta-analysis.

    References
    ----------
    Borenstein, Michael. 2009. Introduction to Meta-Analysis.
        Chichester: Wiley.

    Chen, Ding-Geng, and Karl E. Peace. 2013. Applied Meta-Analysis with R.
        Chapman & Hall/CRC Biostatistics Series.
        Boca Raton: CRC Press/Taylor & Francis Group.

    """
def effectsize_2proportions(count1, nobs1, count2, nobs2, statistic: str = 'diff', zero_correction: Incomplete | None = None, zero_kwds: Incomplete | None = None):
    '''Effects sizes for two sample binomial proportions

    Parameters
    ----------
    count1, nobs1, count2, nobs2 : array_like
        data for two samples
    statistic : {"diff", "odds-ratio", "risk-ratio", "arcsine"}
        statistic for the comparison of two proportions
        Effect sizes for "odds-ratio" and "risk-ratio" are in logarithm.
    zero_correction : {None, float, "tac", "clip"}
        Some statistics are not finite when zero counts are in the data.
        The options to remove zeros are:

        * float : if zero_correction is a single float, then it will be added
          to all count (cells) if the sample has any zeros.
        * "tac" : treatment arm continuity correction see Ruecker et al 2009,
          section 3.2
        * "clip" : clip proportions without adding a value to all cells
          The clip bounds can be set with zero_kwds["clip_bounds"]

    zero_kwds : dict
        additional options to handle zero counts
        "clip_bounds" tuple, default (1e-6, 1 - 1e-6) if zero_correction="clip"
        other options not yet implemented

    Returns
    -------
    effect size : array
        Effect size for each sample.
    var_es : array
        Estimate of variance of the effect size

    Notes
    -----
    Status: API is experimental, Options for zero handling is incomplete.

    The names for ``statistics`` keyword can be shortened to "rd", "rr", "or"
    and "as".

    The statistics are defined as:

     - risk difference = p1 - p2
     - log risk ratio = log(p1 / p2)
     - log odds_ratio = log(p1 / (1 - p1) * (1 - p2) / p2)
     - arcsine-sqrt = arcsin(sqrt(p1)) - arcsin(sqrt(p2))

    where p1 and p2 are the estimated proportions in sample 1 (treatment) and
    sample 2 (control).

    log-odds-ratio and log-risk-ratio can be transformed back to ``or`` and
    `rr` using `exp` function.

    See Also
    --------
    statsmodels.stats.contingency_tables
    '''
def combine_effects(effect, variance, method_re: str = 'iterated', row_names: Incomplete | None = None, use_t: bool = False, alpha: float = 0.05, **kwds):
    '''combining effect sizes for effect sizes using meta-analysis

    This currently does not use np.asarray, all computations are possible in
    pandas.

    Parameters
    ----------
    effect : array
        mean of effect size measure for all samples
    variance : array
        variance of mean or effect size measure for all samples
    method_re : {"iterated", "chi2"}
        method that is use to compute the between random effects variance
        "iterated" or "pm" uses Paule and Mandel method to iteratively
        estimate the random effects variance. Options for the iteration can
        be provided in the ``kwds``
        "chi2" or "dl" uses DerSimonian and Laird one-step estimator.
    row_names : list of strings (optional)
        names for samples or studies, will be included in results summary and
        table.
    alpha : float in (0, 1)
        significance level, default is 0.05, for the confidence intervals

    Returns
    -------
    results : CombineResults
        Contains estimation results and intermediate statistics, and includes
        a method to return a summary table.
        Statistics from intermediate calculations might be removed at a later
        time.

    Notes
    -----
    Status: Basic functionality is verified, mainly compared to R metafor
    package. However, API might still change.

    This computes both fixed effects and random effects estimates. The
    random effects results depend on the method to estimate the RE variance.

    Scale estimate
    In fixed effects models and in random effects models without fully
    iterated random effects variance, the model will in general not account
    for all residual variance. Traditional meta-analysis uses a fixed
    scale equal to 1, that might not produce test statistics and
    confidence intervals with the correct size. Estimating the scale to account
    for residual variance often improves the small sample properties of
    inference and confidence intervals.
    This adjustment to the standard errors is often referred to as HKSJ
    method based attributed to Hartung and Knapp and Sidik and Jonkman.
    However, this is equivalent to estimating the scale in WLS.
    The results instance includes both, fixed scale and estimated scale
    versions of standard errors and confidence intervals.

    References
    ----------
    Borenstein, Michael. 2009. Introduction to Meta-Analysis.
        Chichester: Wiley.

    Chen, Ding-Geng, and Karl E. Peace. 2013. Applied Meta-Analysis with R.
        Chapman & Hall/CRC Biostatistics Series.
        Boca Raton: CRC Press/Taylor & Francis Group.

    '''
