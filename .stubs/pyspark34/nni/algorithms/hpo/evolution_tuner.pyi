from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.tuner import Tuner as Tuner
from nni.utils import OptimizeMode as OptimizeMode, extract_scalar_reward as extract_scalar_reward, json2parameter as json2parameter, json2space as json2space, split_index as split_index

logger: Incomplete

class Individual:
    """
    Individual class to store the indv info.

    Parameters
    ----------
    config : str, default = None
        Search space.
    info : str, default = None
        The str to save information of individual.
    result : float, None = None
        The final metric of a individual.
    """
    config: Incomplete
    result: Incomplete
    info: Incomplete
    def __init__(self, config: Incomplete | None = None, info: Incomplete | None = None, result: Incomplete | None = None) -> None: ...

class EvolutionClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class EvolutionTuner(Tuner):
    """
    Naive Evolution comes from `Large-Scale Evolution of Image Classifiers <https://arxiv.org/pdf/1703.01041.pdf>`__
    It randomly initializes a population based on the search space.
    For each generation, it chooses better ones and does some mutation.
    (e.g., changes a hyperparameter, adds/removes one layer, etc.) on them to get the next generation.
    Naive Evolution requires many trials to works but it’s very simple and it’s easily expanded with new features.

    Examples
    --------

    .. code-block::

        config.tuner.name = 'Evolution'
        config.tuner.class_args = {
                'optimize_mode': 'maximize',
                'population_size': 100
        }

    Parameters
    ----------
    optimize_mode: str
        Optimize mode, 'maximize' or 'minimize'.
        If 'maximize', the tuner will try to maximize metrics. If 'minimize', the tuner will try to minimize metrics.
    population_size: int
        The initial size of the population (trial num) in the evolution tuner(default=32).
        The larger population size, the better evolution performance.
        It's suggested that ``population_size`` be much larger than ``concurrency`` so users can get the most out of the algorithm.
        And at least ``concurrency``, or the tuner will fail on its first generation of parameters.
    """
    optimize_mode: Incomplete
    population_size: Incomplete
    searchspace_json: Incomplete
    running_trials: Incomplete
    num_running_trials: int
    random_state: Incomplete
    population: Incomplete
    space: Incomplete
    credit: int
    send_trial_callback: Incomplete
    param_ids: Incomplete
    def __init__(self, optimize_mode: str = 'maximize', population_size: int = 32) -> None: ...
    def update_search_space(self, search_space) -> None:
        """
        Update search space.
        Search_space contains the information that user pre-defined.

        Parameters
        ----------

        search_space : dict
        """
    def trial_end(self, parameter_id, success, **kwargs) -> None:
        """
        To deal with trial failure. If a trial fails,
        random generate the parameters and add into the population.

        Parameters
        ----------

        parameter_id : int
            Unique identifier for hyper-parameters used by this trial.
        success : bool
            True if the trial successfully completed; False if failed or terminated.
        **kwargs
            Not used
        """
    def generate_multiple_parameters(self, parameter_id_list, **kwargs):
        """
        Returns multiple sets of trial (hyper-)parameters, as iterable of serializable objects.

        Parameters
        ----------

        parameter_id_list : list of int
            Unique identifiers for each set of requested hyper-parameters.
        **kwargs
            Not used

        Returns
        -------
        list
            A list of newly generated configurations
        """
    def generate_parameters(self, parameter_id, **kwargs):
        """
        This function will returns a dict of trial (hyper-)parameters.
        If no trial configration for now, self.credit plus 1 to send the config later

        Parameters
        ----------

        parameter_id : int

        Returns
        -------

        dict
            One newly generated configuration.
        """
    def receive_trial_result(self, parameter_id, parameters, value, **kwargs) -> None:
        '''
        Record the result from a trial

        Parameters
        ----------

        parameter_id : int
        parameters : dict
        value : dict/float
            if value is dict, it should have "default" key.
            value is final metrics of the trial.
        '''
    def import_data(self, data) -> None: ...
