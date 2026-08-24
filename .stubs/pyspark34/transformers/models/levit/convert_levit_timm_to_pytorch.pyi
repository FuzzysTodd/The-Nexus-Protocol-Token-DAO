from _typeshed import Incomplete
from pathlib import Path
from transformers import LevitConfig as LevitConfig, LevitFeatureExtractor as LevitFeatureExtractor, LevitForImageClassificationWithTeacher as LevitForImageClassificationWithTeacher
from transformers.utils import logging as logging

logger: Incomplete

def convert_weight_and_push(hidden_sizes: int, name: str, config: LevitConfig, save_directory: Path, push_to_hub: bool = True): ...
def convert_weights_and_push(save_directory: Path, model_name: str = None, push_to_hub: bool = True): ...
