from _typeshed import Incomplete
from transformers import BeitConfig as BeitConfig, BeitFeatureExtractor as BeitFeatureExtractor, BeitForImageClassification as BeitForImageClassification, BeitForMaskedImageModeling as BeitForMaskedImageModeling, BeitForSemanticSegmentation as BeitForSemanticSegmentation
from transformers.image_utils import PILImageResampling as PILImageResampling
from transformers.utils import logging as logging

logger: Incomplete

def create_rename_keys(config, has_lm_head: bool = False, is_semantic: bool = False): ...
def read_in_q_k_v(state_dict, config, has_lm_head: bool = False, is_semantic: bool = False) -> None: ...
def rename_key(dct, old, new) -> None: ...
def prepare_img(): ...
def convert_beit_checkpoint(checkpoint_url, pytorch_dump_folder_path) -> None:
    """
    Copy/paste/tweak model's weights to our BEiT structure.
    """
