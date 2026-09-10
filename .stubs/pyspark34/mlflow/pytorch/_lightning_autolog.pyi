import pytorch_lightning as pl
from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.utils.autologging_utils import BatchMetricsLogger as BatchMetricsLogger, ExceptionSafeAbstractClass as ExceptionSafeAbstractClass, MlflowAutologgingQueueingClient as MlflowAutologgingQueueingClient, get_autologging_config as get_autologging_config

MIN_REQ_VERSION: Incomplete
MAX_REQ_VERSION: Incomplete

class __MLflowPLCallback(pl.Callback, metaclass=ExceptionSafeAbstractClass):
    """
    Callback for auto-logging metrics and parameters.
    """
    early_stopping: bool
    client: Incomplete
    metrics_logger: Incomplete
    run_id: Incomplete
    log_models: Incomplete
    log_every_n_epoch: Incomplete
    log_every_n_step: Incomplete
    def __init__(self, client, metrics_logger, run_id, log_models, log_every_n_epoch, log_every_n_step) -> None: ...
    def on_train_epoch_end(self, trainer, pl_module, *args) -> None: ...
    def on_train_epoch_end(self, trainer, pl_module, *args) -> None:
        """
            Log loss and other metrics values after each train epoch

            :param trainer: pytorch lightning trainer instance
            :param pl_module: pytorch lightning base module
            """
    def on_validation_epoch_end(self, trainer, pl_module) -> None:
        """
            Log loss and other metrics values after each validation epoch

            :param trainer: pytorch lightning trainer instance
            :param pl_module: pytorch lightning base module
            """
    def on_epoch_end(self, trainer, pl_module) -> None:
        """
            Log loss and other metrics values after each epoch

            :param trainer: pytorch lightning trainer instance
            :param pl_module: pytorch lightning base module
            """
    def on_train_batch_end(self, trainer, pl_module, *args) -> None:
        """
        Log metric values after each step

        :param trainer: pytorch lightning trainer instance
        :param pl_module: pytorch lightning base module
        """
    def on_train_start(self, trainer, pl_module) -> None:
        """
        Logs Optimizer related metrics when the train begins

        :param trainer: pytorch lightning trainer instance
        :param pl_module: pytorch lightning base module
        """
    def on_train_end(self, trainer, pl_module) -> None:
        """
        Logs the model checkpoint into mlflow - models folder on the training end

        :param trainer: pytorch lightning trainer instance
        :param pl_module: pytorch lightning base module
        """
    def on_test_end(self, trainer, pl_module) -> None:
        """
        Logs accuracy and other relevant metrics on the testing end

        :param trainer: pytorch lightning trainer instance
        :param pl_module: pytorch lightning base module
        """

def patched_fit(original, self, *args, **kwargs):
    """
    A patched implementation of `pytorch_lightning.Trainer.fit` which enables logging the
    following parameters, metrics and artifacts:

    - Training epochs
    - Optimizer parameters
    - `EarlyStoppingCallback`_ parameters
    - Metrics stored in `trainer.callback_metrics`
    - Model checkpoints
    - Trained model

    .. _EarlyStoppingCallback:
        https://pytorch-lightning.readthedocs.io/en/latest/early_stopping.html
    """
