import tensorflow as tf
from ...modeling_tf_outputs import TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, get_initializer as get_initializer, shape_list as shape_list, unpack_inputs as unpack_inputs
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from ..bert.modeling_tf_bert import TFBertMainLayer as TFBertMainLayer
from .configuration_dpr import DPRConfig as DPRConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Optional, Tuple, Union

logger: Incomplete
TF_DPR_CONTEXT_ENCODER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
TF_DPR_QUESTION_ENCODER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
TF_DPR_READER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class TFDPRContextEncoderOutput(ModelOutput):
    """
    Class for outputs of [`TFDPRContextEncoder`].

    Args:
        pooler_output (`tf.Tensor` of shape `(batch_size, embeddings_size)`):
            The DPR encoder outputs the *pooler_output* that corresponds to the context representation. Last layer
            hidden-state of the first token of the sequence (classification token) further processed by a Linear layer.
            This output is to be used to embed contexts for nearest neighbors queries with questions embeddings.
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
    pooler_output: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, pooler_output, hidden_states, attentions) -> None: ...

@dataclass
class TFDPRQuestionEncoderOutput(ModelOutput):
    """
    Class for outputs of [`TFDPRQuestionEncoder`].

    Args:
        pooler_output (`tf.Tensor` of shape `(batch_size, embeddings_size)`):
            The DPR encoder outputs the *pooler_output* that corresponds to the question representation. Last layer
            hidden-state of the first token of the sequence (classification token) further processed by a Linear layer.
            This output is to be used to embed questions for nearest neighbors queries with context embeddings.
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
    pooler_output: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, pooler_output, hidden_states, attentions) -> None: ...

@dataclass
class TFDPRReaderOutput(ModelOutput):
    """
    Class for outputs of [`TFDPRReaderEncoder`].

    Args:
        start_logits (`tf.Tensor` of shape `(n_passages, sequence_length)`):
            Logits of the start index of the span for each passage.
        end_logits (`tf.Tensor` of shape `(n_passages, sequence_length)`):
            Logits of the end index of the span for each passage.
        relevance_logits (`tf.Tensor` of shape `(n_passages, )`):
            Outputs of the QA classifier of the DPRReader that corresponds to the scores of each passage to answer the
            question, compared to all the other passages.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    start_logits: tf.Tensor = ...
    end_logits: tf.Tensor = ...
    relevance_logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, start_logits, end_logits, relevance_logits, hidden_states, attentions) -> None: ...

class TFDPREncoderLayer(tf.keras.layers.Layer):
    base_model_prefix: str
    bert_model: Incomplete
    config: Incomplete
    projection_dim: Incomplete
    encode_proj: Incomplete
    def __init__(self, config: DPRConfig, **kwargs) -> None: ...
    def call(self, input_ids: tf.Tensor = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: bool = None, output_hidden_states: bool = None, return_dict: bool = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor, ...]]: ...
    @property
    def embeddings_size(self) -> int: ...

class TFDPRSpanPredictorLayer(tf.keras.layers.Layer):
    base_model_prefix: str
    config: Incomplete
    encoder: Incomplete
    qa_outputs: Incomplete
    qa_classifier: Incomplete
    def __init__(self, config: DPRConfig, **kwargs) -> None: ...
    def call(self, input_ids: tf.Tensor = None, attention_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = False, training: bool = False) -> Union[TFDPRReaderOutput, Tuple[tf.Tensor, ...]]: ...

class TFDPRSpanPredictor(TFPreTrainedModel):
    base_model_prefix: str
    encoder: Incomplete
    def __init__(self, config: DPRConfig, **kwargs) -> None: ...
    def call(self, input_ids: tf.Tensor = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = False, training: bool = False) -> Union[TFDPRReaderOutput, Tuple[tf.Tensor, ...]]: ...

class TFDPREncoder(TFPreTrainedModel):
    base_model_prefix: str
    encoder: Incomplete
    def __init__(self, config: DPRConfig, **kwargs) -> None: ...
    def call(self, input_ids: tf.Tensor = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = False, training: bool = False) -> Union[TFDPRReaderOutput, Tuple[tf.Tensor, ...]]: ...

class TFDPRPretrainedContextEncoder(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DPRConfig
    base_model_prefix: str

class TFDPRPretrainedQuestionEncoder(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DPRConfig
    base_model_prefix: str

class TFDPRPretrainedReader(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DPRConfig
    base_model_prefix: str
    def serving(self, inputs): ...

TF_DPR_START_DOCSTRING: str
TF_DPR_ENCODERS_INPUTS_DOCSTRING: str
TF_DPR_READER_INPUTS_DOCSTRING: str

class TFDPRContextEncoder(TFDPRPretrainedContextEncoder):
    ctx_encoder: Incomplete
    def __init__(self, config: DPRConfig, *args, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False) -> Union[TFDPRContextEncoderOutput, Tuple[tf.Tensor, ...]]:
        '''
        Return:

        Examples:

        ```python
        >>> from transformers import TFDPRContextEncoder, DPRContextEncoderTokenizer

        >>> tokenizer = DPRContextEncoderTokenizer.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")
        >>> model = TFDPRContextEncoder.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base", from_pt=True)
        >>> input_ids = tokenizer("Hello, is my dog cute ?", return_tensors="tf")["input_ids"]
        >>> embeddings = model(input_ids).pooler_output
        ```
        '''
    def serving_output(self, output): ...

class TFDPRQuestionEncoder(TFDPRPretrainedQuestionEncoder):
    question_encoder: Incomplete
    def __init__(self, config: DPRConfig, *args, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False) -> Union[TFDPRQuestionEncoderOutput, Tuple[tf.Tensor, ...]]:
        '''
        Return:

        Examples:

        ```python
        >>> from transformers import TFDPRQuestionEncoder, DPRQuestionEncoderTokenizer

        >>> tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
        >>> model = TFDPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base", from_pt=True)
        >>> input_ids = tokenizer("Hello, is my dog cute ?", return_tensors="tf")["input_ids"]
        >>> embeddings = model(input_ids).pooler_output
        ```
        '''
    def serving_output(self, output): ...

class TFDPRReader(TFDPRPretrainedReader):
    span_predictor: Incomplete
    def __init__(self, config: DPRConfig, *args, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: bool = None, output_hidden_states: bool = None, return_dict: Incomplete | None = None, training: bool = False) -> Union[TFDPRReaderOutput, Tuple[tf.Tensor, ...]]:
        '''
        Return:

        Examples:

        ```python
        >>> from transformers import TFDPRReader, DPRReaderTokenizer

        >>> tokenizer = DPRReaderTokenizer.from_pretrained("facebook/dpr-reader-single-nq-base")
        >>> model = TFDPRReader.from_pretrained("facebook/dpr-reader-single-nq-base", from_pt=True)
        >>> encoded_inputs = tokenizer(
        ...     questions=["What is love ?"],
        ...     titles=["Haddaway"],
        ...     texts=["\'What Is Love\' is a song recorded by the artist Haddaway"],
        ...     return_tensors="tf",
        ... )
        >>> outputs = model(encoded_inputs)
        >>> start_logits = outputs.start_logits
        >>> end_logits = outputs.end_logits
        >>> relevance_logits = outputs.relevance_logits
        ```
        '''
    def serving_output(self, output): ...
