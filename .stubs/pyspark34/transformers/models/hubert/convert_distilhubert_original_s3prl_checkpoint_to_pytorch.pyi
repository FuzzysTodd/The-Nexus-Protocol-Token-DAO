from _typeshed import Incomplete
from transformers import HubertConfig as HubertConfig, HubertModel as HubertModel, Wav2Vec2FeatureExtractor as Wav2Vec2FeatureExtractor, logging as logging

logger: Incomplete
MAPPING: Incomplete

def set_recursively(hf_pointer, key, value, full_name, weight_type) -> None: ...
def recursively_load_weights(fairseq_model, hf_model) -> None: ...
def load_conv_layer(full_name, value, feature_extractor, unused_weights, use_group_norm) -> None: ...
def convert_config(model): ...
def convert_hubert_checkpoint(pytorch_dump_folder_path, config_path: Incomplete | None = None) -> None:
    """
    Copy/paste/tweak model's weights to transformers design.
    """
