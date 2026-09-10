from . import parameter_expressions as parameter_expressions
from _typeshed import Incomplete
from enum import Enum

class OptimizeMode(Enum):
    """Optimize Mode class

    if OptimizeMode is 'minimize', it means the tuner need to minimize the reward
    that received from Trial.

    if OptimizeMode is 'maximize', it means the tuner need to maximize the reward
    that received from Trial.
    """
    Minimize: str
    Maximize: str

class NodeType:
    """Node Type class
    """
    ROOT: str
    TYPE: str
    VALUE: str
    INDEX: str
    NAME: str

class MetricType:
    """The types of metric data
    """
    FINAL: str
    PERIODICAL: str
    REQUEST_PARAMETER: str

def split_index(params):
    """
    Delete index infromation from params
    """
def extract_scalar_reward(value, scalar_key: str = 'default'):
    '''
    Extract scalar reward from trial result.

    Parameters
    ----------
    value : int, float, dict
        the reported final metric data
    scalar_key : str
        the key name that indicates the numeric number

    Raises
    ------
    RuntimeError
        Incorrect final result: the final result should be float/int,
        or a dict which has a key named "default" whose value is float/int.
    '''
def extract_scalar_history(trial_history, scalar_key: str = 'default'):
    '''
    Extract scalar value from a list of intermediate results.

    Parameters
    ----------
    trial_history : list
        accumulated intermediate results of a trial
    scalar_key : str
        the key name that indicates the numeric number

    Raises
    ------
    RuntimeError
        Incorrect final result: the final result should be float/int,
        or a dict which has a key named "default" whose value is float/int.
    '''
def convert_dict2tuple(value):
    """
    convert dict type to tuple to solve unhashable problem.
    NOTE: this function will change original data.
    """
def json2space(x, oldy: Incomplete | None = None, name=...):
    """
    Change search space from json format to hyperopt format

    """
def json2parameter(x, is_rand, random_state, oldy: Incomplete | None = None, Rand: bool = False, name=...):
    """
    Json to pramaters.

    """
def merge_parameter(base_params, override_params):
    """
    Update the parameters in ``base_params`` with ``override_params``.
    Can be useful to override parsed command line arguments.

    Parameters
    ----------
    base_params : namespace or dict
        Base parameters. A key-value mapping.
    override_params : dict or None
        Parameters to override. Usually the parameters got from ``get_next_parameters()``.
        When it is none, nothing will happen.

    Returns
    -------
    namespace or dict
        The updated ``base_params``. Note that ``base_params`` will be updated inplace. The return value is
        only for convenience.
    """

class ClassArgsValidator:
    """
    NNI tuners/assessors/adivisors accept a `classArgs` parameter in experiment configuration file.
    This ClassArgsValidator interface is used to validate the classArgs section in exeperiment
    configuration file.
    """
    def validate_class_args(self, **kwargs) -> None:
        """
        Validate the classArgs configuration in experiment configuration file.

        Parameters
        ----------
        kwargs: dict
            kwargs passed to tuner/assessor/advisor constructor

        Raises:
            Raise an execption if the kwargs is invalid.
        """
    def choices(self, key, *args):
        """
        Utility method to create a scheme to check whether the `key` is one of the `args`.

        Parameters:
        ----------
        key: str
            key name of the data to be validated
        args: list of str
            list of the choices

        Returns: Schema
        --------
            A scheme to check whether the `key` is one of the `args`.
        """
    def range(self, key, keyType, start, end):
        """
        Utility method to create a schema to check whether the `key` is in the range of [start, end].

        Parameters:
        ----------
        key: str
            key name of the data to be validated
        keyType: type
            python data type, such as int, float
        start: type is specified by keyType
            start of the range
        end: type is specified by keyType
            end of the range

        Returns: Schema
        --------
            A scheme to check whether the `key` is in the range of [start, end].
        """
    def path(self, key): ...
