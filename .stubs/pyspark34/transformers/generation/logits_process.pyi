import torch
from ..utils import add_start_docstrings as add_start_docstrings
from ..utils.logging import get_logger as get_logger
from _typeshed import Incomplete
from typing import Callable, List, Tuple, Union

logger: Incomplete
LOGITS_PROCESSOR_INPUTS_DOCSTRING: str

class LogitsProcessor:
    """Abstract base class for all logit processors that can be applied during generation."""
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:
        """Torch method for processing logits."""

class LogitsWarper:
    """Abstract base class for all logit warpers that can be applied during generation with multinomial sampling."""
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:
        """Torch method for warping logits."""

class LogitsProcessorList(list):
    """
    This class can be used to create a list of [`LogitsProcessor`] or [`LogitsWarper`] to subsequently process a
    `scores` input tensor. This class inherits from list and adds a specific *__call__* method to apply each
    [`LogitsProcessor`] or [`LogitsWarper`] to the inputs.
    """
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> torch.FloatTensor: ...

class MinLengthLogitsProcessor(LogitsProcessor):
    '''
    [`LogitsProcessor`] enforcing a min-length by setting EOS probability to 0.

    Args:
        min_length (`int`):
            The minimum length below which the score of `eos_token_id` is set to `-float("Inf")`.
        eos_token_id (`Union[int, List[int]]`):
            The id of the *end-of-sequence* token. Optionally, use a list to set multiple *end-of-sequence* tokens.
    '''
    min_length: Incomplete
    eos_token_id: Incomplete
    def __init__(self, min_length: int, eos_token_id: Union[int, List[int]]) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class MinNewTokensLengthLogitsProcessor(LogitsProcessor):
    '''
    [`LogitsProcessor`] enforcing a min-length of new tokens by setting EOS (End-Of-Sequence) token probability to 0.

    Args:
        prompt_length_to_skip (`int`):
            The input tokens length.
        min_new_tokens (`int`):
            The minimum *new* tokens length below which the score of `eos_token_id` is set to `-float("Inf")`.
        eos_token_id (`int`):
            The id of the *end-of-sequence* token.
    '''
    prompt_length_to_skip: Incomplete
    min_new_tokens: Incomplete
    eos_token_id: Incomplete
    def __init__(self, prompt_length_to_skip: int, min_new_tokens: int, eos_token_id: int) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class TemperatureLogitsWarper(LogitsWarper):
    """
    [`LogitsWarper`] for temperature (exponential scaling output probability distribution).

    Args:
        temperature (`float`):
            The value used to module the logits distribution.
    """
    temperature: Incomplete
    def __init__(self, temperature: float) -> None: ...
    def __call__(self, input_ids: torch.Tensor, scores: torch.Tensor) -> torch.FloatTensor: ...

class RepetitionPenaltyLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] enforcing an exponential penalty on repeated sequences.

    Args:
        repetition_penalty (`float`):
            The parameter for repetition penalty. 1.0 means no penalty. See [this
            paper](https://arxiv.org/pdf/1909.05858.pdf) for more details.
    """
    penalty: Incomplete
    def __init__(self, penalty: float) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class EncoderRepetitionPenaltyLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] enforcing an exponential penalty on tokens that are not in the original input.

    Args:
        hallucination_penalty (`float`):
            The parameter for hallucination penalty. 1.0 means no penalty.
        encoder_input_ids (`torch.LongTensor`):
            The encoder_input_ids that should not be repeated within the decoder ids.
    """
    penalty: Incomplete
    encoder_input_ids: Incomplete
    def __init__(self, penalty: float, encoder_input_ids: torch.LongTensor) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class TopPLogitsWarper(LogitsWarper):
    '''
    [`LogitsWarper`] that performs top-p, i.e. restricting to top tokens summing to prob_cut_off <= prob_cut_off.

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
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class TopKLogitsWarper(LogitsWarper):
    '''
    [`LogitsWarper`] that performs top-k, i.e. restricting to the k highest probability elements.

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
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class TypicalLogitsWarper(LogitsWarper):
    '''
    [`LogitsWarper`] that performs typical decoding. See [Typical Decoding for Natural Language
    Generation](https://arxiv.org/abs/2202.00666) for more information.

    Args:
        mass (`float`):
            Value of typical_p between 0 and 1 inclusive, defaults to 0.9.
        filter_value (`float`, *optional*, defaults to `-float("Inf")`):
            All filtered values will be set to this float value.
        min_tokens_to_keep (`int`, *optional*, defaults to 1):
            Minimum number of tokens that cannot be filtered.
    '''
    filter_value: Incomplete
    mass: Incomplete
    min_tokens_to_keep: Incomplete
    def __init__(self, mass: float = 0.9, filter_value: float = ..., min_tokens_to_keep: int = 1) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class EpsilonLogitsWarper(LogitsWarper):
    '''
    [`LogitsWarper`] that performs epsilon-sampling, i.e. restricting to tokens with `prob >= epsilon`. Takes the
    largest min_tokens_to_keep tokens if no tokens satisfy this constraint. See [Truncation Sampling as Language Model
    Desmoothing](https://arxiv.org/abs/2210.15191) for more information.

    Args:
        epsilon (`float`):
            If set to > 0, only the most tokens with probabilities `epsilon` or higher are kept for generation.
        filter_value (`float`, *optional*, defaults to `-float("Inf")`):
            All filtered values will be set to this float value.
        min_tokens_to_keep (`int`, *optional*, defaults to 1):
            Minimum number of tokens that cannot be filtered.
    '''
    epsilon: Incomplete
    filter_value: Incomplete
    min_tokens_to_keep: Incomplete
    def __init__(self, epsilon: float, filter_value: float = ..., min_tokens_to_keep: int = 1) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class EtaLogitsWarper(LogitsWarper):
    """
    [`LogitsWarper`] that performs eta-sampling, i.e. calculates a dynamic cutoff `eta := min(epsilon, sqrt(epsilon,
    e^-entropy(probabilities)))` and restricts to tokens with `prob >= eta`. Takes the largest min_tokens_to_keep
    tokens if no tokens satisfy this constraint. See [Truncation Sampling as Language Model
    Desmoothing](https://arxiv.org/abs/2210.15191) for more information.

    Args:
        min_tokens_to_keep (`int`, *optional*, defaults to 1):
            Minimum number of tokens that cannot be filtered."""
    epsilon: Incomplete
    filter_value: Incomplete
    min_tokens_to_keep: Incomplete
    def __init__(self, epsilon: float, filter_value: float = ..., min_tokens_to_keep: int = 1) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class NoRepeatNGramLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] that enforces no repetition of n-grams. See
    [Fairseq](https://github.com/pytorch/fairseq/blob/a07cb6f40480928c9e0548b737aadd36ee66ac76/fairseq/sequence_generator.py#L345).

    Args:
        ngram_size (`int`):
            All ngrams of size `ngram_size` can only occur once.
    """
    ngram_size: Incomplete
    def __init__(self, ngram_size: int) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class EncoderNoRepeatNGramLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] that enforces no repetition of encoder input ids n-grams for the decoder ids. See
    [ParlAI](https://github.com/facebookresearch/ParlAI/blob/master/parlai/core/torch_generator_agent.py#L1350).

    Args:
        encoder_ngram_size (`int`):
            All ngrams of size `ngram_size` can only occur within the encoder input ids.
        encoder_input_ids (`int`):
            The encoder_input_ids that should not be repeated within the decoder ids.
    """
    ngram_size: Incomplete
    batch_size: Incomplete
    generated_ngrams: Incomplete
    def __init__(self, encoder_ngram_size: int, encoder_input_ids: torch.LongTensor) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class NoBadWordsLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] that enforces that specified sequences will never be sampled.

    Args:
        bad_words_ids (`List[List[int]]`):
            List of list of token ids that are not allowed to be generated. In order to get the token ids of the words
            that should not appear in the generated text, use `tokenizer(bad_words, add_prefix_space=True,
            add_special_tokens=False).input_ids`.
        eos_token_id (`Union[int, List[int]]`):
            The id of the *end-of-sequence* token. Optionally, use a list to set multiple *end-of-sequence* tokens.
    """
    bad_words_id_length_1: Incomplete
    bad_words_id_length_greater_than_1: Incomplete
    static_bad_words_mask: Incomplete
    def __init__(self, bad_words_ids: List[List[int]], eos_token_id: Union[int, List[int]]) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class PrefixConstrainedLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] that enforces constrained generation and is useful for prefix-conditioned constrained
    generation. See [Autoregressive Entity Retrieval](https://arxiv.org/abs/2010.00904) for more information.

    Args:
        prefix_allowed_tokens_fn: (`Callable[[int, torch.Tensor], List[int]]`):
            This function constraints the beam search to allowed tokens only at each step. This function takes 2
            arguments `inputs_ids` and the batch ID `batch_id`. It has to return a list with the allowed tokens for the
            next generation step conditioned on the previously generated tokens `inputs_ids` and the batch ID
            `batch_id`.
    """
    def __init__(self, prefix_allowed_tokens_fn: Callable[[int, torch.Tensor], List[int]], num_beams: int) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class HammingDiversityLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] that enforces diverse beam search. Note that this logits processor is only effective for
    [`PreTrainedModel.group_beam_search`]. See [Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence
    Models](https://arxiv.org/pdf/1610.02424.pdf) for more details.

    Args:
        diversity_penalty (`float`):
            This value is subtracted from a beam's score if it generates a token same as any beam from other group at a
            particular time. Note that `diversity_penalty` is only effective if `group beam search` is enabled.
        num_beams (`int`):
            Number of beams used for group beam search. See [this paper](https://arxiv.org/pdf/1610.02424.pdf) for more
            details.
        num_beam_groups (`int`):
            Number of groups to divide `num_beams` into in order to ensure diversity among different groups of beams.
            See [this paper](https://arxiv.org/pdf/1610.02424.pdf) for more details.
    """
    def __init__(self, diversity_penalty: float, num_beams: int, num_beam_groups: int) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, current_tokens: torch.LongTensor, beam_group_idx: int) -> torch.FloatTensor: ...

class ForcedBOSTokenLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] that enforces the specified token as the first generated token.

    Args:
        bos_token_id (`int`):
            The id of the token to force as the first generated token.
    """
    bos_token_id: Incomplete
    def __init__(self, bos_token_id: int) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class ForcedEOSTokenLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] that enforces the specified token as the last generated token when `max_length` is reached.

    Args:
        max_length (`int`):
            The maximum length of the sequence to be generated.
        eos_token_id (`Union[int, List[int]]`):
            The id of the token to force as the last generated token when `max_length` is reached. Optionally, use a
            list to set multiple *end-of-sequence* tokens.
    """
    max_length: Incomplete
    eos_token_id: Incomplete
    def __init__(self, max_length: int, eos_token_id: Union[int, List[int]]) -> None: ...
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class InfNanRemoveLogitsProcessor(LogitsProcessor):
    """
    [`LogitsProcessor`] that removes all `nan` and `inf` values to avoid the generation method to fail. Note that using
    the logits processor should only be used if necessary since it can slow down the generation method. `max_length` is
    reached.
    """
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor: ...

class ExponentialDecayLengthPenalty(LogitsProcessor):
    """
    [`LogitsProcessor`] that exponentially increases the score of the eos_token_id after regulation_start has been
    reached.

    Args:
        exponential_decay_length_penalty (`tuple(int, float)`, *optional*):
            This tuple shall consist of: `(start_index, decay_factor)` where `start_index` indicates where penalty
            starts and `decay_factor` represents the factor of exponential decay
        eos_token_id (`Union[int, List[int]]`):
            The id of the *end-of-sequence* token. Optionally, use a list to set multiple *end-of-sequence* tokens.
        input_ids_seq_length (`int`):
            The length of the input sequence.
    """
    regulation_start: Incomplete
    regulation_factor: Incomplete
    eos_token_id: Incomplete
    def __init__(self, exponential_decay_length_penalty: Tuple, eos_token_id: Union[int, List[int]], input_ids_seq_length: int) -> None: ...
    def __call__(self, input_ids: torch.Tensor, scores: torch.Tensor) -> torch.FloatTensor: ...

class LogitNormalization(LogitsProcessor, LogitsWarper):
    """
    [`LogitsWarper`] and [`LogitsProcessor`] for normalizing the scores using log-softmax. It's important to normalize
    the scores during beam search, after applying the logits processors or warpers, since the search algorithm used in
    this library doesn't do it (it only does it before, but they may need re-normalization) but it still supposes that
    the scores are normalized when comparing the hypotheses.
    """
    def __call__(self, input_ids: torch.Tensor, scores: torch.Tensor) -> torch.Tensor: ...

class SuppressTokensAtBeginLogitsProcessor(LogitsProcessor):
    """
    [`SuppressTokensAtBeginLogitsProcessor`] supresses a list of tokens as soon as the `generate` function starts
    generating using `begin_index` tokens. This should ensure that the tokens defined by `begin_suppress_tokens` at not
    sampled at the begining of the generation.
    """
    begin_suppress_tokens: Incomplete
    begin_index: Incomplete
    def __init__(self, begin_suppress_tokens, begin_index) -> None: ...
    def __call__(self, input_ids, scores): ...

class SuppressTokensLogitsProcessor(LogitsProcessor):
    """This processor can be used to suppress a list of tokens. The processor will set their log probs to `-inf` so that they
    are not sampled."""
    suppress_tokens: Incomplete
    def __init__(self, suppress_tokens) -> None: ...
    def __call__(self, input_ids, scores): ...

class ForceTokensLogitsProcessor(LogitsProcessor):
    """This processor takes a list of pairs of integers which indicates a mapping from generation indices to token
    indices that will be forced before sampling. The processor will set their log probs to `inf` so that they are
    sampled at their corresponding index."""
    force_token_map: Incomplete
    def __init__(self, force_token_map: List[List[int]]) -> None: ...
    def __call__(self, input_ids, scores): ...

class WhisperTimeStampLogitsProcessor(LogitsProcessor):
    '''
    Whisper specific Processor. This processor can be used to force a list of tokens. The processor will set their log
    probs to `inf` so that they are sampled at their corresponding index.

    Args:
        begin_index (`int`, *optional*, defaults to 5 ):
            This indicates to the processor where the first tokens are generated. This is used to differentiate between
            the `prompt` tokens and the `generated` tokens. When generating with `WhisperForConditionalGeneration` the
            `prompt` tokens are the first 4 tokens.
        eos_token_id (`int`, *optional*, defaults to 50257):
            The id of the *end-of-sequence* token.
        no_timestamps_token_id (`int`, *optional*, defaults to 50363):
            The id of the `"<|notimestamps|>"` token.
        max_initial_timestamp (`int`, *optional*, defaults to 1):
            Used to set the maximum value of the initial timestamp. This is used to prevent the model from predicting
            timestamps that are too far in the future.
    '''
    eos_token_id: Incomplete
    no_timestamps_token_id: Incomplete
    timestamp_begin: Incomplete
    begin_index: Incomplete
    max_initial_timestamp_index: Incomplete
    def __init__(self, begin_index: int = 5, eos_token_id: int = 50257, no_timestamps_token_id: int = 50363, max_initial_timestamp: int = 1) -> None: ...
    def __call__(self, input_ids, scores): ...
