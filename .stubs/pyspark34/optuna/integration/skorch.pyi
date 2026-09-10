import optuna
from skorch.callbacks import Callback
from skorch.net import NeuralNet as NeuralNet
from typing import Any

Callback = object

class SkorchPruningCallback(Callback):
    """Skorch callback to prune unpromising trials.

    .. versionadded:: 2.1.0

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of the
            objective function.
        monitor:
            An evaluation metric for pruning, e.g. ``val_loss`` or
            ``val_acc``. The metrics are obtained from the returned dictionaries,
            i.e., ``net.histroy``. The names thus depend on how this dictionary
            is formatted.
    """
    def __init__(self, trial: optuna.trial.Trial, monitor: str) -> None: ...
    def on_epoch_end(self, net: NeuralNet, **kwargs: Any) -> None: ...
