import optuna
from _typeshed import Incomplete
from pytorch_lightning import LightningModule, Trainer
from pytorch_lightning.callbacks import Callback

Callback = object
LightningModule = object
Trainer = object

class PyTorchLightningPruningCallback(Callback):
    """PyTorch Lightning callback to prune unpromising trials.

    See `the example <https://github.com/optuna/optuna-examples/blob/
    main/pytorch/pytorch_lightning_simple.py>`__
    if you want to add a pruning callback which observes accuracy.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of the
            objective function.
        monitor:
            An evaluation metric for pruning, e.g., ``val_loss`` or
            ``val_acc``. The metrics are obtained from the returned dictionaries from e.g.
            ``pytorch_lightning.LightningModule.training_step`` or
            ``pytorch_lightning.LightningModule.validation_epoch_end`` and the names thus depend on
            how this dictionary is formatted.
    """
    monitor: Incomplete
    def __init__(self, trial: optuna.trial.Trial, monitor: str) -> None: ...
    def on_validation_end(self, trainer: Trainer, pl_module: LightningModule) -> None: ...
