from ..training_service import TrainingServiceConfig
from dataclasses import dataclass
from typing_extensions import Literal

__all__ = ['DlcConfig']

@dataclass(init=False)
class DlcConfig(TrainingServiceConfig):
    platform: Literal['dlc'] = ...
    type: str = ...
    image: str
    job_type: str = ...
    pod_count: int
    ecs_spec: str
    region: str
    workspace_id: str
    nas_data_source_id: str
    oss_data_source_id: str | None = ...
    access_key_id: str
    access_key_secret: str
    local_storage_mount_point: str
    container_storage_mount_point: str
