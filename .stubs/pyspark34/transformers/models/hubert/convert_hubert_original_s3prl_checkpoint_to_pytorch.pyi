from _typeshed import Incomplete
from transformers import HubertConfig as HubertConfig, HubertForSequenceClassification as HubertForSequenceClassification, Wav2Vec2FeatureExtractor as Wav2Vec2FeatureExtractor, logging as logging

logger: Incomplete
SUPPORTED_MODELS: Incomplete

def convert_s3prl_checkpoint(base_model_name, config_path, checkpoint_path, model_dump_path) -> None:
    """
    Copy/paste/tweak model's weights to transformers design.
    """
