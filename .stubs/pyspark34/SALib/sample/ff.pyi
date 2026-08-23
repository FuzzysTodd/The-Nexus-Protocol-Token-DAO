from . import common_args as common_args
from ..util import read_param_file as read_param_file, scale_samples as scale_samples
from _typeshed import Incomplete

def find_smallest(num_vars):
    """Find the smallest exponent of two that is greater than the number
    of variables.

    Parameters
    ----------
    num_vars : int
        Number of variables

    Returns
    -------
    x : int
        Smallest exponent of two greater than `num_vars`
    """
def extend_bounds(problem):
    """Extends the problem bounds to the nearest power of two.

    Parameters
    ----------
    problem : dict
        The problem definition
    """
def generate_contrast(problem):
    """Generates the raw sample from the problem file.

    Parameters
    ----------
    problem : dict
        The problem definition
    """
def sample(problem, seed: Incomplete | None = None):
    """Generates model inputs using a fractional factorial sample.

    Returns a NumPy matrix containing the model inputs required for a
    fractional factorial analysis.
    The resulting matrix has D columns, where D is smallest power of 2 that is
    greater than the number of parameters.
    These model inputs are intended to be used with
    :func:`SALib.analyze.ff.analyze`.

    The problem file is padded with a number of dummy variables called
    ``dummy_0`` required for this procedure. These dummy variables can be used
    as a check for errors in the analyze procedure.

    This algorithm is an implementation of that contained in Saltelli et al
    [`Saltelli et al. 2008 <http://doi.org/10.1002/9780470725184>`_]

    Parameters
    ----------
    problem : dict
        The problem definition
    seed : int
        Seed to generate a random number

    Returns
    -------
    sample : :class:`numpy.array`

    References
    ----------
    1. Saltelli, A., Ratto, M., Andres, T., Campolongo, F.,
       Cariboni, J., Gatelli, D., Saisana, M., Tarantola, S., 2008.
       Global Sensitivity Analysis: The Primer.
       Wiley, West Sussex, U.K.
       http://doi.org/10.1002/9780470725184
    """

cli_parse: Incomplete

def cli_action(args) -> None:
    """Run sampling method

    Parameters
    ----------
    args : argparse namespace
    """
