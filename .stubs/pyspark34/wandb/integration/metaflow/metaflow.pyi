import pandas as pd
from _typeshed import Incomplete
from pathlib import Path as Path
from sklearn.base import BaseEstimator as BaseEstimator

def wandb_track(name: str, data: pd.DataFrame, datasets: bool = False, run: Incomplete | None = None, testing: bool = False, *args, **kwargs): ...

class ArtifactProxy:
    def __init__(self, flow) -> None: ...
    def __setattr__(self, key, val): ...
    def __getattr__(self, key): ...

def coalesce(*arg): ...
def wandb_log(func: Incomplete | None = None, datasets: bool = False, models: bool = False, others: bool = False, settings: Incomplete | None = None):
    """Automatically log parameters and artifacts to W&B by type dispatch.

    This decorator can be applied to a flow, step, or both.
    - Decorating a step will enable or disable logging for certain types within that step
    - Decorating the flow is equivalent to decorating all steps with a default
    - Decorating a step after decorating the flow will overwrite the flow decoration

    Arguments:
        func: (`Callable`). The method or class being decorated (if decorating a step or flow respectively).
        datasets: (`bool`). If `True`, log datasets.  Datasets can be a `pd.DataFrame` or `pathlib.Path`.  The default value is `False`, so datasets are not logged.
        models: (`bool`). If `True`, log models.  Models can be a `nn.Module` or `sklearn.base.BaseEstimator`.  The default value is `False`, so models are not logged.
        others: (`bool`). If `True`, log anything pickle-able.  The default value is `False`, so files are not logged.
        settings: (`wandb.sdk.wandb_settings.Settings`). Custom settings passed to `wandb.init`.  The default value is `None`, and is the same as passing `wandb.Settings()`.  If `settings.run_group` is `None`, it will be set to `{flow_name}/{run_id}.  If `settings.run_job_type` is `None`, it will be set to `{run_job_type}/{step_name}`
    """
