from _typeshed import Incomplete
from transformers import ConditionalDetrConfig as ConditionalDetrConfig, ConditionalDetrFeatureExtractor as ConditionalDetrFeatureExtractor, ConditionalDetrForObjectDetection as ConditionalDetrForObjectDetection, ConditionalDetrForSegmentation as ConditionalDetrForSegmentation
from transformers.utils import logging as logging

logger: Incomplete
rename_keys: Incomplete

def rename_key(state_dict, old, new) -> None: ...
def rename_backbone_keys(state_dict): ...
def read_in_q_k_v(state_dict, is_panoptic: bool = False) -> None: ...
def prepare_img(): ...
def convert_conditional_detr_checkpoint(model_name, pytorch_dump_folder_path) -> None:
    """
    Copy/paste/tweak model's weights to our CONDITIONAL_DETR structure.
    """
