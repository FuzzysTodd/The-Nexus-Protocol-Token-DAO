import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFCausalLMOutput as TFCausalLMOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFConv1D as TFConv1D, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFSequenceSummary as TFSequenceSummary, TFSharedEmbeddings as TFSharedEmbeddings, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_openai import OpenAIGPTConfig as OpenAIGPTConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Optional, Tuple, Union

logger: Incomplete
TF_OPENAI_GPT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFAttention(tf.keras.layers.Layer):
    n_head: Incomplete
    split_size: Incomplete
    scale: Incomplete
    output_attentions: Incomplete
    c_attn: Incomplete
    c_proj: Incomplete
    attn_dropout: Incomplete
    resid_dropout: Incomplete
    pruned_heads: Incomplete
    def __init__(self, nx, config, scale: bool = False, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    @staticmethod
    def causal_attention_mask(nd, ns):
        """
        1's in the lower triangle, counting from the lower right corner. Same as tf.matrix_band_part(tf.ones([nd, ns]),
        -1, ns-nd), but doesn't produce garbage on TPUs.
        """
    def merge_heads(self, x): ...
    def split_heads(self, x): ...
    def call(self, x, attention_mask, head_mask, output_attentions, training: bool = False): ...

class TFMLP(tf.keras.layers.Layer):
    c_fc: Incomplete
    c_proj: Incomplete
    act: Incomplete
    dropout: Incomplete
    def __init__(self, n_state, config, **kwargs) -> None: ...
    def call(self, x, training: bool = False): ...

class TFBlock(tf.keras.layers.Layer):
    attn: Incomplete
    ln_1: Incomplete
    mlp: Incomplete
    ln_2: Incomplete
    def __init__(self, config, scale: bool = False, **kwargs) -> None: ...
    def call(self, x, attention_mask, head_mask, output_attentions, training: bool = False): ...

class TFOpenAIGPTMainLayer(tf.keras.layers.Layer):
    config_class = OpenAIGPTConfig
    config: Incomplete
    output_hidden_states: Incomplete
    output_attentions: Incomplete
    return_dict: Incomplete
    num_hidden_layers: Incomplete
    n_embd: Incomplete
    n_positions: Incomplete
    initializer_range: Incomplete
    tokens_embed: Incomplete
    drop: Incomplete
    h: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    positions_embed: Incomplete
    def build(self, input_shape) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[Tuple, TFBaseModelOutput]: ...

class TFOpenAIGPTPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = OpenAIGPTConfig
    base_model_prefix: str
    def serving(self, inputs): ...

@dataclass
class TFOpenAIGPTDoubleHeadsModelOutput(ModelOutput):
    """
    Base class for outputs of models predicting if two sentences are consecutive or not.

    Args:
        logits (`tf.Tensor` of shape `(batch_size, num_choices, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        mc_logits (`tf.Tensor` of shape `(batch_size, num_choices)`):
            Prediction scores of the multiple choice classification head (scores for each choice before SoftMax).
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    logits: tf.Tensor = ...
    mc_logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, logits, mc_logits, hidden_states, attentions) -> None: ...

OPENAI_GPT_START_DOCSTRING: str
OPENAI_GPT_INPUTS_DOCSTRING: str

class TFOpenAIGPTModel(TFOpenAIGPTPreTrainedModel):
    transformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[Tuple, TFBaseModelOutput]: ...
    def serving_output(self, output): ...

class TFOpenAIGPTLMHeadModel(TFOpenAIGPTPreTrainedModel, TFCausalLanguageModelingLoss):
    transformer: Incomplete
    supports_xla_generation: bool
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFCausalLMOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss. Indices should be in `[0, ...,
            config.vocab_size - 1]`.
        """
    def serving_output(self, output: TFCausalLMOutput) -> TFCausalLMOutput: ...
    def prepare_inputs_for_generation(self, inputs, **kwargs): ...

class TFOpenAIGPTDoubleHeadsModel(TFOpenAIGPTPreTrainedModel):
    transformer: Incomplete
    multiple_choice_head: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, mc_token_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[Tuple, TFOpenAIGPTDoubleHeadsModelOutput]:
        '''
        mc_token_ids (`tf.Tensor` or `Numpy array` of shape `(batch_size, num_choices)`, *optional*, default to index of the last token of the input):
            Index of the classification token in each input sequence. Selected in the range `[0, input_ids.size(-1) -
            1]`.

        Return:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFOpenAIGPTDoubleHeadsModel

        >>> tokenizer = AutoTokenizer.from_pretrained("openai-gpt")
        >>> model = TFOpenAIGPTDoubleHeadsModel.from_pretrained("openai-gpt")

        >>> # Add a [CLS] to the vocabulary (we should train it also!)
        >>> tokenizer.add_special_tokens({"cls_token": "[CLS]"})
        >>> model.resize_token_embeddings(len(tokenizer))  # Update the model embeddings with the new vocabulary size
        >>> print(tokenizer.cls_token_id, len(tokenizer))  # The newly token the last token of the vocabulary

        >>> choices = ["Hello, my dog is cute [CLS]", "Hello, my cat is cute [CLS]"]
        >>> encoding = tokenizer(choices, return_tensors="tf")
        >>> inputs = {k: tf.expand_dims(v, 0) for k, v in encoding.items()}
        >>> inputs["mc_token_ids"] = tf.constant(
        ...     [inputs["input_ids"].shape[-1] - 1, inputs["input_ids"].shape[-1] - 1]
        ... )[
        ...     None, :
        ... ]  # Batch size 1
        >>> outputs = model(inputs)
        >>> lm_prediction_scores, mc_prediction_scores = outputs[:2]
        ```'''
    def serving(self, inputs): ...
    def serving_output(self, output): ...

class TFOpenAIGPTForSequenceClassification(TFOpenAIGPTPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    score: Incomplete
    transformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFSequenceClassifierOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss. Indices should be in `[0, ...,
            config.vocab_size - 1]`.
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...
