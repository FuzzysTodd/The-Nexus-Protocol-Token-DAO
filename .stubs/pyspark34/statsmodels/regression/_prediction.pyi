from _typeshed import Incomplete

class PredictionResults:
    """
    Results class for predictions.

    Parameters
    ----------
    predicted_mean : ndarray
        The array containing the prediction means.
    var_pred_mean : ndarray
        The array of the variance of the prediction means.
    var_resid : ndarray
        The array of residual variances.
    df : int
        The degree of freedom used if dist is 't'.
    dist : {'norm', 't', object}
        Either a string for the normal or t distribution or another object
        that exposes a `ppf` method.
    row_labels : list[str]
        Row labels used in summary frame.
    """
    predicted: Incomplete
    var_pred: Incomplete
    df: Incomplete
    var_resid: Incomplete
    row_labels: Incomplete
    dist: Incomplete
    dist_args: Incomplete
    def __init__(self, predicted_mean, var_pred_mean, var_resid, df: Incomplete | None = None, dist: Incomplete | None = None, row_labels: Incomplete | None = None) -> None: ...
    @property
    def se_obs(self): ...
    @property
    def se_mean(self): ...
    @property
    def predicted_mean(self): ...
    @property
    def var_pred_mean(self): ...
    @property
    def se(self): ...
    def conf_int(self, obs: bool = False, alpha: float = 0.05):
        """
        Returns the confidence interval of the value, `effect` of the
        constraint.

        This is currently only available for t and z tests.

        Parameters
        ----------
        alpha : float, optional
            The significance level for the confidence interval.
            ie., The default `alpha` = .05 returns a 95% confidence interval.

        Returns
        -------
        ci : ndarray, (k_constraints, 2)
            The array has the lower and the upper limit of the confidence
            interval in the columns.
        """
    table: Incomplete
    def summary_frame(self, alpha: float = 0.05): ...

def get_prediction(self, exog: Incomplete | None = None, transform: bool = True, weights: Incomplete | None = None, row_labels: Incomplete | None = None, pred_kwds: Incomplete | None = None):
    """
    Compute prediction results.

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
    weights : array_like, optional
        Weights interpreted as in WLS, used for the variance of the predicted
        residual.
    row_labels : list
        A list of row labels to use.  If not provided, read `exog` is
        available.
    **kwargs
        Some models can take additional keyword arguments, see the predict
        method of the model for the details.

    Returns
    -------
    linear_model.PredictionResults
        The prediction results instance contains prediction and prediction
        variance and can on demand calculate confidence intervals and summary
        tables for the prediction of the mean and of new observations.
    """
