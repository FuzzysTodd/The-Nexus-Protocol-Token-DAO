from .base import DataCollector, EvaluatorBasedDataCollector, TrainerBasedDataCollector
from torch import Tensor
from typing import Dict, List

__all__ = ['TargetDataCollector', 'EvaluatorBasedTargetDataCollector', 'EvaluatorBasedHookDataCollector', 'WeightDataCollector', 'WeightTrainerBasedDataCollector', 'SingleHookTrainerBasedDataCollector']

class WeightDataCollector(DataCollector):
    """
    Collect all wrapper weights.
    """
    def reset(self) -> None: ...
    def collect(self) -> Dict[str, Dict[str, Tensor]]: ...

class WeightTrainerBasedDataCollector(TrainerBasedDataCollector):
    """
    Collect all wrapper weights after training or inference.
    """
    def collect(self) -> Dict[str, Dict[str, Tensor]]: ...

class SingleHookTrainerBasedDataCollector(TrainerBasedDataCollector):
    """
    Add hooks and collect data during training or inference.
    Single means each wrapper only has one hook to collect data.
    """
    def collect(self) -> Dict[str, Dict[str, List[Tensor]]]: ...

class TargetDataCollector(DataCollector):
    """
    Collect all wrapper targets.
    """
    def reset(self) -> None: ...
    def collect(self) -> Dict[str, Dict[str, Tensor]]: ...

class EvaluatorBasedTargetDataCollector(EvaluatorBasedDataCollector):
    """
    Collect all wrapper pruning target after training or inference.
    """
    def collect(self) -> Dict[str, Dict[str, Tensor]]: ...

class EvaluatorBasedHookDataCollector(EvaluatorBasedDataCollector):
    """
    Add hooks and collect data during training or inference.
    NOTE: Only support one target has one hook right now.
    """
    def collect(self) -> Dict[str, Dict[str, List]]: ...
