import flax.linen as nn
import jax
import jax.numpy as jnp
import os
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions, FlaxSeq2SeqLMOutput as FlaxSeq2SeqLMOutput
from ...modeling_flax_utils import FlaxPreTrainedModel as FlaxPreTrainedModel
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from ..auto.configuration_auto import AutoConfig as AutoConfig
from ..auto.modeling_flax_auto import FlaxAutoModel as FlaxAutoModel, FlaxAutoModelForCausalLM as FlaxAutoModelForCausalLM
from .configuration_speech_encoder_decoder import SpeechEncoderDecoderConfig as SpeechEncoderDecoderConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from jax.random import PRNGKey as PRNGKey
from typing import Optional, Tuple, Union

logger: Incomplete
SPEECH_ENCODER_DECODER_START_DOCSTRING: str
SPEECH_ENCODER_DECODER_INPUTS_DOCSTRING: str
SPEECH_ENCODER_DECODER_ENCODE_INPUTS_DOCSTRING: str
SPEECH_ENCODER_DECODER_DECODE_INPUTS_DOCSTRING: str

class FlaxSpeechEncoderDecoderModule(nn.Module):
    config: SpeechEncoderDecoderConfig
    dtype: jnp.dtype
    encoder: Incomplete
    decoder: Incomplete
    enc_to_dec_proj: Incomplete
    def setup(self) -> None: ...
    def __call__(self, inputs, attention_mask, decoder_input_ids, decoder_attention_mask, decoder_position_ids, encoder_outputs: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True, freeze_feature_encoder: bool = False): ...

class FlaxSpeechEncoderDecoderModel(FlaxPreTrainedModel):
    """
    [`FlaxSpeechEncoderDecoderModel`] is a generic model class that will be instantiated as a transformer architecture
    with the module (flax.nn.Module) of one of the base model classes of the library as encoder module and another one
    as decoder module when created with the :meth*~transformers.FlaxAutoModel.from_pretrained* class method for the
    encoder and :meth*~transformers.FlaxAutoModelForCausalLM.from_pretrained* class method for the decoder.
    """
    config_class = SpeechEncoderDecoderConfig
    base_model_prefix: str
    module_class = FlaxSpeechEncoderDecoderModule
    def __init__(self, config: SpeechEncoderDecoderConfig, input_shape: Optional[Tuple] = None, seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def init_cache(self, batch_size, max_length, encoder_outputs):
        """
        Args:
            batch_size (`int`):
                batch_size used for fast auto-regressive decoding. Defines the batch size of the initialized cache.
            max_length (`int`):
                maximum possible length for auto-regressive decoding. Defines the sequence length of the initialized
                cache.
            encoder_outputs (`Union[FlaxBaseModelOutput, tuple(tuple(jnp.ndarray)]`):
                `encoder_outputs` consists of (`last_hidden_state`, *optional*: `hidden_states`, *optional*:
                `attentions`). `last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, *optional*)
                is a sequence of hidden-states at the output of the last layer of the encoder. Used in the
                cross-attention of the decoder.
        """
    def encode(self, inputs: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, freeze_feature_encoder: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import FlaxSpeechEncoderDecoderModel

        >>> # initialize a wav2vec2-2-bart from pretrained wav2vec2 and bart models. Note that the cross-attention layers will be randomly initialized
        >>> model = FlaxSpeechEncoderDecoderModel.from_encoder_decoder_pretrained(
        ...     "facebook/wav2vec2-large-lv60", "facebook/bart-large"
        ... )

        >>> inputs = jnp.ones((2, 5000), dtype=jnp.float32)
        >>> encoder_outputs = model.encode(inputs)
        ```'''
    def decode(self, decoder_input_ids, encoder_outputs, encoder_attention_mask: Optional[jnp.ndarray] = None, decoder_attention_mask: Optional[jnp.ndarray] = None, decoder_position_ids: Optional[jnp.ndarray] = None, past_key_values: dict = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import FlaxSpeechEncoderDecoderModel
        >>> import jax.numpy as jnp

        >>> # initialize a wav2vec2-2-bart from pretrained wav2vec2 and bart models. Note that the cross-attention layers will be randomly initialized
        >>> model = FlaxSpeechEncoderDecoderModel.from_encoder_decoder_pretrained(
        ...     "facebook/wav2vec2-large-lv60", "facebook/bart-large"
        ... )

        >>> inputs = jnp.ones((2, 5000), dtype=jnp.float32)
        >>> encoder_outputs = model.encode(inputs)

        >>> decoder_start_token_id = model.config.decoder.bos_token_id
        >>> decoder_input_ids = jnp.ones((inputs.shape[0], 1), dtype="i4") * decoder_start_token_id

        >>> outputs = model.decode(decoder_input_ids, encoder_outputs)
        >>> logits = outputs.logits
        ```'''
    def __call__(self, inputs: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = None, decoder_input_ids: Optional[jnp.ndarray] = None, decoder_attention_mask: Optional[jnp.ndarray] = None, decoder_position_ids: Optional[jnp.ndarray] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, freeze_feature_encoder: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import FlaxSpeechEncoderDecoderModel, AutoTokenizer

        >>> # load a fine-tuned wav2vec2-2-bart model
        >>> model = FlaxSpeechEncoderDecoderModel.from_pretrained("patrickvonplaten/wav2vec2-2-bart-large")
        >>> # load output tokenizer
        >>> tokenizer_output = AutoTokenizer.from_pretrained("facebook/bart-large")

        >>> inputs = jnp.ones((2, 5000), dtype=jnp.float32)

        >>> # use bart\'s special bos, pad and eos tokens
        >>> model.config.decoder_start_token_id = model.decoder.config.bos_token_id
        >>> model.config.pad_token_id = model.decoder.config.pad_token_id
        >>> model.config.eos_token_id = model.decoder.config.eos_token_id

        >>> outputs = model.generate(inputs)
        # Assert something? More interesting input? dtype correct?
        ```
        '''
    def prepare_inputs_for_generation(self, decoder_input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None, decoder_attention_mask: Optional[jnp.DeviceArray] = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
    @classmethod
    def from_encoder_decoder_pretrained(cls, encoder_pretrained_model_name_or_path: Optional[Union[str, os.PathLike]] = None, decoder_pretrained_model_name_or_path: Optional[Union[str, os.PathLike]] = None, *model_args, **kwargs) -> FlaxPreTrainedModel:
        '''
        Instantiate an encoder and a decoder from one or two base classes of the library from pretrained model
        checkpoints.

        Params:
            encoder_pretrained_model_name_or_path (`Union[str, os.PathLike]`, *optional*):
                Information necessary to initiate the encoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~FlaxPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.

            decoder_pretrained_model_name_or_path (`Union[str, os.PathLike]`, *optional*, defaults to `None`):
                Information necessary to initiate the decoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~FlaxPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.

            model_args (remaining positional arguments, *optional*):
                All remaning positional arguments will be passed to the underlying model\'s `__init__` method.

            kwargs (remaining dictionary of keyword arguments, *optional*):
                Can be used to update the configuration object (after it being loaded) and initiate the model (e.g.,
                `output_attentions=True`).

                - To update the encoder configuration, use the prefix *encoder_* for each configuration parameter.
                - To update the decoder configuration, use the prefix *decoder_* for each configuration parameter.
                - To update the parent model configuration, do not use a prefix for each configuration parameter.

                Behaves differently depending on whether a `config` is provided or automatically loaded.

        Example:

        ```python
        >>> from transformers import FlaxSpeechEncoderDecoderModel

        >>> # initialize a wav2vec2-2-bart from pretrained wav2vec2 and bart models. Note that the cross-attention layers will be randomly initialized
        >>> model = FlaxSpeechEncoderDecoderModel.from_encoder_decoder_pretrained(
        ...     "facebook/wav2vec2-large-lv60", "facebook/bart-large"
        ... )
        >>> # saving model after fine-tuning
        >>> model.save_pretrained("./wav2vec2-2-bart-large")
        >>> # load fine-tuned model
        >>> model = FlaxSpeechEncoderDecoderModel.from_pretrained("./wav2vec2-2-bart-large")
        ```'''
