from .base import BaseStrategy as BaseStrategy
from nni.nas.oneshot.pytorch.strategy import DARTS as DARTS, ENAS as ENAS, GumbelDARTS as GumbelDARTS, Proxyless as Proxyless, RandomOneShot as RandomOneShot

class ImportFailedStrategy(BaseStrategy):
    def run(self, base_model, applied_mutators) -> None: ...
