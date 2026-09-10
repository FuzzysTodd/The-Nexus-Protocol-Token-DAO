from ..training_service import TrainingServiceConfig
from dataclasses import dataclass
from typing_extensions import Literal

__all__ = ['AmlConfig']

@dataclass(init=False)
class AmlConfig(TrainingServiceConfig):
    platform: Literal['aml'] = ...
    subscription_id: str
    resource_group: str
    workspace_name: str
    compute_target: str
    docker_image: str = ...
    max_trial_number_per_gpu: int = ...
