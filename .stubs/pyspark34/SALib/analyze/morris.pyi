import numpy as np
from . import common_args as common_args
from ..util import ResultDict as ResultDict, compute_groups_matrix as compute_groups_matrix, read_param_file as read_param_file
from _typeshed import Incomplete
from typing import Dict

def analyze(problem: Dict, X: np.ndarray, Y: np.ndarray, num_resamples: int = 100, conf_level: float = 0.95, scaled: bool = False, print_to_console: bool = False, num_levels: int = 4, seed: Incomplete | None = None) -> Dict:
    """Perform Morris Analysis on model outputs.

    Returns a result set with keys ``mu``, ``mu_star``, ``sigma``, and
    ``mu_star_conf``, where each entry corresponds to the parameters
    defined in the problem spec or parameter file.

    - ``mu`` metric indicates the mean of the distribution
    - ``mu_star`` metric indicates the mean of the distribution of absolute
      values
    - ``sigma`` is the standard deviation of the distribution

    When ``scaled`` is True, the elementary effects are scaled by the ratio of
    standard deviation of ``X`` and ``Y`` according to [3]. When using this
    option it is important to ensure that ``X`` contains the actual values
    passed into the model, as the elementary effects are divided by the
    step calculated from ``X`` rather than using `delta` which is calculated from
    the number of levels used in the sample. This could be the case if you
    perform post-processing on the values before passing them to the model.

    Scaled elementary effects are useful when comparing different model outputs
    with each other when the input and output parameters have different scales.
    The ranking between the ordinary elementary effects and the scaled should be
    the same.

    Notes
    -----
    When applied with groups, the ``mu`` metric is less reliable as the effect
    from parameters within a group become averaged out.

    The ``mu_star`` metric avoids this issue as it indicates the mean of the
    absolute values. If the direction of effects is important, Campolongo et
    al., [2] suggest comparing ``mu_star`` with ``mu``. If ``mu`` is low
    and ``mu_star`` is high, then the effects are of different signs.

    ``sigma`` is used as an indicator of interactions between parameters, or
    groups of parameters.

    Compatible with:
        `morris` : :func:`SALib.sample.morris.sample`

    Examples
    --------
    >>> X = morris.sample(problem, 1000, num_levels=4)
    >>> Y = Ishigami.evaluate(X)
    >>> Si = morris.analyze(problem, X, Y, conf_level=0.95,
    >>>                     print_to_console=True, num_levels=4)


    Parameters
    ----------
    problem : dict
        The problem definition
    X : numpy.array
        The NumPy matrix containing the model inputs of dtype=float
    Y : numpy.array
        The NumPy array containing the model outputs of dtype=float
    scaled : bool, default=False
        If True, the elementary effects are scaled by the ratio of
        standard deviation of X and Y according to [3]
    num_resamples : int
        The number of resamples used to compute the confidence
        intervals (default 1000)
    conf_level : float
        The confidence interval level (default 0.95)
    print_to_console : bool
        Print results directly to console (default False)
    num_levels : int
        The number of grid levels, must be identical to the value
        passed to SALib.sample.morris (default 4)
    seed : int
        Seed to generate a random number

    Returns
    -------
    Si : dict
        A dictionary of sensitivity indices containing the following entries.

        - `mu` - the mean elementary effect
        - `mu_star` - the absolute of the mean elementary effect
        - `sigma` - the standard deviation of the elementary effect
        - `mu_star_conf` - the bootstrapped confidence interval
        - `names` - the names of the parameters


    References
    ----------
    1. Morris, M. (1991).
       Factorial Sampling Plans for Preliminary Computational Experiments.
       Technometrics, 33(2):161-174,
       doi:10.1080/00401706.1991.10484804.

    2. Campolongo, F., J. Cariboni, and A. Saltelli (2007).
       An effective screening design for sensitivity analysis
       of large models.
       Environmental Modelling & Software, 22(10):1509-1518,
       doi:10.1016/j.envsoft.2006.10.004.

    3. Sin and Gearney (2009)
       Improving the Morris Method for Sensitivity Analysis
       by Scaling the Elementary Effects.
       19th European Symposium on Computer Aided Process Engineering ESCAPE19:925-930

    4. Moret et al. (2017)
        Characterization of input uncertainties in strategic
        energy planning models.
        Applied Energy, Volume 202, 15 September 2017, Pages 597-617
        https://doi.org/10.1016/j.apenergy.2017.05.106
    """
def cli_parse(parser): ...
def cli_action(args) -> None: ...
