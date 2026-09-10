from _typeshed import Incomplete
from transformers import DeiTConfig as DeiTConfig, DeiTFeatureExtractor as DeiTFeatureExtractor, DeiTForImageClassificationWithTeacher as DeiTForImageClassificationWithTeacher
from transformers.utils import logging as logging

logger: Incomplete

def create_rename_keys(config, base_model: bool = False): ...
def read_in_q_k_v(state_dict, config, base_model: bool = False) -> None: ...
def rename_key(dct, old, new) -> None: ...
def prepare_img(): ...
def convert_deit_checkpoint(deit_name, pytorch_dump_folder_path) -> None:
    """
    Copy/paste/tweak model's weights to our DeiT structure.
    """
