from _typeshed import Incomplete

__all__ = ['plot_fit', 'plot_regress_exog', 'plot_partregress', 'plot_ccpr', 'plot_regress_exog', 'plot_partregress_grid', 'plot_ccpr_grid', 'add_lowess', 'abline_plot', 'influence_plot', 'plot_leverage_resid2', 'added_variable_resids', 'partial_resids', 'ceres_resids', 'plot_added_variable', 'plot_partial_residuals', 'plot_ceres_residuals']

def add_lowess(ax, lines_idx: int = 0, frac: float = 0.2, **lowess_kwargs):
    """
    Add Lowess line to a plot.

    Parameters
    ----------
    ax : AxesSubplot
        The Axes to which to add the plot
    lines_idx : int
        This is the line on the existing plot to which you want to add
        a smoothed lowess line.
    frac : float
        The fraction of the points to use when doing the lowess fit.
    lowess_kwargs
        Additional keyword arguments are passes to lowess.

    Returns
    -------
    Figure
        The figure that holds the instance.
    """
def plot_fit(results, exog_idx, y_true: Incomplete | None = None, ax: Incomplete | None = None, vlines: bool = True, **kwargs):
    '''
    Plot fit against one regressor.

    This creates one graph with the scatterplot of observed values
    compared to fitted values.

    Parameters
    ----------
    results : Results
        A result instance with resid, model.endog and model.exog as
        attributes.
    exog_idx : {int, str}
        Name or index of regressor in exog matrix.
    y_true : array_like. optional
        If this is not None, then the array is added to the plot.
    ax : AxesSubplot, optional
        If given, this subplot is used to plot in instead of a new figure being
        created.
    vlines : bool, optional
        If this not True, then the uncertainty (pointwise prediction intervals) of the fit is not
        plotted.
    **kwargs
        The keyword arguments are passed to the plot command for the fitted
        values points.

    Returns
    -------
    Figure
        If `ax` is None, the created figure.  Otherwise the figure to which
        `ax` is connected.

    Examples
    --------
    Load the Statewide Crime data set and perform linear regression with
    `poverty` and `hs_grad` as variables and `murder` as the response

    >>> import statsmodels.api as sm
    >>> import matplotlib.pyplot as plt

    >>> data = sm.datasets.statecrime.load_pandas().data
    >>> murder = data[\'murder\']
    >>> X = data[[\'poverty\', \'hs_grad\']]

    >>> X["constant"] = 1
    >>> y = murder
    >>> model = sm.OLS(y, X)
    >>> results = model.fit()

    Create a plot just for the variable \'Poverty.\'
    Note that vertical bars representing uncertainty are plotted since vlines is true

    >>> fig, ax = plt.subplots()
    >>> fig = sm.graphics.plot_fit(results, 0, ax=ax)
    >>> ax.set_ylabel("Murder Rate")
    >>> ax.set_xlabel("Poverty Level")
    >>> ax.set_title("Linear Regression")

    >>> plt.show()

    .. plot:: plots/graphics_plot_fit_ex.py
    '''
def plot_regress_exog(results, exog_idx, fig: Incomplete | None = None):
    """Plot regression results against one regressor.

    This plots four graphs in a 2 by 2 figure: 'endog versus exog',
    'residuals versus exog', 'fitted versus exog' and
    'fitted plus residual versus exog'

    Parameters
    ----------
    results : result instance
        A result instance with resid, model.endog and model.exog as attributes.
    exog_idx : int or str
        Name or index of regressor in exog matrix.
    fig : Figure, optional
        If given, this figure is simply returned.  Otherwise a new figure is
        created.

    Returns
    -------
    Figure
        The value of `fig` if provided. Otherwise a new instance.

    Examples
    --------
    Load the Statewide Crime data set and build a model with regressors
    including the rate of high school graduation (hs_grad), population in urban
    areas (urban), households below poverty line (poverty), and single person
    households (single).  Outcome variable is the murder rate (murder).

    Build a 2 by 2 figure based on poverty showing fitted versus actual murder
    rate, residuals versus the poverty rate, partial regression plot of poverty,
    and CCPR plot for poverty rate.

    >>> import statsmodels.api as sm
    >>> import matplotlib.pyplot as plt
    >>> import statsmodels.formula.api as smf

    >>> fig = plt.figure(figsize=(8, 6))
    >>> crime_data = sm.datasets.statecrime.load_pandas()
    >>> results = smf.ols('murder ~ hs_grad + urban + poverty + single',
    ...                   data=crime_data.data).fit()
    >>> sm.graphics.plot_regress_exog(results, 'poverty', fig=fig)
    >>> plt.show()

    .. plot:: plots/graphics_regression_regress_exog.py
    """
def plot_partregress(endog, exog_i, exog_others, data: Incomplete | None = None, title_kwargs={}, obs_labels: bool = True, label_kwargs={}, ax: Incomplete | None = None, ret_coords: bool = False, eval_env: int = 1, **kwargs):
    """Plot partial regression for a single regressor.

    Parameters
    ----------
    endog : {ndarray, str}
       The endogenous or response variable. If string is given, you can use a
       arbitrary translations as with a formula.
    exog_i : {ndarray, str}
        The exogenous, explanatory variable. If string is given, you can use a
        arbitrary translations as with a formula.
    exog_others : {ndarray, list[str]}
        Any other exogenous, explanatory variables. If a list of strings is
        given, each item is a term in formula. You can use a arbitrary
        translations as with a formula. The effect of these variables will be
        removed by OLS regression.
    data : {DataFrame, dict}
        Some kind of data structure with names if the other variables are
        given as strings.
    title_kwargs : dict
        Keyword arguments to pass on for the title. The key to control the
        fonts is fontdict.
    obs_labels : {bool, array_like}
        Whether or not to annotate the plot points with their observation
        labels. If obs_labels is a boolean, the point labels will try to do
        the right thing. First it will try to use the index of data, then
        fall back to the index of exog_i. Alternatively, you may give an
        array-like object corresponding to the observation numbers.
    label_kwargs : dict
        Keyword arguments that control annotate for the observation labels.
    ax : AxesSubplot, optional
        If given, this subplot is used to plot in instead of a new figure being
        created.
    ret_coords : bool
        If True will return the coordinates of the points in the plot. You
        can use this to add your own annotations.
    eval_env : int
        Patsy eval environment if user functions and formulas are used in
        defining endog or exog.
    **kwargs
        The keyword arguments passed to plot for the points.

    Returns
    -------
    fig : Figure
        If `ax` is None, the created figure.  Otherwise the figure to which
        `ax` is connected.
    coords : list, optional
        If ret_coords is True, return a tuple of arrays (x_coords, y_coords).

    See Also
    --------
    plot_partregress_grid : Plot partial regression for a set of regressors.

    Notes
    -----
    The slope of the fitted line is the that of `exog_i` in the full
    multiple regression. The individual points can be used to assess the
    influence of points on the estimated coefficient.

    Examples
    --------
    Load the Statewide Crime data set and plot partial regression of the rate
    of high school graduation (hs_grad) on the murder rate(murder).

    The effects of the percent of the population living in urban areas (urban),
    below the poverty line (poverty) , and in a single person household (single)
    are removed by OLS regression.

    >>> import statsmodels.api as sm
    >>> import matplotlib.pyplot as plt

    >>> crime_data = sm.datasets.statecrime.load_pandas()
    >>> sm.graphics.plot_partregress(endog='murder', exog_i='hs_grad',
    ...                              exog_others=['urban', 'poverty', 'single'],
    ...                              data=crime_data.data, obs_labels=False)
    >>> plt.show()

    .. plot:: plots/graphics_regression_partregress.py

    More detailed examples can be found in the Regression Plots notebook
    on the examples page.
    """
def plot_partregress_grid(results, exog_idx: Incomplete | None = None, grid: Incomplete | None = None, fig: Incomplete | None = None):
    """
    Plot partial regression for a set of regressors.

    Parameters
    ----------
    results : Results instance
        A regression model results instance.
    exog_idx : {None, list[int], list[str]}
        The indices  or column names of the exog used in the plot, default is
        all.
    grid : {None, tuple[int]}
        If grid is given, then it is used for the arrangement of the subplots.
        The format of grid is  (nrows, ncols). If grid is None, then ncol is
        one, if there are only 2 subplots, and the number of columns is two
        otherwise.
    fig : Figure, optional
        If given, this figure is simply returned.  Otherwise a new figure is
        created.

    Returns
    -------
    Figure
        If `fig` is None, the created figure.  Otherwise `fig` itself.

    See Also
    --------
    plot_partregress : Plot partial regression for a single regressor.
    plot_ccpr : Plot CCPR against one regressor

    Notes
    -----
    A subplot is created for each explanatory variable given by exog_idx.
    The partial regression plot shows the relationship between the response
    and the given explanatory variable after removing the effect of all other
    explanatory variables in exog.

    References
    ----------
    See http://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/partregr.htm

    Examples
    --------
    Using the state crime dataset separately plot the effect of the each
    variable on the on the outcome, murder rate while accounting for the effect
    of all other variables in the model visualized with a grid of partial
    regression plots.

    >>> from statsmodels.graphics.regressionplots import plot_partregress_grid
    >>> import statsmodels.api as sm
    >>> import matplotlib.pyplot as plt
    >>> import statsmodels.formula.api as smf

    >>> fig = plt.figure(figsize=(8, 6))
    >>> crime_data = sm.datasets.statecrime.load_pandas()
    >>> results = smf.ols('murder ~ hs_grad + urban + poverty + single',
    ...                   data=crime_data.data).fit()
    >>> plot_partregress_grid(results, fig=fig)
    >>> plt.show()

    .. plot:: plots/graphics_regression_partregress_grid.py
    """
def plot_ccpr(results, exog_idx, ax: Incomplete | None = None):
    """
    Plot CCPR against one regressor.

    Generates a component and component-plus-residual (CCPR) plot.

    Parameters
    ----------
    results : result instance
        A regression results instance.
    exog_idx : {int, str}
        Exogenous, explanatory variable. If string is given, it should
        be the variable name that you want to use, and you can use arbitrary
        translations as with a formula.
    ax : AxesSubplot, optional
        If given, it is used to plot in instead of a new figure being
        created.

    Returns
    -------
    Figure
        If `ax` is None, the created figure.  Otherwise the figure to which
        `ax` is connected.

    See Also
    --------
    plot_ccpr_grid : Creates CCPR plot for multiple regressors in a plot grid.

    Notes
    -----
    The CCPR plot provides a way to judge the effect of one regressor on the
    response variable by taking into account the effects of the other
    independent variables. The partial residuals plot is defined as
    Residuals + B_i*X_i versus X_i. The component adds the B_i*X_i versus
    X_i to show where the fitted line would lie. Care should be taken if X_i
    is highly correlated with any of the other independent variables. If this
    is the case, the variance evident in the plot will be an underestimate of
    the true variance.

    References
    ----------
    http://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/ccpr.htm

    Examples
    --------
    Using the state crime dataset plot the effect of the rate of single
    households ('single') on the murder rate while accounting for high school
    graduation rate ('hs_grad'), percentage of people in an urban area, and rate
    of poverty ('poverty').

    >>> import statsmodels.api as sm
    >>> import matplotlib.pyplot as plt
    >>> import statsmodels.formula.api as smf

    >>> crime_data = sm.datasets.statecrime.load_pandas()
    >>> results = smf.ols('murder ~ hs_grad + urban + poverty + single',
    ...                   data=crime_data.data).fit()
    >>> sm.graphics.plot_ccpr(results, 'single')
    >>> plt.show()

    .. plot:: plots/graphics_regression_ccpr.py
    """
def plot_ccpr_grid(results, exog_idx: Incomplete | None = None, grid: Incomplete | None = None, fig: Incomplete | None = None):
    """
    Generate CCPR plots against a set of regressors, plot in a grid.

    Generates a grid of component and component-plus-residual (CCPR) plots.

    Parameters
    ----------
    results : result instance
        A results instance with exog and params.
    exog_idx : None or list of int
        The indices or column names of the exog used in the plot.
    grid : None or tuple of int (nrows, ncols)
        If grid is given, then it is used for the arrangement of the subplots.
        If grid is None, then ncol is one, if there are only 2 subplots, and
        the number of columns is two otherwise.
    fig : Figure, optional
        If given, this figure is simply returned.  Otherwise a new figure is
        created.

    Returns
    -------
    Figure
        If `ax` is None, the created figure.  Otherwise the figure to which
        `ax` is connected.

    See Also
    --------
    plot_ccpr : Creates CCPR plot for a single regressor.

    Notes
    -----
    Partial residual plots are formed as::

        Res + Betahat(i)*Xi versus Xi

    and CCPR adds::

        Betahat(i)*Xi versus Xi

    References
    ----------
    See http://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/ccpr.htm

    Examples
    --------
    Using the state crime dataset separately plot the effect of the each
    variable on the on the outcome, murder rate while accounting for the effect
    of all other variables in the model.

    >>> import statsmodels.api as sm
    >>> import matplotlib.pyplot as plt
    >>> import statsmodels.formula.api as smf

    >>> fig = plt.figure(figsize=(8, 8))
    >>> crime_data = sm.datasets.statecrime.load_pandas()
    >>> results = smf.ols('murder ~ hs_grad + urban + poverty + single',
    ...                   data=crime_data.data).fit()
    >>> sm.graphics.plot_ccpr_grid(results, fig=fig)
    >>> plt.show()

    .. plot:: plots/graphics_regression_ccpr_grid.py
    """
def abline_plot(intercept: Incomplete | None = None, slope: Incomplete | None = None, horiz: Incomplete | None = None, vert: Incomplete | None = None, model_results: Incomplete | None = None, ax: Incomplete | None = None, **kwargs):
    """
    Plot a line given an intercept and slope.

    Parameters
    ----------
    intercept : float
        The intercept of the line.
    slope : float
        The slope of the line.
    horiz : float or array_like
        Data for horizontal lines on the y-axis.
    vert : array_like
        Data for verterical lines on the x-axis.
    model_results : statsmodels results instance
        Any object that has a two-value `params` attribute. Assumed that it
        is (intercept, slope).
    ax : axes, optional
        Matplotlib axes instance.
    **kwargs
        Options passed to matplotlib.pyplot.plt.

    Returns
    -------
    Figure
        The figure given by `ax.figure` or a new instance.

    Examples
    --------
    >>> import numpy as np
    >>> import statsmodels.api as sm

    >>> np.random.seed(12345)
    >>> X = sm.add_constant(np.random.normal(0, 20, size=30))
    >>> y = np.dot(X, [25, 3.5]) + np.random.normal(0, 30, size=30)
    >>> mod = sm.OLS(y,X).fit()
    >>> fig = sm.graphics.abline_plot(model_results=mod)
    >>> ax = fig.axes[0]
    >>> ax.scatter(X[:,1], y)
    >>> ax.margins(.1)
    >>> import matplotlib.pyplot as plt
    >>> plt.show()

    .. plot:: plots/graphics_regression_abline.py
    """
def influence_plot(results, external: bool = True, alpha: float = 0.05, criterion: str = 'cooks', size: int = 48, plot_alpha: float = 0.75, ax: Incomplete | None = None, **kwargs): ...
def plot_leverage_resid2(results, alpha: float = 0.05, ax: Incomplete | None = None, **kwargs): ...
def plot_added_variable(results, focus_exog, resid_type: Incomplete | None = None, use_glm_weights: bool = True, fit_kwargs: Incomplete | None = None, ax: Incomplete | None = None): ...
def plot_partial_residuals(results, focus_exog, ax: Incomplete | None = None): ...
def plot_ceres_residuals(results, focus_exog, frac: float = 0.66, cond_means: Incomplete | None = None, ax: Incomplete | None = None): ...
def ceres_resids(results, focus_exog, frac: float = 0.66, cond_means: Incomplete | None = None):
    """
    Calculate the CERES residuals (Conditional Expectation Partial
    Residuals) for a fitted model.

    Parameters
    ----------
    results : model results instance
        The fitted model for which the CERES residuals are calculated.
    focus_exog : int
        The column of results.model.exog used as the 'focus variable'.
    frac : float, optional
        Lowess smoothing parameter for estimating the conditional
        means.  Not used if `cond_means` is provided.
    cond_means : array_like, optional
        If provided, the columns of this array are the conditional
        means E[exog | focus exog], where exog ranges over some
        or all of the columns of exog other than focus exog.  If
        this is an empty nx0 array, the conditional means are
        treated as being zero.  If None, the conditional means are
        estimated.

    Returns
    -------
    An array containing the CERES residuals.

    Notes
    -----
    If `cond_means` is not provided, it is obtained by smoothing each
    column of exog (except the focus column) against the focus column.

    Currently only supports GLM, GEE, and OLS models.
    """
def partial_resids(results, focus_exog):
    """
    Returns partial residuals for a fitted model with respect to a
    'focus predictor'.

    Parameters
    ----------
    results : results instance
        A fitted regression model.
    focus col : int
        The column index of model.exog with respect to which the
        partial residuals are calculated.

    Returns
    -------
    An array of partial residuals.

    References
    ----------
    RD Cook and R Croos-Dabrera (1998).  Partial residual plots in
    generalized linear models.  Journal of the American Statistical
    Association, 93:442.
    """
def added_variable_resids(results, focus_exog, resid_type: Incomplete | None = None, use_glm_weights: bool = True, fit_kwargs: Incomplete | None = None):
    """
    Residualize the endog variable and a 'focus' exog variable in a
    regression model with respect to the other exog variables.

    Parameters
    ----------
    results : regression results instance
        A fitted model including the focus exog and all other
        predictors of interest.
    focus_exog : {int, str}
        The column of results.model.exog or a variable name that is
        to be residualized against the other predictors.
    resid_type : str
        The type of residuals to use for the dependent variable.  If
        None, uses `resid_deviance` for GLM/GEE and `resid` otherwise.
    use_glm_weights : bool
        Only used if the model is a GLM or GEE.  If True, the
        residuals for the focus predictor are computed using WLS, with
        the weights obtained from the IRLS calculations for fitting
        the GLM.  If False, unweighted regression is used.
    fit_kwargs : dict, optional
        Keyword arguments to be passed to fit when refitting the
        model.

    Returns
    -------
    endog_resid : array_like
        The residuals for the original exog
    focus_exog_resid : array_like
        The residuals for the focus predictor

    Notes
    -----
    The 'focus variable' residuals are always obtained using linear
    regression.

    Currently only GLM, GEE, and OLS models are supported.
    """
