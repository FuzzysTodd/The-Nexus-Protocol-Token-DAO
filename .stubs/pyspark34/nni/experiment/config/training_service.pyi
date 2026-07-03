from .base import ConfigBase
from .utils import PathLike
from dataclasses import dataclass

__all__ = ['TrainingServiceConfig']

@dataclass(init=False)
class TrainingServiceConfig(ConfigBase):
    """
    The base class of training service config classes.

    See ``LocalConfig`` for example usage.
    """
    platform: str
    trial_command: str
    trial_code_directory: PathLike
    trial_gpu_number: int | None
    nni_manager_ip: str | None
    debug: bool
