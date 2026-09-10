from collections.abc import Generator
from mlflow.entities import Metric as Metric, Param as Param
from mlflow.tracking import MlflowClient as MlflowClient

DISABLED: bool

def disable_pytorch_autologging() -> Generator[None, None, None]: ...
def patched_add_hparams(original, self, hparam_dict, metric_dict, *args, **kwargs):
    """use a synchronous call here since this is going to get called very infrequently."""
def patched_add_event(original, self, event, *args, mlflow_log_every_n_step, **kwargs): ...
def patched_add_summary(original, self, *args, **kwargs): ...
