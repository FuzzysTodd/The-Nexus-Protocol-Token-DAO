import numpy as np
from . import common_args as common_args
from ..util import ResultDict as ResultDict, read_param_file as read_param_file
from typing import Dict

def analyze(problem: Dict, X: np.ndarray, Y: np.ndarray, num_resamples: int = 100, conf_level: float = 0.95, print_to_console: bool = False, seed: int = None, y_resamples: int = None, method: str = 'all') -> Dict:
    '''Perform Delta Moment-Independent Analysis on model outputs.

    Returns a dictionary with keys \'delta\', \'delta_conf\', \'S1\', and \'S1_conf\'
    (first-order sobol indices), where each entry is a list of size D
    (the number of parameters) containing the indices in the same order as the
    parameter file.


    Notes
    -----
    Compatible with:
        all samplers


    Examples
    --------
        >>> X = latin.sample(problem, 1000)
        >>> Y = Ishigami.evaluate(X)
        >>> Si = delta.analyze(problem, X, Y, print_to_console=True)


    Parameters
    ----------
    problem : dict
        The problem definition
    X: numpy.matrix
        A NumPy matrix containing the model inputs
    Y : numpy.array
        A NumPy array containing the model outputs
    num_resamples : int
        The number of resamples when computing confidence intervals (default 100)
    conf_level : float
        The confidence interval level (default 0.95)
    print_to_console : bool
        Print results directly to console (default False)
    y_resamples : int, optional
        Number of samples to use when resampling (bootstrap) (default None)
    method : {"all", "delta", "sobol"}, optional
        Whether to compute "delta", "sobol" or both ("all") indices (default "all")


    References
    ----------
    1. Borgonovo, E. (2007). "A new uncertainty importance measure."
           Reliability Engineering & System Safety, 92(6):771-784,
           doi:10.1016/j.ress.2006.04.015.

    2. Plischke, E., E. Borgonovo, and C. L. Smith (2013). "Global
           sensitivity measures from given data." European Journal of
           Operational Research, 226(3):536-550, doi:10.1016/j.ejor.2012.11.047.
    '''
def calc_delta(Y, Ygrid, X, m):
    """Plischke et al. (2013) delta index estimator (eqn 26) for d_hat."""
def bias_reduced_delta(Y, Ygrid, X, m, num_resamples, conf_level, y_resamples):
    """Plischke et al. 2013 bias reduction technique (eqn 30)"""
def sobol_first(Y, X, m): ...
def sobol_first_conf(Y, X, m, num_resamples, conf_level, y_resamples): ...
def cli_parse(parser): ...
def cli_action(args) -> None: ...
