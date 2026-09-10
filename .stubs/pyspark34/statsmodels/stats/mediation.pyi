from _typeshed import Incomplete
from statsmodels.graphics.utils import maybe_name_or_idx as maybe_name_or_idx

class Mediation:
    '''
    Conduct a mediation analysis.

    Parameters
    ----------
    outcome_model : statsmodels model
        Regression model for the outcome.  Predictor variables include
        the treatment/exposure, the mediator, and any other variables
        of interest.
    mediator_model : statsmodels model
        Regression model for the mediator variable.  Predictor
        variables include the treatment/exposure and any other
        variables of interest.
    exposure : str or (int, int) tuple
        The name or column position of the treatment/exposure
        variable.  If positions are given, the first integer is the
        column position of the exposure variable in the outcome model
        and the second integer is the position of the exposure variable
        in the mediator model.  If a string is given, it must be the name
        of the exposure variable in both regression models.
    mediator : {str, int}
        The name or column position of the mediator variable in the
        outcome regression model.  If None, infer the name from the
        mediator model formula (if present).
    moderators : dict
        Map from variable names or index positions to values of
        moderator variables that are held fixed when calculating
        mediation effects.  If the keys are index position they must
        be tuples `(i, j)` where `i` is the index in the outcome model
        and `j` is the index in the mediator model.  Otherwise the
        keys must be variable names.
    outcome_fit_kwargs : dict-like
        Keyword arguments to use when fitting the outcome model.
    mediator_fit_kwargs : dict-like
        Keyword arguments to use when fitting the mediator model.
    outcome_predict_kwargs : dict-like
        Keyword arguments to use when calling predict on the outcome
        model.

    Returns a ``MediationResults`` object.

    Notes
    -----
    The mediator model class must implement ``get_distribution``.

    Examples
    --------
    A basic mediation analysis using formulas:

    >>> import statsmodels.api as sm
    >>> import statsmodels.genmod.families.links as links
    >>> probit = links.probit
    >>> outcome_model = sm.GLM.from_formula("cong_mesg ~ emo + treat + age + educ + gender + income",
    ...                                     data, family=sm.families.Binomial(link=Probit()))
    >>> mediator_model = sm.OLS.from_formula("emo ~ treat + age + educ + gender + income", data)
    >>> med = Mediation(outcome_model, mediator_model, "treat", "emo").fit()
    >>> med.summary()

    A basic mediation analysis without formulas.  This may be slightly
    faster than the approach using formulas.  If there are any
    interactions involving the treatment or mediator variables this
    approach will not work, you must use formulas.

    >>> import patsy
    >>> outcome = np.asarray(data["cong_mesg"])
    >>> outcome_exog = patsy.dmatrix("emo + treat + age + educ + gender + income", data,
    ...                              return_type=\'dataframe\')
    >>> probit = sm.families.links.probit
    >>> outcome_model = sm.GLM(outcome, outcome_exog, family=sm.families.Binomial(link=Probit()))
    >>> mediator = np.asarray(data["emo"])
    >>> mediator_exog = patsy.dmatrix("treat + age + educ + gender + income", data,
    ...                               return_type=\'dataframe\')
    >>> mediator_model = sm.OLS(mediator, mediator_exog)
    >>> tx_pos = [outcome_exog.columns.tolist().index("treat"),
    ...           mediator_exog.columns.tolist().index("treat")]
    >>> med_pos = outcome_exog.columns.tolist().index("emo")
    >>> med = Mediation(outcome_model, mediator_model, tx_pos, med_pos).fit()
    >>> med.summary()

    A moderated mediation analysis.  The mediation effect is computed
    for people of age 20.

    >>> fml = "cong_mesg ~ emo + treat*age + emo*age + educ + gender + income",
    >>> outcome_model = sm.GLM.from_formula(fml, data,
    ...                                      family=sm.families.Binomial())
    >>> mediator_model = sm.OLS.from_formula("emo ~ treat*age + educ + gender + income", data)
    >>> moderators = {"age" : 20}
    >>> med = Mediation(outcome_model, mediator_model, "treat", "emo",
    ...                 moderators=moderators).fit()

    References
    ----------
    Imai, Keele, Tingley (2010).  A general approach to causal mediation
    analysis. Psychological Methods 15:4, 309-334.
    http://imai.princeton.edu/research/files/BaronKenny.pdf

    Tingley, Yamamoto, Hirose, Keele, Imai (2014).  mediation : R
    package for causal mediation analysis.  Journal of Statistical
    Software 59:5.  http://www.jstatsoft.org/v59/i05/paper
    '''
    outcome_model: Incomplete
    mediator_model: Incomplete
    exposure: Incomplete
    moderators: Incomplete
    mediator: Incomplete
    def __init__(self, outcome_model, mediator_model, exposure, mediator: Incomplete | None = None, moderators: Incomplete | None = None, outcome_fit_kwargs: Incomplete | None = None, mediator_fit_kwargs: Incomplete | None = None, outcome_predict_kwargs: Incomplete | None = None) -> None: ...
    indirect_effects: Incomplete
    direct_effects: Incomplete
    def fit(self, method: str = 'parametric', n_rep: int = 1000):
        """
        Fit a regression model to assess mediation.

        Parameters
        ----------
        method : str
            Either 'parametric' or 'bootstrap'.
        n_rep : int
            The number of simulation replications.

        Returns a MediationResults object.
        """

class MediationResults:
    """
    A class for holding the results of a mediation analysis.

    The following terms are used in the summary output:

    ACME : average causal mediated effect
    ADE : average direct effect
    """
    indirect_effects: Incomplete
    direct_effects: Incomplete
    ACME_ctrl: Incomplete
    ACME_tx: Incomplete
    ADE_ctrl: Incomplete
    ADE_tx: Incomplete
    total_effect: Incomplete
    prop_med_ctrl: Incomplete
    prop_med_tx: Incomplete
    prop_med_avg: Incomplete
    ACME_avg: Incomplete
    ADE_avg: Incomplete
    def __init__(self, indirect_effects, direct_effects) -> None: ...
    def summary(self, alpha: float = 0.05):
        """
        Provide a summary of a mediation analysis.
        """
