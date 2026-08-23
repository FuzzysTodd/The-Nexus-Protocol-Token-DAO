from _typeshed import Incomplete

def contrast_allpairs(nm):
    """contrast or restriction matrix for all pairs of nm variables

    Parameters
    ----------
    nm : int

    Returns
    -------
    contr : ndarray, 2d, (nm*(nm-1)/2, nm)
       contrast matrix for all pairwise comparisons

    """
def contrast_all_one(nm):
    """contrast or restriction matrix for all against first comparison

    Parameters
    ----------
    nm : int

    Returns
    -------
    contr : ndarray, 2d, (nm-1, nm)
       contrast matrix for all against first comparisons

    """
def contrast_diff_mean(nm):
    """contrast or restriction matrix for all against mean comparison

    Parameters
    ----------
    nm : int

    Returns
    -------
    contr : ndarray, 2d, (nm-1, nm)
       contrast matrix for all against mean comparisons

    """
def signstr(x, noplus: bool = False): ...
def contrast_labels(contrasts, names, reverse: bool = False): ...
def contrast_product(names1, names2, intgroup1: Incomplete | None = None, intgroup2: Incomplete | None = None, pairs: bool = False):
    """build contrast matrices for products of two categorical variables

    this is an experimental script and should be converted to a class

    Parameters
    ----------
    names1, names2 : lists of strings
        contains the list of level labels for each categorical variable
    intgroup1, intgroup2 : ndarrays     TODO: this part not tested, finished yet
        categorical variable


    Notes
    -----
    This creates a full rank matrix. It does not do all pairwise comparisons,
    parameterization is using contrast_all_one to get differences with first
    level.

    ? does contrast_all_pairs work as a plugin to get all pairs ?

    """
def dummy_1d(x, varname: Incomplete | None = None):
    """dummy variable for id integer groups

    Parameters
    ----------
    x : ndarray, 1d
        categorical variable, requires integers if varname is None
    varname : str
        name of the variable used in labels for category levels

    Returns
    -------
    dummy : ndarray, 2d
        array of dummy variables, one column for each level of the
        category (full set)
    labels : list[str]
        labels for the columns, i.e. levels of each category


    Notes
    -----
    use tools.categorical instead for more more options

    See Also
    --------
    statsmodels.tools.categorical

    Examples
    --------
    >>> x = np.array(['F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M'],
          dtype='|S1')
    >>> dummy_1d(x, varname='gender')
    (array([[1, 0],
           [1, 0],
           [0, 1],
           [0, 1],
           [1, 0],
           [1, 0],
           [0, 1],
           [0, 1],
           [1, 0],
           [1, 0],
           [0, 1],
           [0, 1]]), ['gender_F', 'gender_M'])

    """
def dummy_product(d1, d2, method: str = 'full'):
    """dummy variable from product of two dummy variables

    Parameters
    ----------
    d1, d2 : ndarray
        two dummy variables, assumes full set for methods 'drop-last'
        and 'drop-first'
    method : {'full', 'drop-last', 'drop-first'}
        'full' returns the full product, encoding of intersection of
        categories.
        The drop methods provide a difference dummy encoding:
        (constant, main effects, interaction effects). The first or last columns
        of the dummy variable (i.e. levels) are dropped to get full rank
        dummy matrix.

    Returns
    -------
    dummy : ndarray
        dummy variable for product, see method

    """
def dummy_limits(d):
    """start and endpoints of groups in a sorted dummy variable array

    helper function for nested categories

    Examples
    --------
    >>> d1 = np.array([[1, 0, 0],
                       [1, 0, 0],
                       [1, 0, 0],
                       [1, 0, 0],
                       [0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0],
                       [0, 0, 1],
                       [0, 0, 1],
                       [0, 0, 1],
                       [0, 0, 1]])
    >>> dummy_limits(d1)
    (array([0, 4, 8]), array([ 4,  8, 12]))

    get group slices from an array

    >>> [np.arange(d1.shape[0])[b:e] for b,e in zip(*dummy_limits(d1))]
    [array([0, 1, 2, 3]), array([4, 5, 6, 7]), array([ 8,  9, 10, 11])]
    >>> [np.arange(d1.shape[0])[b:e] for b,e in zip(*dummy_limits(d1))]
    [array([0, 1, 2, 3]), array([4, 5, 6, 7]), array([ 8,  9, 10, 11])]
    """
def dummy_nested(d1, d2, method: str = 'full'):
    """unfinished and incomplete mainly copy past dummy_product
    dummy variable from product of two dummy variables

    Parameters
    ----------
    d1, d2 : ndarray
        two dummy variables, d2 is assumed to be nested in d1
        Assumes full set for methods 'drop-last' and 'drop-first'.
    method : {'full', 'drop-last', 'drop-first'}
        'full' returns the full product, which in this case is d2.
        The drop methods provide an effects encoding:
        (constant, main effects, subgroup effects). The first or last columns
        of the dummy variable (i.e. levels) are dropped to get full rank
        encoding.

    Returns
    -------
    dummy : ndarray
        dummy variable for product, see method

    """

class DummyTransform:
    """Conversion between full rank dummy encodings


    y = X b + u
    b = C a
    a = C^{-1} b

    y = X C a + u

    define Z = X C, then

    y = Z a + u

    contrasts:

    R_b b = r

    R_a a = R_b C a = r

    where R_a = R_b C

    Here C is the transform matrix, with dot_left and dot_right as the main
    methods, and the same for the inverse transform matrix, C^{-1}

    Note:
     - The class was mainly written to keep left and right straight.
     - No checking is done.
     - not sure yet if method names make sense


    """
    transf_matrix: Incomplete
    invtransf_matrix: Incomplete
    def __init__(self, d1, d2) -> None:
        """C such that d1 C = d2, with d1 = X, d2 = Z

        should be (x, z) in arguments ?
        """
    def dot_left(self, a):
        """ b = C a
        """
    def dot_right(self, x):
        """ z = x C
        """
    def inv_dot_left(self, b):
        """ a = C^{-1} b
        """
    def inv_dot_right(self, z):
        """ x = z C^{-1}
        """

def groupmean_d(x, d):
    """groupmeans using dummy variables

    Parameters
    ----------
    x : array_like, ndim
        data array, tested for 1,2 and 3 dimensions
    d : ndarray, 1d
        dummy variable, needs to have the same length
        as x in axis 0.

    Returns
    -------
    groupmeans : ndarray, ndim-1
        means for each group along axis 0, the levels
        of the groups are the last axis

    Notes
    -----
    This will be memory intensive if there are many levels
    in the categorical variable, i.e. many columns in the
    dummy variable. In this case it is recommended to use
    a more efficient version.

    """

class TwoWay:
    """a wrapper class for two way anova type of analysis with OLS


    currently mainly to bring things together

    Notes
    -----
    unclear: adding multiple test might assume block design or orthogonality

    This estimates the full dummy version with OLS.
    The drop first dummy representation can be recovered through the
    transform method.

    TODO: add more methods, tests, pairwise, multiple, marginal effects
    try out what can be added for userfriendly access.

    missing: ANOVA table

    """
    nobs: Incomplete
    nlevel1: Incomplete
    nlevel2: Incomplete
    transform: Incomplete
    nvars: Incomplete
    exog: Incomplete
    resols: Incomplete
    params: Incomplete
    params_dropf: Incomplete
    start_interaction: Incomplete
    n_interaction: Incomplete
    def __init__(self, endog, factor1, factor2, varnames: Incomplete | None = None) -> None: ...
    R_nointer_transf: Incomplete
    def r_nointer(self):
        """contrast/restriction matrix for no interaction
        """
    def ttest_interaction(self):
        """ttests for no-interaction terms are zero
        """
    def ftest_interaction(self):
        """ttests for no-interaction terms are zero
        """
    def ttest_conditional_effect(self, factorind): ...
    def summary_coeff(self): ...

class TestContrastTools:
    v1name: Incomplete
    v2name: Incomplete
    d1: Incomplete
    def __init__(self) -> None: ...
    def test_dummy_1d(self) -> None: ...
    def test_contrast_product(self) -> None: ...
    def test_dummy_limits(self) -> None: ...
