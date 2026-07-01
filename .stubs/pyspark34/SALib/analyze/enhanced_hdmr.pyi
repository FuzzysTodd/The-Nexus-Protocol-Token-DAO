import numpy as np
from typing import Dict

__all__ = ['analyze', 'cli_parse', 'cli_action']

def analyze(problem: Dict, X: np.ndarray, Y: np.ndarray, max_order: int = 2, poly_order: int = 3, bootstrap: int = 20, subset: int = None, max_iter: int = 100, l2_penalty: float = 0.01, alpha: float = 0.95, extended_base: bool = True, print_to_console: bool = False, return_emulator: bool = False, seed: int = None) -> Dict:
    '''Compute global sensitivity indices using the meta-modeling technique
    known as High-Dimensional Model Representation (HDMR).

    Introduction
    ------------
    HDMR itself is not a sensitivity analysis method but a surrogate modeling
    approach. It constructs a map of relationship between sets of high
    dimensional inputs and output system variables [1]. This I/O relation can
    be constructed using different basis functions (orthonormal polynomials,
    splines, etc.). The model decomposition can be expressed as

    .. math::
        \\tilde{y} \\approx \\widehat{y} &= f_0 + \\sum_{i=1}^{d} f_i(x_i) +
              \\sum_{i=1}^{d-1} \\sum_{j=i+1}^{d} f_{ij} (x_{ij}) +
              \\sum_{i=1}^{d-2} \\sum_{j=i+1}^{d-1}

              \\sum_{j+1}^{d} f_{ijk} (x_{ijk}) + \\epsilon \\\n
        \\widehat{y} &= f_0 + \\sum_{u \\subseteq \\{1, 2, ..., d \\}}^{2^n - 1}
          f_u + \\epsilon

    where :math:`u` represents any subset including an empty set. There is a
    unique decomposition regardless of correlation among the input variables
    under the following condition.

    .. math::
        \\forall v \\subseteq u, \\forall g_v: \\int
        f_u (x_u) g_v (x_v) w(\\bm(x)) d\\bm(x) = 0

    This condition implies that a component function is only required to be
    orthogonal to all nested lower order component functions whose variables
    are a subset of its variables. For example, :math:`f_{ijk} (x_i, x_j, x_k )`
    is only required to be orthogonal to :math:`f_i(x_i), f_j(x_j), f_k (x_k),
    f_{ij}(x_i, x_j), f_{ik}(x_i, x_k),` and :math:`f_{jk} (x_j, x_k)`.
    Please keep in mind that this condition is only satisfied when `extended_base`
    is set to `True`.

    HDMR becomes extremely useful when the computational cost of obtaining
    sufficient Monte Carlo samples are prohibitive, as may be the case with
    Sobol\'s method. It uses least-square regression to reduce the required
    number of samples and thus the number of function (model) evaluations.
    Another advantage of this method is that it can account for correlation
    among the model input. Unlike other variance-based methods, the main
    effects are the combination of structural (uncorrelated) and correlated
    contributions.

    Covariance Decomposition
    ------------------------
    Variance-based sensitivity analysis methods employ a decomposition approach
    to assess the contributions of input sets towards the variance observed in
    the model\'s output. This method uses the same technique while also considering
    the influence of correlation in the decomposition of output variance.The
    following equation ilustrates how correlation plays a role in variance
    decomposition.

    .. math::
        Var[y] = \\sum_{u=1}^{2^n - 1} Var[f_u] +
            \\sum_{u=1}^{2^n - 1} Cov \\left[f_u, \\sum_{v \\neq u} f_v \\right]

    The first component on the right hand side of the equation depicts the
    uncorrelated contribution to the overall variance, while the subsequent
    component signifies the associated contribution of a specific component
    function in correlation with other component functions. In this method,
    we used `Sa` and `Sb` to represent uncorrelated contribution and
    correlated contribution.

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
            \'outputs\': [\'Y\']
        })

        (sp.sample_saltelli(2048)
            .evaluate(Ishigami.evaluate)
            .analyze_enhanced_hdmr()
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
    max_order : int (1-3, default: 2)
        Maximum HDMR expansion order
    poly_order : int (1-10, default: 3)
        Maximum polynomial order
    bootstrap : int (1-100, default: 20)
        Number of bootstrap iterations
    subset : int (300-N, default: N/2)
        Number of bootstrap samples. Will be set to length of `Y` if `K` is set to 1.
    max_iter : int (1-1000, default: 100)
        Max iterations backfitting. Not used if extended_base is `True`
    l2_penalty : float (0-10, default: 0.01)
        Regularization term
    alpha : float (0.5-1, default: 0.95)
        Confidence interval for F-test
    extended_base : bool (default: True)
        Extends base matrix if `True`. This guarantees the hierarchical orthogonality
    print_to_console : bool (default: False)
        Prints results directly to console (default: False)
    return_emulator: bool (default: False)
        Attaches emulate method to the Si if `True`
    seed : int (default: None)
        Seed to generate a random number

    Returns
    -------
    Si : ResultDict,
        -"Sa" : Sensitivity index (uncorrelated contribution)
        -"Sa_conf" : Statistical confidence interval of `Sa`
        -"Sb" : Sensitivity index (correlated contribution)
        -"Sb_conf" : Statistical confidence interval of `Sb`
        -"S" : Sensitivity index (total contribution)
        -"S_conf" : Statistical confidence interval of `S`
        -"ST" : Total Sensitivity indexes of features/inputs
        -"ST_conf" : Statistical confidence interval of `ST`
        -"Signf" : Signigicancy for each bootstrap iteration
        -"Term" : Component name
        -emulate() : Emulator method when return_emulator is set to `True`

    References
    ----------
    1. Rabitz, H. and Aliş, Ö.F.,
       General foundations of high dimensional model representations,
       Journal of Mathematical Chemistry 25, 197-233 (1999)
       https://doi.org/10.1023/A:1019188517934

    2. Genyuan Li, H. Rabitz, P.E. Yelvington, O.O. Oluwole, F. Bacon,
       C.E. Kolb, and J. Schoendorf,
       "Global Sensitivity Analysis for Systems with Independent and/or
       Correlated Inputs",
       Journal of Physical Chemistry A, Vol. 114 (19), pp. 6022 - 6032, 2010,
       https://doi.org/10.1021/jp9096919

    3. Gao, Y., Sahin, A., & Vrugt, J. A. (2023)
       Probabilistic sensitivity analysis with dependent variables:
       Covariance-based decomposition of hydrologic models.
       Water Resources Research, 59, e2022WR032834.
       https://doi.org/10.1029/2022WR032834
    '''
def cli_parse(parser): ...
def cli_action(args) -> None: ...
