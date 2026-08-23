import torch
from ...modeling_outputs import BaseModelOutputWithPooling as BaseModelOutputWithPooling
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from ..bert.modeling_bert import BertEncoder as BertEncoder, BertModel as BertModel
from .configuration_dpr import DPRConfig as DPRConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import Tensor as Tensor
from typing import Optional, Tuple, Union

logger: Incomplete
DPR_CONTEXT_ENCODER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
DPR_QUESTION_ENCODER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
DPR_READER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class DPRContextEncoderOutput(ModelOutput):
    """
    Class for outputs of [`DPRQuestionEncoder`].

    Args:
        pooler_output (`torch.FloatTensor` of shape `(batch_size, embeddings_size)`):
            The DPR encoder outputs the *pooler_output* that corresponds to the context representation. Last layer
            hidden-state of the first token of the sequence (classification token) further processed by a Linear layer.
            This output is to be used to embed contexts for nearest neighbors queries with questions embeddings.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    pooler_output: torch.FloatTensor
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, pooler_output, hidden_states, attentions) -> None: ...

@dataclass
class DPRQuestionEncoderOutput(ModelOutput):
    """
    Class for outputs of [`DPRQuestionEncoder`].

    Args:
        pooler_output (`torch.FloatTensor` of shape `(batch_size, embeddings_size)`):
            The DPR encoder outputs the *pooler_output* that corresponds to the question representation. Last layer
            hidden-state of the first token of the sequence (classification token) further processed by a Linear layer.
            This output is to be used to embed questions for nearest neighbors queries with context embeddings.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    pooler_output: torch.FloatTensor
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, pooler_output, hidden_states, attentions) -> None: ...

@dataclass
class DPRReaderOutput(ModelOutput):
    """
    Class for outputs of [`DPRQuestionEncoder`].

    Args:
        start_logits (`torch.FloatTensor` of shape `(n_passages, sequence_length)`):
            Logits of the start index of the span for each passage.
        end_logits (`torch.FloatTensor` of shape `(n_passages, sequence_length)`):
            Logits of the end index of the span for each passage.
        relevance_logits (`torch.FloatTensor` of shape `(n_passages, )`):
            Outputs of the QA classifier of the DPRReader that corresponds to the scores of each passage to answer the
            question, compared to all the other passages.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    start_logits: torch.FloatTensor
    end_logits: torch.FloatTensor = ...
    relevance_logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, start_logits, end_logits, relevance_logits, hidden_states, attentions) -> None: ...

class DPRPreTrainedModel(PreTrainedModel): ...

class DPREncoder(DPRPreTrainedModel):
    base_model_prefix: str
    bert_model: Incomplete
    projection_dim: Incomplete
    encode_proj: Incomplete
    def __init__(self, config: DPRConfig) -> None: ...
    def forward(self, input_ids: Tensor, attention_mask: Optional[Tensor] = None, token_type_ids: Optional[Tensor] = None, inputs_embeds: Optional[Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = False) -> Union[BaseModelOutputWithPooling, Tuple[Tensor, ...]]: ...
    @property
    def embeddings_size(self) -> int: ...

class DPRSpanPredictor(DPRPreTrainedModel):
    base_model_prefix: str
    encoder: Incomplete
    qa_outputs: Incomplete
    qa_classifier: Incomplete
    def __init__(self, config: DPRConfig) -> None: ...
    def forward(self, input_ids: Tensor, attention_mask: Tensor, inputs_embeds: Optional[Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = False) -> Union[DPRReaderOutput, Tuple[Tensor, ...]]: ...

class DPRPretrainedContextEncoder(DPRPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DPRConfig
    load_tf_weights: Incomplete
    base_model_prefix: str

class DPRPretrainedQuestionEncoder(DPRPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DPRConfig
    load_tf_weights: Incomplete
    base_model_prefix: str

class DPRPretrainedReader(DPRPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DPRConfig
    load_tf_weights: Incomplete
    base_model_prefix: str

DPR_START_DOCSTRING: str
DPR_ENCODERS_INPUTS_DOCSTRING: str
DPR_READER_INPUTS_DOCSTRING: str

class DPRContextEncoder(DPRPretrainedContextEncoder):
    config: Incomplete
    ctx_encoder: Incomplete
    def __init__(self, config: DPRConfig) -> None: ...
    def forward(self, input_ids: Optional[Tensor] = None, attention_mask: Optional[Tensor] = None, token_type_ids: Optional[Tensor] = None, inputs_embeds: Optional[Tensor] = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None) -> Union[DPRContextEncoderOutput, Tuple[Tensor, ...]]:
        '''
        Return:

        Examples:

        ```python
        >>> from transformers import DPRContextEncoder, DPRContextEncoderTokenizer

        >>> tokenizer = DPRContextEncoderTokenizer.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")
        >>> model = DPRContextEncoder.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")
        >>> input_ids = tokenizer("Hello, is my dog cute ?", return_tensors="pt")["input_ids"]
        >>> embeddings = model(input_ids).pooler_output
        ```'''

class DPRQuestionEncoder(DPRPretrainedQuestionEncoder):
    config: Incomplete
    question_encoder: Incomplete
    def __init__(self, config: DPRConfig) -> None: ...
    def forward(self, input_ids: Optional[Tensor] = None, attention_mask: Optional[Tensor] = None, token_type_ids: Optional[Tensor] = None, inputs_embeds: Optional[Tensor] = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None) -> Union[DPRQuestionEncoderOutput, Tuple[Tensor, ...]]:
        '''
        Return:

        Examples:

        ```python
        >>> from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer

        >>> tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
        >>> model = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
        >>> input_ids = tokenizer("Hello, is my dog cute ?", return_tensors="pt")["input_ids"]
        >>> embeddings = model(input_ids).pooler_output
        ```
        '''

class DPRReader(DPRPretrainedReader):
    config: Incomplete
    span_predictor: Incomplete
    def __init__(self, config: DPRConfig) -> None: ...
    def forward(self, input_ids: Optional[Tensor] = None, attention_mask: Optional[Tensor] = None, inputs_embeds: Optional[Tensor] = None, output_attentions: bool = None, output_hidden_states: bool = None, return_dict: Incomplete | None = None) -> Union[DPRReaderOutput, Tuple[Tensor, ...]]:
        '''
        Return:

        Examples:

        ```python
        >>> from transformers import DPRReader, DPRReaderTokenizer

        >>> tokenizer = DPRReaderTokenizer.from_pretrained("facebook/dpr-reader-single-nq-base")
        >>> model = DPRReader.from_pretrained("facebook/dpr-reader-single-nq-base")
        >>> encoded_inputs = tokenizer(
        ...     questions=["What is love ?"],
        ...     titles=["Haddaway"],
        ...     texts=["\'What Is Love\' is a song recorded by the artist Haddaway"],
        ...     return_tensors="pt",
        ... )
        >>> outputs = model(**encoded_inputs)
        >>> start_logits = outputs.start_logits
        >>> end_logits = outputs.end_logits
        >>> relevance_logits = outputs.relevance_logits
        ```
        '''
