import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_utils import TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, get_initializer as get_initializer, keras_serializable as keras_serializable, shape_list as shape_list, unpack_inputs as unpack_inputs
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_lxmert import LxmertConfig as LxmertConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from transformers.tf_utils import stable_softmax as stable_softmax
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_LXMERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class TFLxmertModelOutput(ModelOutput):
    '''
    Lxmert\'s outputs that contain the last hidden states, pooled outputs, and attention probabilities for the language,
    visual, and, cross-modality encoders. (note: the visual encoder in Lxmert is referred to as the "relation-ship"
    encoder")


    Args:
        language_output (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the language encoder.
        vision_output (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the visual encoder.
        pooled_output (`tf.Tensor` of shape `(batch_size, hidden_size)`):
            Last layer hidden-state of the first token of the sequence (classification, CLS, token) further processed
            by a Linear layer and a Tanh activation function. The Linear
        language_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for input features + one for the output of each cross-modality layer) of shape
            `(batch_size, sequence_length, hidden_size)`.
        vision_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for input features + one for the output of each cross-modality layer) of shape
            `(batch_size, sequence_length, hidden_size)`.
        language_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
        vision_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
        cross_encoder_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    '''
    language_output: Optional[tf.Tensor] = ...
    vision_output: Optional[tf.Tensor] = ...
    pooled_output: Optional[tf.Tensor] = ...
    language_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    vision_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    language_attentions: Optional[Tuple[tf.Tensor]] = ...
    vision_attentions: Optional[Tuple[tf.Tensor]] = ...
    cross_encoder_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, language_output, vision_output, pooled_output, language_hidden_states, vision_hidden_states, language_attentions, vision_attentions, cross_encoder_attentions) -> None: ...

@dataclass
class TFLxmertForPreTrainingOutput(ModelOutput):
    """
    Output type of [`LxmertForPreTraining`].

    Args:
        loss (*optional*, returned when `labels` is provided, `tf.Tensor` of shape `(1,)`):
            Total loss as the sum of the masked language modeling loss and the next sequence prediction
            (classification) loss.
        prediction_logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        cross_relationship_score: (`tf.Tensor` of shape `(batch_size, 2)`):
            Prediction scores of the textual matching objective (classification) head (scores of True/False
            continuation before SoftMax).
        question_answering_score: (`tf.Tensor` of shape `(batch_size, n_qa_answers)`):
            Prediction scores of question answering objective (classification).
        language_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for input features + one for the output of each cross-modality layer) of shape
            `(batch_size, sequence_length, hidden_size)`.
        vision_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for input features + one for the output of each cross-modality layer) of shape
            `(batch_size, sequence_length, hidden_size)`.
        language_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
        vision_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
        cross_encoder_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.

    """
    loss: Optional[tf.Tensor] = ...
    prediction_logits: Optional[tf.Tensor] = ...
    cross_relationship_score: Optional[tf.Tensor] = ...
    question_answering_score: Optional[tf.Tensor] = ...
    language_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    vision_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    language_attentions: Optional[Tuple[tf.Tensor]] = ...
    vision_attentions: Optional[Tuple[tf.Tensor]] = ...
    cross_encoder_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, prediction_logits, cross_relationship_score, question_answering_score, language_hidden_states, vision_hidden_states, language_attentions, vision_attentions, cross_encoder_attentions) -> None: ...

class TFLxmertVisualFeatureEncoder(tf.keras.layers.Layer):
    visn_fc: Incomplete
    visn_layer_norm: Incomplete
    box_fc: Incomplete
    box_layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, visn_input, training: bool = False): ...

class TFLxmertEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: Incomplete
    hidden_size: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    weight: Incomplete
    token_type_embeddings: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, input_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, training: bool = False):
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFLxmertAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def transpose_for_scores(self, x, batch_size): ...
    def call(self, hidden_states, context, attention_mask, output_attentions, training: bool = False): ...

class TFLxmertIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFLxmertOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, input_tensor, training: bool = False): ...

class TFLxmertAttentionOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, input_tensor, training: bool = False): ...

class TFLxmertSelfAttentionLayer(tf.keras.layers.Layer):
    self: Incomplete
    attention_output: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, input_tensor, attention_mask, output_attentions, training: bool = False): ...

class TFLxmertCrossAttentionLayer(tf.keras.layers.Layer):
    att: Incomplete
    attention_output: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, input_tensor, ctx_tensor, ctx_att_mask, output_attentions: bool = False, training: bool = False): ...

class TFLxmertLayer(tf.keras.layers.Layer):
    attention: Incomplete
    intermediate: Incomplete
    transformer_output: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask, output_attentions, training: bool = False): ...

class TFLxmertXLayer(tf.keras.layers.Layer):
    visual_attention: Incomplete
    lang_self_att: Incomplete
    visn_self_att: Incomplete
    lang_inter: Incomplete
    lang_output: Incomplete
    visn_inter: Incomplete
    visn_output: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def cross_att(self, lang_input, lang_attention_mask, visn_input, visn_attention_mask, output_attentions, training: bool = False): ...
    def self_att(self, lang_input, lang_attention_mask, visn_input, visn_attention_mask, training: bool = False): ...
    def output_fc(self, lang_input, visn_input, training: bool = False): ...
    def call(self, lang_feats, lang_attention_mask, visn_feats, visn_attention_mask, output_attentions, training: bool = False): ...

class TFLxmertEncoder(tf.keras.layers.Layer):
    visn_fc: Incomplete
    num_l_layers: Incomplete
    num_x_layers: Incomplete
    num_r_layers: Incomplete
    layer: Incomplete
    x_layers: Incomplete
    r_layers: Incomplete
    config: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, lang_feats: Incomplete | None = None, lang_attention_mask: Incomplete | None = None, visual_feats: Incomplete | None = None, visual_pos: Incomplete | None = None, visual_attention_mask: Incomplete | None = None, output_attentions: Incomplete | None = None, training: bool = False): ...

class TFLxmertMainLayer(tf.keras.layers.Layer):
    config_class = LxmertConfig
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    config: Incomplete
    num_l_layers: Incomplete
    num_x_layers: Incomplete
    num_r_layers: Incomplete
    initializer_range: Incomplete
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    return_dict: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Incomplete | None = None, visual_feats: Incomplete | None = None, visual_pos: Incomplete | None = None, attention_mask: Incomplete | None = None, visual_attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False): ...

class TFLxmertPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LxmertConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]: ...
    def serving(self, inputs): ...

LXMERT_START_DOCSTRING: str
LXMERT_INPUTS_DOCSTRING: str

class TFLxmertModel(TFLxmertPreTrainedModel):
    lxmert: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, visual_feats: Optional[tf.Tensor] = None, visual_pos: Optional[tf.Tensor] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, visual_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple, TFLxmertModelOutput]: ...
    def serving_output(self, output): ...

class TFLxmertPooler(tf.keras.layers.Layer):
    dense: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFLxmertPredictionHeadTransform(tf.keras.layers.Layer):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config: LxmertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFLxmertLMPredictionHead(tf.keras.layers.Layer):
    config: Incomplete
    hidden_size: Incomplete
    transform: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config: LxmertConfig, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def get_output_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_output_embeddings(self, value: tf.Variable): ...
    def get_bias(self) -> Dict[str, tf.Variable]: ...
    def set_bias(self, value: tf.Variable): ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFLxmertMLMHead(tf.keras.layers.Layer):
    predictions: Incomplete
    def __init__(self, config: LxmertConfig, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    def call(self, sequence_output: tf.Tensor) -> tf.Tensor: ...

class TFLxmertPreTrainingHeads(tf.keras.layers.Layer):
    predictions: Incomplete
    seq_relationship: Incomplete
    def __init__(self, config, input_embeddings, **kwargs) -> None: ...
    def call(self, sequence_output, pooled_output): ...

class TFLxmertVisualAnswerHead(tf.keras.layers.Layer):
    dense: Incomplete
    activation: Incomplete
    layer_norm: Incomplete
    dense_1: Incomplete
    def __init__(self, config, num_labels, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFLxmertVisualObjHead(tf.keras.layers.Layer):
    transform: Incomplete
    visual_losses: Incomplete
    decoder_dict: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFLxmertForPreTraining(TFLxmertPreTrainedModel):
    config: Incomplete
    num_qa_labels: Incomplete
    visual_loss_normalizer: Incomplete
    task_mask_lm: Incomplete
    task_obj_predict: Incomplete
    task_matched: Incomplete
    task_qa: Incomplete
    lxmert: Incomplete
    cls: Incomplete
    obj_predict_head: Incomplete
    answer_head: Incomplete
    loss_fcts: Incomplete
    visual_losses: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def call(self, input_ids: Incomplete | None = None, visual_feats: Incomplete | None = None, visual_pos: Incomplete | None = None, attention_mask: Incomplete | None = None, visual_attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, masked_lm_labels: Incomplete | None = None, obj_labels: Incomplete | None = None, matched_label: Incomplete | None = None, ans: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False):
        """
        masked_lm_labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        obj_labels: (`Dict[Str: Tuple[tf.Tensor, tf.Tensor]]`, *optional*, defaults to `None`):
            each key is named after each one of the visual losses and each element of the tuple is of the shape
            `(batch_size, num_features)` and `(batch_size, num_features, visual_feature_dim)` for each the label id and
            the label score respectively
        matched_label (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the whether or not the text input matches the image (classification) loss. Input
            should be a sequence pair (see `input_ids` docstring) Indices should be in `[0, 1]`:

            - 0 indicates that the sentence does not match the image,
            - 1 indicates that the sentence does match the image.
        ans (`Torch.Tensor` of shape `(batch_size)`, *optional*, defaults to `None`):
            a one hot representation hof the correct answer *optional*

        Returns:
        """
    def serving_output(self, output): ...
