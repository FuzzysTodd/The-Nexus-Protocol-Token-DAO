from ..interface import BaseOneShotTrainer as BaseOneShotTrainer
from .random import PathSamplingInputChoice as PathSamplingInputChoice, PathSamplingLayerChoice as PathSamplingLayerChoice
from .utils import AverageMeterGroup as AverageMeterGroup, replace_input_choice as replace_input_choice, replace_layer_choice as replace_layer_choice, to_device as to_device
from _typeshed import Incomplete
from nni.nas.oneshot.pytorch.enas import ReinforceController as ReinforceController, ReinforceField as ReinforceField

class EnasTrainer(BaseOneShotTrainer):
    '''
    ENAS trainer.

    Parameters
    ----------
    model : nn.Module
        PyTorch model to be trained.
    loss : callable
        Receives logits and ground truth label, return a loss tensor.
    metrics : callable
        Receives logits and ground truth label, return a dict of metrics.
    reward_function : callable
        Receives logits and ground truth label, return a tensor, which will be feeded to RL controller as reward.
    optimizer : Optimizer
        The optimizer used for optimizing the model.
    num_epochs : int
        Number of epochs planned for training.
    dataset : Dataset
        Dataset for training. Will be split for training weights and architecture weights.
    batch_size : int
        Batch size.
    workers : int
        Workers for data loading.
    device : torch.device
        ``torch.device("cpu")`` or ``torch.device("cuda")``.
    log_frequency : int
        Step count per logging.
    grad_clip : float
        Gradient clipping. Set to 0 to disable. Default: 5.
    entropy_weight : float
        Weight of sample entropy loss.
    skip_weight : float
        Weight of skip penalty loss.
    baseline_decay : float
        Decay factor of baseline. New baseline will be equal to ``baseline_decay * baseline_old + reward * (1 - baseline_decay)``.
    ctrl_lr : float
        Learning rate for RL controller.
    ctrl_steps_aggregate : int
        Number of steps that will be aggregated into one mini-batch for RL controller.
    ctrl_steps : int
        Number of mini-batches for each epoch of RL controller learning.
    ctrl_kwargs : dict
        Optional kwargs that will be passed to :class:`ReinforceController`.
    '''
    model: Incomplete
    loss: Incomplete
    metrics: Incomplete
    optimizer: Incomplete
    num_epochs: Incomplete
    dataset: Incomplete
    batch_size: Incomplete
    workers: Incomplete
    device: Incomplete
    log_frequency: Incomplete
    nas_modules: Incomplete
    nas_fields: Incomplete
    controller: Incomplete
    grad_clip: Incomplete
    reward_function: Incomplete
    ctrl_optim: Incomplete
    entropy_weight: Incomplete
    skip_weight: Incomplete
    baseline_decay: Incomplete
    baseline: float
    ctrl_steps_aggregate: Incomplete
    def __init__(self, model, loss, metrics, reward_function, optimizer, num_epochs, dataset, batch_size: int = 64, workers: int = 4, device: Incomplete | None = None, log_frequency: Incomplete | None = None, grad_clip: float = 5.0, entropy_weight: float = 0.0001, skip_weight: float = 0.8, baseline_decay: float = 0.999, ctrl_lr: float = 0.00035, ctrl_steps_aggregate: int = 20, ctrl_kwargs: Incomplete | None = None) -> None: ...
    train_loader: Incomplete
    valid_loader: Incomplete
    def init_dataloader(self) -> None: ...
    def fit(self) -> None: ...
    def export(self): ...
