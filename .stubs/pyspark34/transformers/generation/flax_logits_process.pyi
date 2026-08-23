import jax.numpy as jnp
from ..utils import add_start_docstrings as add_start_docstrings
from ..utils.logging import get_logger as get_logger
from _typeshed import Incomplete

logger: Incomplete
LOGITS_PROCESSOR_INPUTS_DOCSTRING: str

class FlaxLogitsProcessor:
    """Abstract base class for all logit processors that can be applied during generation."""
    def __call__(self, input_ids: jnp.ndarray, scores: jnp.ndarray) -> jnp.ndarray:
        """Flax method for processing logits."""

class FlaxLogitsWarper:
    """Abstract base class for all logit warpers that can be applied during generation with multinomial sampling."""
    def __call__(self, input_ids: jnp.ndarray, scores: jnp.ndarray) -> jnp.ndarray:
        """Flax method for warping logits."""

class FlaxLogitsProcessorList(list):
    """
    This class can be used to create a list of [`FlaxLogitsProcessor`] or [`FlaxLogitsWarper`] to subsequently process
    a `scores` input tensor. This class inherits from list and adds a specific *__call__* method to apply each
    [`FlaxLogitsProcessor`] or [`FlaxLogitsWarper`] to the inputs.
    """
    def __call__(self, input_ids: jnp.ndarray, scores: jnp.ndarray, cur_len: int, **kwargs) -> jnp.ndarray: ...

class FlaxTemperatureLogitsWarper(FlaxLogitsWarper):
    """
    [`FlaxLogitsWarper`] for temperature (exponential scaling output probability distribution).

    Args:
        temperature (`float`):
            The value used to module the logits distribution.
    """
    temperature: Incomplete
    def __init__(self, temperature: float) -> None: ...
    def __call__(self, input_ids: jnp.ndarray, scores: jnp.ndarray, cur_len: int) -> jnp.ndarray: ...

class FlaxTopPLogitsWarper(FlaxLogitsWarper):
    '''
    [`FlaxLogitsWarper`] that performs top-p, i.e. restricting to top tokens summing to prob_cut_off <= prob_cut_off.

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
    def __call__(self, input_ids: jnp.ndarray, scores: jnp.ndarray, cur_len: int) -> jnp.ndarray: ...

class FlaxTopKLogitsWarper(FlaxLogitsWarper):
    '''
    [`FlaxLogitsWarper`] that performs top-k, i.e. restricting to the k highest probability elements.

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
    def __call__(self, input_ids: jnp.ndarray, scores: jnp.ndarray, cur_len: int) -> jnp.ndarray: ...

class FlaxForcedBOSTokenLogitsProcessor(FlaxLogitsProcessor):
    """
    [`FlaxLogitsProcessor`] that enforces the specified token as the first generated token.

    Args:
        bos_token_id (`int`):
            The id of the token to force as the first generated token.
    """
    bos_token_id: Incomplete
    def __init__(self, bos_token_id: int) -> None: ...
    def __call__(self, input_ids: jnp.ndarray, scores: jnp.ndarray, cur_len: int) -> jnp.ndarray: ...

class FlaxForcedEOSTokenLogitsProcessor(FlaxLogitsProcessor):
    """
    [`FlaxLogitsProcessor`] that enforces the specified token as the last generated token when `max_length` is reached.

    Args:
        max_length (`int`):
            The maximum length of the sequence to be generated.
        eos_token_id (`int`):
            The id of the token to force as the last generated token when `max_length` is reached.
    """
    max_length: Incomplete
    eos_token_id: Incomplete
    def __init__(self, max_length: int, eos_token_id: int) -> None: ...
    def __call__(self, input_ids: jnp.ndarray, scores: jnp.ndarray, cur_len: int) -> jnp.ndarray: ...

class FlaxMinLengthLogitsProcessor(FlaxLogitsProcessor):
    '''
    [`FlaxLogitsProcessor`] enforcing a min-length by setting EOS probability to 0.

    Args:
        min_length (`int`):
            The minimum length below which the score of `eos_token_id` is set to `-float("Inf")`.
        eos_token_id (`int`):
            The id of the *end-of-sequence* token.
    '''
    min_length: Incomplete
    eos_token_id: Incomplete
    def __init__(self, min_length: int, eos_token_id: int) -> None: ...
    def __call__(self, input_ids: jnp.ndarray, scores: jnp.ndarray, cur_len: int) -> jnp.ndarray: ...
