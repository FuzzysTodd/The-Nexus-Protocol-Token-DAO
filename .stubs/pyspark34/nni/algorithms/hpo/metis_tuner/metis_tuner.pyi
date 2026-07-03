from . import lib_constraint_summation as lib_constraint_summation, lib_data as lib_data
from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.common.hpo_utils import validate_search_space as validate_search_space
from nni.tuner import Tuner as Tuner
from nni.utils import OptimizeMode as OptimizeMode, extract_scalar_reward as extract_scalar_reward

logger: Incomplete
NONE_TYPE: str
CONSTRAINT_LOWERBOUND: Incomplete
CONSTRAINT_UPPERBOUND: Incomplete
CONSTRAINT_PARAMS_IDX: Incomplete

class MetisClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class MetisTuner(Tuner):
    '''
    `Metis tuner <https://www.microsoft.com/en-us/research/publication/metis-robustly-tuning-tail-latencies-cloud-systems/>`__ offers
    several benefits over other tuning algorithms.
    While most tools only predict the optimal configuration, Metis gives you two outputs,
    a prediction for the optimal configuration and a suggestion for the next trial.
    No more guess work!

    While most tools assume training datasets do not have noisy data,
    Metis actually tells you if you need to resample a particular hyper-parameter.

    While most tools have problems of being exploitation-heavy,
    Metis\' search strategy balances exploration, exploitation, and (optional) resampling.

    Metis belongs to the class of sequential model-based optimization (SMBO) algorithms
    and it is based on the Bayesian Optimization framework. To model the parameter-vs-performance space,
    Metis uses both a Gaussian Process and GMM. Since each trial can impose a high time cost,
    Metis heavily trades inference computations with naive trials.
    At each iteration, Metis does two tasks (refer to :footcite:t:`li2018metis` for details):


    1. It finds the global optimal point in the Gaussian Process space.
       This point represents the optimal configuration.

    2. It identifies the next hyper-parameter candidate.
       This is achieved by inferring the potential information gain of
       exploration, exploitation, and resampling.

    Note that the only acceptable types in the :doc:`search space </hpo/search_space>` are
    ``quniform``, ``uniform``, ``randint``, and numerical ``choice``.


    Examples
    --------

    .. code-block::

        config.tuner.name = \'Metis\'
        config.tuner.class_args = {
            \'optimize_mode\': \'maximize\'
        }

    Parameters
    ----------
    optimize_mode : str
        optimize_mode is a string that including two mode "maximize" and "minimize"

    no_resampling : bool
        True or False.
        Should Metis consider re-sampling as part of the search strategy?
        If you are confident that the training dataset is noise-free,
        then you do not need re-sampling.

    no_candidates : bool
        True or False.
        Should Metis suggest parameters for the next benchmark?
        If you do not plan to do more benchmarks,
        Metis can skip this step.

    selection_num_starting_points : int
        How many times Metis should try to find the global optimal in the search space?
        The higher the number, the longer it takes to output the solution.

    cold_start_num : int
        Metis need some trial result to get cold start.
        when the number of trial result is less than
        cold_start_num, Metis will randomly sample hyper-parameter for trial.

    exploration_probability: float
        The probability of Metis to select parameter from exploration instead of exploitation.
    '''
    samples_x: Incomplete
    samples_y: Incomplete
    samples_y_aggregation: Incomplete
    total_data: Incomplete
    space: Incomplete
    no_resampling: Incomplete
    no_candidates: Incomplete
    optimize_mode: Incomplete
    key_order: Incomplete
    cold_start_num: Incomplete
    selection_num_starting_points: Incomplete
    exploration_probability: Incomplete
    minimize_constraints_fun: Incomplete
    minimize_starting_points: Incomplete
    supplement_data_num: int
    x_bounds: Incomplete
    x_types: Incomplete
    def __init__(self, optimize_mode: str = 'maximize', no_resampling: bool = True, no_candidates: bool = False, selection_num_starting_points: int = 600, cold_start_num: int = 10, exploration_probability: float = 0.9) -> None: ...
    def update_search_space(self, search_space) -> None:
        """
        Update the self.x_bounds and self.x_types by the search_space.json

        Parameters
        ----------
        search_space : dict
        """
    def generate_parameters(self, parameter_id, **kwargs):
        """
        Generate next parameter for trial

        If the number of trial result is lower than cold start number,
        metis will first random generate some parameters.
        Otherwise, metis will choose the parameters by
        the Gussian Process Model and the Gussian Mixture Model.

        Parameters
        ----------
        parameter_id : int

        Returns
        -------
        result : dict
        """
    def receive_trial_result(self, parameter_id, parameters, value, **kwargs) -> None:
        '''
        Tuner receive result from trial.

        Parameters
        ----------
        parameter_id : int
            The id of parameters, generated by nni manager.
        parameters : dict
            A group of parameters that trial has tried.
        value : dict/float
            if value is dict, it should have "default" key.
        '''
    def import_data(self, data) -> None:
        """
        Import additional data for tuning

        Parameters
        ----------
        data : a list of dict
               each of which has at least two keys: 'parameter' and 'value'.
        """

def get_median(temp_list):
    """
    Return median
    """
