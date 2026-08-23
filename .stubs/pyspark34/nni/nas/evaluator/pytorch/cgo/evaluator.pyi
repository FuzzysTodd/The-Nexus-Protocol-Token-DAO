import torch.nn as nn
import torch.optim as optim
import torchmetrics
from ..lightning import Lightning, LightningModule
from _typeshed import Incomplete
from torch.utils.data import DataLoader
from typing import Dict, List, Type

__all__ = ['_MultiModelSupervisedLearningModule', 'MultiModelSupervisedLearningModule', '_ClassificationModule', 'Classification', '_RegressionModule', 'Regression']

class _MultiModelSupervisedLearningModule(LightningModule):
    criterion: Incomplete
    criterion_cls: Incomplete
    optimizer: Incomplete
    metrics: Incomplete
    metrics_args: Incomplete
    n_models: Incomplete
    def __init__(self, criterion: Type[nn.Module], metrics: Dict[str, torchmetrics.Metric], n_models: int = 0, learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: optim.Optimizer = ...) -> None: ...
    def dump_kwargs(self): ...
    def forward(self, x): ...
    def training_step(self, batch, batch_idx): ...
    def validation_step(self, batch, batch_idx) -> None: ...
    def test_step(self, batch, batch_idx) -> None: ...
    def configure_optimizers(self): ...
    def on_validation_epoch_end(self) -> None: ...
    def teardown(self, stage) -> None: ...

class MultiModelSupervisedLearningModule(_MultiModelSupervisedLearningModule):
    """
    Lightning Module of SupervisedLearning for Cross-Graph Optimization.
    Users who needs cross-graph optimization should use this module.

    Parameters
    ----------
    criterion : nn.Module
        Class for criterion module (not an instance). default: ``nn.CrossEntropyLoss``
    learning_rate : float
        Learning rate. default: 0.001
    weight_decay : float
        L2 weight decay. default: 0
    optimizer : Optimizer
        Class for optimizer (not an instance). default: ``Adam``
    """
    def __init__(self, criterion: nn.Module, metrics: Dict[str, torchmetrics.Metric], learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: optim.Optimizer = ...) -> None: ...

class _ClassificationModule(_MultiModelSupervisedLearningModule):
    def __init__(self, criterion: nn.Module = ..., learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: optim.Optimizer = ...) -> None: ...

class Classification(Lightning):
    """
    Trainer that is used for classification.

    Parameters
    ----------
    criterion : nn.Module
        Class for criterion module (not an instance). default: ``nn.CrossEntropyLoss``
    learning_rate : float
        Learning rate. default: 0.001
    weight_decay : float
        L2 weight decay. default: 0
    optimizer : Optimizer
        Class for optimizer (not an instance). default: ``Adam``
    train_dataloders : DataLoader
        Used in ``trainer.fit()``. A PyTorch DataLoader with training samples.
        If the ``lightning_module`` has a predefined train_dataloader method this will be skipped.
    val_dataloaders : DataLoader or List of DataLoader
        Used in ``trainer.fit()``. Either a single PyTorch Dataloader or a list of them, specifying validation samples.
        If the ``lightning_module`` has a predefined val_dataloaders method this will be skipped.
    trainer_kwargs : dict
        Optional keyword arguments passed to trainer. See
        `Lightning documentation <https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html>`__ for details.
    """
    def __init__(self, criterion: Type[nn.Module] = ..., learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: optim.Optimizer = ..., train_dataloader: DataLoader | None = None, val_dataloaders: DataLoader | List[DataLoader] | None = None, **trainer_kwargs) -> None: ...

class _RegressionModule(_MultiModelSupervisedLearningModule):
    def __init__(self, criterion: Type[nn.Module] = ..., learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: optim.Optimizer = ...) -> None: ...

class Regression(Lightning):
    """
    Trainer that is used for regression.

    Parameters
    ----------
    criterion : nn.Module
        Class for criterion module (not an instance). default: ``nn.MSELoss``
    learning_rate : float
        Learning rate. default: 0.001
    weight_decay : float
        L2 weight decay. default: 0
    optimizer : Optimizer
        Class for optimizer (not an instance). default: ``Adam``
    train_dataloders : DataLoader
        Used in ``trainer.fit()``. A PyTorch DataLoader with training samples.
        If the ``lightning_module`` has a predefined train_dataloader method this will be skipped.
    val_dataloaders : DataLoader or List of DataLoader
        Used in ``trainer.fit()``. Either a single PyTorch Dataloader or a list of them, specifying validation samples.
        If the ``lightning_module`` has a predefined val_dataloaders method this will be skipped.
    trainer_kwargs : dict
        Optional keyword arguments passed to trainer. See
        `Lightning documentation <https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html>`__ for details.
    """
    def __init__(self, criterion: nn.Module = ..., learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: optim.Optimizer = ..., train_dataloader: DataLoader | None = None, val_dataloaders: DataLoader | List[DataLoader] | None = None, **trainer_kwargs) -> None: ...
