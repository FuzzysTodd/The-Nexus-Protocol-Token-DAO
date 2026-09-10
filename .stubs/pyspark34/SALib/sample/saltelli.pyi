from . import common_args as common_args, sobol_sequence as sobol_sequence
from ..util import compute_groups_matrix as compute_groups_matrix, read_param_file as read_param_file, scale_samples as scale_samples
from typing import Dict

def sample(problem: Dict, N: int, calc_second_order: bool = True, skip_values: int = None):
    """Generates model inputs using Saltelli's extension of the Sobol' sequence

    The Sobol' sequence is a popular quasi-random low-discrepancy sequence used
    to generate uniform samples of parameter space.

    Returns a NumPy matrix containing the model inputs using Saltelli's
    sampling scheme.

    Saltelli's scheme extends the Sobol' sequence in a way to reduce
    the error rates in the resulting sensitivity index calculations. If
    `calc_second_order` is False, the resulting matrix has ``N * (D + 2)``
    rows, where ``D`` is the number of parameters.
    If `calc_second_order` is `True`, the resulting matrix has ``N * (2D + 2)``
    rows.
    These model inputs are intended to be used with
    :func:`SALib.analyze.sobol.analyze`.

    .. deprecated:: 1.4.6

    Notes
    -----
    The initial points of the Sobol' sequence has some repetition (see Table 2
    in Campolongo [1]), which can be avoided by setting the `skip_values`
    parameter. Skipping values reportedly improves the uniformity of samples.
    It has been shown that naively skipping values may reduce accuracy,
    increasing the number of samples needed to achieve convergence
    (see Owen [2]).

    A recommendation adopted here is that both `skip_values` and `N` be a power
    of 2, where `N` is the desired number of samples (see [2] and discussion in
    [5] for further context). It is also suggested therein that
    ``skip_values >= N``.

    The method now defaults to setting `skip_values` to a power of two that is
    ``>= N``. If `skip_values` is provided, the method now raises a UserWarning
    in cases where sample sizes may be sub-optimal according to the
    recommendation above.

    Parameters
    ----------
    problem : dict
        The problem definition
    N : int
        The number of samples to generate.
        Ideally a power of 2 and <= `skip_values`.
    calc_second_order : bool
        Calculate second-order sensitivities (default True)
    skip_values : int or None
        Number of points in Sobol' sequence to skip, ideally a value of base 2
        (default: a power of 2 >= N, or 16; whichever is greater)


    References
    ----------
    1. Campolongo, F., Saltelli, A., Cariboni, J., 2011.
           From screening to quantitative sensitivity analysis.
           A unified approach.
           Computer Physics Communications 182, 978-988.
           https://doi.org/10.1016/j.cpc.2010.12.039

    2. Owen, A. B., 2020.
           On dropping the first Sobol' point.
           arXiv:2008.08051 [cs, math, stat].
           Available at: http://arxiv.org/abs/2008.08051
           (Accessed: 20 April 2021).

    3. Saltelli, A., 2002.
           Making best use of model evaluations to compute sensitivity indices.
           Computer Physics Communications 145, 280-297.
           https://doi.org/10.1016/S0010-4655(02)00280-1

    4. Sobol', I.M., 2001.
           Global sensitivity indices for nonlinear mathematical models and
           their Monte Carlo estimates.
           Mathematics and Computers in Simulation,
           The Second IMACS Seminar on Monte Carlo Methods 55, 271-280.
           https://doi.org/10.1016/S0378-4754(00)00270-6

    5. Discussion: https://github.com/scipy/scipy/pull/10844
           https://github.com/scipy/scipy/pull/10844#issuecomment-672186615
           https://github.com/scipy/scipy/pull/10844#issuecomment-673029539
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
