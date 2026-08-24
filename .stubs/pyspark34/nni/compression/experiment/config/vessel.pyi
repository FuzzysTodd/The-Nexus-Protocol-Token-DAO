import torch
from dataclasses import dataclass
from nni.algorithms.compression.v2.pytorch.utils.constructor_helper import OptimizerConstructHelper as OptimizerConstructHelper
from nni.common import dump as dump, load as load
from nni.experiment.config.base import ConfigBase as ConfigBase
from torch import Tensor as Tensor
from torch.nn import Module as Module
from torch.optim import Optimizer
from typing import Any, Callable, Tuple, overload

@dataclass(init=False)
class CompressionVessel(ConfigBase):
    """
    This is an internal class that helps serialize model-related parameters during model compression.

    # FIXME: In fact, it is not a `Config`, the only reason it is a `Config` right now is that its data attribute
    # will go into the search space as a single choice field. Need to refactor after the experiment config is stable.
    """
    model: str
    finetuner: str
    evaluator: str
    dummy_input: str
    trainer: str | None
    optimizer_helper: str | None
    criterion: str | None
    device: str
    @overload
    def __init__(self, model: str, finetuner: str, evaluator: str, dummy_input: str, trainer: str, optimizer_helper: str, criterion: str, device: str) -> None: ...
    @overload
    def __init__(self, model: Module, finetuner: Callable[[Module], None], evaluator: Callable[[Module], float], dummy_input: Tensor, trainer: Callable[[Module, Optimizer, Callable[[Any, Any], Any]], None] | None, optimizer_helper: Optimizer | OptimizerConstructHelper | None, criterion: Callable[[Any, Any], Any] | None, device: str | torch.device) -> None: ...
    def export(self) -> Tuple[Module, Callable[[Module], None], Callable[[Module], float], Tensor, Callable[[Module, Optimizer, Callable[[Any, Any], Any]], None] | None, OptimizerConstructHelper | None, Callable[[Any, Any], Any] | None, torch.device]: ...
    def json(self): ...
