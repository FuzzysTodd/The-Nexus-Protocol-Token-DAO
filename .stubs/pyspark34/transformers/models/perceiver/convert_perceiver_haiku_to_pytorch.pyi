from _typeshed import Incomplete
from transformers import PerceiverConfig as PerceiverConfig, PerceiverFeatureExtractor as PerceiverFeatureExtractor, PerceiverForImageClassificationConvProcessing as PerceiverForImageClassificationConvProcessing, PerceiverForImageClassificationFourier as PerceiverForImageClassificationFourier, PerceiverForImageClassificationLearned as PerceiverForImageClassificationLearned, PerceiverForMaskedLM as PerceiverForMaskedLM, PerceiverForMultimodalAutoencoding as PerceiverForMultimodalAutoencoding, PerceiverForOpticalFlow as PerceiverForOpticalFlow, PerceiverTokenizer as PerceiverTokenizer
from transformers.utils import logging as logging

logger: Incomplete

def prepare_img(): ...
def rename_keys(state_dict, architecture) -> None: ...
def convert_perceiver_checkpoint(pickle_file, pytorch_dump_folder_path, architecture: str = 'MLM') -> None:
    """
    Copy/paste/tweak model's weights to our Perceiver structure.
    """
