import tensorflow as tf
from ..tf_utils import stable_softmax as stable_softmax
from ..utils import add_start_docstrings as add_start_docstrings
from ..utils.logging import get_logger as get_logger
from _typeshed import Incomplete
from typing import List

logger: Incomplete
TF_LOGITS_PROCESSOR_INPUTS_DOCSTRING: str

class TFLogitsProcessor:
    """Abstract base class for all logit processors that can be applied during generation."""
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor:
        """TF method for processing logits."""

class TFLogitsWarper:
    """Abstract base class for all logit warpers that can be applied during generation with multinomial sampling."""
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor:
        """TF method for warping logits."""

class TFLogitsProcessorList(list):
    """
    This class can be used to create a list of [`TFLogitsProcessor`] to subsequently process a `scores` input tensor.
    This class inherits from list and adds a specific *__call__* method to apply each [`TFLogitsProcessor`] to the
    inputs.
    """
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int, **kwargs) -> tf.Tensor: ...

class TFTemperatureLogitsWarper(TFLogitsWarper):
    """
    [`TFLogitsWarper`] for temperature (exponential scaling output probability distribution).

    Args:
        temperature (`float`):
            The value used to module the logits distribution.
    """
    temperature: Incomplete
    def __init__(self, temperature: float) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFTopKLogitsWarper(TFLogitsWarper):
    '''
    [`TFLogitsWarper`] that performs top-k, i.e. restricting to the k highest probability elements.

    Args:
        top_k (`int`):
            The number of highest probability vocabulary tokens to keep for top-k-filtering.
        filter_value (`float`, *optional*, defaults to `-float("Inf")`):
            All filtered values will be set to this float value.
        min_tokens_to_keep (`int`, *optional*, defaults to 1):
            Minimum number of tokens that cannot be filtered.
    '''
    top_k: Incomplete
    filter_value: Incomplete
    def __init__(self, top_k: int, filter_value: float = ..., min_tokens_to_keep: int = 1) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFTopPLogitsWarper(TFLogitsWarper):
    '''
    [`TFLogitsWarper`] that performs top-p, i.e. restricting to top tokens summing to <= prob_cut_off.

    Args:
        top_p (`float`):
            If set to < 1, only the smallest set of most probable tokens with probabilities that add up to `top_p` or
            higher are kept for generation.
        filter_value (`float`, *optional*, defaults to `-float("Inf")`):
            All filtered values will be set to this float value.
        min_tokens_to_keep (`int`, *optional*, defaults to 1):
            Minimum number of tokens that cannot be filtered.
    '''
    top_p: Incomplete
    filter_value: Incomplete
    min_tokens_to_keep: Incomplete
    def __init__(self, top_p: float, filter_value: float = ..., min_tokens_to_keep: int = 1) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFMinLengthLogitsProcessor(TFLogitsProcessor):
    '''
    [`TFLogitsProcessor`] enforcing a min-length by setting EOS probability to 0.

    Args:
        min_length (`int`):
            The minimum length below which the score of `eos_token_id` is set to `-float("Inf")`.
        eos_token_id (`int`):
            The id of the *end-of-sequence* token.
    '''
    min_length: Incomplete
    eos_token_id: Incomplete
    def __init__(self, min_length: int, eos_token_id: int) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFRepetitionPenaltyLogitsProcessor(TFLogitsProcessor):
    """
    [`TFLogitsProcessor`] enforcing an exponential penalty on repeated sequences.

    Args:
        repetition_penalty (`float`):
            The parameter for repetition penalty. 1.0 means no penalty. See [this
            paper](https://arxiv.org/pdf/1909.05858.pdf) for more details.
    """
    penalty: Incomplete
    def __init__(self, penalty: float) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFNoBadWordsLogitsProcessor(TFLogitsProcessor):
    """
    [`TFLogitsProcessor`] that enforces that specified sequences will never be sampled.

    Args:
        bad_words_ids (`List[List[int]]`):
            List of list of token ids that are not allowed to be generated. In order to get the tokens of the words
            that should not appear in the generated text, use `tokenizer(bad_word, add_prefix_space=True).input_ids`.
        eos_token_id (`int`):
            The id of the *end-of-sequence* token.
    """
    bad_word_seqs_ids: Incomplete
    bad_word_seqs_len: Incomplete
    seq_forbidden_tokens: Incomplete
    def __init__(self, bad_words_ids: List[List[int]], eos_token_id: int) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFNoRepeatNGramLogitsProcessor(TFLogitsProcessor):
    """
    [`TFLogitsProcessor`] that enforces no repetition of n-grams. See
    [Fairseq](https://github.com/pytorch/fairseq/blob/a07cb6f40480928c9e0548b737aadd36ee66ac76/fairseq/sequence_generator.py#L345).

    Args:
        ngram_size (`int`):
            All ngrams of size `ngram_size` can only occur once.
    """
    ngram_size: Incomplete
    def __init__(self, ngram_size: int) -> None: ...
    def calc_banned_ngram_tokens(self, input_ids, num_hypos, cur_len): ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFForcedBOSTokenLogitsProcessor(TFLogitsProcessor):
    """
    [`TFLogitsProcessor`] that enforces the specified token as the first generated token.

    Args:
        bos_token_id (`int`):
            The id of the token to force as the first generated token.
    """
    bos_token_id: Incomplete
    def __init__(self, bos_token_id: int) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFForcedEOSTokenLogitsProcessor(TFLogitsProcessor):
    """
    [`TFLogitsProcessor`] that enforces the specified token as the last generated token when `max_length` is reached.

    Args:
        max_length (`int`):
            The maximum length of the sequence to be generated.
        eos_token_id (`int`):
            The id of the token to force as the last generated token when `max_length` is reached.
    """
    max_length: Incomplete
    eos_token_id: Incomplete
    def __init__(self, max_length: int, eos_token_id: int) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFSuppressTokensAtBeginLogitsProcessor(TFLogitsProcessor):
    """
    [`TFSuppressTokensAtBeginLogitsProcessor`] suppresses a list of tokens as soon as the `generate` function starts
    generating using `begin_index` tokens. This should ensure that the tokens defined by `begin_suppress_tokens` at not
    sampled at the begining of the generation.
    """
    begin_suppress_tokens: Incomplete
    begin_index: Incomplete
    def __init__(self, begin_suppress_tokens, begin_index) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFSuppressTokensLogitsProcessor(TFLogitsProcessor):
    """This processor can be used to suppress a list of tokens. The processor will set their log probs to `-inf` so that they
    are not sampled."""
    suppress_tokens: Incomplete
    def __init__(self, suppress_tokens) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...

class TFForceTokensLogitsProcessor(TFLogitsProcessor):
    """This processor takes a list of pairs of integers which indicates a mapping from generation indices to token
    indices that will be forced before sampling. The processor will set their log probs to `0` and all other tokens to
    `-inf` so that they are sampled at their corresponding index."""
    force_token_array: Incomplete
    def __init__(self, force_token_map: List[List[int]]) -> None: ...
    def __call__(self, input_ids: tf.Tensor, scores: tf.Tensor, cur_len: int) -> tf.Tensor: ...
