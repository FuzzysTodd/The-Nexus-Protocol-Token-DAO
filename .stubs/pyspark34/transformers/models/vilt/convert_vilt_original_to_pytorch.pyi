from _typeshed import Incomplete
from transformers import BertTokenizer as BertTokenizer, ViltConfig as ViltConfig, ViltFeatureExtractor as ViltFeatureExtractor, ViltForImageAndTextRetrieval as ViltForImageAndTextRetrieval, ViltForImagesAndTextClassification as ViltForImagesAndTextClassification, ViltForMaskedLM as ViltForMaskedLM, ViltForQuestionAnswering as ViltForQuestionAnswering, ViltProcessor as ViltProcessor
from transformers.utils import logging as logging

logger: Incomplete

def create_rename_keys(config, vqa_model: bool = False, nlvr_model: bool = False, irtr_model: bool = False): ...
def read_in_q_k_v(state_dict, config) -> None: ...
def remove_classification_head_(state_dict) -> None: ...
def rename_key(dct, old, new) -> None: ...
def convert_vilt_checkpoint(checkpoint_url, pytorch_dump_folder_path) -> None:
    """
    Copy/paste/tweak model's weights to our ViLT structure.
    """
