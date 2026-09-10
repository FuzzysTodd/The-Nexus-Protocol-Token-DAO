import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, replace_return_docstrings as replace_return_docstrings
from .configuration_layoutlmv3 import LayoutLMv3Config as LayoutLMv3Config
from _typeshed import Incomplete
from typing import Dict, List, Optional, Tuple, Union

TF_LAYOUTLMV3_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
LARGE_NEGATIVE: float

class TFLayoutLMv3PatchEmbeddings(tf.keras.layers.Layer):
    """LayoutLMv3 image (patch) embeddings."""
    proj: Incomplete
    hidden_size: Incomplete
    num_patches: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor) -> tf.Tensor: ...

class TFLayoutLMv3TextEmbeddings(tf.keras.layers.Layer):
    """
    LayoutLMv3 text embeddings. Same as `RobertaEmbeddings` but with added spatial (layout) embeddings.
    """
    word_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    padding_token_index: Incomplete
    position_embeddings: Incomplete
    x_position_embeddings: Incomplete
    y_position_embeddings: Incomplete
    h_position_embeddings: Incomplete
    w_position_embeddings: Incomplete
    max_2d_positions: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def calculate_spatial_position_embeddings(self, bbox: tf.Tensor) -> tf.Tensor: ...
    def create_position_ids_from_inputs_embeds(self, inputs_embds: tf.Tensor) -> tf.Tensor:
        """
        We are provided embeddings directly. We cannot infer which are padded, so just generate sequential position
        ids.
        """
    def create_position_ids_from_input_ids(self, input_ids: tf.Tensor) -> tf.Tensor:
        """
        Replace non-padding symbols with their position numbers. Position numbers begin at padding_token_index + 1.
        """
    def create_position_ids(self, input_ids: tf.Tensor, inputs_embeds: tf.Tensor) -> tf.Tensor: ...
    def call(self, input_ids: Optional[tf.Tensor] = None, bbox: tf.Tensor = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, training: bool = False) -> tf.Tensor: ...

class TFLayoutLMv3SelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    attention_score_normaliser: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    has_relative_attention_bias: Incomplete
    has_spatial_attention_bias: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def transpose_for_scores(self, x: tf.Tensor): ...
    def cogview_attention(self, attention_scores: tf.Tensor, alpha: Union[float, int] = 32):
        """
        https://arxiv.org/abs/2105.13290 Section 2.4 Stabilization of training: Precision Bottleneck Relaxation
        (PB-Relax). A replacement of the original tf.keras.layers.Softmax(axis=-1)(attention_scores). Seems the new
        attention_probs will result in a slower speed and a little bias. Can use
        tf.debugging.assert_near(standard_attention_probs, cogview_attention_probs, atol=1e-08) for comparison. The
        smaller atol (e.g., 1e-08), the better.
        """
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor], head_mask: Optional[tf.Tensor], output_attentions: bool, rel_pos: Optional[tf.Tensor] = None, rel_2d_pos: Optional[tf.Tensor] = None, training: bool = False) -> Union[Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor]]: ...

class TFLayoutLMv3SelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFLayoutLMv3Attention(tf.keras.layers.Layer):
    self_attention: Incomplete
    self_output: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor], head_mask: Optional[tf.Tensor], output_attentions: bool, rel_pos: Optional[tf.Tensor] = None, rel_2d_pos: Optional[tf.Tensor] = None, training: bool = False) -> Union[Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor]]: ...

class TFLayoutLMv3Intermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFLayoutLMv3Output(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFLayoutLMv3Layer(tf.keras.layers.Layer):
    attention: Incomplete
    intermediate: Incomplete
    bert_output: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor], head_mask: Optional[tf.Tensor], output_attentions: bool, rel_pos: Optional[tf.Tensor] = None, rel_2d_pos: Optional[tf.Tensor] = None, training: bool = False) -> Union[Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor]]: ...

class TFLayoutLMv3Encoder(tf.keras.layers.Layer):
    config: Incomplete
    layer: Incomplete
    has_relative_attention_bias: Incomplete
    has_spatial_attention_bias: Incomplete
    rel_pos_bins: Incomplete
    max_rel_pos: Incomplete
    rel_pos_bias: Incomplete
    max_rel_2d_pos: Incomplete
    rel_2d_pos_bins: Incomplete
    rel_pos_x_bias: Incomplete
    rel_pos_y_bias: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def relative_position_bucket(self, relative_positions: tf.Tensor, num_buckets: int, max_distance: int): ...
    def call(self, hidden_states: tf.Tensor, bbox: Optional[tf.Tensor] = None, attention_mask: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, position_ids: Optional[tf.Tensor] = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor]]: ...

class TFLayoutLMv3MainLayer(tf.keras.layers.Layer):
    config_class = LayoutLMv3Config
    config: Incomplete
    embeddings: Incomplete
    patch_embed: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    norm: Incomplete
    encoder: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    cls_token: Incomplete
    pos_embed: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_input_embeddings(self, value: tf.Variable): ...
    visual_bbox: Incomplete
    def init_visual_bbox(self, image_size: Tuple[int, int], max_len: int = 1000): ...
    def calculate_visual_bbox(self, batch_size: int, dtype: tf.DType): ...
    def embed_image(self, pixel_values: tf.Tensor) -> tf.Tensor: ...
    def get_extended_attention_mask(self, attention_mask: tf.Tensor) -> tf.Tensor: ...
    def get_head_mask(self, head_mask: Optional[tf.Tensor]) -> Union[tf.Tensor, List[Optional[tf.Tensor]]]: ...
    def call(self, input_ids: Optional[tf.Tensor] = None, bbox: Optional[tf.Tensor] = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, pixel_values: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor]]: ...

class TFLayoutLMv3PreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LayoutLMv3Config
    base_model_prefix: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]: ...
    def serving(self, inputs):
        """
        Method used for serving the model.

        Args:
            inputs (`Dict[str, tf.Tensor]`):
                The input of the saved model as a dictionary of tensors.
        """

LAYOUTLMV3_START_DOCSTRING: str
LAYOUTLMV3_INPUTS_DOCSTRING: str

class TFLayoutLMv3Model(TFLayoutLMv3PreTrainedModel):
    layoutlmv3: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[tf.Tensor] = None, bbox: Optional[tf.Tensor] = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, pixel_values: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, TFAutoModel
        >>> from datasets import load_dataset

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = TFAutoModel.from_pretrained("microsoft/layoutlmv3-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = processor(image, words, boxes=boxes, return_tensors="tf")

        >>> outputs = model(**encoding)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
    def serving_output(self, output: TFBaseModelOutput) -> TFBaseModelOutput: ...

class TFLayoutLMv3ClassificationHead(tf.keras.layers.Layer):
    """
    Head for sentence-level classification tasks. Reference: RobertaClassificationHead
    """
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, inputs: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFLayoutLMv3ForSequenceClassification(TFLayoutLMv3PreTrainedModel, TFSequenceClassificationLoss):
    config: Incomplete
    layoutlmv3: Incomplete
    classifier: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, input_ids: Optional[tf.Tensor] = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, labels: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, bbox: Optional[tf.Tensor] = None, pixel_values: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor, tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, TFAutoModelForSequenceClassification
        >>> from datasets import load_dataset
        >>> import tensorflow as tf

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = TFAutoModelForSequenceClassification.from_pretrained("microsoft/layoutlmv3-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = processor(image, words, boxes=boxes, return_tensors="tf")
        >>> sequence_label = tf.convert_to_tensor([1])

        >>> outputs = model(**encoding, labels=sequence_label)
        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```'''
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFLayoutLMv3ForTokenClassification(TFLayoutLMv3PreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    layoutlmv3: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, input_ids: Optional[tf.Tensor] = None, bbox: Optional[tf.Tensor] = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, labels: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, pixel_values: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor, tf.Tensor]]:
        '''
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, TFAutoModelForTokenClassification
        >>> from datasets import load_dataset

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = TFAutoModelForTokenClassification.from_pretrained("microsoft/layoutlmv3-base", num_labels=7)

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]
        >>> word_labels = example["ner_tags"]

        >>> encoding = processor(image, words, boxes=boxes, word_labels=word_labels, return_tensors="tf")

        >>> outputs = model(**encoding)
        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```'''
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFLayoutLMv3ForQuestionAnswering(TFLayoutLMv3PreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    layoutlmv3: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None: ...
    def call(self, input_ids: Optional[tf.Tensor] = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, start_positions: Optional[tf.Tensor] = None, end_positions: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, bbox: Optional[tf.Tensor] = None, pixel_values: Optional[tf.Tensor] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor, tf.Tensor]]:
        '''
        start_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, TFAutoModelForQuestionAnswering
        >>> from datasets import load_dataset
        >>> import tensorflow as tf

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = TFAutoModelForQuestionAnswering.from_pretrained("microsoft/layoutlmv3-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> question = "what\'s his name?"
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = processor(image, question, words, boxes=boxes, return_tensors="tf")
        >>> start_positions = tf.convert_to_tensor([1])
        >>> end_positions = tf.convert_to_tensor([3])

        >>> outputs = model(**encoding, start_positions=start_positions, end_positions=end_positions)
        >>> loss = outputs.loss
        >>> start_scores = outputs.start_logits
        >>> end_scores = outputs.end_logits
        ```'''
    def serving_output(self, output: TFQuestionAnsweringModelOutput) -> TFQuestionAnsweringModelOutput: ...
