from _typeshed import Incomplete
from transformers import ConvNextConfig as ConvNextConfig, ConvNextFeatureExtractor as ConvNextFeatureExtractor, ConvNextForImageClassification as ConvNextForImageClassification
from transformers.utils import logging as logging

logger: Incomplete

def get_convnext_config(checkpoint_url): ...
def rename_key(name): ...
def prepare_img(): ...
def convert_convnext_checkpoint(checkpoint_url, pytorch_dump_folder_path) -> None:
    """
    Copy/paste/tweak model's weights to our ConvNext structure.
    """
