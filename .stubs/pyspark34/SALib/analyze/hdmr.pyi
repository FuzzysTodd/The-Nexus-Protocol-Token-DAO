import numpy as np
from typing import Dict

__all__ = ['analyze', 'cli_parse', 'cli_action']

def analyze(problem: Dict, X: np.ndarray, Y: np.ndarray, maxorder: int = 2, maxiter: int = 100, m: int = 2, K: int = 20, R: int = None, alpha: float = 0.95, lambdax: float = 0.01, print_to_console: bool = False, seed: int = None) -> Dict:
    '''Compute global sensitivity indices using the meta-modeling technique
    known as High-Dimensional Model Representation (HDMR).

    HDMR itself is not a sensitivity analysis method but a surrogate modeling
    approach. It constructs a map of relationship between sets of high
    dimensional inputs and output system variables [1]. This I/O relation can
    be constructed using different basis functions (orthonormal polynomials,
    splines, etc.). The model decomposition can be expressed as

    .. math::
        \\widehat{y} = \\sum_{u \\subseteq \\{1, 2, ..., d \\}} f_u

    where :math:`u` represents any subset including an empty set.

    HDMR becomes extremely useful when the computational cost of obtaining
    sufficient Monte Carlo samples are prohibitive, as may be the case with
    Sobol\'s method. It uses least-square regression to reduce the required
    number of samples and thus the number of function (model) evaluations.
    Another advantage of this method is that it can account for correlation
    among the model input. Unlike other variance-based methods, the main
    effects are the combination of structural (uncorrelated) and
    correlated contributions.

    This method uses as input

    - a N x d matrix of N different d-vectors of model inputs (factors/parameters)
    - a N x 1 vector of corresponding model outputs

    Notes
    -----
    Compatible with:
        all samplers

    Sets an `emulate` method allowing re-use of the emulator.

    Examples
    --------
    .. code-block:: python
        :linenos:

        sp = ProblemSpec({
            \'names\': [\'X1\', \'X2\', \'X3\'],
            \'bounds\': [[-np.pi, np.pi]] * 3,
            # \'groups\': [\'A\', \'B\', \'A\'],
            \'outputs\': [\'Y\']
        })

        (sp.sample_saltelli(2048)
            .evaluate(Ishigami.evaluate)
            .analyze_hdmr()
        )

        sp.emulate()

    Parameters
    ----------
    problem : dict
        The problem definition

    X : numpy.matrix
        The NumPy matrix containing the model inputs, N rows by d columns

    Y : numpy.array
        The NumPy array containing the model outputs for each row of X

    maxorder : int (1-3, default: 2)
        Maximum HDMR expansion order

    maxiter : int (1-1000, default: 100)
        Max iterations backfitting

    m : int (2-10, default: 2)
        Number of B-spline intervals

    K : int (1-100, default: 20)
        Number of bootstrap iterations

    R : int (100-N/2, default: N/2)
        Number of bootstrap samples. Will be set to length of `Y` if `K` is set to 1.

    alpha : float (0.5-1)
        Confidence interval F-test

    lambdax : float (0-10, default: 0.01)
        Regularization term

    print_to_console : bool
        Print results directly to console (default: False)

    seed : bool
        Seed to generate a random number

    Returns
    -------
    Si : ResultDict,
        Sa : Uncorrelated contribution of a term

        Sa_conf : Confidence interval of Sa

        Sb : Correlated contribution of a term

        Sb_conf : Confidence interval of Sb

        S : Total contribution of a particular term
            Sum of Sa and Sb, representing first/second/third order sensitivity indices

        S_conf : Confidence interval of S

        ST : Total contribution of a particular dimension/parameter

        ST_conf : Confidence interval of ST

        select : Number of selection (F-Test)

        Em : Emulator result set
            C1: First order coefficient
            C2: Second order coefficient
            C3: Third Order coefficient

    References
    ----------
    1. Rabitz, H. and Aliş, Ö.F.,
       "General foundations of high dimensional model representations",
       Journal of Mathematical Chemistry 25, 197-233 (1999)
       https://doi.org/10.1023/A:1019188517934

    2. Genyuan Li, H. Rabitz, P.E. Yelvington, O.O. Oluwole, F. Bacon,
       C.E. Kolb, and J. Schoendorf,
       "Global Sensitivity Analysis for Systems with Independent and/or
       Correlated Inputs",
       Journal of Physical Chemistry A, Vol. 114 (19), pp. 6022 - 6032, 2010,
       https://doi.org/10.1021/jp9096919
    '''
def cli_parse(parser): ...
def cli_action(args) -> None: ...
