import numpy as np
from . import common_args as common_args
from ..util import compute_groups_matrix as compute_groups_matrix, read_param_file as read_param_file, scale_samples as scale_samples
from typing import Dict

def sample(problem: Dict, N: int, *, calc_second_order: bool = True, scramble: bool = True, skip_values: int = 0, seed: int | np.random.Generator | None = None):
    """Generates model inputs using Saltelli's extension of the Sobol' sequence.

    The Sobol' sequence is a popular quasi-random low-discrepancy sequence used
    to generate uniform samples of parameter space.
    The general approach is described in [1].

    Returns a NumPy matrix containing the model inputs using Saltelli's
    sampling scheme.

    Saltelli's scheme reduces the number of required model runs from ``N(2D+1)`` to
    ``N(D+1)`` (see [2]).

    If `calc_second_order` is False, the resulting matrix has ``N * (D + 2)``
    rows, where ``D`` is the number of parameters.

    If `calc_second_order` is `True`, the resulting matrix has ``N * (2D + 2)``
    rows.

    These model inputs are intended to be used with
    :func:`SALib.analyze.sobol.analyze`.

    Notes
    -----
    The initial points of the Sobol' sequence has some repetition (see Table 2
    in Campolongo [3]__), which can be avoided by scrambling the sequence.

    Another option, not recommended and available for educational purposes,
    is to use the `skip_values` parameter.
    Skipping values reportedly improves the uniformity of samples.
    But, it has been shown that naively skipping values may reduce accuracy,
    increasing the number of samples needed to achieve convergence
    (see Owen [4]__).

    Parameters
    ----------
    problem : dict,
        The problem definition.
    N : int
        The number of samples to generate.
        Ideally a power of 2 and <= `skip_values`.
    calc_second_order : bool, optional
        Calculate second-order sensitivities. Default is True.
    scramble : bool, optional
        If True, use LMS+shift scrambling. Otherwise, no scrambling is done.
        Default is True.
    skip_values : int, optional
        Number of points in Sobol' sequence to skip, ideally a value of base 2.
        It's recommended not to change this value and use `scramble` instead.
        `scramble` and `skip_values` can be used together.
        Default is 0.
    seed : {None, int, `numpy.random.Generator`}, optional
        If `seed` is None the `numpy.random.Generator` generator is used.
        If `seed` is an int, a new ``Generator`` instance is used,
        seeded with `seed`.
        If `seed` is already a ``Generator`` instance then that instance is
        used. Default is None.

    References
    ----------
    1. Sobol', I.M., 2001.
       Global sensitivity indices for nonlinear mathematical models and
       their Monte Carlo estimates.
       Mathematics and Computers in Simulation,
       The Second IMACS Seminar on Monte Carlo Methods 55, 271-280.
       https://doi.org/10.1016/S0378-4754(00)00270-6

    2. Saltelli, A. (2002).
       Making best use of model evaluations to compute sensitivity indices.
       Computer Physics Communications, 145(2), 280-297.
       https://doi.org/10.1016/S0010-4655(02)00280-1

    3. Campolongo, F., Saltelli, A., Cariboni, J., 2011.
       From screening to quantitative sensitivity analysis.
       A unified approach.
       Computer Physics Communications 182, 978-988.
       https://doi.org/10.1016/j.cpc.2010.12.039

    4. Owen, A. B., 2020.
       On dropping the first Sobol' point.
       arXiv:2008.08051 [cs, math, stat].
       Available at: http://arxiv.org/abs/2008.08051
       (Accessed: 20 April 2021).
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
