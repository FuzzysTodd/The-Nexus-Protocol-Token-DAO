from _typeshed import Incomplete
from transformers import UniSpeechConfig as UniSpeechConfig, UniSpeechForCTC as UniSpeechForCTC, UniSpeechForPreTraining as UniSpeechForPreTraining, Wav2Vec2FeatureExtractor as Wav2Vec2FeatureExtractor, Wav2Vec2PhonemeCTCTokenizer as Wav2Vec2PhonemeCTCTokenizer, Wav2Vec2Processor as Wav2Vec2Processor, logging as logging

logger: Incomplete
MAPPING: Incomplete
TOP_LEVEL_KEYS: Incomplete

def set_recursively(hf_pointer, key, value, full_name, weight_type, is_finetuned) -> None: ...
def recursively_load_weights(fairseq_model, hf_model, is_finetuned) -> None: ...
def load_conv_layer(full_name, value, feature_extractor, unused_weights, use_group_norm) -> None: ...
def convert_unispeech_checkpoint(checkpoint_path, pytorch_dump_folder_path, config_path: Incomplete | None = None, dict_path: Incomplete | None = None, is_finetuned: bool = True) -> None:
    """
    Copy/paste/tweak model's weights to transformers design.
    """
