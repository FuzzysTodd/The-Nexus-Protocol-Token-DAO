from ...tokenization_utils_base import BatchEncoding as BatchEncoding
from ...utils import TensorType as TensorType, add_end_docstrings as add_end_docstrings, add_start_docstrings as add_start_docstrings, logging as logging
from ..bert.tokenization_bert import BertTokenizer as BertTokenizer
from _typeshed import Incomplete
from typing import List, NamedTuple, Optional, Union

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
CONTEXT_ENCODER_PRETRAINED_VOCAB_FILES_MAP: Incomplete
QUESTION_ENCODER_PRETRAINED_VOCAB_FILES_MAP: Incomplete
READER_PRETRAINED_VOCAB_FILES_MAP: Incomplete
CONTEXT_ENCODER_PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
QUESTION_ENCODER_PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
READER_PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
CONTEXT_ENCODER_PRETRAINED_INIT_CONFIGURATION: Incomplete
QUESTION_ENCODER_PRETRAINED_INIT_CONFIGURATION: Incomplete
READER_PRETRAINED_INIT_CONFIGURATION: Incomplete

class DPRContextEncoderTokenizer(BertTokenizer):
    """
    Construct a DPRContextEncoder tokenizer.

    [`DPRContextEncoderTokenizer`] is identical to [`BertTokenizer`] and runs end-to-end tokenization: punctuation
    splitting and wordpiece.

    Refer to superclass [`BertTokenizer`] for usage examples and documentation concerning parameters.
    """
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = CONTEXT_ENCODER_PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = CONTEXT_ENCODER_PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_init_configuration = CONTEXT_ENCODER_PRETRAINED_INIT_CONFIGURATION

class DPRQuestionEncoderTokenizer(BertTokenizer):
    """
    Constructs a DPRQuestionEncoder tokenizer.

    [`DPRQuestionEncoderTokenizer`] is identical to [`BertTokenizer`] and runs end-to-end tokenization: punctuation
    splitting and wordpiece.

    Refer to superclass [`BertTokenizer`] for usage examples and documentation concerning parameters.
    """
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = QUESTION_ENCODER_PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = QUESTION_ENCODER_PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_init_configuration = QUESTION_ENCODER_PRETRAINED_INIT_CONFIGURATION

class DPRSpanPrediction(NamedTuple):
    span_score: Incomplete
    relevance_score: Incomplete
    doc_id: Incomplete
    start_index: Incomplete
    end_index: Incomplete
    text: Incomplete

class DPRReaderOutput(NamedTuple):
    start_logits: Incomplete
    end_logits: Incomplete
    relevance_logits: Incomplete

CUSTOM_DPR_READER_DOCSTRING: str

class CustomDPRReaderTokenizerMixin:
    def __call__(self, questions, titles: Optional[str] = None, texts: Optional[str] = None, padding: Union[bool, str] = False, truncation: Union[bool, str] = False, max_length: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_attention_mask: Optional[bool] = None, **kwargs) -> BatchEncoding: ...
    def decode_best_spans(self, reader_input: BatchEncoding, reader_output: DPRReaderOutput, num_spans: int = 16, max_answer_length: int = 64, num_spans_per_passage: int = 4) -> List[DPRSpanPrediction]:
        '''
        Get the span predictions for the extractive Q&A model.

        Returns: *List* of *DPRReaderOutput* sorted by descending *(relevance_score, span_score)*. Each
        *DPRReaderOutput* is a *Tuple* with:

            - **span_score**: `float` that corresponds to the score given by the reader for this span compared to other
              spans in the same passage. It corresponds to the sum of the start and end logits of the span.
            - **relevance_score**: `float` that corresponds to the score of the each passage to answer the question,
              compared to all the other passages. It corresponds to the output of the QA classifier of the DPRReader.
            - **doc_id**: `int` the id of the passage. - **start_index**: `int` the start index of the span
              (inclusive). - **end_index**: `int` the end index of the span (inclusive).

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
        >>> predicted_spans = tokenizer.decode_best_spans(encoded_inputs, outputs)
        >>> print(predicted_spans[0].text)  # best span
        ```'''

class DPRReaderTokenizer(CustomDPRReaderTokenizerMixin, BertTokenizer):
    """
    Construct a DPRReader tokenizer.

    [`DPRReaderTokenizer`] is almost identical to [`BertTokenizer`] and runs end-to-end tokenization: punctuation
    splitting and wordpiece. The difference is that is has three inputs strings: question, titles and texts that are
    combined to be fed to the [`DPRReader`] model.

    Refer to superclass [`BertTokenizer`] for usage examples and documentation concerning parameters.
    """
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = READER_PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = READER_PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_init_configuration = READER_PRETRAINED_INIT_CONFIGURATION
    model_input_names: Incomplete
