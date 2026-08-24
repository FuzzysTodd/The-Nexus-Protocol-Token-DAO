import torch.nn as nn
from ..interface import BaseOneShotTrainer as BaseOneShotTrainer
from .utils import AverageMeterGroup as AverageMeterGroup, replace_input_choice as replace_input_choice, replace_layer_choice as replace_layer_choice, to_device as to_device
from _typeshed import Incomplete

class PathSamplingLayerChoice(nn.Module):
    """
    Mixed module, in which fprop is decided by exactly one or multiple (sampled) module.
    If multiple module is selected, the result will be sumed and returned.

    Attributes
    ----------
    sampled : int or list of int
        Sampled module indices.
    mask : tensor
        A multi-hot bool 1D-tensor representing the sampled mask.
    """
    op_names: Incomplete
    sampled: Incomplete
    def __init__(self, layer_choice) -> None: ...
    def forward(self, *args, **kwargs): ...
    def __len__(self) -> int: ...
    @property
    def mask(self): ...

class PathSamplingInputChoice(nn.Module):
    """
    Mixed input. Take a list of tensor as input, select some of them and return the sum.

    Attributes
    ----------
    sampled : int or list of int
        Sampled module indices.
    mask : tensor
        A multi-hot bool 1D-tensor representing the sampled mask.
    """
    n_candidates: Incomplete
    n_chosen: Incomplete
    sampled: Incomplete
    def __init__(self, input_choice) -> None: ...
    def forward(self, input_tensors): ...
    def __len__(self) -> int: ...
    @property
    def mask(self): ...

class SinglePathTrainer(BaseOneShotTrainer):
    '''
    Single-path trainer. Samples a path every time and backpropagates on that path.

    Parameters
    ----------
    model : nn.Module
        Model with mutables.
    loss : callable
        Called with logits and targets. Returns a loss tensor.
    metrics : callable
        Returns a dict that maps metrics keys to metrics data.
    optimizer : Optimizer
        Optimizer that optimizes the model.
    num_epochs : int
        Number of epochs of training.
    dataset_train : Dataset
        Dataset of training.
    dataset_valid : Dataset
        Dataset of validation.
    batch_size : int
        Batch size.
    workers: int
        Number of threads for data preprocessing. Not used for this trainer. Maybe removed in future.
    device : torch.device
        Device object. Either ``torch.device("cuda")`` or ``torch.device("cpu")``. When ``None``, trainer will
        automatic detects GPU and selects GPU first.
    log_frequency : int
        Number of mini-batches to log metrics.
    '''
    model: Incomplete
    loss: Incomplete
    metrics: Incomplete
    optimizer: Incomplete
    num_epochs: Incomplete
    dataset_train: Incomplete
    dataset_valid: Incomplete
    batch_size: Incomplete
    workers: Incomplete
    device: Incomplete
    log_frequency: Incomplete
    nas_modules: Incomplete
    train_loader: Incomplete
    valid_loader: Incomplete
    def __init__(self, model, loss, metrics, optimizer, num_epochs, dataset_train, dataset_valid, batch_size: int = 64, workers: int = 4, device: Incomplete | None = None, log_frequency: Incomplete | None = None) -> None: ...
    def fit(self) -> None: ...
    def export(self): ...
RandomTrainer = SinglePathTrainer
