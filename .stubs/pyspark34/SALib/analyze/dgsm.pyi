from . import common_args as common_args
from ..util import ResultDict as ResultDict, read_param_file as read_param_file
from _typeshed import Incomplete

def analyze(problem, X, Y, num_resamples: int = 100, conf_level: float = 0.95, print_to_console: bool = False, seed: Incomplete | None = None):
    '''Calculates Derivative-based Global Sensitivity Measure on model outputs.

    Returns a dictionary with keys \'vi\', \'vi_std\', \'dgsm\', and \'dgsm_conf\',
    where each entry is a list of size D (the number of parameters) containing
    the indices in the same order as the parameter file.


    Notes
    -----
    Compatible with:
        `finite_diff` : :func:`SALib.sample.finite_diff.sample`


    Examples
    --------
        >>> X = finite_diff.sample(problem, 1000)
        >>> Y = Ishigami.evaluate(X)
        >>> Si = dgsm.analyze(problem, Y, print_to_console=False)


    Parameters
    ----------
    problem : dict
        The problem definition
    X : numpy.matrix
        The NumPy matrix containing the model inputs
    Y : numpy.array
        The NumPy array containing the model outputs
    num_resamples : int
        The number of resamples used to compute the confidence
        intervals (default 1000)
    conf_level : float
        The confidence interval level (default 0.95)
    print_to_console : bool
        Print results directly to console (default False)
    seed : int
        Seed to generate a random number


    References
    ----------
    1. Sobol, I. M. and S. Kucherenko (2009). "Derivative based global
           sensitivity measures and their link with global sensitivity
           indices." Mathematics and Computers in Simulation, 79(10):3009-3017,
           doi:10.1016/j.matcom.2009.01.023.
    '''
def calc_vi_stats(base, perturbed, x_delta):
    """Calculate v_i mean and std.

    v_i sensitivity measure following Sobol and Kucherenko (2009)
    For comparison, Morris mu* < sqrt(v_i)

    Same as calc_vi_mean but returns standard deviation as well.
    """
def calc_vi_mean(base, perturbed, x_delta):
    """Calculate v_i mean.

    Same as calc_vi_stats but only returns the mean.
    """
def calc_dgsm(base, perturbed, x_delta, bounds, num_resamples, conf_level):
    """v_i sensitivity measure following Sobol and Kucherenko (2009).
    For comparison, total order S_tot <= dgsm
    """
def cli_parse(parser): ...
def cli_action(args) -> None: ...
