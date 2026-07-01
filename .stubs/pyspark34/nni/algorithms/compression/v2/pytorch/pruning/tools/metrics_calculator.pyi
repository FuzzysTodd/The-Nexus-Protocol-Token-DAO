from ...utils import Scaling
from .base import MetricsCalculator
from _typeshed import Incomplete
from torch import Tensor
from typing import Dict, List

__all__ = ['NormMetricsCalculator', 'HookDataNormMetricsCalculator', 'DistMetricsCalculator', 'APoZRankMetricsCalculator', 'MeanRankMetricsCalculator', 'StraightMetricsCalculator']

class StraightMetricsCalculator(MetricsCalculator):
    """
    This metrics calculator directly returns a copy of data as metrics.
    """
    def calculate_metrics(self, data: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]: ...

class NormMetricsCalculator(MetricsCalculator):
    """
    Calculate the specify norm for each tensor in data.
    L1, L2, Level, Slim pruner use this to calculate metric.

    Parameters
    ----------
    p
        The order of norm. None means Frobenius norm.
    scalers
        Please view the base class `MetricsCalculator` docstring.
    """
    p: Incomplete
    def __init__(self, p: int | float | None = None, scalers: Dict[str, Dict[str, Scaling]] | Scaling | None = None) -> None: ...
    def calculate_metrics(self, data: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]: ...

class HookDataNormMetricsCalculator(NormMetricsCalculator):
    """
    The hook data value format is a two-element list [batch_number, cumulative_data].
    Directly use the cumulative_data as new_data to calculate norm metric.
    TaylorFO pruner uses this to calculate metric.
    """
    def calculate_metrics(self, data: Dict[str, Dict[str, List[Tensor]]]) -> Dict[str, Dict[str, Tensor]]: ...

class DistMetricsCalculator(MetricsCalculator):
    """
    Calculate the sum of specify distance for each element with all other elements in specify `dim` in each tensor in data.
    FPGM pruner uses this to calculate metric.

    Parameters
    ----------
    p
        The order of norm. None means Frobenius norm.
    scalers
        Please view the base class `MetricsCalculator` docstring.
    """
    p: Incomplete
    def __init__(self, p: int | float | None = None, scalers: Dict[str, Dict[str, Scaling]] | Scaling | None = None) -> None: ...
    def calculate_metrics(self, data: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]: ...

class APoZRankMetricsCalculator(MetricsCalculator):
    """
    The data value format is a two-element list [batch_number, batch_wise_zeros_count_sum].
    This metric sum the zero number on `dim` then devide the (batch_number * across_dim_size) to calculate the non-zero rate.
    Note that the metric we return is (1 - apoz), because we assume a higher metric value has higher importance.
    APoZRank pruner uses this to calculate metric.
    """
    def calculate_metrics(self, data: Dict[str, Dict[str, List[Tensor]]]) -> Dict[str, Dict[str, Tensor]]: ...

class MeanRankMetricsCalculator(MetricsCalculator):
    """
    The data value format is a two-element list [batch_number, batch_wise_activation_sum].
    This metric simply calculate the average on `self.dim`, then divide by the batch_number.
    MeanRank pruner uses this to calculate metric.
    """
    def calculate_metrics(self, data: Dict[str, Dict[str, List[Tensor]]]) -> Dict[str, Dict[str, Tensor]]: ...
