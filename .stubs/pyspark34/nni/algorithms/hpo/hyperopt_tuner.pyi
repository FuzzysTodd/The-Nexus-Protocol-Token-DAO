from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.common.hpo_utils import validate_search_space as validate_search_space
from nni.tuner import Tuner as Tuner
from nni.utils import NodeType as NodeType, OptimizeMode as OptimizeMode, extract_scalar_reward as extract_scalar_reward, split_index as split_index

logger: Incomplete

def json2space(in_x, name=...):
    """
    Change json to search space in hyperopt.

    Parameters
    ----------
    in_x : dict/list/str/int/float
        The part of json.
    name : str
        name could be NodeType.ROOT, NodeType.TYPE, NodeType.VALUE or NodeType.INDEX, NodeType.NAME.
    """
def json2parameter(in_x, parameter, name=...):
    """
    Change json to parameters.
    """
def json2vals(in_x, vals, out_y, name=...) -> None: ...

class HyperoptClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class HyperoptTuner(Tuner):
    """
    NNI wraps `hyperopt <https://github.com/hyperopt/hyperopt>`__ to provide anneal tuner.

    This simple annealing algorithm begins by sampling from the prior
    but tends over time to sample from points closer and closer to the best ones observed.
    This algorithm is a simple variation of random search that leverages smoothness in the response surface.
    The annealing rate is not adaptive.

    Note that it needs additional installation using the following command:

    .. code-block:: bash

        pip install nni[Anneal]

    Examples
    --------

    .. code-block::

        config.tuner.name = 'Anneal'
        config.tuner.class_args = {
            'optimize_mode': 'minimize'
        }

    Parameters
    ----------
    optimze_mode: 'minimize' or 'maximize'
        Whether optimize to minimize or maximize trial result.
    """
    algorithm_name: Incomplete
    optimize_mode: Incomplete
    json: Incomplete
    total_data: Incomplete
    rval: Incomplete
    supplement_data_num: int
    parallel: Incomplete
    CL_rval: Incomplete
    constant_liar_type: Incomplete
    running_data: Incomplete
    optimal_y: Incomplete
    def __init__(self, algorithm_name, optimize_mode: str = 'minimize', parallel_optimize: bool = False, constant_liar_type: str = 'min') -> None: ...
    def update_search_space(self, search_space) -> None: ...
    def generate_parameters(self, parameter_id, **kwargs): ...
    def receive_trial_result(self, parameter_id, parameters, value, **kwargs) -> None: ...
    def import_data(self, data) -> None: ...
