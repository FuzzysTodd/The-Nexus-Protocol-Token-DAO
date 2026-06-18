import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFMaskedLMOutput as TFMaskedLMOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_deberta_v2 import DebertaV2Config as DebertaV2Config
from _typeshed import Incomplete
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_DEBERTA_V2_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFDebertaV2ContextPooler(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    def call(self, hidden_states, training: bool = False): ...
    @property
    def output_dim(self) -> int: ...

class TFDebertaV2XSoftmax(tf.keras.layers.Layer):
    """
    Masked Softmax which is optimized for saving memory

    Args:
        input (`tf.Tensor`): The input tensor that will apply softmax.
        mask (`tf.Tensor`): The mask matrix where 0 indicate that element will be ignored in the softmax calculation.
        dim (int): The dimension that will apply softmax
    """
    axis: Incomplete
    def __init__(self, axis: int = -1, **kwargs) -> None: ...
    def call(self, inputs: tf.Tensor, mask: tf.Tensor): ...

class TFDebertaV2StableDropout(tf.keras.layers.Layer):
    """
    Optimized dropout module for stabilizing the training

    Args:
        drop_prob (float): the dropout probabilities
    """
    drop_prob: Incomplete
    def __init__(self, drop_prob, **kwargs) -> None: ...
    def xdropout(self, inputs):
        """
        Applies dropout to the inputs, as vanilla dropout, but also scales the remaining elements up by 1/drop_prob.
        """
    def call(self, inputs: tf.Tensor, training: tf.Tensor = False): ...

class TFDebertaV2SelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    def call(self, hidden_states, input_tensor, training: bool = False): ...

class TFDebertaV2Attention(tf.keras.layers.Layer):
    self: Incomplete
    dense_output: Incomplete
    config: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    def call(self, input_tensor: tf.Tensor, attention_mask: tf.Tensor, query_states: tf.Tensor = None, relative_pos: tf.Tensor = None, rel_embeddings: tf.Tensor = None, output_attentions: bool = False, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFDebertaV2Intermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFDebertaV2Output(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFDebertaV2Layer(tf.keras.layers.Layer):
    attention: Incomplete
    intermediate: Incomplete
    bert_output: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, query_states: tf.Tensor = None, relative_pos: tf.Tensor = None, rel_embeddings: tf.Tensor = None, output_attentions: bool = False, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFDebertaV2ConvLayer(tf.keras.layers.Layer):
    kernel_size: Incomplete
    conv_act: Incomplete
    padding: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    conv_kernel: Incomplete
    conv_bias: Incomplete
    def build(self, input_shape): ...
    def call(self, hidden_states: tf.Tensor, residual_states: tf.Tensor, input_mask: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFDebertaV2Encoder(tf.keras.layers.Layer):
    layer: Incomplete
    relative_attention: Incomplete
    config: Incomplete
    max_relative_positions: Incomplete
    position_buckets: Incomplete
    pos_ebd_size: Incomplete
    norm_rel_ebd: Incomplete
    LayerNorm: Incomplete
    conv: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    rel_embeddings: Incomplete
    def build(self, input_shape): ...
    def get_rel_embedding(self): ...
    def get_attention_mask(self, attention_mask): ...
    def get_rel_pos(self, hidden_states, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None): ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, query_states: tf.Tensor = None, relative_pos: tf.Tensor = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

def make_log_bucket_position(relative_pos, bucket_size, max_position): ...
def build_relative_position(query_size, key_size, bucket_size: int = -1, max_position: int = -1):
    """
    Build relative position according to the query and key

    We assume the absolute position of query \\(P_q\\) is range from (0, query_size) and the absolute position of key
    \\(P_k\\) is range from (0, key_size), The relative positions from query to key is \\(R_{q \\rightarrow k} = P_q -
    P_k\\)

    Args:
        query_size (int): the length of query
        key_size (int): the length of key
        bucket_size (int): the size of position bucket
        max_position (int): the maximum allowed absolute position

    Return:
        `tf.Tensor`: A tensor with shape [1, query_size, key_size]

    """
def c2p_dynamic_expand(c2p_pos, query_layer, relative_pos): ...
def p2c_dynamic_expand(c2p_pos, query_layer, key_layer): ...
def pos_dynamic_expand(pos_index, p2c_att, key_layer): ...
def take_along_axis(x, indices): ...

class TFDebertaV2DisentangledSelfAttention(tf.keras.layers.Layer):
    """
    Disentangled self-attention module

    Parameters:
        config (`DebertaV2Config`):
            A model config class instance with the configuration to build a new model. The schema is similar to
            *BertConfig*, for more details, please refer [`DebertaV2Config`]

    """
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query_proj: Incomplete
    key_proj: Incomplete
    value_proj: Incomplete
    share_att_key: Incomplete
    pos_att_type: Incomplete
    relative_attention: Incomplete
    position_buckets: Incomplete
    max_relative_positions: Incomplete
    pos_ebd_size: Incomplete
    pos_dropout: Incomplete
    pos_key_proj: Incomplete
    pos_query_proj: Incomplete
    softmax: Incomplete
    dropout: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, attention_heads: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, query_states: tf.Tensor = None, relative_pos: tf.Tensor = None, rel_embeddings: tf.Tensor = None, output_attentions: bool = False, training: bool = False) -> Tuple[tf.Tensor]:
        """
        Call the module

        Args:
            hidden_states (`tf.Tensor`):
                Input states to the module usually the output from previous layer, it will be the Q,K and V in
                *Attention(Q,K,V)*

            attention_mask (`tf.Tensor`):
                An attention mask matrix of shape [*B*, *N*, *N*] where *B* is the batch size, *N* is the maximum
                sequence length in which element [i,j] = *1* means the *i* th token in the input can attend to the *j*
                th token.

            return_att (`bool`, optional):
                Whether return the attention matrix.

            query_states (`tf.Tensor`, optional):
                The *Q* state in *Attention(Q,K,V)*.

            relative_pos (`tf.Tensor`):
                The relative position encoding between the tokens in the sequence. It's of shape [*B*, *N*, *N*] with
                values ranging in [*-max_relative_positions*, *max_relative_positions*].

            rel_embeddings (`tf.Tensor`):
                The embedding of relative distances. It's a tensor of shape [\\(2 \\times
                \\text{max_relative_positions}\\), *hidden_size*].


        """
    def disentangled_att_bias(self, query_layer, key_layer, relative_pos, rel_embeddings, scale_factor): ...

class TFDebertaV2Embeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: Incomplete
    embedding_size: Incomplete
    hidden_size: Incomplete
    max_position_embeddings: Incomplete
    position_biased_input: Incomplete
    initializer_range: Incomplete
    embed_proj: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    weight: Incomplete
    token_type_embeddings: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, input_ids: tf.Tensor = None, position_ids: tf.Tensor = None, token_type_ids: tf.Tensor = None, inputs_embeds: tf.Tensor = None, mask: tf.Tensor = None, training: bool = False) -> tf.Tensor:
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFDebertaV2PredictionHeadTransform(tf.keras.layers.Layer):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFDebertaV2LMPredictionHead(tf.keras.layers.Layer):
    config: Incomplete
    hidden_size: Incomplete
    transform: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config: DebertaV2Config, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def get_output_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_output_embeddings(self, value: tf.Variable): ...
    def get_bias(self) -> Dict[str, tf.Variable]: ...
    def set_bias(self, value: tf.Variable): ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFDebertaV2OnlyMLMHead(tf.keras.layers.Layer):
    predictions: Incomplete
    def __init__(self, config: DebertaV2Config, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    def call(self, sequence_output: tf.Tensor) -> tf.Tensor: ...

class TFDebertaV2MainLayer(tf.keras.layers.Layer):
    config_class = DebertaV2Config
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    def __init__(self, config: DebertaV2Config, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_input_embeddings(self, value: tf.Variable): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFDebertaV2PreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DebertaV2Config
    base_model_prefix: str

DEBERTA_START_DOCSTRING: str
DEBERTA_INPUTS_DOCSTRING: str

class TFDebertaV2Model(TFDebertaV2PreTrainedModel):
    deberta: Incomplete
    def __init__(self, config: DebertaV2Config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...
    def serving_output(self, output: TFBaseModelOutput) -> TFBaseModelOutput: ...

class TFDebertaV2ForMaskedLM(TFDebertaV2PreTrainedModel, TFMaskedLanguageModelingLoss):
    deberta: Incomplete
    mlm: Incomplete
    def __init__(self, config: DebertaV2Config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self) -> tf.keras.layers.Layer: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMaskedLMOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFDebertaV2ForSequenceClassification(TFDebertaV2PreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    deberta: Incomplete
    pooler: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: DebertaV2Config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFDebertaV2ForTokenClassification(TFDebertaV2PreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    deberta: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: DebertaV2Config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFDebertaV2ForQuestionAnswering(TFDebertaV2PreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    deberta: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config: DebertaV2Config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor]]:
        """
        start_positions (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        """
    def serving_output(self, output: TFQuestionAnsweringModelOutput) -> TFQuestionAnsweringModelOutput: ...
