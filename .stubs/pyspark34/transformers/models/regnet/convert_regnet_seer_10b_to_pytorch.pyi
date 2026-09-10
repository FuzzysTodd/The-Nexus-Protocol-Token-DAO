import torch.nn as nn
from _typeshed import Incomplete
from classy_vision.models.regnet import RegNetParams
from dataclasses import dataclass
from pathlib import Path
from torch import Tensor as Tensor
from transformers import AutoFeatureExtractor as AutoFeatureExtractor, RegNetConfig as RegNetConfig, RegNetForImageClassification as RegNetForImageClassification, RegNetModel as RegNetModel
from transformers.modeling_utils import PreTrainedModel as PreTrainedModel
from transformers.utils import logging as logging
from typing import Dict, List

logger: Incomplete

@dataclass
class Tracker:
    module: nn.Module
    traced: List[nn.Module] = ...
    handles: list = ...
    name2module: Dict[str, nn.Module] = ...
    def __call__(self, x: Tensor): ...
    @property
    def parametrized(self): ...
    def __init__(self, module, traced, handles, name2module) -> None: ...

class FakeRegNetVisslWrapper(nn.Module):
    """
    Fake wrapper for RegNet that mimics what vissl does without the need to pass a config file.
    """
    def __init__(self, model: nn.Module) -> None: ...
    def forward(self, x: Tensor): ...

class FakeRegNetParams(RegNetParams):
    """
    Used to instantiace a RegNet model from classy vision with the same depth as the 10B one but with super small
    parameters, so we can trace it in memory.
    """
    def get_expanded_params(self): ...

def get_from_to_our_keys(model_name: str) -> Dict[str, str]:
    """
    Returns a dictionary that maps from original model's key -> our implementation's keys
    """
def convert_weights_and_push(save_directory: Path, model_name: str = None, push_to_hub: bool = True): ...
