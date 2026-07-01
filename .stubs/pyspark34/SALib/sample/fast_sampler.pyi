from . import common_args as common_args
from ..util import read_param_file as read_param_file, scale_samples as scale_samples
from _typeshed import Incomplete

def sample(problem, N, M: int = 4, seed: Incomplete | None = None):
    """Generate model inputs for extended Fourier Amplitude Sensitivity Test.

    Returns a NumPy matrix containing the model inputs required by the extended
    Fourier Amplitude sensitivity test.  The resulting matrix contains N * D
    rows and D columns, where D is the number of parameters.

    The samples generated are intended to be used by
    :func:`SALib.analyze.fast.analyze`.

    Parameters
    ----------
    problem : dict
        The problem definition
    N : int
        The number of samples to generate
    M : int
        The interference parameter, i.e., the number of harmonics to sum in the
        Fourier series decomposition (default 4)
    seed : int
        Seed to generate a random number

    References
    ----------
    1. Cukier, R.I., Fortuin, C.M., Shuler, K.E., Petschek, A.G.,
       Schaibly, J.H., 1973.
       Study of the sensitivity of coupled reaction systems to
       uncertainties in rate coefficients. I theory.
       Journal of Chemical Physics 59, 3873-3878.
       https://doi.org/10.1063/1.1680571

    2. Saltelli, A., S. Tarantola, and K. P.-S. Chan (1999).
       A Quantitative Model-Independent Method for Global Sensitivity Analysis
       of Model Output.
       Technometrics, 41(1):39-56,
       doi:10.1080/00401706.1999.10485594.
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
def cli_action(args) -> None:
    """Run sampling method

    Parameters
    ----------
    args : argparse namespace
    """
