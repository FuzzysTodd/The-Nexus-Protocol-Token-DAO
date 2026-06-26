import fastai
import wandb
from _typeshed import Incomplete
from fastai.callbacks import TrackerCallback
from typing import Any, Literal

class WandbCallback(TrackerCallback):
    '''Callback for saving model topology, losses & metrics.

    Optionally logs weights, gradients, sample predictions and best trained model.

    Arguments:
        learn (fastai.basic_train.Learner): the fast.ai learner to hook.
        log (str): "gradients", "parameters", "all", or None. Losses & metrics are always logged.
        save_model (bool): save model at the end of each epoch. It will also load best model at the end of training.
        monitor (str): metric to monitor for saving best model. None uses default TrackerCallback monitor value.
        mode (str): "auto", "min" or "max" to compare "monitor" values and define best model.
        input_type (str): "images" or None. Used to display sample predictions.
        validation_data (list): data used for sample predictions if input_type is set.
        predictions (int): number of predictions to make if input_type is set and validation_data is None.
        seed (int): initialize random generator for sample predictions if input_type is set and validation_data is None.
    '''
    save_model: Incomplete
    model_path: Incomplete
    log: Incomplete
    input_type: Incomplete
    best: Incomplete
    validation_data: Incomplete
    def __init__(self, learn: fastai.basic_train.Learner, log: Literal['gradients', 'parameters', 'all'] | None = 'gradients', save_model: bool = True, monitor: str | None = None, mode: Literal['auto', 'min', 'max'] = 'auto', input_type: Literal['images'] | None = None, validation_data: list | None = None, predictions: int = 36, seed: int = 12345) -> None: ...
    def on_train_begin(self, **kwargs: Any) -> None:
        """Call watch method to log model topology, gradients & weights."""
    def on_epoch_end(self, epoch: int, smooth_loss: float, last_metrics: list, **kwargs: Any) -> None:
        """Log training loss, validation loss and custom metrics & log prediction samples & save model."""
    def on_train_end(self, **kwargs: Any) -> None:
        """Load the best model."""

class FastaiError(wandb.Error): ...
