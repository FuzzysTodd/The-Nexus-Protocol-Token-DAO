import numpy as np
import tensorflow as tf
from ...file_utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from ...modeling_tf_outputs import TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFBaseModelOutputWithPoolingAndCrossAttentions as TFBaseModelOutputWithPoolingAndCrossAttentions, TFMaskedLMOutput as TFMaskedLMOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, get_tf_activation as get_tf_activation, shape_list as shape_list, unpack_inputs as unpack_inputs
from ...tf_utils import stable_softmax as stable_softmax
from ...utils import logging as logging
from .configuration_esm import EsmConfig as EsmConfig
from _typeshed import Incomplete
from tensorflow.keras.layers import Layer
from typing import Optional, Tuple, Union

logger: Incomplete
TF_ESM_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def rotate_half(x): ...
def apply_rotary_pos_emb(x, cos, sin): ...
def symmetrize(x):
    """Make layer symmetric in final two dimensions, used for contact prediction."""
def average_product_correct(x):
    """Perform average product correct, used for contact prediction."""

class TFRotaryEmbedding(Layer):
    """
    Rotary position embeddings based on those in
    [RoFormer](https://huggingface.co/docs/transformers/model_doc/roformer). Query and keys are transformed by rotation
    matrices which depend on their relative positions.
    """
    dim: Incomplete
    def __init__(self, dim: int, name: Incomplete | None = None) -> None: ...
    inv_freq: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, q: tf.Tensor, k: tf.Tensor) -> Tuple[tf.Tensor, tf.Tensor]: ...

class TFEsmContactPredictionHead(Layer):
    """Performs symmetrization, apc, and computes a logistic regression on the output features"""
    eos_idx: Incomplete
    in_features: Incomplete
    regression: Incomplete
    def __init__(self, in_features: int, bias: bool = True, eos_idx: int = 2, name: Incomplete | None = None) -> None: ...
    def build(self, input_shape) -> None: ...
    def call(self, tokens, attentions): ...

class TFEsmEmbeddings(Layer):
    """
    Same as BertEmbeddings with a tiny tweak for positional embeddings indexing.
    """
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    layer_norm: Incomplete
    position_embedding_type: Incomplete
    position_ids: Incomplete
    padding_idx: Incomplete
    token_dropout: Incomplete
    mask_token_id: Incomplete
    config: Incomplete
    def __init__(self, config, name: Incomplete | None = None) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, past_key_values_length: int = 0): ...
    def create_position_ids_from_inputs_embeds(self, inputs_embeds):
        """
        We are provided embeddings directly. We cannot infer which are padded so just generate sequential position ids.

        Args:
            inputs_embeds: tf.Tensor

        Returns: tf.Tensor
        """

class TFEsmSelfAttention(Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    rotary_embeddings: Incomplete
    max_position_embeddings: Incomplete
    distance_embedding: Incomplete
    is_decoder: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def transpose_for_scores(self, x: tf.Tensor) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, encoder_hidden_states: Optional[tf.Tensor] = None, encoder_attention_mask: Optional[tf.Tensor] = None, past_key_value: Optional[Tuple[Tuple[tf.Tensor]]] = None, output_attentions: Optional[bool] = False, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFEsmSelfOutput(Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, name: Incomplete | None = None) -> None: ...
    def call(self, hidden_states, input_tensor, training: bool = False): ...

class TFEsmAttention(Layer):
    self: Incomplete
    output_layer: Incomplete
    pruned_heads: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config, name: Incomplete | None = None) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, output_attentions: bool = False, training: bool = False): ...

class TFEsmIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: EsmConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFEsmOutput(Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, name: Incomplete | None = None) -> None: ...
    def call(self, hidden_states, input_tensor, training: bool = False): ...

class TFEsmLayer(Layer):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    is_decoder: Incomplete
    add_cross_attention: Incomplete
    crossattention: Incomplete
    intermediate: Incomplete
    output_layer: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config, name: Incomplete | None = None) -> None: ...
    def call(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, output_attentions: bool = False, training: bool = False): ...

class TFEsmEncoder(Layer):
    config: Incomplete
    layer: Incomplete
    emb_layer_norm_after: Incomplete
    def __init__(self, config, name: Incomplete | None = None) -> None: ...
    def call(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, training: bool = False): ...

class TFEsmPooler(Layer):
    dense: Incomplete
    def __init__(self, config: EsmConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFEsmPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = EsmConfig
    base_model_prefix: str

ESM_START_DOCSTRING: str
ESM_INPUTS_DOCSTRING: str

class TFEsmMainLayer(Layer):
    """

    The model can behave as an encoder (with only self-attention) as well as a decoder, in which case a layer of
    cross-attention is added between the self-attention layers, following the architecture described in [Attention is
    all you need](https://arxiv.org/abs/1706.03762) by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit,
    Llion Jones, Aidan N. Gomez, Lukasz Kaiser and Illia Polosukhin.

    To behave as an decoder the model needs to be initialized with the `is_decoder` argument of the configuration set
    to `True`. To be used in a Seq2Seq model, the model needs to initialized with both `is_decoder` argument and
    `add_cross_attention` set to `True`; an `encoder_hidden_states` is then expected as an input to the forward pass.
    """
    config: Incomplete
    is_decoder: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    contact_head: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True, name: Incomplete | None = None, **kwargs) -> None: ...
    def build(self, input_shape) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value: tf.Variable): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPoolingAndCrossAttentions, Tuple[tf.Tensor]]: ...
    def predict_contacts(self, tokens, attention_mask): ...

class TFEsmModel(TFEsmPreTrainedModel):
    esm: Incomplete
    def __init__(self, config: EsmConfig, add_pooling_layer: bool = True, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPoolingAndCrossAttentions, Tuple[tf.Tensor]]:
        """
        encoder_hidden_states  (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention if
            the model is configured as a decoder.
        encoder_attention_mask (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Mask to avoid performing attention on the padding token indices of the encoder input. This mask is used in
            the cross-attention if the model is configured as a decoder. Mask values selected in `[0, 1]`:

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.

        past_key_values (`Tuple[Tuple[tf.Tensor]]` of length `config.n_layers`)
            contains precomputed key and value hidden states of the attention blocks. Can be used to speed up decoding.
            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        use_cache (`bool`, *optional*, defaults to `True`):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`). Set to `False` during training, `True` during generation
        """
    def serving(self, inputs): ...
    def serving_output(self, output: TFBaseModelOutputWithPoolingAndCrossAttentions) -> TFBaseModelOutputWithPoolingAndCrossAttentions: ...
    def predict_contacts(self, tokens, attention_mask): ...

class TFEsmForMaskedLM(TFEsmPreTrainedModel, TFMaskedLanguageModelingLoss):
    esm: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def get_lm_head(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFMaskedLMOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        kwargs (`Dict[str, any]`, optional, defaults to *{}*):
            Used to hide legacy arguments that have been deprecated.
        """
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...
    def serving(self, inputs): ...
    def predict_contacts(self, tokens, attention_mask): ...

class TFEsmLMHead(Layer):
    """ESM Head for masked language modeling."""
    dense: Incomplete
    layer_norm: Incomplete
    decoder: Incomplete
    config: Incomplete
    def __init__(self, config, name: Incomplete | None = None) -> None: ...
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def get_bias(self): ...
    def call(self, features): ...

class TFEsmForSequenceClassification(TFEsmPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    config: Incomplete
    esm: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...
    def serving(self, inputs): ...

class TFEsmForTokenClassification(TFEsmPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    esm: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...
    def serving(self, inputs): ...

class TFEsmClassificationHead(Layer):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config, name: Incomplete | None = None) -> None: ...
    def call(self, features, training: bool = False): ...

def create_position_ids_from_input_ids(input_ids, padding_idx, past_key_values_length: int = 0):
    """
    Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding symbols
    are ignored. This is modified from fairseq's `utils.make_positions`.

    Args:
        x: tf.Tensor x:

    Returns: tf.Tensor
    """
