from _typeshed import Incomplete
from statsmodels.base._penalties import SCADSmoothed as SCADSmoothed

class ScreeningResults:
    """Results for Variable Screening

    Note: Indices except for exog_idx and in the iterated case also
    idx_nonzero_batches are based on the combined [exog_keep, exog] array.

    Attributes
    ----------
    results_final : instance
        Results instance returned by the final fit of the penalized model, i.e.
        after trimming exog with params below trimming threshold.
    results_pen : results instance
        Results instance of the penalized model before trimming. This includes
        variables from the last forward selection
    idx_nonzero
        index of exog columns in the final selection including exog_keep
    idx_exog
        index of exog columns in the final selection for exog candidates, i.e.
        without exog_keep
    idx_excl
        idx of excluded exog based on combined [exog_keep, exog] array. This is
        the complement of idx_nonzero
    converged : bool
        True if the iteration has converged and stopped before maxiter has been
        reached. False if maxiter has been reached.
    iterations : int
        number of iterations in the screening process. Each iteration consists
        of a forward selection step and a trimming step.
    history : dict of lists
        results collected for each iteration during the screening process
        'idx_nonzero' 'params_keep'].append(start_params)
            history['idx_added'].append(idx)

    The ScreeningResults returned by `screen_exog_iterator` has additional
    attributes:

    idx_nonzero_batches : ndarray 2-D
        Two-dimensional array with batch index in the first column and variable
        index withing batch in the second column. They can be used jointly as
        index for the data in the exog_iterator.
    exog_final_names : list[str]
        'var<bidx>_<idx>' where `bidx` is the batch index and `idx` is the
        index of the selected column withing batch `bidx`.
    history_batches : dict of lists
        This provides information about the selected variables within each
        batch during the first round screening
        'idx_nonzero' is based ond the array that includes exog_keep, while
        'idx_exog' is the index based on the exog of the batch.
    """
    screener: Incomplete
    def __init__(self, screener, **kwds) -> None: ...

class VariableScreening:
    """Ultra-high, conditional sure independence screening

    This is an adjusted version of Fan's sure independence screening.

    Parameters
    ----------
    model : instance of penalizing model
        examples: GLMPenalized, PoissonPenalized and LogitPenalized.
        The attributes of the model instance `pen_weight` and `penal` will be
        ignored.
    pen_weight : None or float
        penalization weight use in SCAD penalized MLE
    k_add : int
        number of exog to add during expansion or forward selection
        see Notes section for tie handling
    k_max_add : int
        maximum number of variables to include during variable addition, i.e.
        forward selection. default is 30
    threshold_trim : float
        threshold for trimming parameters to zero, default is 1e-4
    k_max_included : int
        maximum total number of variables to include in model.
    ranking_attr : str
        This determines the result attribute or model method that is used for
        the ranking of exog to include. The availability of attributes depends
        on the model.
        Default is 'resid_pearson', 'model.score_factor' can be used in GLM.
    ranking_project : bool
        If ranking_project is True, then the exog candidates for inclusion are
        first projected on the already included exog before the computation
        of the ranking measure. This brings the ranking measure closer to
        the statistic of a score test for variable addition.

    Notes
    -----
    Status: experimental, tested only on a limited set of models and
    with a limited set of model options.

    Tie handling: If there are ties at the decision threshold, then all those
    tied exog columns are treated in the same way. During forward selection
    all exog columns with the same boundary value are included. During
    elimination, the tied columns are not dropped. Consequently, if ties are
    present, then the number of included exog can be larger than specified
    by k_add, k_max_add and k_max_included.

    The screening algorithm works similar to step wise regression. Each
    iteration of the screening algorithm includes a forward selection step
    where variables are added to the model, and a backwards selection step
    where variables are removed. In contrast to step wise regression, we add
    a fixed number of variables at each forward selection step. The
    backwards selection step is based on SCAD penalized estimation and
    trimming of variables with estimated coefficients below a threshold.
    The tuning parameters can be used to adjust the number of variables to add
    and to include depending on the size of the dataset.

    There is currently no automatic tuning parameter selection. Candidate
    explanatory variables should be standardized or should be on a similar
    scale because penalization and trimming are based on the absolute values
    of the parameters.


    TODOs and current limitations:

    freq_weights are not supported in this. Candidate ranking uses
    moment condition with resid_pearson or others without freq_weights.
    pearson_resid: GLM resid_pearson does not include freq_weights.

    variable names: do we keep track of those? currently made-up names

    currently only supports numpy arrays, no exog type check or conversion

    currently only single columns are selected, no terms (multi column exog)
    """
    model: Incomplete
    model_class: Incomplete
    init_kwds: Incomplete
    endog: Incomplete
    exog_keep: Incomplete
    k_keep: Incomplete
    nobs: Incomplete
    penal: Incomplete
    pen_weight: Incomplete
    use_weights: Incomplete
    k_add: Incomplete
    k_max_add: Incomplete
    threshold_trim: Incomplete
    k_max_included: Incomplete
    ranking_attr: Incomplete
    ranking_project: Incomplete
    def __init__(self, model, pen_weight: Incomplete | None = None, use_weights: bool = True, k_add: int = 30, k_max_add: int = 30, threshold_trim: float = 0.0001, k_max_included: int = 20, ranking_attr: str = 'resid_pearson', ranking_project: bool = True) -> None: ...
    def ranking_measure(self, res_pen, exog, keep: Incomplete | None = None):
        """compute measure for ranking exog candidates for inclusion
        """
    def screen_exog(self, exog, endog: Incomplete | None = None, maxiter: int = 100, method: str = 'bfgs', disp: bool = False, fit_kwds: Incomplete | None = None):
        """screen and select variables (columns) in exog

        Parameters
        ----------
        exog : ndarray
            candidate explanatory variables that are screened for inclusion in
            the model
        endog : ndarray (optional)
            use a new endog in the screening model.
            This is not tested yet, and might not work correctly
        maxiter : int
            number of screening iterations
        method : str
            optimization method to use in fit, needs to be only of the gradient
            optimizers
        disp : bool
            display option for fit during optimization

        Returns
        -------
        res_screen : instance of ScreeningResults
            The attribute `results_final` contains is the results instance
            with the final model selection.
            `idx_nonzero` contains the index of the selected exog in the full
            exog, combined exog that are always kept plust exog_candidates.
            see ScreeningResults for a full description
        """
    def screen_exog_iterator(self, exog_iterator):
        """
        batched version of screen exog

        This screens variables in a two step process:

        In the first step screen_exog is used on each element of the
        exog_iterator, and the batch winners are collected.

        In the second step all batch winners are combined into a new array
        of exog candidates and `screen_exog` is used to select a final
        model.

        Parameters
        ----------
        exog_iterator : iterator over ndarrays

        Returns
        -------
        res_screen_final : instance of ScreeningResults
            This is the instance returned by the second round call to
            `screen_exog`. Additional attributes are added to provide
            more information about the batched selection process.
            The index of final nonzero variables is
            `idx_nonzero_batches` which is a 2-dimensional array with batch
            index in the first column and variable index within batch in the
            second column. They can be used jointly as index for the data
            in the exog_iterator.
            see ScreeningResults for a full description
        """
