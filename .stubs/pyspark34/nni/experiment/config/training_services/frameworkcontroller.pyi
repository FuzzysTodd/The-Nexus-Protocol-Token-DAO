from ..base import ConfigBase
from ..training_service import TrainingServiceConfig
from .k8s_storage import K8sStorageConfig
from dataclasses import dataclass
from typing import List
from typing_extensions import Literal

__all__ = ['FrameworkControllerConfig', 'FrameworkControllerRoleConfig', 'FrameworkAttemptCompletionPolicy']

@dataclass(init=False)
class FrameworkAttemptCompletionPolicy(ConfigBase):
    min_failed_task_count: int
    min_succeed_task_count: int

@dataclass(init=False)
class FrameworkControllerRoleConfig(ConfigBase):
    name: str
    docker_image: str = ...
    task_number: int
    command: str
    gpu_number: int
    cpu_number: int
    memory_size: str | int
    framework_attempt_completion_policy: FrameworkAttemptCompletionPolicy

@dataclass(init=False)
class FrameworkControllerConfig(TrainingServiceConfig):
    platform: Literal['frameworkcontroller'] = ...
    storage: K8sStorageConfig
    service_account_name: str | None
    task_roles: List[FrameworkControllerRoleConfig]
    reuse_mode: bool | None = ...
    namespace: str = ...
