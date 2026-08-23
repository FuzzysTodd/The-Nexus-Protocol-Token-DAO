from . import common_args as common_args
from SALib.sample.ff import extend_bounds as extend_bounds, generate_contrast as generate_contrast
from SALib.util import ResultDict as ResultDict, read_param_file as read_param_file
from _typeshed import Incomplete

def analyze(problem, X, Y, second_order: bool = False, print_to_console: bool = False, seed: Incomplete | None = None):
    """Perform a fractional factorial analysis

    Returns a dictionary with keys 'ME' (main effect) and 'IE' (interaction
    effect). The techniques bulks out the number of parameters with dummy
    parameters to the nearest 2**n.  Any results involving dummy parameters
    could indicate a problem with the model runs.


    Notes
    -----
    Compatible with:
        `ff` : :func:`SALib.sample.ff.sample`


    Examples
    --------
        >>> X = sample(problem)
        >>> Y = X[:, 0] + (0.1 * X[:, 1]) + ((1.2 * X[:, 2]) * (0.2 + X[:, 0]))
        >>> analyze(problem, X, Y, second_order=True, print_to_console=True)


    Parameters
    ----------
    problem: dict
        The problem definition
    X: numpy.matrix
        The NumPy matrix containing the model inputs
    Y: numpy.array
        The NumPy array containing the model outputs
    second_order: bool, default=False
        Include interaction effects
    print_to_console: bool, default=False
        Print results directly to console
    seed : int
        Seed to generate a random number


    Returns
    -------
    Si: dict
        A dictionary of sensitivity indices, including main effects ``ME``,
        and interaction effects ``IE`` (if ``second_order`` is True)


    References
    ----------
    1. Saltelli, A., Ratto, M., Andres, T., Campolongo, F.,
           Cariboni, J., Gatelli, D.,
           Saisana, M., Tarantola, S., 2008.
           Global Sensitivity Analysis: The Primer.
           Wiley, West Sussex, U.K.
           http://doi.org/10.1002/9780470725184
    """
def to_df(self):
    """Conversion method to Pandas DataFrame. To be attached to ResultDict.

    Returns
    -------
    main_effect, inter_effect: tuple
        A tuple of DataFrames for main effects and interaction effects.
        The second element (for interactions) will be `None` if not available.
    """
def interactions(problem, Y):
    """Computes the second order effects

    Computes the second order effects (interactions) between
    all combinations of pairs of input factors

    Parameters
    ----------
    problem: dict
        The problem definition
    Y: numpy.array
        The NumPy array containing the model outputs

    Returns
    -------
    ie_names: list
        The names of the interaction pairs
    IE: list
        The sensitivity indices for the pairwise interactions
    """
def cli_parse(parser): ...
def cli_action(args) -> None: ...
