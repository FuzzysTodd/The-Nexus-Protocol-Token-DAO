from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from ..auto.configuration_auto import AutoConfig as AutoConfig
from _typeshed import Incomplete

logger: Incomplete

class SpeechEncoderDecoderConfig(PretrainedConfig):
    '''
    [`SpeechEncoderDecoderConfig`] is the configuration class to store the configuration of a
    [`SpeechEncoderDecoderModel`]. It is used to instantiate an Encoder Decoder model according to the specified
    arguments, defining the encoder and decoder configs.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        kwargs (*optional*):
            Dictionary of keyword arguments. Notably:

                - **encoder** ([`PretrainedConfig`], *optional*) -- An instance of a configuration object that defines
                  the encoder config.
                - **decoder** ([`PretrainedConfig`], *optional*) -- An instance of a configuration object that defines
                  the decoder config.

    Examples:

    ```python
    >>> from transformers import BertConfig, Wav2Vec2Config, SpeechEncoderDecoderConfig, SpeechEncoderDecoderModel

    >>> # Initializing a Wav2Vec2 & BERT style configuration
    >>> config_encoder = Wav2Vec2Config()
    >>> config_decoder = BertConfig()

    >>> config = SpeechEncoderDecoderConfig.from_encoder_decoder_configs(config_encoder, config_decoder)

    >>> # Initializing a Wav2Vec2Bert model from a Wav2Vec2 & bert-base-uncased style configurations
    >>> model = SpeechEncoderDecoderModel(config=config)

    >>> # Accessing the model configuration
    >>> config_encoder = model.config.encoder
    >>> config_decoder = model.config.decoder
    >>> # set decoder config to causal lm
    >>> config_decoder.is_decoder = True
    >>> config_decoder.add_cross_attention = True

    >>> # Saving the model, including its configuration
    >>> model.save_pretrained("my-model")

    >>> # loading model and config from pretrained folder
    >>> encoder_decoder_config = SpeechEncoderDecoderConfig.from_pretrained("my-model")
    >>> model = SpeechEncoderDecoderModel.from_pretrained("my-model", config=encoder_decoder_config)
    ```'''
    model_type: str
    is_composition: bool
    encoder: Incomplete
    decoder: Incomplete
    is_encoder_decoder: bool
    def __init__(self, **kwargs) -> None: ...
    @classmethod
    def from_encoder_decoder_configs(cls, encoder_config: PretrainedConfig, decoder_config: PretrainedConfig, **kwargs) -> PretrainedConfig:
        """
        Instantiate a [`SpeechEncoderDecoderConfig`] (or a derived class) from a pre-trained encoder model
        configuration and decoder model configuration.

        Returns:
            [`SpeechEncoderDecoderConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default *to_dict()* from *PretrainedConfig*.

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
