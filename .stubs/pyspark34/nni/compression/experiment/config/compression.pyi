from .pruner import PrunerConfig
from .quantizer import QuantizerConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from nni.experiment.config import ExperimentConfig
from nni.experiment.config.base import ConfigBase
from torch.nn import Module
from typing import List, Type

__all__ = ['CompressionConfig', 'CompressionExperimentConfig']

@dataclass
class CompressionConfig(ConfigBase):
    """
    Attributes
    ----------
    params
        The upper bound of the ratio of remaining model parameters.
        E.g., 0.6 means at most 60% parameters are kept while 40% parameters are pruned.
    flops
        The upper bound of the ratio of remaining model flops.
        E.g., 0.6 means at most 60% flops are kept while 40% flops are pruned.
    metric
        The lower bound of the ratio of remaining model metric.
        Metric is the evaluator's return value, usually it is a float number representing the model accuracy.
        E.g., 0.9 means the compressed model should have at least 90% of the performance compared to the original model.
        This means that if the accuracy of the original model is 80%, then the accuracy of the compressed model should
        not be lower than 72% (0.9 * 80%).
    module_types
        The modules of the type in this list will be compressed.
    module_names
        The modules in this list will be compressed.
    exclude_module_names
        The modules in this list will not be compressed.
    pruners
        A list of `PrunerConfig`, possible pruner choices.
    quantizers
        A list of `QuantizerConfig`, possible quantizer choices.
    """
    params: str | int | float | None = ...
    flops: str | int | float | None = ...
    metric: float | None = ...
    module_types: List[Type[Module] | str] | None = ...
    module_names: List[str] | None = ...
    exclude_module_names: List[str] | None = ...
    pruners: List[PrunerConfig] | None = ...
    quantizers: List[QuantizerConfig] | None = ...
    def __init__(self, params, flops, metric, module_types, module_names, exclude_module_names, pruners, quantizers) -> None: ...

@dataclass(init=False)
class CompressionExperimentConfig(ExperimentConfig):
    compression_setting: CompressionConfig
    def __init__(self, training_service_platform: Incomplete | None = None, compression_setting: Incomplete | None = None, **kwargs) -> None: ...
