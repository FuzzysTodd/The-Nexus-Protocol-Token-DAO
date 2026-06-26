from ...file_utils import PaddingStrategy as PaddingStrategy, TensorType as TensorType, add_end_docstrings as add_end_docstrings
from ...tokenization_utils import AddedToken as AddedToken, PreTrainedTokenizer as PreTrainedTokenizer
from ...tokenization_utils_base import BatchEncoding as BatchEncoding, ENCODE_KWARGS_DOCSTRING as ENCODE_KWARGS_DOCSTRING, EncodedInput as EncodedInput, PreTokenizedInput as PreTokenizedInput, TextInput as TextInput, TextInputPair as TextInputPair, TruncationStrategy as TruncationStrategy
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import List, Optional, Tuple, Union

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
MARKUPLM_ENCODE_PLUS_ADDITIONAL_KWARGS_DOCSTRING: str

def bytes_to_unicode():
    """
    Returns list of utf-8 byte and a mapping to unicode strings. We specifically avoids mapping to whitespace/control
    characters the bpe code barfs on. The reversible bpe codes work on unicode strings. This means you need a large #
    of unicode characters in your vocab if you want to avoid UNKs. When you're at something like a 10B token dataset
    you end up needing around 5K for decent coverage. This is a significant percentage of your normal, say, 32K bpe
    vocab. To avoid that, we want lookup tables between utf-8 bytes and unicode strings.
    """
def get_pairs(word):
    """
    Return set of symbol pairs in a word. Word is represented as tuple of symbols (symbols being variable-length
    strings).
    """

class MarkupLMTokenizer(PreTrainedTokenizer):
    '''
    Construct a MarkupLM tokenizer. Based on byte-level Byte-Pair-Encoding (BPE). [`MarkupLMTokenizer`] can be used to
    turn HTML strings into to token-level `input_ids`, `attention_mask`, `token_type_ids`, `xpath_tags_seq` and
    `xpath_tags_seq`. This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods.
    Users should refer to this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
        merges_file (`str`):
            Path to the merges file.
        errors (`str`, *optional*, defaults to `"replace"`):
            Paradigm to follow when decoding bytes to UTF-8. See
            [bytes.decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) for more information.
        bos_token (`str`, *optional*, defaults to `"<s>"`):
            The beginning of sequence token that was used during pretraining. Can be used a sequence classifier token.

            <Tip>

            When building a sequence using special tokens, this is not the token that is used for the beginning of
            sequence. The token used is the `cls_token`.

            </Tip>

        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sequence token.

            <Tip>

            When building a sequence using special tokens, this is not the token that is used for the end of sequence.
            The token used is the `sep_token`.

            </Tip>

        sep_token (`str`, *optional*, defaults to `"</s>"`):
            The separator token, which is used when building a sequence from multiple sequences, e.g. two sequences for
            sequence classification or for a text and a question for question answering. It is also used as the last
            token of a sequence built with special tokens.
        cls_token (`str`, *optional*, defaults to `"<s>"`):
            The classifier token which is used when doing sequence classification (classification of the whole sequence
            instead of per-token classification). It is the first token of the sequence when built with special tokens.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.
        mask_token (`str`, *optional*, defaults to `"<mask>"`):
            The token used for masking values. This is the token used when training this model with masked language
            modeling. This is the token which the model will try to predict.
        add_prefix_space (`bool`, *optional*, defaults to `False`):
            Whether or not to add an initial space to the input. This allows to treat the leading word just as any
            other word. (RoBERTa tokenizer detect beginning of words by the preceding space).
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    encoder: Incomplete
    tags_dict: Incomplete
    decoder: Incomplete
    errors: Incomplete
    byte_encoder: Incomplete
    byte_decoder: Incomplete
    bpe_ranks: Incomplete
    cache: Incomplete
    add_prefix_space: Incomplete
    pat: Incomplete
    max_depth: Incomplete
    max_width: Incomplete
    pad_width: Incomplete
    unk_tag_id: Incomplete
    pad_tag_id: Incomplete
    pad_xpath_tags_seq: Incomplete
    pad_xpath_subs_seq: Incomplete
    pad_token_label: Incomplete
    only_label_first_subword: Incomplete
    def __init__(self, vocab_file, merges_file, tags_dict, errors: str = 'replace', bos_token: str = '<s>', eos_token: str = '</s>', sep_token: str = '</s>', cls_token: str = '<s>', unk_token: str = '<unk>', pad_token: str = '<pad>', mask_token: str = '<mask>', add_prefix_space: bool = False, max_depth: int = 50, max_width: int = 1000, pad_width: int = 1001, pad_token_label: int = -100, only_label_first_subword: bool = True, **kwargs) -> None: ...
    def get_xpath_seq(self, xpath):
        '''
        Given the xpath expression of one particular node (like "/html/body/div/li[1]/div/span[2]"), return a list of
        tag IDs and corresponding subscripts, taking into account max depth.
        '''
    @property
    def vocab_size(self): ...
    def get_vocab(self): ...
    def bpe(self, token): ...
    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (string) in a single string."""
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
    def prepare_for_tokenization(self, text, is_split_into_words: bool = False, **kwargs): ...
    def build_inputs_with_special_tokens(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. A RoBERTa sequence has the following format:
        - single sequence: `<s> X </s>`
        - pair of sequences: `<s> A </s></s> B </s>`

        Args:
            token_ids_0 (`List[int]`):
                List of IDs to which the special tokens will be added.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.
        Returns:
            `List[int]`: List of [input IDs](../glossary#input-ids) with the appropriate special tokens.
        """
    def build_xpath_tags_with_special_tokens(self, xpath_tags_0: List[int], xpath_tags_1: Optional[List[int]] = None) -> List[int]: ...
    def build_xpath_subs_with_special_tokens(self, xpath_subs_0: List[int], xpath_subs_1: Optional[List[int]] = None) -> List[int]: ...
    def get_special_tokens_mask(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None, already_has_special_tokens: bool = False) -> List[int]:
        """
        Args:
        Retrieve sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer `prepare_for_model` method.
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.
            already_has_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not the token list is already formatted with special tokens for the model.
        Returns:
            `List[int]`: A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
        """
    def create_token_type_ids_from_sequences(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. RoBERTa does not
        make use of token type ids, therefore a list of zeros is returned.

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.
        Returns:
            `List[int]`: List of zeros.
        """
    def __call__(self, text: Union[TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]], text_pair: Optional[Union[PreTokenizedInput, List[PreTokenizedInput]]] = None, xpaths: Union[List[List[int]], List[List[List[int]]]] = None, node_labels: Optional[Union[List[int], List[List[int]]]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TruncationStrategy] = None, max_length: Optional[int] = None, stride: int = 0, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, **kwargs) -> BatchEncoding:
        """
        Main method to tokenize and prepare for the model one or several sequence(s) or one or several pair(s) of
        sequences with node-level xpaths and optional labels.

        Args:
            text (`str`, `List[str]`, `List[List[str]]`):
                The sequence or batch of sequences to be encoded. Each sequence can be a string, a list of strings
                (nodes of a single example or questions of a batch of examples) or a list of list of strings (batch of
                nodes).
            text_pair (`List[str]`, `List[List[str]]`):
                The sequence or batch of sequences to be encoded. Each sequence should be a list of strings
                (pretokenized string).
            xpaths (`List[List[int]]`, `List[List[List[int]]]`):
                Node-level xpaths.
            node_labels (`List[int]`, `List[List[int]]`, *optional*):
                Node-level integer labels (for token classification tasks).
        """
    def batch_encode_plus(self, batch_text_or_text_pairs: Union[List[TextInput], List[TextInputPair], List[PreTokenizedInput]], is_pair: bool = None, xpaths: Optional[List[List[List[int]]]] = None, node_labels: Optional[Union[List[int], List[List[int]]]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TruncationStrategy] = None, max_length: Optional[int] = None, stride: int = 0, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, **kwargs) -> BatchEncoding: ...
    def encode(self, text: Union[TextInput, PreTokenizedInput], text_pair: Optional[PreTokenizedInput] = None, xpaths: Optional[List[List[int]]] = None, node_labels: Optional[List[int]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TruncationStrategy] = None, max_length: Optional[int] = None, stride: int = 0, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, **kwargs) -> List[int]: ...
    def encode_plus(self, text: Union[TextInput, PreTokenizedInput], text_pair: Optional[PreTokenizedInput] = None, xpaths: Optional[List[List[int]]] = None, node_labels: Optional[List[int]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TruncationStrategy] = None, max_length: Optional[int] = None, stride: int = 0, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, **kwargs) -> BatchEncoding:
        """
        Tokenize and prepare for the model a sequence or a pair of sequences. .. warning:: This method is deprecated,
        `__call__` should be used instead.

        Args:
            text (`str`, `List[str]`, `List[List[str]]`):
                The first sequence to be encoded. This can be a string, a list of strings or a list of list of strings.
            text_pair (`List[str]` or `List[int]`, *optional*):
                Optional second sequence to be encoded. This can be a list of strings (nodes of a single example) or a
                list of list of strings (nodes of a batch of examples).
        """
    def prepare_for_model(self, text: Union[TextInput, PreTokenizedInput], text_pair: Optional[PreTokenizedInput] = None, xpaths: Optional[List[List[int]]] = None, node_labels: Optional[List[int]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TruncationStrategy] = None, max_length: Optional[int] = None, stride: int = 0, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, prepend_batch_axis: bool = False, **kwargs) -> BatchEncoding:
        """
        Prepares a sequence or a pair of sequences so that it can be used by the model. It adds special tokens,
        truncates sequences if overflowing while taking into account the special tokens and manages a moving window
        (with user defined stride) for overflowing tokens. Please Note, for *text_pair* different than `None` and
        *truncation_strategy = longest_first* or `True`, it is not possible to return overflowing tokens. Such a
        combination of arguments will raise an error.

        Node-level `xpaths` are turned into token-level `xpath_tags_seq` and `xpath_subs_seq`. If provided, node-level
        `node_labels` are turned into token-level `labels`. The node label is used for the first token of the node,
        while remaining tokens are labeled with -100, such that they will be ignored by the loss function.

        Args:
            text (`str`, `List[str]`, `List[List[str]]`):
                The first sequence to be encoded. This can be a string, a list of strings or a list of list of strings.
            text_pair (`List[str]` or `List[int]`, *optional*):
                Optional second sequence to be encoded. This can be a list of strings (nodes of a single example) or a
                list of list of strings (nodes of a batch of examples).
        """
    def truncate_sequences(self, ids: List[int], xpath_tags_seq: List[List[int]], xpath_subs_seq: List[List[int]], pair_ids: Optional[List[int]] = None, pair_xpath_tags_seq: Optional[List[List[int]]] = None, pair_xpath_subs_seq: Optional[List[List[int]]] = None, labels: Optional[List[int]] = None, num_tokens_to_remove: int = 0, truncation_strategy: Union[str, TruncationStrategy] = 'longest_first', stride: int = 0) -> Tuple[List[int], List[int], List[int]]:
        """
        Args:
        Truncates a sequence pair in-place following the strategy.
            ids (`List[int]`):
                Tokenized input ids of the first sequence. Can be obtained from a string by chaining the `tokenize` and
                `convert_tokens_to_ids` methods.
            xpath_tags_seq (`List[List[int]]`):
                XPath tag IDs of the first sequence.
            xpath_subs_seq (`List[List[int]]`):
                XPath sub IDs of the first sequence.
            pair_ids (`List[int]`, *optional*):
                Tokenized input ids of the second sequence. Can be obtained from a string by chaining the `tokenize`
                and `convert_tokens_to_ids` methods.
            pair_xpath_tags_seq (`List[List[int]]`, *optional*):
                XPath tag IDs of the second sequence.
            pair_xpath_subs_seq (`List[List[int]]`, *optional*):
                XPath sub IDs of the second sequence.
            num_tokens_to_remove (`int`, *optional*, defaults to 0):
                Number of tokens to remove using the truncation strategy.
            truncation_strategy (`str` or [`~tokenization_utils_base.TruncationStrategy`], *optional*, defaults to
            `False`):
                The strategy to follow for truncation. Can be:
                - `'longest_first'`: Truncate to a maximum length specified with the argument `max_length` or to the
                  maximum acceptable input length for the model if that argument is not provided. This will truncate
                  token by token, removing a token from the longest sequence in the pair if a pair of sequences (or a
                  batch of pairs) is provided.
                - `'only_first'`: Truncate to a maximum length specified with the argument `max_length` or to the
                  maximum acceptable input length for the model if that argument is not provided. This will only
                  truncate the first sequence of a pair if a pair of sequences (or a batch of pairs) is provided.
                - `'only_second'`: Truncate to a maximum length specified with the argument `max_length` or to the
                  maximum acceptable input length for the model if that argument is not provided. This will only
                  truncate the second sequence of a pair if a pair of sequences (or a batch of pairs) is provided.
                - `'do_not_truncate'` (default): No truncation (i.e., can output batch with sequence lengths greater
                  than the model maximum admissible input size).
            stride (`int`, *optional*, defaults to 0):
                If set to a positive number, the overflowing tokens returned will contain some tokens from the main
                sequence returned. The value of this argument defines the number of additional tokens.
        Returns:
            `Tuple[List[int], List[int], List[int]]`: The truncated `ids`, the truncated `pair_ids` and the list of
            overflowing tokens. Note: The *longest_first* strategy returns empty list of overflowing tokens if a pair
            of sequences (or a batch of pairs) is provided.
        """
