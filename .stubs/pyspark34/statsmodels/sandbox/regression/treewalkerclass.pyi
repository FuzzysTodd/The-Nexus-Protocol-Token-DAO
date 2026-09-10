from _typeshed import Incomplete
from statsmodels.compat.python import lrange as lrange

def randintw(w, size: int = 1):
    """generate integer random variables given probabilties

    useful because it can be used as index into any array or sequence type

    Parameters
    ----------
    w : 1d array_like
        sequence of weights, probabilities. The weights are normalized to add
        to one.
    size : int or tuple of ints
        shape of output array

    Returns
    -------
    rvs : array of shape given by size
        random variables each distributed according to the same discrete
        distribution defined by (normalized) w.

    Examples
    --------
    >>> np.random.seed(0)
    >>> randintw([0.4, 0.4, 0.2], size=(2,6))
    array([[1, 1, 1, 1, 1, 1],
           [1, 2, 2, 0, 1, 1]])

    >>> np.bincount(randintw([0.6, 0.4, 0.0], size=3000))/3000.
    array([ 0.59566667,  0.40433333])

    """
def getbranches(tree):
    """
    walk tree to get list of branches

    Parameters
    ----------
    tree : list of tuples
        tree as defined for RU2NMNL

    Returns
    -------
    branch : list
        list of all branch names

    """
def getnodes(tree):
    """
    walk tree to get list of branches and list of leaves

    Parameters
    ----------
    tree : list of tuples
        tree as defined for RU2NMNL

    Returns
    -------
    branch : list
        list of all branch names
    leaves : list
        list of all leaves names

    """

testxb: int

class RU2NMNL:
    """Nested Multinomial Logit with Random Utility 2 parameterization


    Parameters
    ----------
    endog : ndarray
        not used in this part
    exog : dict_like
        dictionary access to data where keys correspond to branch and leaf
        names. The values are the data arrays for the exog in that node.
    tree : nested tuples and lists
        each branch, tree or subtree, is defined by a tuple
        (branch_name, [subtree1, subtree2, ..., subtreek])
        Bottom branches have as subtrees the list of leaf names.
    paramsind : dictionary
        dictionary that maps branch and leaf names to the names of parameters,
        the coefficients for exogs)

    Methods
    -------
    get_probs

    Attributes
    ----------
    branches
    leaves
    paramsnames
    parinddict

    Notes
    -----
    endog needs to be encoded so it is consistent with self.leaves, which
    defines the columns for the probability array. The ordering in leaves is
    determined by the ordering of the tree.
    In the dummy encoding of endog, the columns of endog need to have the
    same order as self.leaves. In the integer encoding, the integer for a
    choice has to correspond to the index in self.leaves.
    (This could be made more robust, by handling the endog encoding internally
    by leaf names, if endog is defined as categorical variable with
    associated category level names.)

    """
    endog: Incomplete
    datadict: Incomplete
    tree: Incomplete
    paramsind: Incomplete
    branchsum: str
    probs: Incomplete
    probstxt: Incomplete
    branchleaves: Incomplete
    branchvalues: Incomplete
    branchsums: Incomplete
    bprobs: Incomplete
    nbranches: Incomplete
    paramsnames: Incomplete
    nparams: Incomplete
    paramsidx: Incomplete
    parinddict: Incomplete
    recursionparams: Incomplete
    def __init__(self, endog, exog, tree, paramsind) -> None: ...
    def get_probs(self, params):
        """
        obtain the probability array given an array of parameters

        This is the function that can be called by loglike or other methods
        that need the probabilities as function of the params.

        Parameters
        ----------
        params : 1d array, (nparams,)
            coefficients and tau that parameterize the model. The required
            length can be obtained by nparams. (and will depend on the number
            of degenerate leaves - not yet)

        Returns
        -------
        probs : ndarray, (nobs, nchoices)
            probabilities for all choices for each observation. The order
            is available by attribute leaves. See note in docstring of class



        """
    def calc_prob(self, tree, parent: Incomplete | None = None):
        """walking a tree bottom-up based on dictionary
        """
