from _typeshed import Incomplete
from transformers import Wav2Vec2Config as Wav2Vec2Config, Wav2Vec2FeatureExtractor as Wav2Vec2FeatureExtractor, Wav2Vec2ForAudioFrameClassification as Wav2Vec2ForAudioFrameClassification, Wav2Vec2ForSequenceClassification as Wav2Vec2ForSequenceClassification, Wav2Vec2ForXVector as Wav2Vec2ForXVector, logging as logging

logger: Incomplete

def convert_classification(base_model_name, hf_config, downstream_dict): ...
def convert_diarization(base_model_name, hf_config, downstream_dict): ...
def convert_xvector(base_model_name, hf_config, downstream_dict): ...
def convert_s3prl_checkpoint(base_model_name, config_path, checkpoint_path, model_dump_path) -> None:
    """
    Copy/paste/tweak model's weights to transformers design.
    """
