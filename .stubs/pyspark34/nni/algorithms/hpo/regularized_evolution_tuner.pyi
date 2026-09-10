from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.tuner import Tuner as Tuner
from nni.utils import OptimizeMode as OptimizeMode, extract_scalar_reward as extract_scalar_reward

logger: Incomplete

class FinishedIndividual:
    parameter_id: Incomplete
    parameters: Incomplete
    result: Incomplete
    def __init__(self, parameter_id, parameters, result) -> None:
        """
        Parameters
        ----------
        parameter_id: int
            the index of the parameter
        parameters : dict
            chosen architecture and parameters
        result : float
            final metric of the chosen one
        """

class EvolutionClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class RegularizedEvolutionTuner(Tuner):
    """
    RegularizedEvolutionTuner is tuner using Evolution NAS Tuner.
    See ``Regularized Evolution for Image Classifier Architecture Search`` for details.

    Parameters
    ---
    optimize_mode: str
        whether to maximize metric or not. default: 'maximize'
    population_size: int
        the maximum number of kept models
    sample_size: int
        the number of models chosen from population each time when evolution
    """
    optimize_mode: Incomplete
    population_size: Incomplete
    sample_size: Incomplete
    initial_population: Incomplete
    population: Incomplete
    history: Incomplete
    search_space: Incomplete
    def __init__(self, optimize_mode: str = 'maximize', population_size: int = 100, sample_size: int = 25) -> None: ...
    def generate_parameters(self, parameter_id, **kwargs):
        """
        This function will returns a dict of trial (hyper-)parameters, as a serializable object.

        Parameters
        ---
        parameter_id: int
            the index of current set of parameters
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
    def update_search_space(self, search_space) -> None:
        """
        Update search space.
        Search_space contains the information that user pre-defined.

        Parameters
        ----------
        search_space : dict
        """
    def trial_end(self, parameter_id, success, **kwargs) -> None: ...
