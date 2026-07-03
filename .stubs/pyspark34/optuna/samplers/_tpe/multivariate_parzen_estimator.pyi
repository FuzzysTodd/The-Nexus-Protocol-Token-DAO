import numpy as np
from optuna import distributions as distributions
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.samplers._tpe.parzen_estimator import _ParzenEstimatorParameters
from typing import Dict

EPS: float
SIGMA0_MAGNITUDE: float

class _MultivariateParzenEstimator:
    def __init__(self, multivariate_observations: Dict[str, np.ndarray], search_space: Dict[str, BaseDistribution], parameters: _ParzenEstimatorParameters) -> None: ...
    def sample(self, rng: np.random.RandomState, size: int) -> Dict[str, np.ndarray]: ...
    def log_pdf(self, multivariate_samples: Dict[str, np.ndarray]) -> np.ndarray: ...
