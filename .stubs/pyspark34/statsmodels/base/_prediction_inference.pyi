from _typeshed import Incomplete

class PredictionResultsBase:
    """Based class for get_prediction results
    """
    predicted: Incomplete
    var_pred: Incomplete
    func: Incomplete
    deriv: Incomplete
    df: Incomplete
    row_labels: Incomplete
    dist: Incomplete
    dist_args: Incomplete
    def __init__(self, predicted, var_pred, func: Incomplete | None = None, deriv: Incomplete | None = None, df: Incomplete | None = None, dist: Incomplete | None = None, row_labels: Incomplete | None = None, **kwds) -> None: ...
    @property
    def se(self): ...
    @property
    def tvalues(self): ...
    def t_test(self, value: int = 0, alternative: str = 'two-sided'):
        """z- or t-test for hypothesis that mean is equal to value

        Parameters
        ----------
        value : array_like
            value under the null hypothesis
        alternative : str
            'two-sided', 'larger', 'smaller'

        Returns
        -------
        stat : ndarray
            test statistic
        pvalue : ndarray
            p-value of the hypothesis test, the distribution is given by
            the attribute of the instance, specified in `__init__`. Default
            if not specified is the normal distribution.

        """
    def conf_int(self, *, alpha: float = 0.05, **kwds):
        """Confidence interval for the predicted value.

        Parameters
        ----------
        alpha : float, optional
            The significance level for the confidence interval.
            ie., The default `alpha` = .05 returns a 95% confidence interval.

        kwds : extra keyword arguments
            Ignored in base class, only for compatibility, consistent signature
            with subclasses

        Returns
        -------
        ci : ndarray, (k_constraints, 2)
            The array has the lower and the upper limit of the confidence
            interval in the columns.
        """
    table: Incomplete
    def summary_frame(self, alpha: float = 0.05):
        """Summary frame

        Parameters
        ----------
        alpha : float, optional
            The significance level for the confidence interval.
            ie., The default `alpha` = .05 returns a 95% confidence interval.

        Returns
        -------
        pandas DataFrame with columns 'predicted', 'se', 'ci_lower', 'ci_upper'
        """

class PredictionResultsMonotonic(PredictionResultsBase):
    predicted: Incomplete
    var_pred: Incomplete
    linpred: Incomplete
    linpred_se: Incomplete
    func: Incomplete
    deriv: Incomplete
    df: Incomplete
    row_labels: Incomplete
    dist: Incomplete
    dist_args: Incomplete
    def __init__(self, predicted, var_pred, linpred: Incomplete | None = None, linpred_se: Incomplete | None = None, func: Incomplete | None = None, deriv: Incomplete | None = None, df: Incomplete | None = None, dist: Incomplete | None = None, row_labels: Incomplete | None = None) -> None: ...
    def conf_int(self, method: str = 'endpoint', alpha: float = 0.05, **kwds):
        '''Confidence interval for the predicted value.

        This is currently only available for t and z tests.

        Parameters
        ----------
        method : {"endpoint", "delta"}
            Method for confidence interval, "m
            If method is "endpoint", then the confidence interval of the
            linear predictor is transformed by the prediction function.
            If method is "delta", then the delta-method is used. The confidence
            interval in this case might reach outside the range of the
            prediction, for example probabilities larger than one or smaller
            than zero.
        alpha : float, optional
            The significance level for the confidence interval.
            ie., The default `alpha` = .05 returns a 95% confidence interval.
        kwds : extra keyword arguments
            currently ignored, only for compatibility, consistent signature

        Returns
        -------
        ci : ndarray, (k_constraints, 2)
            The array has the lower and the upper limit of the confidence
            interval in the columns.
        '''

class PredictionResultsDelta(PredictionResultsBase):
    """Prediction results based on delta method
    """
    def __init__(self, results_delta, **kwds) -> None: ...

class PredictionResultsMean(PredictionResultsBase):
    """Prediction results for GLM.

    This results class is used for backwards compatibility for
    `get_prediction` with GLM. The new PredictionResults classes dropped the
    `_mean` post fix in the attribute names.
    """
    predicted: Incomplete
    var_pred: Incomplete
    df: Incomplete
    var_resid: Incomplete
    row_labels: Incomplete
    linpred: Incomplete
    link: Incomplete
    dist: Incomplete
    dist_args: Incomplete
    def __init__(self, predicted_mean, var_pred_mean, var_resid: Incomplete | None = None, df: Incomplete | None = None, dist: Incomplete | None = None, row_labels: Incomplete | None = None, linpred: Incomplete | None = None, link: Incomplete | None = None) -> None: ...
    @property
    def predicted_mean(self): ...
    @property
    def var_pred_mean(self): ...
    @property
    def se_mean(self): ...
    def conf_int(self, method: str = 'endpoint', alpha: float = 0.05, **kwds):
        '''Confidence interval for the predicted value.

        This is currently only available for t and z tests.

        Parameters
        ----------
        method : {"endpoint", "delta"}
            Method for confidence interval, "m
            If method is "endpoint", then the confidence interval of the
            linear predictor is transformed by the prediction function.
            If method is "delta", then the delta-method is used. The confidence
            interval in this case might reach outside the range of the
            prediction, for example probabilities larger than one or smaller
            than zero.
        alpha : float, optional
            The significance level for the confidence interval.
            ie., The default `alpha` = .05 returns a 95% confidence interval.
        kwds : extra keyword arguments
            currently ignored, only for compatibility, consistent signature

        Returns
        -------
        ci : ndarray, (k_constraints, 2)
            The array has the lower and the upper limit of the confidence
            interval in the columns.
        '''
    table: Incomplete
    def summary_frame(self, alpha: float = 0.05):
        """Summary frame

        Parameters
        ----------
        alpha : float, optional
            The significance level for the confidence interval.
            ie., The default `alpha` = .05 returns a 95% confidence interval.

        Returns
        -------
        pandas DataFrame with columns
        'mean', 'mean_se', 'mean_ci_lower', 'mean_ci_upper'.
        """

def get_prediction_glm(self, exog: Incomplete | None = None, transform: bool = True, row_labels: Incomplete | None = None, linpred: Incomplete | None = None, link: Incomplete | None = None, pred_kwds: Incomplete | None = None):
    """
    Compute prediction results for GLM compatible models.

    Parameters
    ----------
    exog : array_like, optional
        The values for which you want to predict.
    transform : bool, optional
        If the model was fit via a formula, do you want to pass
        exog through the formula. Default is True. E.g., if you fit
        a model y ~ log(x1) + log(x2), and transform is True, then
        you can pass a data structure that contains x1 and x2 in
        their original form. Otherwise, you'd need to log the data
        first.
    row_labels : list of str or None
        If row_lables are provided, then they will replace the generated
        labels.
    linpred : linear prediction instance
        Instance of linear prediction results used for confidence intervals
        based on endpoint transformation.
    link : instance of link function
        If no link function is provided, then the `model.family.link` is used.
    pred_kwds : dict
        Some models can take additional keyword arguments, such as offset or
        additional exog in multi-part models. See the predict method of the
        model for the details.

    Returns
    -------
    prediction_results : generalized_linear_model.PredictionResults
        The prediction results instance contains prediction and prediction
        variance and can on demand calculate confidence intervals and summary
        tables for the prediction of the mean and of new observations.
    """
def get_prediction_linear(self, exog: Incomplete | None = None, transform: bool = True, row_labels: Incomplete | None = None, pred_kwds: Incomplete | None = None, index: Incomplete | None = None):
    """
    Compute prediction results for linear prediction.

    Parameters
    ----------
    exog : array_like, optional
        The values for which you want to predict.
    transform : bool, optional
        If the model was fit via a formula, do you want to pass
        exog through the formula. Default is True. E.g., if you fit
        a model y ~ log(x1) + log(x2), and transform is True, then
        you can pass a data structure that contains x1 and x2 in
        their original form. Otherwise, you'd need to log the data
        first.
    row_labels : list of str or None
        If row_lables are provided, then they will replace the generated
        labels.
    pred_kwargs :
        Some models can take additional keyword arguments, such as offset or
        additional exog in multi-part models.
        See the predict method of the model for the details.
    index : slice or array-index
        Is used to select rows and columns of cov_params, if the prediction
        function only depends on a subset of parameters.

    Returns
    -------
    prediction_results : PredictionResults
        The prediction results instance contains prediction and prediction
        variance and can on demand calculate confidence intervals and summary
        tables for the prediction.
    """
def get_prediction_monotonic(self, exog: Incomplete | None = None, transform: bool = True, row_labels: Incomplete | None = None, link: Incomplete | None = None, pred_kwds: Incomplete | None = None, index: Incomplete | None = None):
    """
    Compute prediction results when endpoint transformation is valid.

    Parameters
    ----------
    exog : array_like, optional
        The values for which you want to predict.
    transform : bool, optional
        If the model was fit via a formula, do you want to pass
        exog through the formula. Default is True. E.g., if you fit
        a model y ~ log(x1) + log(x2), and transform is True, then
        you can pass a data structure that contains x1 and x2 in
        their original form. Otherwise, you'd need to log the data
        first.
    row_labels : list of str or None
        If row_lables are provided, then they will replace the generated
        labels.
    link : instance of link function
        If no link function is provided, then the ``mmodel.family.link` is
        used.
    pred_kwargs :
        Some models can take additional keyword arguments, such as offset or
        additional exog in multi-part models.
        See the predict method of the model for the details.
    index : slice or array-index
        Is used to select rows and columns of cov_params, if the prediction
        function only depends on a subset of parameters.

    Returns
    -------
    prediction_results : PredictionResults
        The prediction results instance contains prediction and prediction
        variance and can on demand calculate confidence intervals and summary
        tables for the prediction.
    """
def get_prediction_delta(self, exog: Incomplete | None = None, which: str = 'mean', average: bool = False, agg_weights: Incomplete | None = None, transform: bool = True, row_labels: Incomplete | None = None, pred_kwds: Incomplete | None = None):
    """
    compute prediction results

    Parameters
    ----------
    exog : array_like, optional
        The values for which you want to predict.
    which : str
        The statistic that is prediction. Which statistics are available
        depends on the model.predict method.
    average : bool
        If average is True, then the mean prediction is computed, that is,
        predictions are computed for individual exog and then them mean over
        observation is used.
        If average is False, then the results are the predictions for all
        observations, i.e. same length as ``exog``.
    agg_weights : ndarray, optional
        Aggregation weights, only used if average is True.
        The weights are not normalized.
    transform : bool, optional
        If the model was fit via a formula, do you want to pass
        exog through the formula. Default is True. E.g., if you fit
        a model y ~ log(x1) + log(x2), and transform is True, then
        you can pass a data structure that contains x1 and x2 in
        their original form. Otherwise, you'd need to log the data
        first.
    row_labels : list of str or None
        If row_lables are provided, then they will replace the generated
        labels.
    pred_kwargs :
        Some models can take additional keyword arguments, such as offset or
        additional exog in multi-part models.
        See the predict method of the model for the details.

    Returns
    -------
    prediction_results : generalized_linear_model.PredictionResults
        The prediction results instance contains prediction and prediction
        variance and can on demand calculate confidence intervals and summary
        tables for the prediction of the mean and of new observations.
    """
def get_prediction(self, exog: Incomplete | None = None, transform: bool = True, which: str = 'mean', row_labels: Incomplete | None = None, average: bool = False, agg_weights: Incomplete | None = None, pred_kwds: Incomplete | None = None):
    '''
    Compute prediction results when endpoint transformation is valid.

    Parameters
    ----------
    exog : array_like, optional
        The values for which you want to predict.
    transform : bool, optional
        If the model was fit via a formula, do you want to pass
        exog through the formula. Default is True. E.g., if you fit
        a model y ~ log(x1) + log(x2), and transform is True, then
        you can pass a data structure that contains x1 and x2 in
        their original form. Otherwise, you\'d need to log the data
        first.
    which : str
        Which statistic is to be predicted. Default is "mean".
        The available statistics and options depend on the model.
        see the model.predict docstring
    linear : bool
        Linear has been replaced by the `which` keyword and will be
        deprecated.
        If linear is True, then `which` is ignored and the linear
        prediction is returned.
    row_labels : list of str or None
        If row_lables are provided, then they will replace the generated
        labels.
    average : bool
        If average is True, then the mean prediction is computed, that is,
        predictions are computed for individual exog and then the average
        over observation is used.
        If average is False, then the results are the predictions for all
        observations, i.e. same length as ``exog``.
    agg_weights : ndarray, optional
        Aggregation weights, only used if average is True.
        The weights are not normalized.
    **kwargs :
        Some models can take additional keyword arguments, such as offset,
        exposure or additional exog in multi-part models like zero inflated
        models.
        See the predict method of the model for the details.

    Returns
    -------
    prediction_results : PredictionResults
        The prediction results instance contains prediction and prediction
        variance and can on demand calculate confidence intervals and
        summary dataframe for the prediction.

    Notes
    -----
    Status: new in 0.14, experimental
    '''
def params_transform_univariate(params, cov_params, link: Incomplete | None = None, transform: Incomplete | None = None, row_labels: Incomplete | None = None):
    """
    results for univariate, nonlinear, monotonicaly transformed parameters

    This provides transformed values, standard errors and confidence interval
    for transformations of parameters, for example in calculating rates with
    `exp(params)` in the case of Poisson or other models with exponential
    mean function.
    """
