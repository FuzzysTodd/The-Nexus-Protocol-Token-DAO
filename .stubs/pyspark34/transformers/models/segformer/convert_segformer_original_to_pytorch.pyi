from _typeshed import Incomplete
from transformers import SegformerConfig as SegformerConfig, SegformerFeatureExtractor as SegformerFeatureExtractor, SegformerForImageClassification as SegformerForImageClassification, SegformerForSemanticSegmentation as SegformerForSemanticSegmentation
from transformers.utils import logging as logging

logger: Incomplete

def rename_keys(state_dict, encoder_only: bool = False): ...
def read_in_k_v(state_dict, config) -> None: ...
def prepare_img(): ...
def convert_segformer_checkpoint(model_name, checkpoint_path, pytorch_dump_folder_path) -> None:
    """
    Copy/paste/tweak model's weights to our SegFormer structure.
    """
