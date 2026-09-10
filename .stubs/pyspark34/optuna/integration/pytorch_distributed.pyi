import optuna
import torch
from datetime import datetime
from optuna._experimental import experimental as experimental
from optuna._imports import try_import as try_import
from optuna.distributions import BaseDistribution as BaseDistribution, CategoricalChoiceType as CategoricalChoiceType
from typing import Any, Dict, Sequence

class TorchDistributedTrial(optuna.trial.BaseTrial):
    '''A wrapper of :class:`~optuna.trial.Trial` to incorporate Optuna with PyTorch distributed.

    .. seealso::
        :class:`~optuna.integration.TorchDistributedTrial` provides the same interface as
        :class:`~optuna.trial.Trial`. Please refer to :class:`optuna.trial.Trial` for further
        details.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    pytorch/pytorch_distributed_simple.py>`__
    if you want to optimize an objective function that trains neural network
    written with PyTorch distributed data parallel.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` object or :obj:`None`. Please set trial object in
            rank-0 node and set :obj:`None` in the other rank node.
        device:
            A `torch.device` to communicate with the other nodes. Please set a CUDA device
            assigned to the current node if you use "nccl" as `torch.distributed` backend.

    .. note::
        The methods of :class:`~optuna.integration.TorchDistributedTrial` are expected to be
        called by all workers at once. They invoke synchronous data transmission to share
        processing results and synchronize timing.

    '''
    def __init__(self, trial: optuna.trial.Trial | None, device: torch.device | None = None) -> None: ...
    def suggest_float(self, name: str, low: float, high: float, *, step: float | None = None, log: bool = False) -> float: ...
    def suggest_uniform(self, name: str, low: float, high: float) -> float: ...
    def suggest_loguniform(self, name: str, low: float, high: float) -> float: ...
    def suggest_discrete_uniform(self, name: str, low: float, high: float, q: float) -> float: ...
    def suggest_int(self, name: str, low: int, high: int, step: int = 1, log: bool = False) -> int: ...
    def suggest_categorical(self, name: str, choices: Sequence['CategoricalChoiceType']) -> Any: ...
    def report(self, value: float, step: int) -> None: ...
    def should_prune(self) -> bool: ...
    def set_user_attr(self, key: str, value: Any) -> None: ...
    def set_system_attr(self, key: str, value: Any) -> None: ...
    @property
    def number(self) -> int: ...
    @property
    def params(self) -> Dict[str, Any]: ...
    @property
    def distributions(self) -> Dict[str, BaseDistribution]: ...
    @property
    def user_attrs(self) -> Dict[str, Any]: ...
    @property
    def system_attrs(self) -> Dict[str, Any]: ...
    @property
    def datetime_start(self) -> datetime | None: ...
