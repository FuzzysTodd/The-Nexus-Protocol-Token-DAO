import numpy as np
import tensorflow as tf
from ...modeling_tf_utils import TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_transfo_xl import TransfoXLConfig as TransfoXLConfig
from .modeling_tf_transfo_xl_utilities import TFAdaptiveSoftmaxMask as TFAdaptiveSoftmaxMask
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

logger: Incomplete
TF_TRANSFO_XL_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFPositionalEmbedding(tf.keras.layers.Layer):
    inv_freq: Incomplete
    def __init__(self, demb, **kwargs) -> None: ...
    def call(self, pos_seq, bsz: Incomplete | None = None): ...

class TFPositionwiseFF(tf.keras.layers.Layer):
    d_model: Incomplete
    d_inner: Incomplete
    dropout: Incomplete
    layer_1: Incomplete
    drop_1: Incomplete
    layer_2: Incomplete
    drop_2: Incomplete
    layer_norm: Incomplete
    pre_lnorm: Incomplete
    def __init__(self, d_model, d_inner, dropout, pre_lnorm: bool = False, layer_norm_epsilon: float = 1e-05, init_std: float = 0.02, **kwargs) -> None: ...
    def call(self, inp, training: bool = False): ...

class TFRelPartialLearnableMultiHeadAttn(tf.keras.layers.Layer):
    n_head: Incomplete
    d_model: Incomplete
    d_head: Incomplete
    dropout: Incomplete
    output_attentions: Incomplete
    qkv_net: Incomplete
    drop: Incomplete
    dropatt: Incomplete
    o_net: Incomplete
    layer_norm: Incomplete
    scale: Incomplete
    pre_lnorm: Incomplete
    r_r_bias: Incomplete
    r_w_bias: Incomplete
    r_net: Incomplete
    def __init__(self, n_head, d_model, d_head, dropout, dropatt: float = 0.0, pre_lnorm: bool = False, r_r_bias: Incomplete | None = None, r_w_bias: Incomplete | None = None, layer_norm_epsilon: float = 1e-05, init_std: float = 0.02, output_attentions: bool = False, **kwargs) -> None: ...
    def build(self, input_shape) -> None: ...
    def call(self, w, r, attn_mask, mems, head_mask, output_attentions, training: bool = False): ...

class TFRelPartialLearnableDecoderLayer(tf.keras.layers.Layer):
    dec_attn: Incomplete
    pos_ff: Incomplete
    def __init__(self, n_head, d_model, d_head, d_inner, dropout, dropatt: float = 0.0, pre_lnorm: bool = False, r_w_bias: Incomplete | None = None, r_r_bias: Incomplete | None = None, layer_norm_epsilon: float = 1e-05, init_std: float = 0.02, output_attentions: bool = False, **kwargs) -> None: ...
    def call(self, dec_inp, r, dec_attn_mask, mems, head_mask, output_attentions, training: bool = False): ...

class TFTransfoEmbeddings(tf.keras.layers.Layer):
    vocab_size: Incomplete
    emb_size: Incomplete
    init_std: Incomplete
    def __init__(self, vocab_size, emb_size, init_std, **kwargs) -> None: ...
    weight: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...

class TFAdaptiveEmbedding(tf.keras.layers.Layer):
    n_token: Incomplete
    d_embed: Incomplete
    init_std: Incomplete
    cutoffs: Incomplete
    div_val: Incomplete
    d_proj: Incomplete
    emb_scale: Incomplete
    cutoff_ends: Incomplete
    emb_layers: Incomplete
    emb_projs: Incomplete
    def __init__(self, n_token, d_embed, d_proj, cutoffs, div_val: int = 1, init_std: float = 0.02, sample_softmax: bool = False, **kwargs) -> None: ...
    def build(self, input_shape) -> None: ...
    def call(self, inp): ...

class TFTransfoXLMainLayer(tf.keras.layers.Layer):
    config_class = TransfoXLConfig
    config: Incomplete
    output_hidden_states: Incomplete
    output_attentions: Incomplete
    return_dict: Incomplete
    n_token: Incomplete
    d_embed: Incomplete
    d_model: Incomplete
    n_head: Incomplete
    d_head: Incomplete
    untie_r: Incomplete
    word_emb: Incomplete
    drop: Incomplete
    n_layer: Incomplete
    mem_len: Incomplete
    attn_type: Incomplete
    layers: Incomplete
    same_length: Incomplete
    clamp_len: Incomplete
    pos_emb: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    r_w_bias: Incomplete
    r_r_bias: Incomplete
    def build(self, input_shape) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    sample_softmax: int
    def backward_compatible(self) -> None: ...
    def reset_memory_length(self, mem_len) -> None: ...
    def init_mems(self, bsz): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, mems: Optional[List[tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False): ...

class TFTransfoXLPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = TransfoXLConfig
    base_model_prefix: str
    def serving(self, inputs): ...

@dataclass
class TFTransfoXLModelOutput(ModelOutput):
    """
    Base class for model's outputs that may also contain a past key/values (to speed up sequential decoding).

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states (key and values in the attention blocks). Can be used (see `mems`
            input) to speed up sequential decoding. The token ids which have their past given to this model should not
            be passed as input ids as they have already been computed.
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
    last_hidden_state: tf.Tensor = ...
    mems: List[tf.Tensor] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, mems, hidden_states, attentions) -> None: ...

@dataclass
class TFTransfoXLLMHeadModelOutput(ModelOutput):
    """
    Base class for model's outputs that may also contain a past key/values (to speed up sequential decoding).

    Args:
        losses (`tf.Tensor` of shape *(batch_size, sequence_length-1)*, *optional*, returned when `labels` is provided):
            Language modeling losses (not reduced).
        prediction_scores (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token after SoftMax).
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states (key and values in the attention blocks). Can be used (see `mems`
            input) to speed up sequential decoding. The token ids which have their past given to this model should not
            be passed as input ids as they have already been computed.
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
    prediction_scores: tf.Tensor = ...
    mems: List[tf.Tensor] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, prediction_scores, mems, hidden_states, attentions) -> None: ...

@dataclass
class TFTransfoXLSequenceClassifierOutputWithPast(ModelOutput):
    """
    Base class for outputs of sentence classification models.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`tf.Tensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states (key and values in the attention blocks). Can be used (see `mems`
            input) to speed up sequential decoding. The token ids which have their past given to this model should not
            be passed as input ids as they have already been computed.
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
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    mems: List[tf.Tensor] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

TRANSFO_XL_START_DOCSTRING: str
TRANSFO_XL_INPUTS_DOCSTRING: str

class TFTransfoXLModel(TFTransfoXLPreTrainedModel):
    transformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, mems: Optional[List[tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False): ...
    def serving_output(self, output): ...

class TFTransfoXLLMHeadModel(TFTransfoXLPreTrainedModel):
    transformer: Incomplete
    sample_softmax: Incomplete
    crit: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self):
        """Double-check if you are using adaptive softmax."""
    def reset_memory_length(self, mem_len) -> None: ...
    def init_mems(self, bsz): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, mems: Optional[List[tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False): ...
    def serving_output(self, output): ...
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, **model_kwargs): ...

class TFTransfoXLForSequenceClassification(TFTransfoXLPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    score: Incomplete
    transformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_output_embeddings(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, mems: Optional[List[tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFTransfoXLSequenceClassifierOutputWithPast]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss. Indices should be in `[0, ...,
            config.vocab_size - 1]`.
        """
    def serving_output(self, output): ...
