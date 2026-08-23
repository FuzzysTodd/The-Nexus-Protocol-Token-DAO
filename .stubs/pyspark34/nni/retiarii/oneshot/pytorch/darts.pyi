import torch.nn as nn
from ..interface import BaseOneShotTrainer as BaseOneShotTrainer
from .utils import AverageMeterGroup as AverageMeterGroup, replace_input_choice as replace_input_choice, replace_layer_choice as replace_layer_choice, to_device as to_device
from _typeshed import Incomplete
from collections.abc import Generator

class DartsLayerChoice(nn.Module):
    name: Incomplete
    op_choices: Incomplete
    alpha: Incomplete
    def __init__(self, layer_choice) -> None: ...
    def forward(self, *args, **kwargs): ...
    def parameters(self) -> Generator[Incomplete, None, None]: ...
    def named_parameters(self) -> Generator[Incomplete, None, None]: ...
    def export(self): ...

class DartsInputChoice(nn.Module):
    name: Incomplete
    alpha: Incomplete
    n_chosen: Incomplete
    def __init__(self, input_choice) -> None: ...
    def forward(self, inputs): ...
    def parameters(self) -> Generator[Incomplete, None, None]: ...
    def named_parameters(self) -> Generator[Incomplete, None, None]: ...
    def export(self): ...

class DartsTrainer(BaseOneShotTrainer):
    '''
    DARTS trainer.

    Parameters
    ----------
    model : nn.Module
        PyTorch model to be trained.
    loss : callable
        Receives logits and ground truth label, return a loss tensor.
    metrics : callable
        Receives logits and ground truth label, return a dict of metrics.
    optimizer : Optimizer
        The optimizer used for optimizing the model.
    num_epochs : int
        Number of epochs planned for training.
    dataset : Dataset
        Dataset for training. Will be split for training weights and architecture weights.
    grad_clip : float
        Gradient clipping. Set to 0 to disable. Default: 5.
    learning_rate : float
        Learning rate to optimize the model.
    batch_size : int
        Batch size.
    workers : int
        Workers for data loading.
    device : torch.device
        ``torch.device("cpu")`` or ``torch.device("cuda")``.
    log_frequency : int
        Step count per logging.
    arc_learning_rate : float
        Learning rate of architecture parameters.
    unrolled : float
        ``True`` if using second order optimization, else first order optimization.
    '''
    model: Incomplete
    loss: Incomplete
    metrics: Incomplete
    num_epochs: Incomplete
    dataset: Incomplete
    batch_size: Incomplete
    workers: Incomplete
    device: Incomplete
    log_frequency: Incomplete
    nas_modules: Incomplete
    model_optim: Incomplete
    ctrl_optim: Incomplete
    unrolled: Incomplete
    grad_clip: float
    def __init__(self, model, loss, metrics, optimizer, num_epochs, dataset, grad_clip: float = 5.0, learning_rate: float = 0.0025, batch_size: int = 64, workers: int = 4, device: Incomplete | None = None, log_frequency: Incomplete | None = None, arc_learning_rate: float = 0.0003, unrolled: bool = False) -> None: ...
    def fit(self) -> None: ...
    def export(self): ...
