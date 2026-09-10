from numpy import ndarray
from typing import Callable, NamedTuple

EPS: float

class _ParzenEstimatorParameters(NamedTuple('_ParzenEstimatorParameters', [('consider_prior', bool), ('prior_weight', float | None), ('consider_magic_clip', bool), ('consider_endpoints', bool), ('weights', Callable[[int], ndarray])])): ...

class _ParzenEstimator:
    def __init__(self, mus: ndarray, low: float, high: float, parameters: _ParzenEstimatorParameters) -> None: ...
