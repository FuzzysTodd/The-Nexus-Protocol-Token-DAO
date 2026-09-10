from _typeshed import Incomplete

class TryCLogit:
    """
    Conditional Logit, data handling test

    Parameters
    ----------

    endog : array (nobs,nchoices)
        dummy encoding of realized choices
    exog_bychoices : list of arrays
        explanatory variables, one array of exog for each choice. Variables
        with common coefficients have to be first in each array
    ncommon : int
        number of explanatory variables with common coefficients

    Notes
    -----

    Utility for choice j is given by

        $V_j = X_j * beta + Z * gamma_j$

    where X_j contains generic variables (terminology Hess) that have the same
    coefficient across choices, and Z are variables, like individual-specific
    variables that have different coefficients across variables.

    If there are choice specific constants, then they should be contained in Z.
    For identification, the constant of one choice should be dropped.


    """
    endog: Incomplete
    exog_bychoices: Incomplete
    ncommon: Incomplete
    nchoices: Incomplete
    beta_indices: Incomplete
    def __init__(self, endog, exog_bychoices, ncommon) -> None: ...
    def xbetas(self, params):
        """these are the V_i
        """
    def loglike(self, params): ...
    def fit(self, start_params: Incomplete | None = None): ...

class TryNCLogit:
    """
    Nested Conditional Logit (RUNMNL), data handling test

    unfinished, does not do anything yet

    """
    endog: Incomplete
    exog_bychoices: Incomplete
    ncommon: Incomplete
    nchoices: Incomplete
    beta_indices: Incomplete
    def __init__(self, endog, exog_bychoices, ncommon) -> None: ...
    def xbetas(self, params):
        """these are the V_i
        """
    def loglike_leafbranch(self, params, tau): ...
    def loglike_branch(self, params, tau) -> None: ...

testxb: int

class RU2NMNL:
    """Nested Multinomial Logit with Random Utility 2 parameterization

    """
    endog: Incomplete
    datadict: Incomplete
    tree: Incomplete
    paramsind: Incomplete
    branchsum: str
    probs: Incomplete
    def __init__(self, endog, exog, tree, paramsind) -> None: ...
    def calc_prob(self, tree, keys: Incomplete | None = None):
        """walking a tree bottom-up based on dictionary
        """

dta: Incomplete
endog: Incomplete
nobs: Incomplete
nchoices: Incomplete
datafloat: Incomplete
exog: Incomplete
varnames: Incomplete
modes: Incomplete
exog_choice_names: Incomplete
exog_choice: Incomplete
exog_individual: Incomplete
choice_index: Incomplete
hinca: Incomplete
dta2: Incomplete
xi: Incomplete
dta1: Incomplete
xivar: Incomplete
ncommon: int
betaind: Incomplete
zi: Incomplete
z: Incomplete
betaindices: Incomplete
beta: Incomplete
betai: Incomplete
xifloat: Incomplete
clogit: Incomplete
debug: int
res: Incomplete
tab2324: Incomplete
res2: Incomplete
res3: Incomplete
res3corr: Incomplete
tree0: Incomplete
datadict: Incomplete
paramsind: Incomplete
modru: Incomplete
