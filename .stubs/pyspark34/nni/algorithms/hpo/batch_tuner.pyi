from _typeshed import Incomplete
from nni.common.hpo_utils import validate_search_space as validate_search_space
from nni.tuner import Tuner as Tuner

TYPE: str
CHOICE: str
VALUE: str
LOGGER: Incomplete

class BatchTuner(Tuner):
    """
    Batch tuner is a special tuner that allows users to simply provide several hyperparameter sets,
    and it will evaluate each set.

    Batch tuner does **not** support standard search space.

    Search space of batch tuner looks like a single ``choice`` in standard search space,
    but it has different meaning.

    Consider following search space:

    .. code-block::

        'combine_params': {
            '_type': 'choice',
            '_value': [
                {'x': 0, 'y': 1},
                {'x': 1, 'y': 2},
                {'x': 1, 'y': 3},
            ]
        }

    Batch tuner will generate following 4 hyperparameter sets:

    1. {'x': 0, 'y': 1}
    2. {'x': 1, 'y': 2}
    3. {'x': 1, 'y': 3}

    If this search space was used with grid search tuner, it would instead generate:

    1. {'combine_params': {'x': 0, 'y': 1 }}
    2. {'combine_params': {'x': 1, 'y': 2 }}
    3. {'combine_params': {'x': 1, 'y': 3 }}

    Examples
    --------

    .. code-block::

        config.search_space = {
            'combine_params': {
                '_type': 'choice',
                '_value': [
                    {'optimizer': 'Adam', 'learning_rate': 0.001},
                    {'optimizer': 'Adam', 'learning_rate': 0.0001},
                    {'optimizer': 'Adam', 'learning_rate': 0.00001},
                    {'optimizer': 'SGD', 'learning_rate': 0.01},
                    {'optimizer': 'SGD', 'learning_rate': 0.005},
                ]
            }
        }
        config.tuner.name = 'Batch'
    """
    def __init__(self) -> None: ...
    def update_search_space(self, search_space) -> None: ...
    def generate_parameters(self, parameter_id, **kwargs): ...
    def receive_trial_result(self, parameter_id, parameters, value, **kwargs) -> None: ...
    def import_data(self, data) -> None: ...
