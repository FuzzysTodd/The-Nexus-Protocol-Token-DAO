from _typeshed import Incomplete
from transformers import ProphetNetForConditionalGeneration as ProphetNetForConditionalGeneration, XLMProphetNetForConditionalGeneration as XLMProphetNetForConditionalGeneration, logging as logging

logger: Incomplete

def convert_prophetnet_checkpoint_to_pytorch(prophetnet_checkpoint_path: str, pytorch_dump_folder_path: str):
    """
    Copy/paste/tweak prohpetnet's weights to our prophetnet structure.
    """
