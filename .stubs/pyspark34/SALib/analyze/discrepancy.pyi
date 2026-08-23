import numpy as np
from SALib.analyze import common_args as common_args
from SALib.util import ResultDict as ResultDict, read_param_file as read_param_file
from typing import Dict

def analyze(problem: Dict, X: np.ndarray, Y: np.ndarray, method: str = 'WD', print_to_console: bool = False, seed: int = None):
    '''Discrepancy indices.

    Parameters
    ----------
    problem : dict
        The problem definition
    X, Y : numpy.ndarray
        An array of model inputs and outputs.
    method : {"WD", "CD", "MD", "L2-star"}
        Type of discrepancy. Refer to `scipy.stats.qmc.discrepancy` for more
        details. Default is "WD".
    print_to_console : bool, optional
        Print results directly to console (default False)
    seed : int, optional
        Seed value to ensure deterministic results
        Unused, but defined to maintain compatibility with other functions.

    Notes
    -----
    Compatible with:
        all samplers

    Based on 2D sub projections of ``[Xi,Y]``, the discrepancy of each sample
    is calculated which gives a value for all ``Xi``. This information is used
    as a measure of sensitivity.

    Discrepancy analysis is very fast and is visually explainable. Considering
    two variables ``X1`` and ``X2``, ``X1`` is more influential than ``X2``
    when the scatterplot of ``X1`` against ``Y`` displays a more discernible
    shape than the scatterplot of ``X2`` against ``Y``.

    For the method to work properly, the input parameter space need to be
    uniformly covered as the quality of the measure depends on the value of
    the discrepancy. Taking a 2D sub projection, if the distribution of sample
    along ``Xi`` is not uniform, it will have an impact on the discrepancy,
    the value will increase, i.e. the importance of this parameter would be
    inflated.

    References
    ----------
    1. A. Puy, P.T. Roy and A. Saltelli. 2023. Discrepancy measures for
    sensitivity analysis. https://arxiv.org/abs/2206.13470

    2. A. Saltelli, M. Ratto, T. Andres, F. Campolongo, J. Cariboni, D. Gatelli,
    M. Saisana, and S. Tarantola. 2008.
    Global Sensitivity Analysis: The Primer.
    Wiley, West Sussex, U.K.
    https://dx.doi.org/10.1002/9780470725184
    Accessible at:
    http://www.andreasaltelli.eu/file/repository/Primer_Corrected_2022.pdf

    Examples
    --------

        >>> import numpy as np
        >>> from SALib.sample import latin
        >>> from SALib.analyze import discrepancy
        >>> from SALib.test_functions import Ishigami

        >>> problem = {
        ...   \'num_vars\': 3,
        ...   \'names\': [\'x1\', \'x2\', \'x3\'],
        ...   \'bounds\': [[-np.pi, np.pi]]*3
        ... }
        >>> X = latin.sample(problem, 1000)
        >>> Y = Ishigami.evaluate(X)
        >>> Si = discrepancy.analyze(problem, X, Y, print_to_console=True)
    '''
def cli_parse(parser): ...
def cli_action(args) -> None: ...
