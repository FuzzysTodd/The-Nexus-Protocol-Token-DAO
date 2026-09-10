import torch.nn as nn
from _typeshed import Incomplete
from dataclasses import dataclass
from pathlib import Path
from torch import Tensor as Tensor
from transformers import AutoFeatureExtractor as AutoFeatureExtractor, ResNetConfig as ResNetConfig, ResNetForImageClassification as ResNetForImageClassification
from transformers.utils import logging as logging
from typing import List

logger: Incomplete

@dataclass
class Tracker:
    module: nn.Module
    traced: List[nn.Module] = ...
    handles: list = ...
    def __call__(self, x: Tensor): ...
    @property
    def parametrized(self): ...
    def __init__(self, module, traced, handles) -> None: ...

@dataclass
class ModuleTransfer:
    src: nn.Module
    dest: nn.Module
    verbose: int = ...
    src_skip: List = ...
    dest_skip: List = ...
    def __call__(self, x: Tensor):
        """
        Transfer the weights of `self.src` to `self.dest` by performing a forward pass using `x` as input. Under the
        hood we tracked all the operations in both modules.
        """
    def __init__(self, src, dest, verbose, src_skip, dest_skip) -> None: ...

def convert_weight_and_push(name: str, config: ResNetConfig, save_directory: Path, push_to_hub: bool = True): ...
def convert_weights_and_push(save_directory: Path, model_name: str = None, push_to_hub: bool = True): ...
