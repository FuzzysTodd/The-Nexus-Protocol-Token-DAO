from _typeshed import Incomplete
from transformers import BertTokenizer as BertTokenizer, BlipConfig as BlipConfig, BlipForConditionalGeneration as BlipForConditionalGeneration, BlipForImageTextRetrieval as BlipForImageTextRetrieval, BlipForQuestionAnswering as BlipForQuestionAnswering

def load_demo_image(image_size, device): ...
def rename_key(key): ...
def convert_blip_checkpoint(pytorch_dump_folder_path, config_path: Incomplete | None = None) -> None:
    """
    Copy/paste/tweak model's weights to transformers design.
    """
