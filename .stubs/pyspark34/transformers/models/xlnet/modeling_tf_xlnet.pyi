import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFSequenceSummary as TFSequenceSummary, TFSharedEmbeddings as TFSharedEmbeddings, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_xlnet import XLNetConfig as XLNetConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

logger: Incomplete
TF_XLNET_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFXLNetRelativeAttention(tf.keras.layers.Layer):
    n_head: Incomplete
    d_head: Incomplete
    d_model: Incomplete
    scale: Incomplete
    initializer_range: Incomplete
    output_attentions: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    q: Incomplete
    k: Incomplete
    v: Incomplete
    o: Incomplete
    r: Incomplete
    r_r_bias: Incomplete
    r_s_bias: Incomplete
    r_w_bias: Incomplete
    seg_embed: Incomplete
    def build(self, input_shape) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def rel_shift(self, x, klen: int = -1):
        """perform relative shift to form the relative attention score."""
    def rel_attn_core(self, q_head, k_head_h, v_head_h, k_head_r, seg_mat, attn_mask, head_mask, output_attentions, training: bool = False):
        """Core relative positional attention operations."""
    def post_attention(self, h, attn_vec, residual: bool = True, training: bool = False):
        """Post-attention processing."""
    def call(self, h, g, attn_mask_h, attn_mask_g, r, seg_mat, mems: Optional[Union[np.ndarray, tf.Tensor]] = None, target_mapping: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = False, training: bool = False): ...

class TFXLNetFeedForward(tf.keras.layers.Layer):
    layer_norm: Incomplete
    layer_1: Incomplete
    layer_2: Incomplete
    dropout: Incomplete
    activation_function: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, inp, training: bool = False): ...

class TFXLNetLayer(tf.keras.layers.Layer):
    rel_attn: Incomplete
    ff: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, output_h, output_g, non_tgt_mask, attn_mask, pos_emb, seg_mat, mems: Optional[Union[np.ndarray, tf.Tensor]] = None, target_mapping: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = False, training: bool = False): ...

class TFXLNetLMHead(tf.keras.layers.Layer):
    config: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config, input_embeddings, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    def set_bias(self, value) -> None: ...
    def call(self, hidden_states): ...

class TFXLNetMainLayer(tf.keras.layers.Layer):
    config_class = XLNetConfig
    config: Incomplete
    output_hidden_states: Incomplete
    output_attentions: Incomplete
    return_dict: Incomplete
    mem_len: Incomplete
    reuse_len: Incomplete
    d_model: Incomplete
    same_length: Incomplete
    attn_type: Incomplete
    bi_data: Incomplete
    clamp_len: Incomplete
    n_layer: Incomplete
    use_bfloat16: Incomplete
    initializer_range: Incomplete
    word_embedding: Incomplete
    layer: Incomplete
    dropout: Incomplete
    use_mems_eval: Incomplete
    use_mems_train: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    mask_emb: Incomplete
    def build(self, input_shape) -> None: ...
    def create_mask(self, qlen, mlen):
        """
        Creates causal attention mask. Float mask where 1.0 indicates masked, 0.0 indicates not-masked.

        Args:
            qlen: TODO Lysandre didn't fill
            mlen: TODO Lysandre didn't fill

        ```

                  same_length=False:      same_length=True:
                  <mlen > <  qlen >       <mlen > <  qlen >
               ^ [0 0 0 0 0 1 1 1 1]     [0 0 0 0 0 1 1 1 1]
                 [0 0 0 0 0 0 1 1 1]     [1 0 0 0 0 0 1 1 1]
            qlen [0 0 0 0 0 0 0 1 1]     [1 1 0 0 0 0 0 1 1]
                 [0 0 0 0 0 0 0 0 1]     [1 1 1 0 0 0 0 0 1]
               v [0 0 0 0 0 0 0 0 0]     [1 1 1 1 0 0 0 0 0]
        ```
        """
    def cache_mem(self, curr_out, prev_mem): ...
    @staticmethod
    def positional_embedding(pos_seq, inv_freq, bsz: Incomplete | None = None): ...
    def relative_positional_encoding(self, qlen, klen, bsz: Incomplete | None = None):
        """create relative positional encoding."""
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, mems: Optional[Union[np.ndarray, tf.Tensor]] = None, perm_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, target_mapping: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, input_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False): ...

class TFXLNetPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = XLNetConfig
    base_model_prefix: str

@dataclass
class TFXLNetModelOutput(ModelOutput):
    """
    Output type of [`TFXLNetModel`].

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, num_predict, hidden_size)`):
            Sequence of hidden-states at the last layer of the model.

            `num_predict` corresponds to `target_mapping.shape[1]`. If `target_mapping` is `None`, then `num_predict`
            corresponds to `sequence_length`.
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
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
    mems: Optional[List[tf.Tensor]] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, mems, hidden_states, attentions) -> None: ...

@dataclass
class TFXLNetLMHeadModelOutput(ModelOutput):
    """
    Output type of [`TFXLNetLMHeadModel`].

    Args:
        loss (`tf.Tensor` of shape *(1,)*, *optional*, returned when `labels` is provided)
            Language modeling loss (for next-token prediction).
        logits (`tf.Tensor` of shape `(batch_size, num_predict, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).

            `num_predict` corresponds to `target_mapping.shape[1]`. If `target_mapping` is `None`, then `num_predict`
            corresponds to `sequence_length`.
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
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
    mems: Optional[List[tf.Tensor]] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class TFXLNetForSequenceClassificationOutput(ModelOutput):
    """
    Output type of [`TFXLNetForSequenceClassification`].

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `label` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`tf.Tensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
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
    mems: Optional[List[tf.Tensor]] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class TFXLNetForTokenClassificationOutput(ModelOutput):
    """
    Output type of [`TFXLNetForTokenClassificationOutput`].

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided) :
            Classification loss.
        logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.num_labels)`):
            Classification scores (before SoftMax).
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
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
    mems: Optional[List[tf.Tensor]] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class TFXLNetForMultipleChoiceOutput(ModelOutput):
    """
    Output type of [`TFXLNetForMultipleChoice`].

    Args:
        loss (`tf.Tensor` of shape *(1,)*, *optional*, returned when `labels` is provided):
            Classification loss.
        logits (`tf.Tensor` of shape `(batch_size, num_choices)`):
            *num_choices* is the second dimension of the input tensors. (see *input_ids* above).

            Classification scores (before SoftMax).
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
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
    mems: Optional[List[tf.Tensor]] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class TFXLNetForQuestionAnsweringSimpleOutput(ModelOutput):
    """
    Output type of [`TFXLNetForQuestionAnsweringSimple`].

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Total span extraction loss is the sum of a Cross-Entropy for the start and end positions.
        start_logits (`tf.Tensor` of shape `(batch_size, sequence_length,)`):
            Span-start scores (before SoftMax).
        end_logits (`tf.Tensor` of shape `(batch_size, sequence_length,)`):
            Span-end scores (before SoftMax).
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
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
    start_logits: tf.Tensor = ...
    end_logits: tf.Tensor = ...
    mems: Optional[List[tf.Tensor]] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, start_logits, end_logits, mems, hidden_states, attentions) -> None: ...

XLNET_START_DOCSTRING: str
XLNET_INPUTS_DOCSTRING: str

class TFXLNetModel(TFXLNetPreTrainedModel):
    transformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, mems: Optional[Union[np.ndarray, tf.Tensor]] = None, perm_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, target_mapping: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, input_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFXLNetModelOutput, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class TFXLNetLMHeadModel(TFXLNetPreTrainedModel, TFCausalLanguageModelingLoss):
    transformer: Incomplete
    lm_loss: Incomplete
    supports_xla_generation: bool
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def prepare_inputs_for_generation(self, inputs, past_key_values: Incomplete | None = None, use_mems: Incomplete | None = None, **kwargs): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, mems: Optional[Union[np.ndarray, tf.Tensor]] = None, perm_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, target_mapping: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, input_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[TFXLNetLMHeadModelOutput, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss. Indices should be in `[0, ...,
            config.vocab_size - 1]`.

        Return:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> import numpy as np
        >>> from transformers import AutoTokenizer, TFXLNetLMHeadModel

        >>> tokenizer = AutoTokenizer.from_pretrained("xlnet-large-cased")
        >>> model = TFXLNetLMHeadModel.from_pretrained("xlnet-large-cased")

        >>> # We show how to setup inputs to predict a next token using a bi-directional context.
        >>> input_ids = tf.constant(tokenizer.encode("Hello, my dog is very <mask>", add_special_tokens=True))[
        ...     None, :
        ... ]  # We will predict the masked token

        >>> perm_mask = np.zeros((1, input_ids.shape[1], input_ids.shape[1]))
        >>> perm_mask[:, :, -1] = 1.0  # Previous tokens don\'t see last token

        >>> target_mapping = np.zeros(
        ...     (1, 1, input_ids.shape[1])
        ... )  # Shape [1, 1, seq_length] => let\'s predict one token
        >>> target_mapping[
        ...     0, 0, -1
        ... ] = 1.0  # Our first (and only) prediction will be the last token of the sequence (the masked token)

        >>> outputs = model(
        ...     input_ids,
        ...     perm_mask=tf.constant(perm_mask, dtype=tf.float32),
        ...     target_mapping=tf.constant(target_mapping, dtype=tf.float32),
        ... )

        >>> next_token_logits = outputs[
        ...     0
        ... ]  # Output has shape [target_mapping.size(0), target_mapping.size(1), config.vocab_size]
        ```'''
    def serving_output(self, output): ...

class TFXLNetForSequenceClassification(TFXLNetPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    transformer: Incomplete
    sequence_summary: Incomplete
    logits_proj: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, mems: Optional[Union[np.ndarray, tf.Tensor]] = None, perm_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, target_mapping: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, input_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[TFXLNetForSequenceClassificationOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output): ...

class TFXLNetForMultipleChoice(TFXLNetPreTrainedModel, TFMultipleChoiceLoss):
    transformer: Incomplete
    sequence_summary: Incomplete
    logits_proj: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    def call(self, input_ids: Optional[TFModelInputType] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, input_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, mems: Optional[Union[np.ndarray, tf.Tensor]] = None, perm_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, target_mapping: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[TFXLNetForMultipleChoiceOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs): ...
    def serving_output(self, output): ...

class TFXLNetForTokenClassification(TFXLNetPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    transformer: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, mems: Optional[Union[np.ndarray, tf.Tensor]] = None, perm_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, target_mapping: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, input_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[TFXLNetForTokenClassificationOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output): ...

class TFXLNetForQuestionAnsweringSimple(TFXLNetPreTrainedModel, TFQuestionAnsweringLoss):
    transformer: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, mems: Optional[Union[np.ndarray, tf.Tensor]] = None, perm_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, target_mapping: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, input_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[TFXLNetForQuestionAnsweringSimpleOutput, Tuple[tf.Tensor]]:
        """
        start_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        """
    def serving_output(self, output): ...
