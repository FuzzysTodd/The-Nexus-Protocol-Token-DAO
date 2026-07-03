import numpy as np
from . import common_args as common_args
from ..util import ResultDict as ResultDict, read_param_file as read_param_file
from _typeshed import Incomplete

def analyze(problem, Y, M: int = 4, num_resamples: int = 100, conf_level: float = 0.95, print_to_console: bool = False, seed: Incomplete | None = None):
    """Perform extended Fourier Amplitude Sensitivity Test on model outputs.

    Returns a dictionary with keys 'S1' and 'ST', where each entry is a list of
    size D (the number of parameters) containing the indices in the same order
    as the parameter file.

    Notes
    -----
    Compatible with:
        `fast_sampler` : :func:`SALib.sample.fast_sampler.sample`

    Examples
    --------
        >>> X = fast_sampler.sample(problem, 1000)
        >>> Y = Ishigami.evaluate(X)
        >>> Si = fast.analyze(problem, Y, print_to_console=False)

    Parameters
    ----------
    problem : dict
        The problem definition
    Y : numpy.array
        A NumPy array containing the model outputs
    M : int
        The interference parameter, i.e., the number of harmonics to sum in
        the Fourier series decomposition (default 4)
    print_to_console : bool
        Print results directly to console (default False)
    seed : int
        Seed to generate a random number

    References
    ----------
    1. Cukier, R. I., C. M. Fortuin, K. E. Shuler, A. G. Petschek, and
       J. H. Schaibly (1973).
       Study of the sensitivity of coupled reaction systems to
       uncertainties in rate coefficients.
       J. Chem. Phys., 59(8):3873-3878
       doi:10.1063/1.1680571

    2. Saltelli, A., S. Tarantola, and K. P.-S. Chan (1999).
       A Quantitative Model-Independent Method for Global Sensitivity Analysis
       of Model Output.
       Technometrics, 41(1):39-56,
       doi:10.1080/00401706.1999.10485594.

    3. Pujol, G. (2006)
       fast99 - R `sensitivity` package
       https://github.com/cran/sensitivity/blob/master/R/fast99.R
    """
def compute_orders(outputs: np.ndarray, N: int, M: int, omega: int): ...
def bootstrap(Y: np.ndarray, M: int, resamples: int, conf_level: float):
    """Compute CIs.

    Infers ``N`` from results of sub-sample ``Y`` and re-estimates omega (ω)
    for the above ``N``.
    """
def cli_parse(parser):
    """Add method specific options to CLI parser.

    Parameters
    ----------
    parser : argparse object

    Returns
    -------
    Updated argparse object
    """
def cli_action(args) -> None: ...
