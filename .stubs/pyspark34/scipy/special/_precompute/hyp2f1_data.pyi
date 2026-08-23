from _typeshed import Incomplete
from scipy.special import hyp2f1 as hyp2f1
from scipy.special.tests.test_hyp2f1 import mp_hyp2f1 as mp_hyp2f1

def get_region(z):
    """Assign numbers for regions where hyp2f1 must be handled differently."""
def get_result(a, b, c, z, group):
    """Get results for given parameter and value combination."""
def get_result_no_mp(a, b, c, z, group):
    """Get results for given parameter and value combination."""
def get_results(params, Z, n_jobs: int = 1, compute_mp: bool = True):
    """Batch compute results for multiple parameter and argument values.

    Parameters
    ----------
    params : iterable
        iterable of tuples of floats (a, b, c) specificying parameter values
        a, b, c for hyp2f1
    Z : iterable of complex
        Arguments at which to evaluate hyp2f1
    n_jobs : Optional[int]
        Number of jobs for parallel execution.

    Returns
    -------
    list
        List of tuples of results values. See return value in source code
        of `get_result`.
    """
def make_hyp2f1_test_cases(rows):
    """Generate string for a list of test cases for test_hyp2f1.py.

    Parameters
    ----------
    rows : list
        List of lists of the form [a, b, c, z, rtol] where a, b, c, z are
        parameters and the argument for hyp2f1 and rtol is an expected
        relative error for the associated test case.

    Returns
    -------
    str
        String for a list of test cases. The output string can be printed
        or saved to a file and then copied into an argument for
        `pytest.mark.parameterize` within `scipy.special.tests.test_hyp2f1.py`.
    """
def main(outpath, n_jobs: int = 1, box_size: float = 2.0, grid_size: int = 20, regions: Incomplete | None = None, parameter_groups: Incomplete | None = None, compute_mp: bool = True): ...
