from _typeshed import Incomplete
from transformers import ASTConfig as ASTConfig, ASTFeatureExtractor as ASTFeatureExtractor, ASTForAudioClassification as ASTForAudioClassification
from transformers.utils import logging as logging

logger: Incomplete

def get_audio_spectrogram_transformer_config(model_name): ...
def rename_key(name): ...
def convert_state_dict(orig_state_dict, config): ...
def remove_keys(state_dict) -> None: ...
def convert_audio_spectrogram_transformer_checkpoint(model_name, pytorch_dump_folder_path, push_to_hub: bool = False) -> None:
    """
    Copy/paste/tweak model's weights to our Audio Spectrogram Transformer structure.
    """
