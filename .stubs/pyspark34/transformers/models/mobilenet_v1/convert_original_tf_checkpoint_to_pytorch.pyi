from _typeshed import Incomplete
from transformers import MobileNetV1Config as MobileNetV1Config, MobileNetV1FeatureExtractor as MobileNetV1FeatureExtractor, MobileNetV1ForImageClassification as MobileNetV1ForImageClassification, load_tf_weights_in_mobilenet_v1 as load_tf_weights_in_mobilenet_v1
from transformers.utils import logging as logging

logger: Incomplete

def get_mobilenet_v1_config(model_name): ...
def prepare_img(): ...
def convert_movilevit_checkpoint(model_name, checkpoint_path, pytorch_dump_folder_path, push_to_hub: bool = False) -> None:
    """
    Copy/paste/tweak model's weights to our MobileNetV1 structure.
    """
