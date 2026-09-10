from _typeshed import Incomplete
from transformers import Wav2Vec2CTCTokenizer as Wav2Vec2CTCTokenizer, Wav2Vec2ConformerConfig as Wav2Vec2ConformerConfig, Wav2Vec2ConformerForCTC as Wav2Vec2ConformerForCTC, Wav2Vec2ConformerForPreTraining as Wav2Vec2ConformerForPreTraining, Wav2Vec2FeatureExtractor as Wav2Vec2FeatureExtractor, Wav2Vec2Processor as Wav2Vec2Processor, logging as logging

logger: Incomplete
MAPPING: Incomplete
TOP_LEVEL_KEYS: Incomplete

def set_recursively(hf_pointer, key, value, full_name, weight_type) -> None: ...
def recursively_load_weights(fairseq_model, hf_model, is_headless) -> None: ...
def load_conv_layer(full_name, value, feature_extractor, unused_weights, use_group_norm) -> None: ...
def convert_wav2vec2_conformer_checkpoint(checkpoint_path, pytorch_dump_folder_path, config_path: Incomplete | None = None, dict_path: Incomplete | None = None, is_finetuned: bool = True) -> None:
    """
    Copy/paste/tweak model's weights to transformers design.
    """
