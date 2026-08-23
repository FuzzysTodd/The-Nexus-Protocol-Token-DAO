from _typeshed import Incomplete
from transformers import MobileNetV2Config as MobileNetV2Config, MobileNetV2ForImageClassification as MobileNetV2ForImageClassification, MobileNetV2ForSemanticSegmentation as MobileNetV2ForSemanticSegmentation, MobileNetV2ImageProcessor as MobileNetV2ImageProcessor, load_tf_weights_in_mobilenet_v2 as load_tf_weights_in_mobilenet_v2
from transformers.utils import logging as logging

logger: Incomplete

def get_mobilenet_v2_config(model_name): ...
def prepare_img(): ...
def convert_movilevit_checkpoint(model_name, checkpoint_path, pytorch_dump_folder_path, push_to_hub: bool = False) -> None:
    """
    Copy/paste/tweak model's weights to our MobileNetV2 structure.
    """
