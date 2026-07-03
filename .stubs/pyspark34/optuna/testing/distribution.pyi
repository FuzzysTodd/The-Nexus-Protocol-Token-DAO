from optuna.distributions import BaseDistribution as BaseDistribution

class UnsupportedDistribution(BaseDistribution):
    def single(self) -> bool: ...
