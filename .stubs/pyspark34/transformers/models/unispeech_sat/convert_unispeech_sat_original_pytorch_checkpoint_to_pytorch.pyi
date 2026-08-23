from _typeshed import Incomplete
from transformers import UniSpeechSatConfig as UniSpeechSatConfig, UniSpeechSatForCTC as UniSpeechSatForCTC, UniSpeechSatForPreTraining as UniSpeechSatForPreTraining, logging as logging

logger: Incomplete
MAPPING: Incomplete
TOP_LEVEL_KEYS: Incomplete

def set_recursively(hf_pointer, key, value, full_name, weight_type) -> None: ...
def recursively_load_weights(fairseq_model, hf_model) -> None: ...
def load_conv_layer(full_name, value, feature_extractor, unused_weights, use_group_norm) -> None: ...
def convert_unispeech_sat_checkpoint(checkpoint_path, pytorch_dump_folder_path, config_path: Incomplete | None = None, dict_path: Incomplete | None = None, is_finetuned: bool = True) -> None:
    """
    Copy/paste/tweak model's weights to transformers design.
    """
