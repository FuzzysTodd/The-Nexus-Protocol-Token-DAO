from _typeshed import Incomplete
from statsmodels.api import OLS as OLS, stats as stats

def multiOLS(model, dataframe, column_list: Incomplete | None = None, method: str = 'fdr_bh', alpha: float = 0.05, subset: Incomplete | None = None, model_type=..., **kwargs):
    """apply a linear model to several endogenous variables on a dataframe

    Take a linear model definition via formula and a dataframe that will be
    the environment of the model, and apply the linear model to a subset
    (or all) of the columns of the dataframe. It will return a dataframe
    with part of the information from the linear model summary.

    Parameters
    ----------
    model : str
        formula description of the model
    dataframe : pandas.dataframe
        dataframe where the model will be evaluated
    column_list : list[str], optional
        Names of the columns to analyze with the model.
        If None (Default) it will perform the function on all the
        eligible columns (numerical type and not in the model definition)
    model_type : model class, optional
        The type of model to be used. The default is the linear model.
        Can be any linear model (OLS, WLS, GLS, etc..)
    method : str, optional
        the method used to perform the pvalue correction for multiple testing.
        default is the Benjamini/Hochberg, other available methods are:

            `bonferroni` : one-step correction
            `sidak` : on-step correction
            `holm-sidak` :
            `holm` :
            `simes-hochberg` :
            `hommel` :
            `fdr_bh` : Benjamini/Hochberg
            `fdr_by` : Benjamini/Yekutieli

    alpha : float, optional
        the significance level used for the pvalue correction (default 0.05)
    subset : bool array
        the selected rows to be used in the regression

    all the other parameters will be directed to the model creation.

    Returns
    -------
    summary : pandas.DataFrame
        a dataframe containing an extract from the summary of the model
        obtained for each columns. It will give the model complexive f test
        result and p-value, and the regression value and standard deviarion
        for each of the regressors. The DataFrame has a hierachical column
        structure, divided as:

            - params: contains the parameters resulting from the models. Has
            an additional column named _f_test containing the result of the
            F test.
            - pval: the pvalue results of the models. Has the _f_test column
            for the significativity of the whole test.
            - adj_pval: the corrected pvalues via the multitest function.
            - std: uncertainties of the model parameters
            - statistics: contains the r squared statistics and the adjusted
            r squared.

    Notes
    -----
    The main application of this function is on system biology to perform
    a linear model testing of a lot of different parameters, like the
    different genetic expression of several genes.

    See Also
    --------
    statsmodels.stats.multitest
        contains several functions to perform the multiple p-value correction

    Examples
    --------
    Using the longley data as dataframe example

    >>> import statsmodels.api as sm
    >>> data = sm.datasets.longley.load_pandas()
    >>> df = data.exog
    >>> df['TOTEMP'] = data.endog

    This will perform the specified linear model on all the
    other columns of the dataframe
    >>> multiOLS('GNP + 1', df)

    This select only a certain subset of the columns
    >>> multiOLS('GNP + 0', df, ['GNPDEFL', 'TOTEMP', 'POP'])

    It is possible to specify a trasformation also on the target column,
    conforming to the patsy formula specification
    >>> multiOLS('GNP + 0', df, ['I(GNPDEFL**2)', 'center(TOTEMP)'])

    It is possible to specify the subset of the dataframe
    on which perform the analysis
    >> multiOLS('GNP + 1', df, subset=df.GNPDEFL > 90)

    Even a single column name can be given without enclosing it in a list
    >>> multiOLS('GNP + 0', df, 'GNPDEFL')
    """
def multigroup(pvals, groups, exact: bool = True, keep_all: bool = True, alpha: float = 0.05):
    '''Test if the given groups are different from the total partition.

    Given a boolean array test if each group has a proportion of positives
    different than the complexive proportion.
    The test can be done as an exact Fisher test or approximated as a
    Chi squared test for more speed.

    Parameters
    ----------
    pvals : pandas series of boolean
        the significativity of the variables under analysis
    groups : dict of list
        the name of each category of variables under exam.
        each one is a list of the variables included
    exact : bool, optional
        If True (default) use the fisher exact test, otherwise
        use the chi squared test for contingencies tables.
        For high number of elements in the array the fisher test can
        be significantly slower than the chi squared.
    keep_all : bool, optional
        if False it will drop those groups where the fraction
        of positive is below the expected result. If True (default)
         it will keep all the significant results.
    alpha : float, optional
        the significativity level for the pvalue correction
        on the whole set of groups (not inside the groups themselves).

    Returns
    -------
    result_df: pandas dataframe
        for each group returns:

            pvals - the fisher p value of the test
            adj_pvals - the adjusted pvals
            increase - the log of the odd ratio between the
                internal significant ratio versus the external one
            _in_sign - significative elements inside the group
            _in_non - non significative elements inside the group
            _out_sign - significative elements outside the group
            _out_non - non significative elements outside the group

    Notes
    -----
    This test allow to see if a category of variables is generally better
    suited to be described for the model. For example to see if a predictor
    gives more information on demographic or economical parameters,
    by creating two groups containing the endogenous variables of each
    category.

    This function is conceived for medical dataset with a lot of variables
    that can be easily grouped into functional groups. This is because
    The significativity of a group require a rather large number of
    composing elements.

    Examples
    --------
    A toy example on a real dataset, the Guerry dataset from R
    >>> url = "https://raw.githubusercontent.com/vincentarelbundock/"
    >>> url = url + "Rdatasets/csv/HistData/Guerry.csv"
    >>> df = pd.read_csv(url, index_col=\'dept\')

    evaluate the relationship between the various paramenters whith the Wealth
    >>> pvals = multiOLS(\'Wealth\', df)[\'adj_pvals\', \'_f_test\']

    define the groups
    >>> groups = {}
    >>> groups[\'crime\'] = [\'Crime_prop\', \'Infanticide\',
    ...     \'Crime_parents\', \'Desertion\', \'Crime_pers\']
    >>> groups[\'religion\'] = [\'Donation_clergy\', \'Clergy\', \'Donations\']
    >>> groups[\'wealth\'] = [\'Commerce\', \'Lottery\', \'Instruction\', \'Literacy\']

    do the analysis of the significativity
    >>> multigroup(pvals < 0.05, groups)
    '''
