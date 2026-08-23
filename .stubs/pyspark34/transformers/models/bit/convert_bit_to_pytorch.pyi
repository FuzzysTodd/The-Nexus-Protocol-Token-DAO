from _typeshed import Incomplete
from transformers import BitConfig as BitConfig, BitForImageClassification as BitForImageClassification, BitImageProcessor as BitImageProcessor
from transformers.image_utils import PILImageResampling as PILImageResampling
from transformers.utils import logging as logging

logger: Incomplete

def get_config(model_name): ...
def rename_key(name): ...
def prepare_img(): ...
def convert_bit_checkpoint(model_name, pytorch_dump_folder_path, push_to_hub: bool = False) -> None:
    """
    Copy/paste/tweak model's weights to our BiT structure.
    """
