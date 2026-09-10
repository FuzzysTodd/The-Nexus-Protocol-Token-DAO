from . import common_args as common_args
from ..util import ResultDict as ResultDict, extract_group_names as extract_group_names, read_param_file as read_param_file
from _typeshed import Incomplete

CONST_RESULT_MSG: str

def analyze(problem, Y, calc_second_order: bool = True, num_resamples: int = 100, conf_level: float = 0.95, print_to_console: bool = False, parallel: bool = False, n_processors: Incomplete | None = None, keep_resamples: bool = False, seed: Incomplete | None = None):
    """Perform Sobol Analysis on model outputs.

    Returns a dictionary with keys 'S1', 'S1_conf', 'ST', and 'ST_conf', where
    each entry is a list of size D (the number of parameters) containing the
    indices in the same order as the parameter file.  If calc_second_order is
    True, the dictionary also contains keys 'S2' and 'S2_conf'.

    There are several approaches to estimating sensitivity indices.
    The general approach is described in [1]. The implementation offered here
    follows [2] for first and total order indices, whereas estimation of
    second order sensitivities follows [3]. A noteworthy point is the
    improvement to reduce error rates in sensitivity estimation is introduced
    in [4].

    Notes
    -----
    Compatible with:
        `saltelli` : :func:`SALib.sample.saltelli.sample`
        `sobol` : :func:`SALib.sample.sobol.sample`


    Examples
    --------
    >>> X = saltelli.sample(problem, 512)
    >>> Y = Ishigami.evaluate(X)
    >>> Si = sobol.analyze(problem, Y, print_to_console=True)


    Parameters
    ----------
    problem : dict
        The problem definition
    Y : numpy.array
        A NumPy array containing the model outputs
    calc_second_order : bool
        Calculate second-order sensitivities (default True)
    num_resamples : int
        The number of resamples (default 100)
    conf_level : float
        The confidence interval level (default 0.95)
    print_to_console : bool
        Print results directly to console (default False)
    parallel : bool
        Perform analysis in parallel if True
    n_processors : int
        Number of parallel processes (only used if parallel is True)
    keep_resamples : bool
        Whether or not to store intermediate resampling results (default False)
    seed : int
        Seed to generate a random number

    References
    ----------
    1. Sobol, I. M. (2001).
       Global sensitivity indices for nonlinear
       mathematical models and their Monte Carlo estimates.
       Mathematics and Computers in Simulation, 55(1-3):271-280,
       doi:10.1016/S0378-4754(00)00270-6.

    2. Saltelli, A., P. Annoni, I. Azzini, F. Campolongo, M. Ratto, and
       S. Tarantola (2010).
       Variance based sensitivity analysis of model output. Design and
       estimator for the total sensitivity index.
       Computer Physics Communications, 181(2):259-270,
       doi:10.1016/j.cpc.2009.09.018.

    3. Saltelli, A. (2002).
       Making best use of model evaluations to compute sensitivity indices.
       Computer Physics Communications, 145(2):280-297
       doi:10.1016/S0010-4655(02)00280-1.

    4. Sobol', I. M., Tarantola, S., Gatelli, D., Kucherenko, S. S., &
       Mauntz, W. (2007).
       Estimating the approximation error when fixing unessential factors in global
       sensitivity analysis.
       Reliability Engineering & System Safety, 92(7), 957-960.
       https://doi.org/10.1016/j.ress.2006.07.001
    """
def first_order(A, AB, B):
    """
    First order estimator following Saltelli et al. 2010 CPC, normalized by
    sample variance
    """
def total_order(A, AB, B):
    """
    Total order estimator following Saltelli et al. 2010 CPC, normalized by
    sample variance
    """
def second_order(A, ABj, ABk, BAj, B):
    """Second order estimator following Saltelli 2002"""
def create_Si_dict(D: int, num_resamples: int, keep_resamples: bool, calc_second_order: bool):
    """initialize empty dict to store sensitivity indices"""
def separate_output_values(Y, D, N, calc_second_order): ...
def sobol_parallel(Z, A, AB, BA, B, r, tasks): ...
def create_task_list(D, calc_second_order, n_processors):
    """
    Create list with one entry (key, parameter 1, parameter 2) per sobol
    index (+conf.). This is used to supply parallel tasks to
    multiprocessing.Pool
    """
def Si_list_to_dict(S_list, D: int, num_resamples: int, keep_resamples: bool, calc_second_order: bool):
    """Convert the parallel output into the regular dict format for
    printing/returning"""
def Si_to_pandas_dict(S_dict):
    """Convert Si information into Pandas DataFrame compatible dict.


    Examples
    --------
    >>> X = saltelli.sample(problem, 512)
    >>> Y = Ishigami.evaluate(X)
    >>> Si = sobol.analyze(problem, Y, print_to_console=True)
    >>> T_Si, first_Si, (idx, second_Si) = sobol.Si_to_pandas_dict(Si, problem)


    Parameters
    ----------
    S_dict : ResultDict
        Sobol sensitivity indices

    See Also
    --------
    Si_list_to_dict

    Returns
    -------
    tuple : of total, first, and second order sensitivities.
            Total and first order are dicts.
            Second order sensitivities contain a tuple of parameter name
            combinations for use as the DataFrame index and second order
            sensitivities.
            If no second order indices found, then returns tuple of
            (None, None)
    """
def to_df(self):
    """Conversion method to Pandas DataFrame. To be attached to ResultDict.

    Returns
    -------
    List : of Pandas DataFrames in order of Total, First, Second

    Examples
    --------
    >>> Si = sobol.analyze(problem, Y, print_to_console=True)
    >>> total_Si, first_Si, second_Si = Si.to_df()
    """
def cli_parse(parser): ...
def cli_action(args) -> None: ...
