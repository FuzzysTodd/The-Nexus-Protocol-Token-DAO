from _typeshed import Incomplete
from statsmodels.compat.python import lzip as lzip
from statsmodels.iolib import SimpleTable as SimpleTable

mat: Incomplete

class VARSummary:
    default_fmt: Incomplete
    part1_fmt: Incomplete
    part2_fmt: Incomplete
    model: Incomplete
    summary: Incomplete
    def __init__(self, estimator) -> None: ...
    def make(self, endog_names: Incomplete | None = None, exog_names: Incomplete | None = None):
        """
        Summary of VAR model
        """

def normality_summary(results): ...
def hypothesis_test_table(results, title, null_hyp): ...
def pprint_matrix(values, rlabels, clabels, col_space: Incomplete | None = None): ...
