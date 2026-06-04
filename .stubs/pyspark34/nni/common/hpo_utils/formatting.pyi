from nni.typehint import Parameters, SearchSpace
from typing import Any, NamedTuple

__all__ = ['ParameterSpec', 'deformat_parameters', 'format_parameters', 'format_search_space']

class ParameterSpec(NamedTuple):
    """
    Specification (aka space / range / domain) of one single parameter.

    NOTE: For `loguniform` (and `qloguniform`), the fields `low` and `high` are logarithm of original values.
    """
    name: str
    type: str
    values: list[Any]
    key: ParameterKey
    categorical: bool
    size: int = ...
    chosen_size: int | None = ...
    low: float = ...
    high: float = ...
    normal_distributed: bool = ...
    mu: float = ...
    sigma: float = ...
    q: float | None = ...
    clip: tuple[float, float] | None = ...
    log_distributed: bool = ...
    def is_activated_in(self, partial_parameters: FormattedParameters) -> bool:
        """
        For nested search space, check whether this parameter should be skipped for current set of paremters.
        This function must be used in a pattern similar to random tuner. Otherwise it will misbehave.
        """
    def is_nested(self):
        """
        Check whether this parameter is inside a nested choice.
        """

def format_search_space(search_space: SearchSpace) -> FormattedSearchSpace:
    """
    Convert user provided search space into a dict of ParameterSpec.
    The dict key is dict value's `ParameterSpec.key`.
    """
def deformat_parameters(formatted_parameters: FormattedParameters, formatted_search_space: FormattedSearchSpace) -> Parameters:
    '''
    Convert internal format parameters to users\' expected format.

    "test/ut/sdk/test_hpo_formatting.py" provides examples of how this works.

    The function do following jobs:
     1. For "choice" and "randint", convert index (integer) to corresponding value.
     2. For "*log*", convert x to `exp(x)`.
     3. For "q*", convert x to `round(x / q) * q`, then clip into range.
     4. For nested choices, convert flatten key-value pairs into nested structure.
    '''
def format_parameters(parameters: Parameters, formatted_search_space: FormattedSearchSpace) -> FormattedParameters:
    '''
    Convert end users\' parameter format back to internal format, mainly for resuming experiments.

    The result is not accurate for "q*" and for "choice" that have duplicate candidates.
    '''
