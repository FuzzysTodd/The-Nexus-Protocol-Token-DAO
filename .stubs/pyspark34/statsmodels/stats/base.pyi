from _typeshed import Incomplete
from statsmodels.compat.python import lzip as lzip
from statsmodels.tools.testing import Holder as Holder

class HolderTuple(Holder):
    """Holder class with indexing

    """
    tuple: Incomplete
    def __init__(self, tuple_: Incomplete | None = None, **kwds) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
    def __array__(self, dtype: Incomplete | None = None): ...

class AllPairsResults:
    """Results class for pairwise comparisons, based on p-values

    Parameters
    ----------
    pvals_raw : array_like, 1-D
        p-values from a pairwise comparison test
    all_pairs : list of tuples
        list of indices, one pair for each comparison
    multitest_method : str
        method that is used by default for p-value correction. This is used
        as default by the methods like if the multiple-testing method is not
        specified as argument.
    levels : {list[str], None}
        optional names of the levels or groups
    n_levels : None or int
        If None, then the number of levels or groups is inferred from the
        other arguments. It can be explicitly specified, if the inferred
        number is incorrect.

    Notes
    -----
    This class can also be used for other pairwise comparisons, for example
    comparing several treatments to a control (as in Dunnet's test).

    """
    pvals_raw: Incomplete
    all_pairs: Incomplete
    n_levels: Incomplete
    multitest_method: Incomplete
    levels: Incomplete
    all_pairs_names: Incomplete
    def __init__(self, pvals_raw, all_pairs, multitest_method: str = 'hs', levels: Incomplete | None = None, n_levels: Incomplete | None = None) -> None: ...
    def pval_corrected(self, method: Incomplete | None = None):
        """p-values corrected for multiple testing problem

        This uses the default p-value correction of the instance stored in
        ``self.multitest_method`` if method is None.

        """
    def pval_table(self):
        """create a (n_levels, n_levels) array with corrected p_values

        this needs to improve, similar to R pairwise output
        """
    def summary(self):
        """returns text summarizing the results

        uses the default pvalue correction of the instance stored in
        ``self.multitest_method``
        """
