from _typeshed import Incomplete
from transformers import PoolFormerConfig as PoolFormerConfig, PoolFormerFeatureExtractor as PoolFormerFeatureExtractor, PoolFormerForImageClassification as PoolFormerForImageClassification
from transformers.utils import logging as logging

logger: Incomplete

def replace_key_with_offset(key, offset, original_name, new_name):
    """
    Replaces the key by subtracting the offset from the original layer number
    """
def rename_keys(state_dict): ...
def prepare_img(): ...
def convert_poolformer_checkpoint(model_name, checkpoint_path, pytorch_dump_folder_path) -> None:
    """
    Copy/paste/tweak model's weights to our PoolFormer structure.
    """
