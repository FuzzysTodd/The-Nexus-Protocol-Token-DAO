from ..base import ConfigBase
from ..training_service import TrainingServiceConfig
from .k8s_storage import K8sStorageConfig
from dataclasses import dataclass
from typing_extensions import Literal

__all__ = ['KubeflowConfig', 'KubeflowRoleConfig']

@dataclass(init=False)
class KubeflowRoleConfig(ConfigBase):
    replicas: int
    command: str
    gpu_number: int | None = ...
    cpu_number: int
    memory_size: str | int
    docker_image: str = ...
    code_directory: str

@dataclass(init=False)
class KubeflowConfig(TrainingServiceConfig):
    platform: Literal['kubeflow'] = ...
    operator: str
    api_version: str
    storage: K8sStorageConfig
    worker: KubeflowRoleConfig | None = ...
    ps: KubeflowRoleConfig | None = ...
    master: KubeflowRoleConfig | None = ...
    reuse_mode: bool | None = ...
    namespace: str = ...
