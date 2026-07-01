from _typeshed import Incomplete
from statsmodels.base.model import LikelihoodModelResults as LikelihoodModelResults
from statsmodels.regression.linear_model import OLS as OLS

class PatsyFormula:
    """
    A simple wrapper for a string to be interpreted as a Patsy formula.
    """
    formula: Incomplete
    def __init__(self, formula) -> None: ...

class MICEData:
    __doc__: Incomplete
    regularized: Incomplete
    data: Incomplete
    history_callback: Incomplete
    history: Incomplete
    predict_kwds: Incomplete
    perturbation_method: Incomplete
    ix_obs: Incomplete
    ix_miss: Incomplete
    models: Incomplete
    results: Incomplete
    conditional_formula: Incomplete
    init_kwds: Incomplete
    fit_kwds: Incomplete
    model_class: Incomplete
    params: Incomplete
    k_pmm: Incomplete
    def __init__(self, data, perturbation_method: str = 'gaussian', k_pmm: int = 20, history_callback: Incomplete | None = None) -> None: ...
    def next_sample(self):
        """
        Returns the next imputed dataset in the imputation process.

        Returns
        -------
        data : array_like
            An imputed dataset from the MICE chain.

        Notes
        -----
        `MICEData` does not have a `skip` parameter.  Consecutive
        values returned by `next_sample` are immediately consecutive
        in the imputation chain.

        The returned value is a reference to the data attribute of
        the class and should be copied before making any changes.
        """
    def set_imputer(self, endog_name, formula: Incomplete | None = None, model_class: Incomplete | None = None, init_kwds: Incomplete | None = None, fit_kwds: Incomplete | None = None, predict_kwds: Incomplete | None = None, k_pmm: int = 20, perturbation_method: Incomplete | None = None, regularized: bool = False) -> None:
        """
        Specify the imputation process for a single variable.

        Parameters
        ----------
        endog_name : str
            Name of the variable to be imputed.
        formula : str
            Conditional formula for imputation. Defaults to a formula
            with main effects for all other variables in dataset.  The
            formula should only include an expression for the mean
            structure, e.g. use 'x1 + x2' not 'x4 ~ x1 + x2'.
        model_class : statsmodels model
            Conditional model for imputation. Defaults to OLS.  See below
            for more information.
        init_kwds : dit-like
            Keyword arguments passed to the model init method.
        fit_kwds : dict-like
            Keyword arguments passed to the model fit method.
        predict_kwds : dict-like
            Keyword arguments passed to the model predict method.
        k_pmm : int
            Determines number of neighboring observations from which
            to randomly sample when using predictive mean matching.
        perturbation_method : str
            Either 'gaussian' or 'bootstrap'. Determines the method
            for perturbing parameters in the imputation model.  If
            None, uses the default specified at class initialization.
        regularized : dict
            If regularized[name]=True, `fit_regularized` rather than
            `fit` is called when fitting imputation models for this
            variable.  When regularized[name]=True for any variable,
            perturbation_method must be set to boot.

        Notes
        -----
        The model class must meet the following conditions:
            * A model must have a 'fit' method that returns an object.
            * The object returned from `fit` must have a `params` attribute
              that is an array-like object.
            * The object returned from `fit` must have a cov_params method
              that returns a square array-like object.
            * The model must have a `predict` method.
        """
    def update_all(self, n_iter: int = 1) -> None:
        """
        Perform a specified number of MICE iterations.

        Parameters
        ----------
        n_iter : int
            The number of updates to perform.  Only the result of the
            final update will be available.

        Notes
        -----
        The imputed values are stored in the class attribute `self.data`.
        """
    def get_split_data(self, vname):
        """
        Return endog and exog for imputation of a given variable.

        Parameters
        ----------
        vname : str
           The variable for which the split data is returned.

        Returns
        -------
        endog_obs : DataFrame
            Observed values of the variable to be imputed.
        exog_obs : DataFrame
            Current values of the predictors where the variable to be
            imputed is observed.
        exog_miss : DataFrame
            Current values of the predictors where the variable to be
            Imputed is missing.
        init_kwds : dict-like
            The init keyword arguments for `vname`, processed through Patsy
            as required.
        fit_kwds : dict-like
            The fit keyword arguments for `vname`, processed through Patsy
            as required.
        """
    def get_fitting_data(self, vname):
        """
        Return the data needed to fit a model for imputation.

        The data is used to impute variable `vname`, and therefore
        only includes cases for which `vname` is observed.

        Values of type `PatsyFormula` in `init_kwds` or `fit_kwds` are
        processed through Patsy and subset to align with the model's
        endog and exog.

        Parameters
        ----------
        vname : str
           The variable for which the fitting data is returned.

        Returns
        -------
        endog : DataFrame
            Observed values of `vname`.
        exog : DataFrame
            Regression design matrix for imputing `vname`.
        init_kwds : dict-like
            The init keyword arguments for `vname`, processed through Patsy
            as required.
        fit_kwds : dict-like
            The fit keyword arguments for `vname`, processed through Patsy
            as required.
        """
    def plot_missing_pattern(self, ax: Incomplete | None = None, row_order: str = 'pattern', column_order: str = 'pattern', hide_complete_rows: bool = False, hide_complete_columns: bool = False, color_row_patterns: bool = True):
        """
        Generate an image showing the missing data pattern.

        Parameters
        ----------
        ax : AxesSubplot
            Axes on which to draw the plot.
        row_order : str
            The method for ordering the rows.  Must be one of 'pattern',
            'proportion', or 'raw'.
        column_order : str
            The method for ordering the columns.  Must be one of 'pattern',
            'proportion', or 'raw'.
        hide_complete_rows : bool
            If True, rows with no missing values are not drawn.
        hide_complete_columns : bool
            If True, columns with no missing values are not drawn.
        color_row_patterns : bool
            If True, color the unique row patterns, otherwise use grey
            and white as colors.

        Returns
        -------
        A figure containing a plot of the missing data pattern.
        """
    def plot_bivariate(self, col1_name, col2_name, lowess_args: Incomplete | None = None, lowess_min_n: int = 40, jitter: Incomplete | None = None, plot_points: bool = True, ax: Incomplete | None = None):
        """
        Plot observed and imputed values for two variables.

        Displays a scatterplot of one variable against another.  The
        points are colored according to whether the values are
        observed or imputed.

        Parameters
        ----------
        col1_name : str
            The variable to be plotted on the horizontal axis.
        col2_name : str
            The variable to be plotted on the vertical axis.
        lowess_args : dictionary
            A dictionary of dictionaries, keys are 'ii', 'io', 'oi'
            and 'oo', where 'o' denotes 'observed' and 'i' denotes
            imputed.  See Notes for details.
        lowess_min_n : int
            Minimum sample size to plot a lowess fit
        jitter : float or tuple
            Standard deviation for jittering points in the plot.
            Either a single scalar applied to both axes, or a tuple
            containing x-axis jitter and y-axis jitter, respectively.
        plot_points : bool
            If True, the data points are plotted.
        ax : AxesSubplot
            Axes on which to plot, created if not provided.

        Returns
        -------
        The matplotlib figure on which the plot id drawn.
        """
    def plot_fit_obs(self, col_name, lowess_args: Incomplete | None = None, lowess_min_n: int = 40, jitter: Incomplete | None = None, plot_points: bool = True, ax: Incomplete | None = None):
        """
        Plot fitted versus imputed or observed values as a scatterplot.

        Parameters
        ----------
        col_name : str
            The variable to be plotted on the horizontal axis.
        lowess_args : dict-like
            Keyword arguments passed to lowess fit.  A dictionary of
            dictionaries, keys are 'o' and 'i' denoting 'observed' and
            'imputed', respectively.
        lowess_min_n : int
            Minimum sample size to plot a lowess fit
        jitter : float or tuple
            Standard deviation for jittering points in the plot.
            Either a single scalar applied to both axes, or a tuple
            containing x-axis jitter and y-axis jitter, respectively.
        plot_points : bool
            If True, the data points are plotted.
        ax : AxesSubplot
            Axes on which to plot, created if not provided.

        Returns
        -------
        The matplotlib figure on which the plot is drawn.
        """
    def plot_imputed_hist(self, col_name, ax: Incomplete | None = None, imp_hist_args: Incomplete | None = None, obs_hist_args: Incomplete | None = None, all_hist_args: Incomplete | None = None):
        """
        Display imputed values for one variable as a histogram.

        Parameters
        ----------
        col_name : str
            The name of the variable to be plotted.
        ax : AxesSubplot
            An axes on which to draw the histograms.  If not provided,
            one is created.
        imp_hist_args : dict
            Keyword arguments to be passed to pyplot.hist when
            creating the histogram for imputed values.
        obs_hist_args : dict
            Keyword arguments to be passed to pyplot.hist when
            creating the histogram for observed values.
        all_hist_args : dict
            Keyword arguments to be passed to pyplot.hist when
            creating the histogram for all values.

        Returns
        -------
        The matplotlib figure on which the histograms were drawn
        """
    def perturb_params(self, vname) -> None: ...
    def impute(self, vname) -> None: ...
    def update(self, vname) -> None:
        """
        Impute missing values for a single variable.

        This is a two-step process in which first the parameters are
        perturbed, then the missing values are re-imputed.

        Parameters
        ----------
        vname : str
            The name of the variable to be updated.
        """
    def impute_pmm(self, vname) -> None:
        """
        Use predictive mean matching to impute missing values.

        Notes
        -----
        The `perturb_params` method must be called first to define the
        model.
        """

class MICE:
    __doc__: Incomplete
    model_formula: Incomplete
    model_class: Incomplete
    n_skip: Incomplete
    data: Incomplete
    results_list: Incomplete
    init_kwds: Incomplete
    fit_kwds: Incomplete
    def __init__(self, model_formula, model_class, data, n_skip: int = 3, init_kwds: Incomplete | None = None, fit_kwds: Incomplete | None = None) -> None: ...
    def next_sample(self):
        """
        Perform one complete MICE iteration.

        A single MICE iteration updates all missing values using their
        respective imputation models, then fits the analysis model to
        the imputed data.

        Returns
        -------
        params : array_like
            The model parameters for the analysis model.

        Notes
        -----
        This function fits the analysis model and returns its
        parameter estimate.  The parameter vector is not stored by the
        class and is not used in any subsequent calls to `combine`.
        Use `fit` to run all MICE steps together and obtain summary
        results.

        The complete cycle of missing value imputation followed by
        fitting the analysis model is repeated `n_skip + 1` times and
        the analysis model parameters from the final fit are returned.
        """
    endog_names: Incomplete
    exog_names: Incomplete
    def fit(self, n_burnin: int = 10, n_imputations: int = 10):
        """
        Fit a model using MICE.

        Parameters
        ----------
        n_burnin : int
            The number of burn-in cycles to skip.
        n_imputations : int
            The number of data sets to impute
        """
    def combine(self):
        """
        Pools MICE imputation results.

        This method can only be used after the `run` method has been
        called.  Returns estimates and standard errors of the analysis
        model parameters.

        Returns a MICEResults instance.
        """

class MICEResults(LikelihoodModelResults):
    def __init__(self, model, params, normalized_cov_params) -> None: ...
    def summary(self, title: Incomplete | None = None, alpha: float = 0.05):
        """
        Summarize the results of running MICE.

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
