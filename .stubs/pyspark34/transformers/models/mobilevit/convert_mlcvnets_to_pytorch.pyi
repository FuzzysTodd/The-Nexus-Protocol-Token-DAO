from _typeshed import Incomplete
from transformers import MobileViTConfig as MobileViTConfig, MobileViTFeatureExtractor as MobileViTFeatureExtractor, MobileViTForImageClassification as MobileViTForImageClassification, MobileViTForSemanticSegmentation as MobileViTForSemanticSegmentation
from transformers.utils import logging as logging

logger: Incomplete

def get_mobilevit_config(mobilevit_name): ...
def rename_key(name, base_model: bool = False): ...
def convert_state_dict(orig_state_dict, model, base_model: bool = False): ...
def prepare_img(): ...
def convert_movilevit_checkpoint(mobilevit_name, checkpoint_path, pytorch_dump_folder_path, push_to_hub: bool = False) -> None:
    """
    Copy/paste/tweak model's weights to our MobileViT structure.
    """
