import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFBaseModelOutputWithPoolingAndCrossAttentions as TFBaseModelOutputWithPoolingAndCrossAttentions, TFMaskedLMOutput as TFMaskedLMOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_layoutlm import LayoutLMConfig as LayoutLMConfig
from _typeshed import Incomplete
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_LAYOUTLM_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFLayoutLMEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: Incomplete
    hidden_size: Incomplete
    max_position_embeddings: Incomplete
    max_2d_position_embeddings: Incomplete
    initializer_range: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    weight: Incomplete
    token_type_embeddings: Incomplete
    position_embeddings: Incomplete
    x_position_embeddings: Incomplete
    y_position_embeddings: Incomplete
    h_position_embeddings: Incomplete
    w_position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, input_ids: tf.Tensor = None, bbox: tf.Tensor = None, position_ids: tf.Tensor = None, token_type_ids: tf.Tensor = None, inputs_embeds: tf.Tensor = None, training: bool = False) -> tf.Tensor:
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFLayoutLMSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    is_decoder: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: tf.Tensor, encoder_attention_mask: tf.Tensor, past_key_value: Tuple[tf.Tensor], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFLayoutLMSelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFLayoutLMAttention(tf.keras.layers.Layer):
    self_attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: tf.Tensor, encoder_attention_mask: tf.Tensor, past_key_value: Tuple[tf.Tensor], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFLayoutLMIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFLayoutLMOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFLayoutLMLayer(tf.keras.layers.Layer):
    attention: Incomplete
    is_decoder: Incomplete
    add_cross_attention: Incomplete
    crossattention: Incomplete
    intermediate: Incomplete
    bert_output: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: Optional[tf.Tensor], encoder_attention_mask: Optional[tf.Tensor], past_key_value: Optional[Tuple[tf.Tensor]], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFLayoutLMEncoder(tf.keras.layers.Layer):
    config: Incomplete
    layer: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: Optional[tf.Tensor], encoder_attention_mask: Optional[tf.Tensor], past_key_values: Optional[Tuple[Tuple[tf.Tensor]]], use_cache: Optional[bool], output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutputWithPastAndCrossAttentions, Tuple[tf.Tensor]]: ...

class TFLayoutLMPooler(tf.keras.layers.Layer):
    dense: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFLayoutLMPredictionHeadTransform(tf.keras.layers.Layer):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config: LayoutLMConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFLayoutLMLMPredictionHead(tf.keras.layers.Layer):
    config: Incomplete
    hidden_size: Incomplete
    transform: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config: LayoutLMConfig, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def get_output_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_output_embeddings(self, value: tf.Variable): ...
    def get_bias(self) -> Dict[str, tf.Variable]: ...
    def set_bias(self, value: tf.Variable): ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFLayoutLMMLMHead(tf.keras.layers.Layer):
    predictions: Incomplete
    def __init__(self, config: LayoutLMConfig, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    def call(self, sequence_output: tf.Tensor) -> tf.Tensor: ...

class TFLayoutLMMainLayer(tf.keras.layers.Layer):
    config_class = LayoutLMConfig
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config: LayoutLMConfig, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_input_embeddings(self, value: tf.Variable): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, bbox: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPoolingAndCrossAttentions, Tuple[tf.Tensor]]: ...

class TFLayoutLMPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LayoutLMConfig
    base_model_prefix: str

LAYOUTLM_START_DOCSTRING: str
LAYOUTLM_INPUTS_DOCSTRING: str

class TFLayoutLMModel(TFLayoutLMPreTrainedModel):
    layoutlm: Incomplete
    def __init__(self, config: LayoutLMConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, bbox: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPoolingAndCrossAttentions, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFLayoutLMModel
        >>> import tensorflow as tf

        >>> tokenizer = AutoTokenizer.from_pretrained("microsoft/layoutlm-base-uncased")
        >>> model = TFLayoutLMModel.from_pretrained("microsoft/layoutlm-base-uncased")

        >>> words = ["Hello", "world"]
        >>> normalized_word_boxes = [637, 773, 693, 782], [698, 773, 733, 782]

        >>> token_boxes = []
        >>> for word, box in zip(words, normalized_word_boxes):
        ...     word_tokens = tokenizer.tokenize(word)
        ...     token_boxes.extend([box] * len(word_tokens))
        >>> # add bounding boxes of cls + sep tokens
        >>> token_boxes = [[0, 0, 0, 0]] + token_boxes + [[1000, 1000, 1000, 1000]]

        >>> encoding = tokenizer(" ".join(words), return_tensors="tf")
        >>> input_ids = encoding["input_ids"]
        >>> attention_mask = encoding["attention_mask"]
        >>> token_type_ids = encoding["token_type_ids"]
        >>> bbox = tf.convert_to_tensor([token_boxes])

        >>> outputs = model(
        ...     input_ids=input_ids, bbox=bbox, attention_mask=attention_mask, token_type_ids=token_type_ids
        ... )

        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
    def serving_output(self, output: TFBaseModelOutputWithPoolingAndCrossAttentions) -> TFBaseModelOutputWithPoolingAndCrossAttentions: ...

class TFLayoutLMForMaskedLM(TFLayoutLMPreTrainedModel, TFMaskedLanguageModelingLoss):
    layoutlm: Incomplete
    mlm: Incomplete
    def __init__(self, config: LayoutLMConfig, *inputs, **kwargs) -> None: ...
    def get_lm_head(self) -> tf.keras.layers.Layer: ...
    def get_prefix_bias_name(self) -> str: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, bbox: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMaskedLMOutput, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFLayoutLMForMaskedLM
        >>> import tensorflow as tf

        >>> tokenizer = AutoTokenizer.from_pretrained("microsoft/layoutlm-base-uncased")
        >>> model = TFLayoutLMForMaskedLM.from_pretrained("microsoft/layoutlm-base-uncased")

        >>> words = ["Hello", "[MASK]"]
        >>> normalized_word_boxes = [637, 773, 693, 782], [698, 773, 733, 782]

        >>> token_boxes = []
        >>> for word, box in zip(words, normalized_word_boxes):
        ...     word_tokens = tokenizer.tokenize(word)
        ...     token_boxes.extend([box] * len(word_tokens))
        >>> # add bounding boxes of cls + sep tokens
        >>> token_boxes = [[0, 0, 0, 0]] + token_boxes + [[1000, 1000, 1000, 1000]]

        >>> encoding = tokenizer(" ".join(words), return_tensors="tf")
        >>> input_ids = encoding["input_ids"]
        >>> attention_mask = encoding["attention_mask"]
        >>> token_type_ids = encoding["token_type_ids"]
        >>> bbox = tf.convert_to_tensor([token_boxes])

        >>> labels = tokenizer("Hello world", return_tensors="tf")["input_ids"]

        >>> outputs = model(
        ...     input_ids=input_ids,
        ...     bbox=bbox,
        ...     attention_mask=attention_mask,
        ...     token_type_ids=token_type_ids,
        ...     labels=labels,
        ... )

        >>> loss = outputs.loss
        ```'''
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFLayoutLMForSequenceClassification(TFLayoutLMPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    layoutlm: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: LayoutLMConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, bbox: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFLayoutLMForSequenceClassification
        >>> import tensorflow as tf

        >>> tokenizer = AutoTokenizer.from_pretrained("microsoft/layoutlm-base-uncased")
        >>> model = TFLayoutLMForSequenceClassification.from_pretrained("microsoft/layoutlm-base-uncased")

        >>> words = ["Hello", "world"]
        >>> normalized_word_boxes = [637, 773, 693, 782], [698, 773, 733, 782]

        >>> token_boxes = []
        >>> for word, box in zip(words, normalized_word_boxes):
        ...     word_tokens = tokenizer.tokenize(word)
        ...     token_boxes.extend([box] * len(word_tokens))
        >>> # add bounding boxes of cls + sep tokens
        >>> token_boxes = [[0, 0, 0, 0]] + token_boxes + [[1000, 1000, 1000, 1000]]

        >>> encoding = tokenizer(" ".join(words), return_tensors="tf")
        >>> input_ids = encoding["input_ids"]
        >>> attention_mask = encoding["attention_mask"]
        >>> token_type_ids = encoding["token_type_ids"]
        >>> bbox = tf.convert_to_tensor([token_boxes])
        >>> sequence_label = tf.convert_to_tensor([1])

        >>> outputs = model(
        ...     input_ids=input_ids,
        ...     bbox=bbox,
        ...     attention_mask=attention_mask,
        ...     token_type_ids=token_type_ids,
        ...     labels=sequence_label,
        ... )

        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```'''
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFLayoutLMForTokenClassification(TFLayoutLMPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    layoutlm: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: LayoutLMConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, bbox: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFLayoutLMForTokenClassification

        >>> tokenizer = AutoTokenizer.from_pretrained("microsoft/layoutlm-base-uncased")
        >>> model = TFLayoutLMForTokenClassification.from_pretrained("microsoft/layoutlm-base-uncased")

        >>> words = ["Hello", "world"]
        >>> normalized_word_boxes = [637, 773, 693, 782], [698, 773, 733, 782]

        >>> token_boxes = []
        >>> for word, box in zip(words, normalized_word_boxes):
        ...     word_tokens = tokenizer.tokenize(word)
        ...     token_boxes.extend([box] * len(word_tokens))
        >>> # add bounding boxes of cls + sep tokens
        >>> token_boxes = [[0, 0, 0, 0]] + token_boxes + [[1000, 1000, 1000, 1000]]

        >>> encoding = tokenizer(" ".join(words), return_tensors="tf")
        >>> input_ids = encoding["input_ids"]
        >>> attention_mask = encoding["attention_mask"]
        >>> token_type_ids = encoding["token_type_ids"]
        >>> bbox = tf.convert_to_tensor([token_boxes])
        >>> token_labels = tf.convert_to_tensor([1, 1, 0, 0])

        >>> outputs = model(
        ...     input_ids=input_ids,
        ...     bbox=bbox,
        ...     attention_mask=attention_mask,
        ...     token_type_ids=token_type_ids,
        ...     labels=token_labels,
        ... )

        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```'''
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFLayoutLMForQuestionAnswering(TFLayoutLMPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    layoutlm: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config: LayoutLMConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, bbox: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor]]:
        '''
        start_positions (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.

        Returns:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFLayoutLMForQuestionAnswering
        >>> from datasets import load_dataset

        >>> tokenizer = AutoTokenizer.from_pretrained("impira/layoutlm-document-qa", add_prefix_space=True)
        >>> model = TFLayoutLMForQuestionAnswering.from_pretrained("impira/layoutlm-document-qa", revision="1e3ebac")

        >>> dataset = load_dataset("nielsr/funsd", split="train")
        >>> example = dataset[0]
        >>> question = "what\'s his name?"
        >>> words = example["words"]
        >>> boxes = example["bboxes"]

        >>> encoding = tokenizer(
        ...     question.split(), words, is_split_into_words=True, return_token_type_ids=True, return_tensors="tf"
        ... )
        >>> bbox = []
        >>> for i, s, w in zip(encoding.input_ids[0], encoding.sequence_ids(0), encoding.word_ids(0)):
        ...     if s == 1:
        ...         bbox.append(boxes[w])
        ...     elif i == tokenizer.sep_token_id:
        ...         bbox.append([1000] * 4)
        ...     else:
        ...         bbox.append([0] * 4)
        >>> encoding["bbox"] = tf.convert_to_tensor([bbox])

        >>> word_ids = encoding.word_ids(0)
        >>> outputs = model(**encoding)
        >>> loss = outputs.loss
        >>> start_scores = outputs.start_logits
        >>> end_scores = outputs.end_logits
        >>> start, end = word_ids[tf.math.argmax(start_scores, -1)[0]], word_ids[tf.math.argmax(end_scores, -1)[0]]
        >>> print(" ".join(words[start : end + 1]))
        M. Hamann P. Harper, P. Martinez
        ```'''
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...
