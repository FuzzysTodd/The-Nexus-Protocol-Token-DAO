from ._binomtest import BinomTestResult as BinomTestResult
from ._fit import FitResult as FitResult
from ._hypotests import TukeyHSDResult as TukeyHSDResult
from ._odds_ratio import OddsRatioResult as OddsRatioResult
from ._relative_risk import RelativeRiskResult as RelativeRiskResult
from ._stats_py import PearsonRResult as PearsonRResult, TtestResult as TtestResult

__all__ = ['BinomTestResult', 'RelativeRiskResult', 'TukeyHSDResult', 'PearsonRResult', 'FitResult', 'OddsRatioResult', 'TtestResult']
