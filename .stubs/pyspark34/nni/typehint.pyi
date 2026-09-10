from _typeshed import Incomplete
from typing import Any, Dict
from typing_extensions import TypedDict

__all__ = ['Parameters', 'SearchSpace', 'TrialMetric', 'TrialRecord']

Parameters = Dict[str, Any]

class _ParameterSearchSpace(TypedDict): ...

SearchSpace: Incomplete
TrialMetric = float

class TrialRecord(TypedDict):
    parameter: Parameters
    value: TrialMetric
