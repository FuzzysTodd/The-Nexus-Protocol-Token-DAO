import enum
import pandas as pd
from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...tokenization_utils_base import BatchEncoding as BatchEncoding, ENCODE_KWARGS_DOCSTRING as ENCODE_KWARGS_DOCSTRING, EncodedInput as EncodedInput, PreTokenizedInput as PreTokenizedInput, TextInput as TextInput
from ...utils import ExplicitEnum as ExplicitEnum, PaddingStrategy as PaddingStrategy, TensorType as TensorType, add_end_docstrings as add_end_docstrings, is_pandas_available as is_pandas_available, logging as logging
from _typeshed import Incomplete
from collections.abc import Generator
from dataclasses import dataclass
from typing import List, NamedTuple, Optional, Text, Tuple, Union

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
PRETRAINED_INIT_CONFIGURATION: Incomplete

class TapasTruncationStrategy(ExplicitEnum):
    """
    Possible values for the `truncation` argument in [`~TapasTokenizer.__call__`]. Useful for tab-completion in an IDE.
    """
    DROP_ROWS_TO_FIT: str
    DO_NOT_TRUNCATE: str

class TableValue(NamedTuple):
    token: Incomplete
    column_id: Incomplete
    row_id: Incomplete

@dataclass(frozen=True)
class TokenCoordinates:
    column_index: int
    row_index: int
    token_index: int
    def __init__(self, column_index, row_index, token_index) -> None: ...

@dataclass
class TokenizedTable:
    rows: List[List[List[Text]]]
    selected_tokens: List[TokenCoordinates]
    def __init__(self, rows, selected_tokens) -> None: ...

@dataclass(frozen=True)
class SerializedExample:
    tokens: List[Text]
    column_ids: List[int]
    row_ids: List[int]
    segment_ids: List[int]
    def __init__(self, tokens, column_ids, row_ids, segment_ids) -> None: ...

def load_vocab(vocab_file):
    """Loads a vocabulary file into a dictionary."""
def whitespace_tokenize(text):
    """Runs basic whitespace cleaning and splitting on a piece of text."""

TAPAS_ENCODE_PLUS_ADDITIONAL_KWARGS_DOCSTRING: str

class TapasTokenizer(PreTrainedTokenizer):
    '''
    Construct a TAPAS tokenizer. Based on WordPiece. Flattens a table and one or more related sentences to be used by
    TAPAS models.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer to
    this superclass for more information regarding those methods. [`TapasTokenizer`] creates several token type ids to
    encode tabular structure. To be more precise, it adds 7 token type ids, in the following order: `segment_ids`,
    `column_ids`, `row_ids`, `prev_labels`, `column_ranks`, `inv_column_ranks` and `numeric_relations`:

    - segment_ids: indicate whether a token belongs to the question (0) or the table (1). 0 for special tokens and
      padding.
    - column_ids: indicate to which column of the table a token belongs (starting from 1). Is 0 for all question
      tokens, special tokens and padding.
    - row_ids: indicate to which row of the table a token belongs (starting from 1). Is 0 for all question tokens,
      special tokens and padding. Tokens of column headers are also 0.
    - prev_labels: indicate whether a token was (part of) an answer to the previous question (1) or not (0). Useful in
      a conversational setup (such as SQA).
    - column_ranks: indicate the rank of a table token relative to a column, if applicable. For example, if you have a
      column "number of movies" with values 87, 53 and 69, then the column ranks of these tokens are 3, 1 and 2
      respectively. 0 for all question tokens, special tokens and padding.
    - inv_column_ranks: indicate the inverse rank of a table token relative to a column, if applicable. For example, if
      you have a column "number of movies" with values 87, 53 and 69, then the inverse column ranks of these tokens are
      1, 3 and 2 respectively. 0 for all question tokens, special tokens and padding.
    - numeric_relations: indicate numeric relations between the question and the tokens of the table. 0 for all
      question tokens, special tokens and padding.

    [`TapasTokenizer`] runs end-to-end tokenization on a table and associated sentences: punctuation splitting and
    wordpiece.

    Args:
        vocab_file (`str`):
            File containing the vocabulary.
        do_lower_case (`bool`, *optional*, defaults to `True`):
            Whether or not to lowercase the input when tokenizing.
        do_basic_tokenize (`bool`, *optional*, defaults to `True`):
            Whether or not to do basic tokenization before WordPiece.
        never_split (`Iterable`, *optional*):
            Collection of tokens which will never be split during tokenization. Only has an effect when
            `do_basic_tokenize=True`
        unk_token (`str`, *optional*, defaults to `"[UNK]"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        sep_token (`str`, *optional*, defaults to `"[SEP]"`):
            The separator token, which is used when building a sequence from multiple sequences, e.g. two sequences for
            sequence classification or for a text and a question for question answering. It is also used as the last
            token of a sequence built with special tokens.
        pad_token (`str`, *optional*, defaults to `"[PAD]"`):
            The token used for padding, for example when batching sequences of different lengths.
        cls_token (`str`, *optional*, defaults to `"[CLS]"`):
            The classifier token which is used when doing sequence classification (classification of the whole sequence
            instead of per-token classification). It is the first token of the sequence when built with special tokens.
        mask_token (`str`, *optional*, defaults to `"[MASK]"`):
            The token used for masking values. This is the token used when training this model with masked language
            modeling. This is the token which the model will try to predict.
        empty_token (`str`, *optional*, defaults to `"[EMPTY]"`):
            The token used for empty cell values in a table. Empty cell values include "", "n/a", "nan" and "?".
        tokenize_chinese_chars (`bool`, *optional*, defaults to `True`):
            Whether or not to tokenize Chinese characters. This should likely be deactivated for Japanese (see this
            [issue](https://github.com/huggingface/transformers/issues/328)).
        strip_accents (`bool`, *optional*):
            Whether or not to strip all accents. If this option is not specified, then it will be determined by the
            value for `lowercase` (as in the original BERT).
        cell_trim_length (`int`, *optional*, defaults to -1):
            If > 0: Trim cells so that the length is <= this value. Also disables further cell trimming, should thus be
            used with `truncation` set to `True`.
        max_column_id (`int`, *optional*):
            Max column id to extract.
        max_row_id (`int`, *optional*):
            Max row id to extract.
        strip_column_names (`bool`, *optional*, defaults to `False`):
            Whether to add empty strings instead of column names.
        update_answer_coordinates (`bool`, *optional*, defaults to `False`):
            Whether to recompute the answer coordinates from the answer text.
        min_question_length (`int`, *optional*):
            Minimum length of each question in terms of tokens (will be skipped otherwise).
        max_question_length (`int`, *optional*):
            Maximum length of each question in terms of tokens (will be skipped otherwise).
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    vocab: Incomplete
    ids_to_tokens: Incomplete
    do_basic_tokenize: Incomplete
    basic_tokenizer: Incomplete
    wordpiece_tokenizer: Incomplete
    cell_trim_length: Incomplete
    max_column_id: Incomplete
    max_row_id: Incomplete
    strip_column_names: Incomplete
    update_answer_coordinates: Incomplete
    min_question_length: Incomplete
    max_question_length: Incomplete
    def __init__(self, vocab_file, do_lower_case: bool = True, do_basic_tokenize: bool = True, never_split: Incomplete | None = None, unk_token: str = '[UNK]', sep_token: str = '[SEP]', pad_token: str = '[PAD]', cls_token: str = '[CLS]', mask_token: str = '[MASK]', empty_token: str = '[EMPTY]', tokenize_chinese_chars: bool = True, strip_accents: Incomplete | None = None, cell_trim_length: int = -1, max_column_id: int = None, max_row_id: int = None, strip_column_names: bool = False, update_answer_coordinates: bool = False, min_question_length: Incomplete | None = None, max_question_length: Incomplete | None = None, model_max_length: int = 512, additional_special_tokens: Optional[List[str]] = None, **kwargs) -> None: ...
    @property
    def do_lower_case(self): ...
    @property
    def vocab_size(self): ...
    def get_vocab(self): ...
    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (string) in a single string."""
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
    def create_attention_mask_from_sequences(self, query_ids: List[int], table_values: List[TableValue]) -> List[int]:
        """
        Creates the attention mask according to the query token IDs and a list of table values.

        Args:
            query_ids (`List[int]`): list of token IDs corresponding to the ID.
            table_values (`List[TableValue]`): lift of table values, which are named tuples containing the
                token value, the column ID and the row ID of said token.

        Returns:
            `List[int]`: List of ints containing the attention mask values.
        """
    def create_segment_token_type_ids_from_sequences(self, query_ids: List[int], table_values: List[TableValue]) -> List[int]:
        """
        Creates the segment token type IDs according to the query token IDs and a list of table values.

        Args:
            query_ids (`List[int]`): list of token IDs corresponding to the ID.
            table_values (`List[TableValue]`): lift of table values, which are named tuples containing the
                token value, the column ID and the row ID of said token.

        Returns:
            `List[int]`: List of ints containing the segment token type IDs values.
        """
    def create_column_token_type_ids_from_sequences(self, query_ids: List[int], table_values: List[TableValue]) -> List[int]:
        """
        Creates the column token type IDs according to the query token IDs and a list of table values.

        Args:
            query_ids (`List[int]`): list of token IDs corresponding to the ID.
            table_values (`List[TableValue]`): lift of table values, which are named tuples containing the
                token value, the column ID and the row ID of said token.

        Returns:
            `List[int]`: List of ints containing the column token type IDs values.
        """
    def create_row_token_type_ids_from_sequences(self, query_ids: List[int], table_values: List[TableValue]) -> List[int]:
        """
        Creates the row token type IDs according to the query token IDs and a list of table values.

        Args:
            query_ids (`List[int]`): list of token IDs corresponding to the ID.
            table_values (`List[TableValue]`): lift of table values, which are named tuples containing the
                token value, the column ID and the row ID of said token.

        Returns:
            `List[int]`: List of ints containing the row token type IDs values.
        """
    def build_inputs_with_special_tokens(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Build model inputs from a question and flattened table for question answering or sequence classification tasks
        by concatenating and adding special tokens.

        Args:
            token_ids_0 (`List[int]`): The ids of the question.
            token_ids_1 (`List[int]`, *optional*): The ids of the flattened table.

        Returns:
            `List[int]`: The model input with special tokens.
        """
    def get_special_tokens_mask(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None, already_has_special_tokens: bool = False) -> List[int]:
        """
        Retrieve sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer `prepare_for_model` method.

        Args:
            token_ids_0 (`List[int]`):
                List of question IDs.
            token_ids_1 (`List[int]`, *optional*):
                List of flattened table IDs.
            already_has_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not the token list is already formatted with special tokens for the model.

        Returns:
            `List[int]`: A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
        """
    def __call__(self, table: pd.DataFrame, queries: Optional[Union[TextInput, PreTokenizedInput, EncodedInput, List[TextInput], List[PreTokenizedInput], List[EncodedInput]]] = None, answer_coordinates: Optional[Union[List[Tuple], List[List[Tuple]]]] = None, answer_text: Optional[Union[List[TextInput], List[List[TextInput]]]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TapasTruncationStrategy] = False, max_length: Optional[int] = None, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, **kwargs) -> BatchEncoding:
        """
        Main method to tokenize and prepare for the model one or several sequence(s) related to a table.

        Args:
            table (`pd.DataFrame`):
                Table containing tabular data. Note that all cell values must be text. Use *.astype(str)* on a Pandas
                dataframe to convert it to string.
            queries (`str` or `List[str]`):
                Question or batch of questions related to a table to be encoded. Note that in case of a batch, all
                questions must refer to the **same** table.
            answer_coordinates (`List[Tuple]` or `List[List[Tuple]]`, *optional*):
                Answer coordinates of each table-question pair in the batch. In case only a single table-question pair
                is provided, then the answer_coordinates must be a single list of one or more tuples. Each tuple must
                be a (row_index, column_index) pair. The first data row (not the column header row) has index 0. The
                first column has index 0. In case a batch of table-question pairs is provided, then the
                answer_coordinates must be a list of lists of tuples (each list corresponding to a single
                table-question pair).
            answer_text (`List[str]` or `List[List[str]]`, *optional*):
                Answer text of each table-question pair in the batch. In case only a single table-question pair is
                provided, then the answer_text must be a single list of one or more strings. Each string must be the
                answer text of a corresponding answer coordinate. In case a batch of table-question pairs is provided,
                then the answer_coordinates must be a list of lists of strings (each list corresponding to a single
                table-question pair).
        """
    def batch_encode_plus(self, table: pd.DataFrame, queries: Optional[Union[List[TextInput], List[PreTokenizedInput], List[EncodedInput]]] = None, answer_coordinates: Optional[List[List[Tuple]]] = None, answer_text: Optional[List[List[TextInput]]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TapasTruncationStrategy] = False, max_length: Optional[int] = None, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, **kwargs) -> BatchEncoding:
        """
        Prepare a table and a list of strings for the model.

        <Tip warning={true}>

        This method is deprecated, `__call__` should be used instead.

        </Tip>

        Args:
            table (`pd.DataFrame`):
                Table containing tabular data. Note that all cell values must be text. Use *.astype(str)* on a Pandas
                dataframe to convert it to string.
            queries (`List[str]`):
                Batch of questions related to a table to be encoded. Note that all questions must refer to the **same**
                table.
            answer_coordinates (`List[Tuple]` or `List[List[Tuple]]`, *optional*):
                Answer coordinates of each table-question pair in the batch. Each tuple must be a (row_index,
                column_index) pair. The first data row (not the column header row) has index 0. The first column has
                index 0. The answer_coordinates must be a list of lists of tuples (each list corresponding to a single
                table-question pair).
            answer_text (`List[str]` or `List[List[str]]`, *optional*):
                Answer text of each table-question pair in the batch. In case a batch of table-question pairs is
                provided, then the answer_coordinates must be a list of lists of strings (each list corresponding to a
                single table-question pair). Each string must be the answer text of a corresponding answer coordinate.
        """
    def encode(self, table: pd.DataFrame, query: Optional[Union[TextInput, PreTokenizedInput, EncodedInput]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TapasTruncationStrategy] = False, max_length: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, **kwargs) -> List[int]:
        """
        Prepare a table and a string for the model. This method does not return token type IDs, attention masks, etc.
        which are necessary for the model to work correctly. Use that method if you want to build your processing on
        your own, otherwise refer to `__call__`.

        Args:
            table (`pd.DataFrame`):
                Table containing tabular data. Note that all cell values must be text. Use *.astype(str)* on a Pandas
                dataframe to convert it to string.
            query (`str` or `List[str]`):
                Question related to a table to be encoded.
        """
    def encode_plus(self, table: pd.DataFrame, query: Optional[Union[TextInput, PreTokenizedInput, EncodedInput]] = None, answer_coordinates: Optional[List[Tuple]] = None, answer_text: Optional[List[TextInput]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TapasTruncationStrategy] = False, max_length: Optional[int] = None, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, **kwargs) -> BatchEncoding:
        """
        Prepare a table and a string for the model.

        Args:
            table (`pd.DataFrame`):
                Table containing tabular data. Note that all cell values must be text. Use *.astype(str)* on a Pandas
                dataframe to convert it to string.
            query (`str` or `List[str]`):
                Question related to a table to be encoded.
            answer_coordinates (`List[Tuple]` or `List[List[Tuple]]`, *optional*):
                Answer coordinates of each table-question pair in the batch. The answer_coordinates must be a single
                list of one or more tuples. Each tuple must be a (row_index, column_index) pair. The first data row
                (not the column header row) has index 0. The first column has index 0.
            answer_text (`List[str]` or `List[List[str]]`, *optional*):
                Answer text of each table-question pair in the batch. The answer_text must be a single list of one or
                more strings. Each string must be the answer text of a corresponding answer coordinate.
        """
    def prepare_for_model(self, raw_table: pd.DataFrame, raw_query: Union[TextInput, PreTokenizedInput, EncodedInput], tokenized_table: Optional[TokenizedTable] = None, query_tokens: Optional[TokenizedTable] = None, answer_coordinates: Optional[List[Tuple]] = None, answer_text: Optional[List[TextInput]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TapasTruncationStrategy] = False, max_length: Optional[int] = None, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_token_type_ids: Optional[bool] = True, return_attention_mask: Optional[bool] = True, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, prepend_batch_axis: bool = False, **kwargs) -> BatchEncoding:
        """
        Prepares a sequence of input id so that it can be used by the model. It adds special tokens, truncates
        sequences if overflowing while taking into account the special tokens.

        Args:
            raw_table (`pd.DataFrame`):
                The original table before any transformation (like tokenization) was applied to it.
            raw_query (`TextInput` or `PreTokenizedInput` or `EncodedInput`):
                The original query before any transformation (like tokenization) was applied to it.
            tokenized_table (`TokenizedTable`):
                The table after tokenization.
            query_tokens (`List[str]`):
                The query after tokenization.
            answer_coordinates (`List[Tuple]` or `List[List[Tuple]]`, *optional*):
                Answer coordinates of each table-question pair in the batch. The answer_coordinates must be a single
                list of one or more tuples. Each tuple must be a (row_index, column_index) pair. The first data row
                (not the column header row) has index 0. The first column has index 0.
            answer_text (`List[str]` or `List[List[str]]`, *optional*):
                Answer text of each table-question pair in the batch. The answer_text must be a single list of one or
                more strings. Each string must be the answer text of a corresponding answer coordinate.
        """
    def get_answer_ids(self, column_ids, row_ids, tokenized_table, answer_texts_question, answer_coordinates_question): ...
    def convert_logits_to_predictions(self, data, logits, logits_agg: Incomplete | None = None, cell_classification_threshold: float = 0.5):
        """
        Converts logits of [`TapasForQuestionAnswering`] to actual predicted answer coordinates and optional
        aggregation indices.

        The original implementation, on which this function is based, can be found
        [here](https://github.com/google-research/tapas/blob/4908213eb4df7aa988573350278b44c4dbe3f71b/tapas/experiments/prediction_utils.py#L288).

        Args:
            data (`dict`):
                Dictionary mapping features to actual values. Should be created using [`TapasTokenizer`].
            logits (`torch.Tensor` or `tf.Tensor` of shape `(batch_size, sequence_length)`):
                Tensor containing the logits at the token level.
            logits_agg (`torch.Tensor` or `tf.Tensor` of shape `(batch_size, num_aggregation_labels)`, *optional*):
                Tensor containing the aggregation logits.
            cell_classification_threshold (`float`, *optional*, defaults to 0.5):
                Threshold to be used for cell selection. All table cells for which their probability is larger than
                this threshold will be selected.

        Returns:
            `tuple` comprising various elements depending on the inputs:

            - predicted_answer_coordinates (`List[List[[tuple]]` of length `batch_size`): Predicted answer coordinates
              as a list of lists of tuples. Each element in the list contains the predicted answer coordinates of a
              single example in the batch, as a list of tuples. Each tuple is a cell, i.e. (row index, column index).
            - predicted_aggregation_indices (`List[int]`of length `batch_size`, *optional*, returned when
              `logits_aggregation` is provided): Predicted aggregation operator indices of the aggregation head.
        """

class BasicTokenizer:
    """
    Constructs a BasicTokenizer that will run basic tokenization (punctuation splitting, lower casing, etc.).

    Args:
        do_lower_case (`bool`, *optional*, defaults to `True`):
            Whether or not to lowercase the input when tokenizing.
        never_split (`Iterable`, *optional*):
            Collection of tokens which will never be split during tokenization. Only has an effect when
            `do_basic_tokenize=True`
        tokenize_chinese_chars (`bool`, *optional*, defaults to `True`):
            Whether or not to tokenize Chinese characters.

            This should likely be deactivated for Japanese (see this
            [issue](https://github.com/huggingface/transformers/issues/328)).
        strip_accents (`bool`, *optional*):
            Whether or not to strip all accents. If this option is not specified, then it will be determined by the
            value for `lowercase` (as in the original BERT).
    """
    do_lower_case: Incomplete
    never_split: Incomplete
    tokenize_chinese_chars: Incomplete
    strip_accents: Incomplete
    def __init__(self, do_lower_case: bool = True, never_split: Incomplete | None = None, tokenize_chinese_chars: bool = True, strip_accents: Incomplete | None = None) -> None: ...
    def tokenize(self, text, never_split: Incomplete | None = None):
        '''
        Basic Tokenization of a piece of text. Split on "white spaces" only, for sub-word tokenization, see
        WordPieceTokenizer.

        Args:
            never_split (`List[str]`, *optional*)
                Kept for backward compatibility purposes. Now implemented directly at the base class level (see
                [`PreTrainedTokenizer.tokenize`]) List of token not to split.
        '''

class WordpieceTokenizer:
    """Runs WordPiece tokenization."""
    vocab: Incomplete
    unk_token: Incomplete
    max_input_chars_per_word: Incomplete
    def __init__(self, vocab, unk_token, max_input_chars_per_word: int = 100) -> None: ...
    def tokenize(self, text):
        '''
        Tokenizes a piece of text into its word pieces. This uses a greedy longest-match-first algorithm to perform
        tokenization using the given vocabulary.

        For example, `input = "unaffable"` wil return as output `["un", "##aff", "##able"]`.

        Args:
            text: A single token or whitespace separated tokens. This should have
                already been passed through *BasicTokenizer*.

        Returns:
            A list of wordpiece tokens.
        '''

class Relation(enum.Enum):
    HEADER_TO_CELL: int
    CELL_TO_HEADER: int
    QUERY_TO_HEADER: int
    QUERY_TO_CELL: int
    ROW_TO_CELL: int
    CELL_TO_ROW: int
    EQ: int
    LT: int
    GT: int

@dataclass
class Date:
    year: Optional[int] = ...
    month: Optional[int] = ...
    day: Optional[int] = ...
    def __init__(self, year, month, day) -> None: ...

@dataclass
class NumericValue:
    float_value: Optional[float] = ...
    date: Optional[Date] = ...
    def __init__(self, float_value, date) -> None: ...

@dataclass
class NumericValueSpan:
    begin_index: int = ...
    end_index: int = ...
    values: List[NumericValue] = ...
    def __init__(self, begin_index, end_index, values) -> None: ...

@dataclass
class Cell:
    text: Text
    numeric_value: Optional[NumericValue] = ...
    def __init__(self, text, numeric_value) -> None: ...

@dataclass
class Question:
    original_text: Text
    text: Text
    numeric_spans: Optional[List[NumericValueSpan]] = ...
    def __init__(self, original_text, text, numeric_spans) -> None: ...

class _DateMask(NamedTuple):
    year: Incomplete
    month: Incomplete
    day: Incomplete

def get_all_spans(text, max_ngram_length) -> Generator[Incomplete, None, None]:
    """
    Split a text into all possible ngrams up to 'max_ngram_length'. Split points are white space and punctuation.

    Args:
      text: Text to split.
      max_ngram_length: maximal ngram length.
    Yields:
      Spans, tuples of begin-end index.
    """
def normalize_for_match(text): ...
def format_text(text):
    """Lowercases and strips punctuation."""
def parse_text(text):
    """
    Extracts longest number and date spans.

    Args:
      text: text to annotate

    Returns:
      List of longest numeric value spans.
    """

EMPTY_TEXT: str
NUMBER_TYPE: str
DATE_TYPE: str

def get_numeric_sort_key_fn(numeric_values):
    '''
    Creates a function that can be used as a sort key or to compare the values. Maps to primitive types and finds the
    biggest common subset. Consider the values "05/05/2010" and "August 2007". With the corresponding primitive values
    (2010.,5.,5.) and (2007.,8., None). These values can be compared by year and date so we map to the sequence (2010.,
    5.), (2007., 8.). If we added a third value "2006" with primitive value (2006., None, None), we could only compare
    by the year so we would map to (2010.,), (2007.,) and (2006.,).

    Args:
     numeric_values: Values to compare

    Returns:
     A function that can be used as a sort key function (mapping numeric values to a comparable tuple)

    Raises:
      ValueError if values don\'t have a common type or are not comparable.
    '''
def get_numeric_relation(value, other_value, sort_key_fn):
    """Compares two values and returns their relation or None."""
def add_numeric_values_to_question(question):
    """Adds numeric value spans to a question."""
def filter_invalid_unicode(text):
    """Return an empty string and True if 'text' is in invalid unicode."""
def filter_invalid_unicode_from_table(table) -> None:
    """
    Removes invalid unicode from table. Checks whether a table cell text contains an invalid unicode encoding. If yes,
    reset the table cell text to an empty str and log a warning for each invalid cell

    Args:
        table: table to clean.
    """
def add_numeric_table_values(table, min_consolidation_fraction: float = 0.7, debug_info: Incomplete | None = None):
    """
    Parses text in table column-wise and adds the consolidated values. Consolidation refers to finding values with a
    common types (date or number)

    Args:
        table:
            Table to annotate.
        min_consolidation_fraction:
            Fraction of cells in a column that need to have consolidated value.
        debug_info:
            Additional information used for logging.
    """
