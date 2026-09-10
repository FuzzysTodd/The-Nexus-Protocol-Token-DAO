from statsmodels.compat.python import lmap as lmap

def data2dummy(x, returnall: bool = False):
    """convert array of categories to dummy variables
    by default drops dummy variable for last category
    uses ravel, 1d only"""
def data2proddummy(x):
    """creates product dummy variables from 2 columns of 2d array

    drops last dummy variable, but not from each category
    singular with simple dummy variable but not with constant

    quickly written, no safeguards

    """
def data2groupcont(x1, x2):
    """create dummy continuous variable

    Parameters
    ----------
    x1 : 1d array
        label or group array
    x2 : 1d array (float)
        continuous variable

    Notes
    -----
    useful for group specific slope coefficients in regression
    """

anova_str0: str
anova_str: str

def anovadict(res):
    """update regression results dictionary with ANOVA specific statistics

    not checked for completeness
    """
def form2design(ss, data):
    """convert string formula to data dictionary

    ss : str
     * I : add constant
     * varname : for simple varnames data is used as is
     * F:varname : create dummy variables for factor varname
     * P:varname1*varname2 : create product dummy variables for
       varnames
     * G:varname1*varname2 : create product between factor and
       continuous variable
    data : dict or structured array
       data set, access of variables by name as in dictionaries

    Returns
    -------
    vars : dictionary
        dictionary of variables with converted dummy variables
    names : list
        list of names, product (P:) and grouped continuous
        variables (G:) have name by joining individual names
        sorted according to input

    Examples
    --------
    >>> xx, n = form2design('I a F:b P:c*d G:c*f', testdata)
    >>> xx.keys()
    ['a', 'b', 'const', 'cf', 'cd']
    >>> n
    ['const', 'a', 'b', 'cd', 'cf']

    Notes
    -----

    with sorted dict, separate name list would not be necessary
    """
def dropname(ss, li):
    """drop names from a list of strings,
    names to drop are in space delimited list
    does not change original list
    """
