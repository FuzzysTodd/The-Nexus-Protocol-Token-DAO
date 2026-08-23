import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFMaskedLMOutput as TFMaskedLMOutput, TFMultipleChoiceModelOutput as TFMultipleChoiceModelOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_funnel import FunnelConfig as FunnelConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_FUNNEL_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
INF: float

class TFFunnelEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: Incomplete
    hidden_size: Incomplete
    initializer_std: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    weight: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, input_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, training: bool = False):
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFFunnelAttentionStructure:
    """
    Contains helpers for `TFFunnelRelMultiheadAttention `.
    """
    cls_token_type_id: int
    d_model: Incomplete
    attention_type: Incomplete
    num_blocks: Incomplete
    separate_cls: Incomplete
    truncate_seq: Incomplete
    pool_q_only: Incomplete
    pooling_type: Incomplete
    sin_dropout: Incomplete
    cos_dropout: Incomplete
    pooling_mult: Incomplete
    def __init__(self, config) -> None: ...
    seq_len: Incomplete
    def init_attention_inputs(self, inputs_embeds, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, training: bool = False):
        """Returns the attention inputs associated to the inputs of the model."""
    def token_type_ids_to_mat(self, token_type_ids):
        """Convert `token_type_ids` to `token_type_mat`."""
    def get_position_embeds(self, seq_len, training: bool = False):
        """
        Create and cache inputs related to relative position encoding. Those are very different depending on whether we
        are using the factorized or the relative shift attention:

        For the factorized attention, it returns the matrices (phi, pi, psi, omega) used in the paper, appendix A.2.2,
        final formula.

        For the relative shift attention, it returns all possible vectors R used in the paper, appendix A.2.1, final
        formula.

        Paper link: https://arxiv.org/abs/2006.03236
        """
    def stride_pool_pos(self, pos_id, block_index):
        """
        Pool `pos_id` while keeping the cls token separate (if `self.separate_cls=True`).
        """
    def relative_pos(self, pos, stride, pooled_pos: Incomplete | None = None, shift: int = 1):
        """
        Build the relative positional vector between `pos` and `pooled_pos`.
        """
    def stride_pool(self, tensor, axis):
        """
        Perform pooling by stride slicing the tensor along the given axis.
        """
    def pool_tensor(self, tensor, mode: str = 'mean', stride: int = 2):
        """Apply 1D pooling to a tensor of size [B x T (x H)]."""
    def pre_attention_pooling(self, output, attention_inputs):
        """Pool `output` and the proper parts of `attention_inputs` before the attention layer."""
    def post_attention_pooling(self, attention_inputs):
        """Pool the proper parts of `attention_inputs` after the attention layer."""

class TFFunnelRelMultiheadAttention(tf.keras.layers.Layer):
    attention_type: Incomplete
    n_head: Incomplete
    d_head: Incomplete
    d_model: Incomplete
    initializer_range: Incomplete
    block_index: Incomplete
    hidden_dropout: Incomplete
    attention_dropout: Incomplete
    q_head: Incomplete
    k_head: Incomplete
    v_head: Incomplete
    post_proj: Incomplete
    layer_norm: Incomplete
    scale: Incomplete
    def __init__(self, config, block_index, **kwargs) -> None: ...
    r_w_bias: Incomplete
    r_r_bias: Incomplete
    r_kernel: Incomplete
    r_s_bias: Incomplete
    seg_embed: Incomplete
    def build(self, input_shape) -> None: ...
    def relative_positional_attention(self, position_embeds, q_head, context_len, cls_mask: Incomplete | None = None):
        """Relative attention score for the positional encodings"""
    def relative_token_type_attention(self, token_type_mat, q_head, cls_mask: Incomplete | None = None):
        """Relative attention score for the token_type_ids"""
    def call(self, query, key, value, attention_inputs, output_attentions: bool = False, training: bool = False): ...

class TFFunnelPositionwiseFFN(tf.keras.layers.Layer):
    linear_1: Incomplete
    activation_function: Incomplete
    activation_dropout: Incomplete
    linear_2: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden, training: bool = False): ...

class TFFunnelLayer(tf.keras.layers.Layer):
    attention: Incomplete
    ffn: Incomplete
    def __init__(self, config, block_index, **kwargs) -> None: ...
    def call(self, query, key, value, attention_inputs, output_attentions: bool = False, training: bool = False): ...

class TFFunnelEncoder(tf.keras.layers.Layer):
    separate_cls: Incomplete
    pool_q_only: Incomplete
    block_repeats: Incomplete
    attention_structure: Incomplete
    blocks: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, inputs_embeds, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, training: bool = False): ...

def upsample(x, stride, target_len, separate_cls: bool = True, truncate_seq: bool = False):
    """
    Upsample tensor `x` to match `target_len` by repeating the tokens `stride` time on the sequence length dimension.
    """

class TFFunnelDecoder(tf.keras.layers.Layer):
    separate_cls: Incomplete
    truncate_seq: Incomplete
    stride: Incomplete
    attention_structure: Incomplete
    layers: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, final_hidden, first_block_hidden, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, training: bool = False): ...

class TFFunnelBaseLayer(tf.keras.layers.Layer):
    """Base model without decoder"""
    config_class = FunnelConfig
    config: Incomplete
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    return_dict: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False): ...

class TFFunnelMainLayer(tf.keras.layers.Layer):
    """Base model with decoder"""
    config_class = FunnelConfig
    config: Incomplete
    block_sizes: Incomplete
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    return_dict: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False): ...

class TFFunnelDiscriminatorPredictions(tf.keras.layers.Layer):
    """Prediction module for the discriminator, made up of two dense layers."""
    dense: Incomplete
    activation_function: Incomplete
    dense_prediction: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, discriminator_hidden_states): ...

class TFFunnelMaskedLMHead(tf.keras.layers.Layer):
    config: Incomplete
    hidden_size: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config, input_embeddings, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    def set_bias(self, value) -> None: ...
    def call(self, hidden_states, training: bool = False): ...

class TFFunnelClassificationHead(tf.keras.layers.Layer):
    linear_hidden: Incomplete
    dropout: Incomplete
    linear_out: Incomplete
    def __init__(self, config, n_labels, **kwargs) -> None: ...
    def call(self, hidden, training: bool = False): ...

class TFFunnelPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = FunnelConfig
    base_model_prefix: str

@dataclass
class TFFunnelForPreTrainingOutput(ModelOutput):
    """
    Output type of [`FunnelForPreTraining`].

    Args:
        logits (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            Prediction scores of the head (scores for each token before SoftMax).
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
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, logits, hidden_states, attentions) -> None: ...

FUNNEL_START_DOCSTRING: str
FUNNEL_INPUTS_DOCSTRING: str

class TFFunnelBaseModel(TFFunnelPreTrainedModel):
    funnel: Incomplete
    def __init__(self, config: FunnelConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFBaseModelOutput]: ...
    def serving_output(self, output): ...

class TFFunnelModel(TFFunnelPreTrainedModel):
    funnel: Incomplete
    def __init__(self, config: FunnelConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFBaseModelOutput]: ...
    def serving_output(self, output): ...

class TFFunnelForPreTraining(TFFunnelPreTrainedModel):
    funnel: Incomplete
    discriminator_predictions: Incomplete
    def __init__(self, config: FunnelConfig, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False, **kwargs) -> Union[Tuple[tf.Tensor], TFFunnelForPreTrainingOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFFunnelForPreTraining
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("funnel-transformer/small")
        >>> model = TFFunnelForPreTraining.from_pretrained("funnel-transformer/small")

        >>> inputs = tokenizer("Hello, my dog is cute", return_tensors="tf")
        >>> logits = model(inputs).logits
        ```'''
    def serving_output(self, output): ...

class TFFunnelForMaskedLM(TFFunnelPreTrainedModel, TFMaskedLanguageModelingLoss):
    funnel: Incomplete
    lm_head: Incomplete
    def __init__(self, config: FunnelConfig, *inputs, **kwargs) -> None: ...
    def get_lm_head(self) -> TFFunnelMaskedLMHead: ...
    def get_prefix_bias_name(self) -> str: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFMaskedLMOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFFunnelForSequenceClassification(TFFunnelPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    funnel: Incomplete
    classifier: Incomplete
    def __init__(self, config: FunnelConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFSequenceClassifierOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFFunnelForMultipleChoice(TFFunnelPreTrainedModel, TFMultipleChoiceLoss):
    funnel: Incomplete
    classifier: Incomplete
    def __init__(self, config: FunnelConfig, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFMultipleChoiceModelOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs: Dict[str, tf.Tensor]) -> TFMultipleChoiceModelOutput: ...
    def serving_output(self, output: TFMultipleChoiceModelOutput) -> TFMultipleChoiceModelOutput: ...

class TFFunnelForTokenClassification(TFFunnelPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    funnel: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: FunnelConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFTokenClassifierOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFFunnelForQuestionAnswering(TFFunnelPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    funnel: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config: FunnelConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFQuestionAnsweringModelOutput]:
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
    def serving_output(self, output: TFQuestionAnsweringModelOutput) -> TFQuestionAnsweringModelOutput: ...
