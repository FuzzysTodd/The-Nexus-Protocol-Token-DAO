import optuna
from tensorflow.keras.callbacks import Callback
from typing import Any, Dict

Callback = object

class TFKerasPruningCallback(Callback):
    """tf.keras callback to prune unpromising trials.

    This callback is intend to be compatible for TensorFlow v1 and v2,
    but only tested with TensorFlow v2.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    tfkeras/tfkeras_integration.py>`__
    if you want to add a pruning callback which observes the validation accuracy.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of the
            objective function.
        monitor:
            An evaluation metric for pruning, e.g., ``val_loss`` or ``val_acc``.
    """
    def __init__(self, trial: optuna.trial.Trial, monitor: str) -> None: ...
    def on_epoch_end(self, epoch: int, logs: Dict[str, Any] | None = None) -> None: ...
