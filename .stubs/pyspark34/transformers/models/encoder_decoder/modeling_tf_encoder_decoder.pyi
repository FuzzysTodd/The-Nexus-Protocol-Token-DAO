import tensorflow as tf
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFSeq2SeqLMOutput as TFSeq2SeqLMOutput
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFPreTrainedModel as TFPreTrainedModel, get_initializer as get_initializer, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list
from ...utils import DUMMY_INPUTS as DUMMY_INPUTS, ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from ..auto.configuration_auto import AutoConfig as AutoConfig
from ..auto.modeling_tf_auto import TFAutoModel as TFAutoModel, TFAutoModelForCausalLM as TFAutoModelForCausalLM
from .configuration_encoder_decoder import EncoderDecoderConfig as EncoderDecoderConfig
from _typeshed import Incomplete
from typing import Optional

logger: Incomplete
DEPRECATION_WARNING: str
ENCODER_DECODER_START_DOCSTRING: str
ENCODER_DECODER_INPUTS_DOCSTRING: str

def shift_tokens_right(input_ids: tf.Tensor, pad_token_id: int, decoder_start_token_id: int): ...

class TFEncoderDecoderModel(TFPreTrainedModel, TFCausalLanguageModelingLoss):
    """
    [`TFEncoderDecoderModel`] is a generic model class that will be instantiated as a transformer architecture with one
    of the base model classes of the library as encoder and another one as decoder when created with the
    [`~TFAutoModel.from_pretrained`] class method for the encoder and [`~TFAutoModelForCausalLM.from_pretrained`] class
    method for the decoder.
    """
    config_class = EncoderDecoderConfig
    base_model_prefix: str
    load_weight_prefix: str
    encoder: Incomplete
    decoder: Incomplete
    enc_to_dec_proj: Incomplete
    def __init__(self, config: Optional[PretrainedConfig] = None, encoder: Optional[TFPreTrainedModel] = None, decoder: Optional[TFPreTrainedModel] = None) -> None: ...
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def get_encoder(self): ...
    def get_decoder(self): ...
    def get_input_embeddings(self): ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings): ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        '''
        Example:

        ```python
        >>> from transformers import TFEncoderDecoderModel

        >>> model = TFEncoderDecoderModel.from_pretrained("ydshieh/bert2bert-cnn_dailymail-fp16")
        ```'''
    @classmethod
    def from_encoder_decoder_pretrained(cls, encoder_pretrained_model_name_or_path: str = None, decoder_pretrained_model_name_or_path: str = None, *model_args, **kwargs) -> TFPreTrainedModel:
        '''
        Instantiate an encoder and a decoder from one or two base classes of the library from pretrained model
        checkpoints.


        Params:
            encoder_pretrained_model_name_or_path (`str`, *optional*):
                Information necessary to initiate the encoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~TFPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *pytorch index checkpoint file* (e.g, `./pt_model/`). In this case,
                      `encoder_from_pt` should be set to `True`.

            decoder_pretrained_model_name_or_path (`str`, *optional*, defaults to `None`):
                Information necessary to initiate the decoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~TFPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *pytorch checkpoint file* (e.g, `./pt_model/`). In this case,
                      `decoder_from_pt` should be set to `True`.

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
        >>> from transformers import TFEncoderDecoderModel

        >>> # initialize a bert2gpt2 from two pretrained BERT models. Note that the cross-attention layers will be randomly initialized
        >>> model = TFEncoderDecoderModel.from_encoder_decoder_pretrained("bert-base-uncased", "gpt2")
        >>> # saving model after fine-tuning
        >>> model.save_pretrained("./bert2gpt2")
        >>> # load fine-tuned model
        >>> model = TFEncoderDecoderModel.from_pretrained("./bert2gpt2")
        ```'''
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_input_ids: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, encoder_outputs: Incomplete | None = None, past_key_values: Incomplete | None = None, inputs_embeds: Incomplete | None = None, decoder_inputs_embeds: Incomplete | None = None, labels: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False, **kwargs):
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import TFEncoderDecoderModel, BertTokenizer

        >>> # initialize a bert2gpt2 from a pretrained BERT and GPT2 models. Note that the cross-attention layers will be randomly initialized
        >>> model = TFEncoderDecoderModel.from_encoder_decoder_pretrained("bert-base-cased", "gpt2")

        >>> tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

        >>> # forward
        >>> input_ids = tokenizer.encode(
        ...     "Hello, my dog is cute", add_special_tokens=True, return_tensors="tf"
        ... )  # Batch size 1
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=input_ids)

        >>> # training
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=input_ids, labels=input_ids)
        >>> loss, logits = outputs.loss, outputs.logits

        >>> # save and load from pretrained
        >>> model.save_pretrained("bert2gpt2")
        >>> model = TFEncoderDecoderModel.from_pretrained("bert2gpt2")

        >>> # generation
        >>> generated = model.generate(input_ids, decoder_start_token_id=model.config.decoder.bos_token_id)
        ```'''
    def serving_output(self, output): ...
    def prepare_inputs_for_generation(self, input_ids, past: Incomplete | None = None, attention_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def prepare_decoder_input_ids_from_labels(self, labels: tf.Tensor): ...
    def resize_token_embeddings(self, *args, **kwargs) -> None: ...
