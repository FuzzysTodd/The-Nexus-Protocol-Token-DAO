from . import common_args as common_args
from ..util import ResultDict as ResultDict, read_param_file as read_param_file
from _typeshed import Incomplete

def analyze(problem, X, Y, M: int = 10, num_resamples: int = 100, conf_level: float = 0.95, print_to_console: bool = False, seed: Incomplete | None = None):
    """Performs the Random Balanced Design - Fourier Amplitude Sensitivity Test
    (RBD-FAST) on model outputs.

    Returns a dictionary with keys 'S1', where each entry is a list of
    size D (the number of parameters) containing the indices in the same order
    as the parameter file.

    Notes
    -----
    Compatible with:
        all samplers


    Examples
    --------
        >>> X = latin.sample(problem, 1000)
        >>> Y = Ishigami.evaluate(X)
        >>> Si = rbd_fast.analyze(problem, X, Y, print_to_console=False)


    Parameters
    ----------
    problem : dict
        The problem definition
    X : numpy.array
        A NumPy array containing the model inputs
    Y : numpy.array
        A NumPy array containing the model outputs
    M : int
        The interference parameter, i.e., the number of harmonics to sum in
        the Fourier series decomposition (default 10)
    print_to_console : bool
        Print results directly to console (default False)
    seed : int
        Seed to generate a random number


    References
    ----------
    1. S. Tarantola, D. Gatelli and T. Mara (2006)
       Random Balance Designs for the Estimation of First Order Global
       Sensitivity Indices,
       Reliability Engineering and System Safety, 91:6, 717-727
       https://doi.org/10.1016/j.ress.2005.06.003

    2. Elmar Plischke (2010)
        An effective algorithm for computing global sensitivity indices
        (EASI),
        Reliability Engineering & System Safety,
        95:4, 354-360. doi:10.1016/j.ress.2009.11.005

    3. Jean-Yves Tissot, Clémentine Prieur (2012)
        Bias correction for the estimation of sensitivity indices based
        on random balance designs,
        Reliability Engineering and System Safety, Elsevier, 107, 205-213.
        doi:10.1016/j.ress.2012.06.010

    4. Jeanne Goffart, Mickael Rabouille & Nathan Mendes (2015)
         Uncertainty and sensitivity analysis applied to hygrothermal
         simulation of a brick building in a hot and humid climate,
         Journal of Building Performance Simulation.
         doi:10.1080/19401493.2015.1112430
    """
def permute_outputs(X, Y):
    '''
    Permute the output according to one of the inputs as in [_2]

    References
    ----------
    .. [2] Elmar Plischke (2010) "An effective algorithm for computing global
          sensitivity indices (EASI) Reliability Engineering & System Safety",
          95:4, 354-360. doi:10.1016/j.ress.2009.11.005

    '''
def compute_first_order(permuted_outputs, M): ...
def unskew_S1(S1, M, N):
    '''
    Unskew the sensitivity indices
    (Jean-Yves Tissot, Clémentine Prieur (2012) "Bias correction for the
    estimation of sensitivity indices based on random balance designs.",
    Reliability Engineering and System Safety, Elsevier, 107, 205-213.
    doi:10.1016/j.ress.2012.06.010)
    '''
def bootstrap(X_d, Y, M, resamples, conf_level): ...
def cli_parse(parser): ...
def cli_action(args) -> None: ...
