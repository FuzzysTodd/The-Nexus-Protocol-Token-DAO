from _typeshed import Incomplete
from tensorflow.keras import callbacks
from typing import Any, Dict
from wandb.integration.keras.keras import patch_tf_keras as patch_tf_keras
from wandb.sdk.lib import telemetry as telemetry

LogStrategy: Incomplete

class WandbMetricsLogger(callbacks.Callback):
    '''Logger that sends system metrics to W&B.

    `WandbMetricsLogger` automatically logs the `logs` dictionary that callback methods
    take as argument to wandb.

    This callback automatically logs the following to a W&B run page:
    * system (CPU/GPU/TPU) metrics,
    * train and validation metrics defined in `model.compile`,
    * learning rate (both for a fixed value or a learning rate scheduler)

    Notes:
    If you resume training by passing `initial_epoch` to `model.fit` and you are using a
    learning rate scheduler, make sure to pass `initial_global_step` to
    `WandbMetricsLogger`. The `initial_global_step` is `step_size * initial_step`, where
    `step_size` is number of training steps per epoch. `step_size` can be calculated as
    the product of the cardinality of the training dataset and the batch size.

    Arguments:
        log_freq: ("epoch", "batch", or int) if "epoch", logs metrics
            at the end of each epoch. If "batch", logs metrics at the end
            of each batch. If an integer, logs metrics at the end of that
            many batches. Defaults to "epoch".
        initial_global_step: (int) Use this argument to correcly log the
            learning rate when you resume training from some `initial_epoch`,
            and a learning rate scheduler is used. This can be computed as
            `step_size * initial_step`. Defaults to 0.
    '''
    logging_batch_wise: Incomplete
    log_freq: Incomplete
    global_batch: int
    global_step: Incomplete
    def __init__(self, log_freq: LogStrategy | int = 'epoch', initial_global_step: int = 0, *args: Any, **kwargs: Any) -> None: ...
    def on_epoch_end(self, epoch: int, logs: Dict[str, Any] | None = None) -> None:
        """Called at the end of an epoch."""
    def on_batch_end(self, batch: int, logs: Dict[str, Any] | None = None) -> None: ...
    def on_train_batch_end(self, batch: int, logs: Dict[str, Any] | None = None) -> None:
        """Called at the end of a training batch in `fit` methods."""
