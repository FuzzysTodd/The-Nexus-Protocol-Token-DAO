from ... import PreTrainedTokenizerBase as PreTrainedTokenizerBase, TensorType as TensorType
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...utils import logging as logging
from ..auto.configuration_auto import AutoConfig as AutoConfig
from _typeshed import Incomplete
from typing import Any, Mapping, Optional

logger: Incomplete

class VisionEncoderDecoderConfig(PretrainedConfig):
    '''
    [`VisionEncoderDecoderConfig`] is the configuration class to store the configuration of a
    [`VisionEncoderDecoderModel`]. It is used to instantiate a Vision-Encoder-Text-Decoder model according to the
    specified arguments, defining the encoder and decoder configs.

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
    >>> from transformers import BertConfig, ViTConfig, VisionEncoderDecoderConfig, VisionEncoderDecoderModel

    >>> # Initializing a ViT & BERT style configuration
    >>> config_encoder = ViTConfig()
    >>> config_decoder = BertConfig()

    >>> config = VisionEncoderDecoderConfig.from_encoder_decoder_configs(config_encoder, config_decoder)

    >>> # Initializing a ViTBert model (with random weights) from a ViT & bert-base-uncased style configurations
    >>> model = VisionEncoderDecoderModel(config=config)

    >>> # Accessing the model configuration
    >>> config_encoder = model.config.encoder
    >>> config_decoder = model.config.decoder
    >>> # set decoder config to causal lm
    >>> config_decoder.is_decoder = True
    >>> config_decoder.add_cross_attention = True

    >>> # Saving the model, including its configuration
    >>> model.save_pretrained("my-model")

    >>> # loading model and config from pretrained folder
    >>> encoder_decoder_config = VisionEncoderDecoderConfig.from_pretrained("my-model")
    >>> model = VisionEncoderDecoderModel.from_pretrained("my-model", config=encoder_decoder_config)
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
        Instantiate a [`VisionEncoderDecoderConfig`] (or a derived class) from a pre-trained encoder model
        configuration and decoder model configuration.

        Returns:
            [`VisionEncoderDecoderConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default *to_dict()* from *PretrainedConfig*.

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """

class VisionEncoderDecoderEncoderOnnxConfig(OnnxConfig):
    torch_onnx_minimum_version: Incomplete
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def atol_for_validation(self) -> float: ...
    @property
    def outputs(self) -> Mapping[str, Mapping[int, str]]: ...

class VisionEncoderDecoderDecoderOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    def generate_dummy_inputs(self, tokenizer: PreTrainedTokenizerBase, batch_size: int = -1, seq_length: int = -1, is_pair: bool = False, framework: Optional['TensorType'] = None) -> Mapping[str, Any]: ...

class VisionEncoderDecoderOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> None: ...
    def get_encoder_config(self, encoder_config: PretrainedConfig) -> OnnxConfig:
        """
        Returns ONNX encoder config for `VisionEncoderDecoder` model.

        Args:
            encoder_config (`PretrainedConfig`):
                The encoder model's configuration to use when exporting to ONNX.

        Returns:
            [`VisionEncoderDecoderEncoderOnnxConfig`]: An instance of the ONNX configuration object
        """
    def get_decoder_config(self, encoder_config: PretrainedConfig, decoder_config: PretrainedConfig, feature: str = 'default') -> OnnxConfig:
        """
        Returns ONNX decoder config for `VisionEncoderDecoder` model.

        Args:
            encoder_config (`PretrainedConfig`):
                The encoder model's configuration to use when exporting to ONNX.
            decoder_config (`PretrainedConfig`):
                The decoder model's configuration to use when exporting to ONNX
            feature (`str`, *optional*):
                The type of feature to export the model with.

        Returns:
            [`VisionEncoderDecoderDecoderOnnxConfig`]: An instance of the ONNX configuration object.
        """
