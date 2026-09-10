import optuna
from keras.callbacks import Callback
from optuna._deprecated import deprecated as deprecated
from typing import Dict

Callback = object

class KerasPruningCallback(Callback):
    """Keras callback to prune unpromising trials.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    keras/keras_integration.py>`__
    if you want to add a pruning callback which observes validation accuracy.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of the
            objective function.
        monitor:
            An evaluation metric for pruning, e.g., ``val_loss`` and
            ``val_accuracy``. Please refer to `keras.Callback reference
            <https://keras.io/callbacks/#callback>`_ for further details.
        interval:
            Check if trial should be pruned every n-th epoch. By default ``interval=1`` and
            pruning is performed after every epoch. Increase ``interval`` to run several
            epochs faster before applying pruning.
    """
    def __init__(self, trial: optuna.trial.Trial, monitor: str, interval: int = 1) -> None: ...
    def on_epoch_end(self, epoch: int, logs: Dict[str, float] | None = None) -> None: ...
