import torch
import torch.nn as nn
from ..interface import BaseOneShotTrainer as BaseOneShotTrainer
from .utils import AverageMeterGroup as AverageMeterGroup, replace_input_choice as replace_input_choice, replace_layer_choice as replace_layer_choice, to_device as to_device
from _typeshed import Incomplete

class ArchGradientFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, binary_gates, run_func, backward_func): ...
    @staticmethod
    def backward(ctx, grad_output): ...

class ProxylessLayerChoice(nn.Module):
    ops: Incomplete
    alpha: Incomplete
    sampled: Incomplete
    def __init__(self, ops) -> None: ...
    def forward(self, *args): ...
    def resample(self) -> None: ...
    def finalize_grad(self) -> None: ...
    def export(self): ...
    def export_prob(self): ...

class ProxylessInputChoice(nn.Module):
    def __init__(self, *args, **kwargs) -> None: ...

class HardwareLatencyEstimator:
    predictor_name: Incomplete
    latency_predictor: Incomplete
    block_latency_table: Incomplete
    def __init__(self, applied_hardware, model, dummy_input=(1, 3, 224, 224), dump_lat_table: str = 'data/latency_table.yaml') -> None: ...
    def cal_expected_latency(self, current_architecture_prob): ...
    def export_latency(self, current_architecture): ...

class ProxylessTrainer(BaseOneShotTrainer):
    '''
    Proxyless trainer.

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
    warmup_epochs : int
        Number of epochs to warmup model parameters.
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
    grad_reg_loss_type: string
        Regularization type to add hardware related loss, allowed types include
        - ``"mul#log"``: ``regularized_loss = (torch.log(expected_latency) / math.log(self.ref_latency)) ** beta``
        - ``"add#linear"``: ``regularized_loss = reg_lambda * (expected_latency - self.ref_latency) / self.ref_latency``
        - None: do not apply loss regularization.
    grad_reg_loss_params: dict
        Regularization params, allowed params include
        - ``"alpha"`` and ``"beta"`` is required when ``grad_reg_loss_type == "mul#log"``
        - ``"lambda"`` is required when ``grad_reg_loss_type == "add#linear"``
    applied_hardware: string
        Applied hardware for to constraint the model\'s latency. Latency is predicted by Microsoft
        nn-Meter (https://github.com/microsoft/nn-Meter).
    dummy_input: tuple
        The dummy input shape when applied to the target hardware.
    ref_latency: float
        Reference latency value in the applied hardware (ms).
    '''
    model: Incomplete
    loss: Incomplete
    metrics: Incomplete
    optimizer: Incomplete
    num_epochs: Incomplete
    warmup_epochs: Incomplete
    dataset: Incomplete
    batch_size: Incomplete
    workers: Incomplete
    device: Incomplete
    log_frequency: Incomplete
    latency_estimator: Incomplete
    reg_loss_type: Incomplete
    reg_loss_params: Incomplete
    ref_latency: Incomplete
    nas_modules: Incomplete
    ctrl_optim: Incomplete
    def __init__(self, model, loss, metrics, optimizer, num_epochs, dataset, warmup_epochs: int = 0, batch_size: int = 64, workers: int = 4, device: Incomplete | None = None, log_frequency: Incomplete | None = None, arc_learning_rate: float = 0.001, grad_reg_loss_type: Incomplete | None = None, grad_reg_loss_params: Incomplete | None = None, applied_hardware: Incomplete | None = None, dummy_input=(1, 3, 224, 224), ref_latency: float = 65.0) -> None: ...
    def fit(self) -> None: ...
    def export(self): ...
