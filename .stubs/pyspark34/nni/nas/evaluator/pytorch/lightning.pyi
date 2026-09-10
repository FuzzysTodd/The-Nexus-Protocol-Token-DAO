import pytorch_lightning as pl
import torch.nn as nn
import torch.optim as optim
import torchmetrics
from _typeshed import Incomplete
from nni.nas.evaluator import Evaluator
from nni.typehint import Literal
from pathlib import Path
from typing import Any, Callable, Dict, List, Type

__all__ = ['LightningModule', 'Trainer', 'DataLoader', 'Lightning', 'Classification', 'Regression', 'SupervisedLearningModule', 'ClassificationModule', 'RegressionModule', 'AccuracyWithLogits']

class LightningModule(pl.LightningModule):
    """
    Basic wrapper of generated model.
    Lightning modules used in NNI should inherit this class.

    It's a subclass of ``pytorch_lightning.LightningModule``.
    See https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html
    """
    running_mode: Literal['multi', 'oneshot']
    model: Incomplete
    def set_model(self, model: Callable[[], nn.Module] | nn.Module) -> None:
        """Set the inner model (architecture) to train / evaluate.

        Parameters
        ----------
        model : callable or nn.Module
            Can be a callable returning nn.Module or nn.Module.
        """

Trainer: Incomplete
DataLoader: Incomplete

class Lightning(Evaluator):
    """
    Delegate the whole training to PyTorch Lightning.

    Since the arguments passed to the initialization needs to be serialized, ``LightningModule``, ``Trainer`` or
    ``DataLoader`` in this file should be used. Another option is to hide dataloader in the Lightning module, in
    which case, dataloaders are not required for this class to work.

    Following the programming style of Lightning, metrics sent to NNI should be obtained from ``callback_metrics``
    in trainer. Two hooks are added at the end of validation epoch and the end of ``fit``, respectively. The metric name
    and type depend on the specific task.

    .. warning::

       The Lightning evaluator are stateful. If you try to use a previous Lightning evaluator,
       please note that the inner ``lightning_module`` and ``trainer`` will be reused.

    Parameters
    ----------
    lightning_module
        Lightning module that defines the training logic.
    trainer
        Lightning trainer that handles the training.
    train_dataloders
        Used in ``trainer.fit()``. A PyTorch DataLoader with training samples.
        If the ``lightning_module`` has a predefined train_dataloader method this will be skipped.
        It can be `any types of dataloader supported by Lightning <https://pytorch-lightning.readthedocs.io/en/stable/guides/data.html>`__.
    val_dataloaders
        Used in ``trainer.fit()``. Either a single PyTorch Dataloader or a list of them, specifying validation samples.
        If the ``lightning_module`` has a predefined val_dataloaders method this will be skipped.
        It can be `any types of dataloader supported by Lightning <https://pytorch-lightning.readthedocs.io/en/stable/guides/data.html>`__.
    fit_kwargs
        Keyword arguments passed to ``trainer.fit()``.
    """
    module: Incomplete
    trainer: Incomplete
    train_dataloaders: Incomplete
    val_dataloaders: Incomplete
    fit_kwargs: Incomplete
    def __init__(self, lightning_module: LightningModule, trainer: Trainer, train_dataloaders: Any | None = None, val_dataloaders: Any | None = None, train_dataloader: Any | None = None, fit_kwargs: Dict[str, Any] | None = None) -> None: ...
    @property
    def train_dataloader(self) -> None: ...
    def __eq__(self, other): ...
    def fit(self, model):
        """
        Fit the model with provided dataloader, with Lightning trainer.
        If ``train_dataloaders`` is not provided, ``trainer.validate()`` will be called.

        Parameters
        ----------
        model : nn.Module
            The model to fit.
        """

class SupervisedLearningModule(LightningModule):
    trainer: pl.Trainer
    criterion: Incomplete
    optimizer: Incomplete
    metrics: Incomplete
    export_onnx: Incomplete
    def __init__(self, criterion: Type[nn.Module], metrics: Dict[str, Type[torchmetrics.Metric]], learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: Type[optim.Optimizer] = ..., export_onnx: Path | str | bool | None = None) -> None: ...
    def forward(self, x): ...
    def training_step(self, batch, batch_idx): ...
    def validation_step(self, batch, batch_idx) -> None: ...
    def test_step(self, batch, batch_idx) -> None: ...
    def configure_optimizers(self): ...
    def on_validation_epoch_end(self) -> None: ...
    def on_fit_end(self) -> None: ...
    def on_validation_end(self) -> None: ...

class AccuracyWithLogits(torchmetrics.Accuracy):
    def update(self, pred, target): ...

class ClassificationModule(SupervisedLearningModule):
    def __init__(self, criterion: Type[nn.Module] = ..., learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: Type[optim.Optimizer] = ..., export_onnx: bool = True) -> None: ...

class Classification(Lightning):
    """
    Evaluator that is used for classification.

    Available callback metrics in :class:`Classification` are:

    - train_loss
    - train_acc
    - val_loss
    - val_acc

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
    train_dataloaders : DataLoader
        Used in ``trainer.fit()``. A PyTorch DataLoader with training samples.
        If the ``lightning_module`` has a predefined train_dataloader method this will be skipped.
    val_dataloaders : DataLoader or List of DataLoader
        Used in ``trainer.fit()``. Either a single PyTorch Dataloader or a list of them, specifying validation samples.
        If the ``lightning_module`` has a predefined val_dataloaders method this will be skipped.
    export_onnx : bool
        If true, model will be exported to ``model.onnx`` before training starts. default true
    trainer_kwargs : dict
        Optional keyword arguments passed to trainer. See
        `Lightning documentation <https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html>`__ for details.

    Examples
    --------
    >>> evaluator = Classification()

    To use customized criterion and optimizer:

    >>> evaluator = Classification(nn.LabelSmoothingCrossEntropy, optimizer=torch.optim.SGD)

    Extra keyword arguments will be passed to trainer, some of which might be necessary to enable GPU acceleration:

    >>> evaluator = Classification(accelerator='gpu', devices=2, strategy='ddp')
    """
    def __init__(self, criterion: Type[nn.Module] = ..., learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: Type[optim.Optimizer] = ..., train_dataloaders: DataLoader | None = None, val_dataloaders: DataLoader | List[DataLoader] | None = None, export_onnx: bool = True, train_dataloader: DataLoader | None = None, **trainer_kwargs) -> None: ...

class RegressionModule(SupervisedLearningModule):
    def __init__(self, criterion: Type[nn.Module] = ..., learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: Type[optim.Optimizer] = ..., export_onnx: bool = True) -> None: ...

class Regression(Lightning):
    """
    Evaluator that is used for regression.

    Available callback metrics in :class:`Regression` are:

    - train_loss
    - train_mse
    - val_loss
    - val_mse

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
    train_dataloaders : DataLoader
        Used in ``trainer.fit()``. A PyTorch DataLoader with training samples.
        If the ``lightning_module`` has a predefined train_dataloader method this will be skipped.
    val_dataloaders : DataLoader or List of DataLoader
        Used in ``trainer.fit()``. Either a single PyTorch Dataloader or a list of them, specifying validation samples.
        If the ``lightning_module`` has a predefined val_dataloaders method this will be skipped.
    export_onnx : bool
        If true, model will be exported to ``model.onnx`` before training starts. default: true
    trainer_kwargs : dict
        Optional keyword arguments passed to trainer. See
        `Lightning documentation <https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html>`__ for details.

    Examples
    --------
    >>> evaluator = Regression()

    Extra keyword arguments will be passed to trainer, some of which might be necessary to enable GPU acceleration:

    >>> evaluator = Regression(gpus=1)
    """
    def __init__(self, criterion: Type[nn.Module] = ..., learning_rate: float = 0.001, weight_decay: float = 0.0, optimizer: Type[optim.Optimizer] = ..., train_dataloaders: DataLoader | None = None, val_dataloaders: DataLoader | List[DataLoader] | None = None, export_onnx: bool = True, train_dataloader: DataLoader | None = None, **trainer_kwargs) -> None: ...
