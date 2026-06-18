from _typeshed import Incomplete
from transformers import RobertaTokenizer as RobertaTokenizer, TrOCRConfig as TrOCRConfig, TrOCRForCausalLM as TrOCRForCausalLM, TrOCRProcessor as TrOCRProcessor, ViTConfig as ViTConfig, ViTFeatureExtractor as ViTFeatureExtractor, ViTModel as ViTModel, VisionEncoderDecoderModel as VisionEncoderDecoderModel
from transformers.utils import logging as logging

logger: Incomplete

def create_rename_keys(encoder_config, decoder_config): ...
def read_in_q_k_v(state_dict, encoder_config) -> None: ...
def rename_key(dct, old, new) -> None: ...
def prepare_img(checkpoint_url): ...
def convert_tr_ocr_checkpoint(checkpoint_url, pytorch_dump_folder_path) -> None:
    """
    Copy/paste/tweak model's weights to our VisionEncoderDecoderModel structure.
    """
