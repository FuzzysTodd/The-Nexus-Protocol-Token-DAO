import numpy as np
from typing import Dict

__all__ = ['sample']

def sample(problem: Dict, N: int, num_levels: int = 4, optimal_trajectories: int = None, local_optimization: bool = True, seed: int = None) -> np.ndarray:
    '''Generate model inputs using the Method of Morris.

    Three variants of Morris\' sampling for elementary effects is supported:

    - Vanilla Morris (see [1])
      when ``optimal_trajectories`` is ``None``/``False`` and
      ``local_optimization`` is ``False``
    - Optimised trajectories when ``optimal_trajectories=True`` using
        Campolongo\'s enhancements (see [2]) and optionally Ruano\'s enhancement
        (see [3]) when ``local_optimization=True``
    - Morris with groups when the problem definition specifies groups of
      parameters

    Results from these model inputs are intended to be used with
    :func:`SALib.analyze.morris.analyze`.

    Notes
    -----
    Campolongo et al., [2] introduces an optimal trajectories approach which
    attempts to maximize the parameter space scanned for a given number of
    trajectories (where `optimal_trajectories` :math:`\\in {2, ..., N}`).
    The approach accomplishes this aim by randomly generating a high number
    of possible trajectories (500 to 1000 in [2]) and selecting a subset of
    ``r`` trajectories which have the highest spread in parameter space.
    The ``r`` variable in [2] corresponds to the ``optimal_trajectories``
    parameter here.

    Calculating all possible combinations of trajectories can be
    computationally expensive. The number of factors makes little
    difference, but the ratio between number of optimal trajectories and the
    sample size results in an exponentially increasing number of scores that
    must be computed to find the optimal combination of trajectories. We
    suggest going no higher than 4 levels from a pool of 100 samples with this
    "brute force" approach.

    Ruano et al., [3] proposed an alternative approach with an iterative
    process that maximizes the distance between subgroups of generated
    trajectories, from which the final set of trajectories are selected, again
    maximizing the distance between each. The approach is not guaranteed to
    produce the most optimal spread of trajectories, but are at least locally
    maximized and significantly reduce the time taken to select trajectories.
    With ``local_optimization = True`` (which is default), it is possible to
    go higher than the previously suggested 4 levels from a pool of 100
    samples.

    Parameters
    ----------
    problem : dict
        The problem definition
    N : int
        The number of trajectories to generate
    num_levels : int, default=4
        The number of grid levels (should be even)
    optimal_trajectories : int
        The number of optimal trajectories to sample (between 2 and N)
    local_optimization : bool, default=True
        Flag whether to use local optimization according to Ruano et al. (2012)
        Speeds up the process tremendously for bigger N and num_levels.
        If set to ``False`` brute force method is used, unless ``gurobipy`` is
        available
    seed : int
        Seed to generate a random number

    Returns
    -------
    sample_morris : np.ndarray
        Array containing the model inputs required for Method of Morris.
        The resulting matrix has :math:`(G/D+1)*N/T` rows and :math:`D`
        columns, where :math:`D` is the number of parameters, :math:`G`
        is the number of groups (if no groups are selected, the number
        of parameters). :math:`T` is the number of trajectories
        :math:`N`, or `optimal_trajectories` if selected.

    References
    ----------
    1. Morris, M.D., 1991.
       Factorial Sampling Plans for Preliminary Computational Experiments.
       Technometrics 33, 161-174.
       https://doi.org/10.1080/00401706.1991.10484804

    2. Campolongo, F., Cariboni, J., & Saltelli, A. 2007.
       An effective screening design for sensitivity analysis of large
       models.
       Environmental Modelling & Software, 22(10), 1509-1518.
       https://doi.org/10.1016/j.envsoft.2006.10.004

    3. Ruano, M.V., Ribes, J., Seco, A., Ferrer, J., 2012.
       An improved sampling strategy based on trajectory design for
       application of the Morris method to systems with many input
       factors.
       Environmental Modelling & Software 37, 103-109.
       https://doi.org/10.1016/j.envsoft.2012.03.008
    '''
