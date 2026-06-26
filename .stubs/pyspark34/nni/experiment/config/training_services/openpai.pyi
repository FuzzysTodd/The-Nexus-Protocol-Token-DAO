from ..training_service import TrainingServiceConfig
from ..utils import PathLike
from dataclasses import dataclass
from typing import Dict
from typing_extensions import Literal

__all__ = ['OpenpaiConfig']

@dataclass(init=False)
class OpenpaiConfig(TrainingServiceConfig):
    platform: Literal['openpai'] = ...
    host: str
    username: str
    token: str
    trial_cpu_number: int
    trial_memory_size: str | int
    storage_config_name: str
    docker_image: str = ...
    virtual_cluster: str | None
    local_storage_mount_point: PathLike
    container_storage_mount_point: str
    reuse_mode: bool = ...
    openpai_config: Dict | None = ...
    openpai_config_file: PathLike | None = ...
