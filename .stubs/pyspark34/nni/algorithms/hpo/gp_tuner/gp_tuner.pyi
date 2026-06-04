from .target_space import TargetSpace as TargetSpace
from .util import UtilityFunction as UtilityFunction, acq_max as acq_max
from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.common.hpo_utils import validate_search_space as validate_search_space
from nni.tuner import Tuner as Tuner
from nni.utils import OptimizeMode as OptimizeMode, extract_scalar_reward as extract_scalar_reward

logger: Incomplete

class GPClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class GPTuner(Tuner):
    """
    GP tuner is a Bayesian Optimization method where Gaussian Process
    is used for modeling loss functions.

    Bayesian optimization works by constructing a posterior distribution of functions
    (a Gaussian Process) that best describes the function you want to optimize.
    As the number of observations grows, the posterior distribution improves,
    and the algorithm becomes more certain of which regions in parameter space
    are worth exploring and which are not.

    GP tuner is designed to minimize/maximize the number of steps required to find
    a combination of parameters that are close to the optimal combination.
    To do so, this method uses a proxy optimization problem (finding the maximum of
    the acquisition function) that, albeit still a hard problem, is cheaper
    (in the computational sense) to solve, and it's amenable to common tools.
    Therefore, Bayesian Optimization is suggested for situations where sampling the function
    to be optimized is very expensive.

    Note that the only acceptable types in the :doc:`search space </hpo/search_space>` are
    ``randint``, ``uniform``, ``quniform``, ``loguniform``, ``qloguniform``, and numerical ``choice``.

    This optimization approach is described in Section 3 of the paper
    `Algorithms for Hyper-Parameter Optimization <https://papers.nips.cc/paper/4443-algorithms-for-hyper-parameter-optimization.pdf>`__
    ( :footcite:t:`bergstra2011algorithms` ).

    Examples
    --------

    .. code-block::

        config.tuner.name = 'GP'
        config.tuner.class_args = {
            'optimize_mode': 'maximize',
            'utility': 'ei',
            'kappa': 5.0,
            'xi': 0.0,
            'nu': 2.5,
            'alpha': 1e-6,
            'cold_start_num': 10,
            'selection_num_warm_up': 100000,
            'selection_num_starting_points': 250
        }

    Parameters
    ----------
    optimize_mode : str
        Optimize mode, 'maximize' or 'minimize', by default 'maximize'
    utility : str
        Utility function (also called 'acquisition funcition') to use,
        which can be 'ei', 'ucb' or 'poi'. By default 'ei'.
    kappa : float
        Value used by utility function 'ucb'. The bigger kappa is,
        the more the tuner will be exploratory. By default 5.
    xi : float
        Used by utility function 'ei' and 'poi'. The bigger xi is,
        the more the tuner will be exploratory. By default 0.
    nu : float
        Used to specify Matern kernel. The smaller nu,
        the less smooth the approximated function is. By default 2.5.
    alpha : float
        Used to specify Gaussian Process Regressor.
        Larger values correspond to increased noise level in the observations.
        By default 1e-6.
    cold_start_num : int
        Number of random exploration to perform before Gaussian Process.
        By default 10.
    selection_num_warm_up : int
        Number of random points to evaluate for getting the point which
        maximizes the acquisition function. By default 100000
    selection_num_starting_points : int
        Number of times to run L-BFGS-B from a random starting point after the warmup.
        By default 250.
    """
    def __init__(self, optimize_mode: str = 'maximize', utility: str = 'ei', kappa: int = 5, xi: int = 0, nu: float = 2.5, alpha: float = 1e-06, cold_start_num: int = 10, selection_num_warm_up: int = 100000, selection_num_starting_points: int = 250) -> None: ...
    def update_search_space(self, search_space) -> None:
        """
        Update the self.bounds and self.types by the search_space.json file.

        Override of the abstract method in :class:`~nni.tuner.Tuner`.
        """
    def generate_parameters(self, parameter_id, **kwargs):
        """
        Method which provides one set of hyper-parameters.
        If the number of trial result is lower than cold_start_number, GPTuner will first randomly generate some parameters.
        Otherwise, choose the parameters by the Gussian Process Model.

        Override of the abstract method in :class:`~nni.tuner.Tuner`.
        """
    def receive_trial_result(self, parameter_id, parameters, value, **kwargs) -> None:
        """
        Method invoked when a trial reports its final result.

        Override of the abstract method in :class:`~nni.tuner.Tuner`.
        """
    def import_data(self, data) -> None:
        """
        Import additional data for tuning.

        Override of the abstract method in :class:`~nni.tuner.Tuner`.
        """
