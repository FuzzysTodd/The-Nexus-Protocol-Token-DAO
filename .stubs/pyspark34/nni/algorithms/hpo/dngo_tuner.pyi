from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.common.hpo_utils import validate_search_space as validate_search_space
from nni.tuner import Tuner as Tuner

class DNGOTuner(Tuner):
    """
    Use neural networks as an alternative to GPs to model distributions over functions in bayesian optimization.

    Parameters
    ----------
    optimize : maximize | minimize, default = maximize
        If 'maximize', the tuner will target to maximize metrics. If 'minimize', the tuner will target to minimize metrics.
    sample_size : int, default = 1000
        Number of samples to select in each iteration. The best one will be picked from the samples as the next trial.
    trials_per_update : int, default = 20
        Number of trials to collect before updating the model.
    num_epochs_per_training : int, default = 500
        Number of epochs to train DNGO model.
    """
    searchspace_json: Incomplete
    random_state: Incomplete
    model: Incomplete
    sample_size: Incomplete
    trials_per_update: Incomplete
    optimize_mode: Incomplete
    x: Incomplete
    y: Incomplete
    def __init__(self, optimize_mode: str = 'maximize', sample_size: int = 1000, trials_per_update: int = 20, num_epochs_per_training: int = 500) -> None: ...
    def receive_trial_result(self, parameter_id, parameters, value, **kwargs) -> None: ...
    def generate_parameters(self, parameter_id, **kwargs): ...
    def update_search_space(self, search_space) -> None: ...
    def import_data(self, data) -> None: ...

class DNGOClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...
