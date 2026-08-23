import torch
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, Seq2SeqLMOutput as Seq2SeqLMOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from ..auto.configuration_auto import AutoConfig as AutoConfig
from ..auto.modeling_auto import AutoModel as AutoModel, AutoModelForCausalLM as AutoModelForCausalLM
from .configuration_encoder_decoder import EncoderDecoderConfig as EncoderDecoderConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
DEPRECATION_WARNING: str
ENCODER_DECODER_START_DOCSTRING: str
ENCODER_DECODER_INPUTS_DOCSTRING: str

def shift_tokens_right(input_ids: torch.Tensor, pad_token_id: int, decoder_start_token_id: int):
    """
    Shift input ids one token to the right.
    """

class EncoderDecoderModel(PreTrainedModel):
    """
    [`EncoderDecoderModel`] is a generic model class that will be instantiated as a transformer architecture with one
    of the base model classes of the library as encoder and another one as decoder when created with the
    :meth*~transformers.AutoModel.from_pretrained* class method for the encoder and
    :meth*~transformers.AutoModelForCausalLM.from_pretrained* class method for the decoder.
    """
    config_class = EncoderDecoderConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool
    encoder: Incomplete
    decoder: Incomplete
    enc_to_dec_proj: Incomplete
    def __init__(self, config: Optional[PretrainedConfig] = None, encoder: Optional[PreTrainedModel] = None, decoder: Optional[PreTrainedModel] = None) -> None: ...
    def tie_weights(self) -> None: ...
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
        >>> from transformers import EncoderDecoderModel

        >>> model = EncoderDecoderModel.from_pretrained("patrickvonplaten/bert2bert-cnn_dailymail-fp16")
        ```'''
    @classmethod
    def from_encoder_decoder_pretrained(cls, encoder_pretrained_model_name_or_path: str = None, decoder_pretrained_model_name_or_path: str = None, *model_args, **kwargs) -> PreTrainedModel:
        '''
        Instantiate an encoder and a decoder from one or two base classes of the library from pretrained model
        checkpoints.


        The model is set in evaluation mode by default using `model.eval()` (Dropout modules are deactivated). To train
        the model, you need to first set it back in training mode with `model.train()`.

        Params:
            encoder_pretrained_model_name_or_path (`str`, *optional*):
                Information necessary to initiate the encoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~PreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *tensorflow index checkpoint file* (e.g, `./tf_model/model.ckpt.index`). In
                      this case, `from_tf` should be set to `True` and a configuration object should be provided as
                      `config` argument. This loading path is slower than converting the TensorFlow checkpoint in a
                      PyTorch model using the provided conversion scripts and loading the PyTorch model afterwards.

            decoder_pretrained_model_name_or_path (`str`, *optional*, defaults to `None`):
                Information necessary to initiate the decoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~PreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *tensorflow index checkpoint file* (e.g, `./tf_model/model.ckpt.index`). In
                      this case, `from_tf` should be set to `True` and a configuration object should be provided as
                      `config` argument. This loading path is slower than converting the TensorFlow checkpoint in a
                      PyTorch model using the provided conversion scripts and loading the PyTorch model afterwards.

            model_args (remaining positional arguments, *optional*):
                All remaining positional arguments will be passed to the underlying model\'s `__init__` method.

            kwargs (remaining dictionary of keyword arguments, *optional*):
                Can be used to update the configuration object (after it being loaded) and initiate the model (e.g.,
                `output_attentions=True`).

                - To update the encoder configuration, use the prefix *encoder_* for each configuration parameter.
                - To update the decoder configuration, use the prefix *decoder_* for each configuration parameter.
                - To update the parent model configuration, do not use a prefix for each configuration parameter.

                Behaves differently depending on whether a `config` is provided or automatically loaded.

        Example:

        ```python
        >>> from transformers import EncoderDecoderModel

        >>> # initialize a bert2bert from two pretrained BERT models. Note that the cross-attention layers will be randomly initialized
        >>> model = EncoderDecoderModel.from_encoder_decoder_pretrained("bert-base-uncased", "bert-base-uncased")
        >>> # saving model after fine-tuning
        >>> model.save_pretrained("./bert2bert")
        >>> # load fine-tuned model
        >>> model = EncoderDecoderModel.from_pretrained("./bert2bert")
        ```'''
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, encoder_outputs: Optional[Tuple[torch.FloatTensor]] = None, past_key_values: Tuple[Tuple[torch.FloatTensor]] = None, inputs_embeds: Optional[torch.FloatTensor] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple, Seq2SeqLMOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import EncoderDecoderModel, BertTokenizer
        >>> import torch

        >>> tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        >>> model = EncoderDecoderModel.from_encoder_decoder_pretrained(
        ...     "bert-base-uncased", "bert-base-uncased"
        ... )  # initialize Bert2Bert from pre-trained checkpoints

        >>> # training
        >>> model.config.decoder_start_token_id = tokenizer.cls_token_id
        >>> model.config.pad_token_id = tokenizer.pad_token_id
        >>> model.config.vocab_size = model.config.decoder.vocab_size

        >>> input_ids = tokenizer("This is a really long text", return_tensors="pt").input_ids
        >>> labels = tokenizer("This is the corresponding summary", return_tensors="pt").input_ids
        >>> outputs = model(input_ids=input_ids, labels=labels)
        >>> loss, logits = outputs.loss, outputs.logits

        >>> # save and load from pretrained
        >>> model.save_pretrained("bert2bert")
        >>> model = EncoderDecoderModel.from_pretrained("bert2bert")

        >>> # generation
        >>> generated = model.generate(input_ids)
        ```'''
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): ...
    def prepare_inputs_for_generation(self, input_ids, past: Incomplete | None = None, attention_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def resize_token_embeddings(self, *args, **kwargs) -> None: ...
