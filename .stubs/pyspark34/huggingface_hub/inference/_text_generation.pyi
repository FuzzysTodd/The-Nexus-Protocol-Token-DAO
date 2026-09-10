from ..utils import is_pydantic_available as is_pydantic_available
from dataclasses import dataclass
from enum import Enum
from requests import HTTPError
from typing import List, NoReturn

@dataclass
class TextGenerationParameters:
    """
    Parameters for text generation.

    Args:
        do_sample (`bool`, *optional*):
            Activate logits sampling. Defaults to False.
        max_new_tokens (`int`, *optional*):
            Maximum number of generated tokens. Defaults to 20.
        repetition_penalty (`Optional[float]`, *optional*):
            The parameter for repetition penalty. A value of 1.0 means no penalty. See [this paper](https://arxiv.org/pdf/1909.05858.pdf)
            for more details. Defaults to None.
        return_full_text (`bool`, *optional*):
            Whether to prepend the prompt to the generated text. Defaults to False.
        stop (`List[str]`, *optional*):
            Stop generating tokens if a member of `stop_sequences` is generated. Defaults to an empty list.
        seed (`Optional[int]`, *optional*):
            Random sampling seed. Defaults to None.
        temperature (`Optional[float]`, *optional*):
            The value used to modulate the logits distribution. Defaults to None.
        top_k (`Optional[int]`, *optional*):
            The number of highest probability vocabulary tokens to keep for top-k-filtering. Defaults to None.
        top_p (`Optional[float]`, *optional*):
            If set to a value less than 1, only the smallest set of most probable tokens with probabilities that add up
            to `top_p` or higher are kept for generation. Defaults to None.
        truncate (`Optional[int]`, *optional*):
            Truncate input tokens to the given size. Defaults to None.
        typical_p (`Optional[float]`, *optional*):
            Typical Decoding mass. See [Typical Decoding for Natural Language Generation](https://arxiv.org/abs/2202.00666)
            for more information. Defaults to None.
        best_of (`Optional[int]`, *optional*):
            Generate `best_of` sequences and return the one with the highest token logprobs. Defaults to None.
        watermark (`bool`, *optional*):
            Watermarking with [A Watermark for Large Language Models](https://arxiv.org/abs/2301.10226). Defaults to False.
        details (`bool`, *optional*):
            Get generation details. Defaults to False.
        decoder_input_details (`bool`, *optional*):
            Get decoder input token logprobs and ids. Defaults to False.
    """
    do_sample: bool = ...
    max_new_tokens: int = ...
    repetition_penalty: float | None = ...
    return_full_text: bool = ...
    stop: List[str] = ...
    seed: int | None = ...
    temperature: float | None = ...
    top_k: int | None = ...
    top_p: float | None = ...
    truncate: int | None = ...
    typical_p: float | None = ...
    best_of: int | None = ...
    watermark: bool = ...
    details: bool = ...
    decoder_input_details: bool = ...
    def valid_best_of(cls, field_value, values): ...
    def valid_repetition_penalty(cls, v): ...
    def valid_seed(cls, v): ...
    def valid_temp(cls, v): ...
    def valid_top_k(cls, v): ...
    def valid_top_p(cls, v): ...
    def valid_truncate(cls, v): ...
    def valid_typical_p(cls, v): ...

@dataclass
class TextGenerationRequest:
    """
    Request object for text generation (only for internal use).

    Args:
        inputs (`str`):
            The prompt for text generation.
        parameters (`Optional[TextGenerationParameters]`, *optional*):
            Generation parameters.
        stream (`bool`, *optional*):
            Whether to stream output tokens. Defaults to False.
    """
    inputs: str
    parameters: TextGenerationParameters | None = ...
    stream: bool = ...
    def valid_input(cls, v): ...
    def valid_best_of_stream(cls, field_value, values): ...

@dataclass
class InputToken:
    """
    Represents an input token.

    Args:
        id (`int`):
            Token ID from the model tokenizer.
        text (`str`):
            Token text.
        logprob (`float` or `None`):
            Log probability of the token. Optional since the logprob of the first token cannot be computed.
    """
    id: int
    text: str
    logprob: float | None = ...

@dataclass
class Token:
    """
    Represents a token.

    Args:
        id (`int`):
            Token ID from the model tokenizer.
        text (`str`):
            Token text.
        logprob (`float`):
            Log probability of the token.
        special (`bool`):
            Indicates whether the token is a special token. It can be used to ignore
            tokens when concatenating.
    """
    id: int
    text: str
    logprob: float
    special: bool

class FinishReason(str, Enum):
    Length: str
    EndOfSequenceToken: str
    StopSequence: str

@dataclass
class BestOfSequence:
    """
    Represents a best-of sequence generated during text generation.

    Args:
        generated_text (`str`):
            The generated text.
        finish_reason (`FinishReason`):
            The reason for the generation to finish, represented by a `FinishReason` value.
        generated_tokens (`int`):
            The number of generated tokens in the sequence.
        seed (`Optional[int]`):
            The sampling seed if sampling was activated.
        prefill (`List[InputToken]`):
            The decoder input tokens. Empty if `decoder_input_details` is False. Defaults to an empty list.
        tokens (`List[Token]`):
            The generated tokens. Defaults to an empty list.
    """
    generated_text: str
    finish_reason: FinishReason
    generated_tokens: int
    seed: int | None = ...
    prefill: List[InputToken] = ...
    tokens: List[Token] = ...

@dataclass
class Details:
    """
    Represents details of a text generation.

    Args:
        finish_reason (`FinishReason`):
            The reason for the generation to finish, represented by a `FinishReason` value.
        generated_tokens (`int`):
            The number of generated tokens.
        seed (`Optional[int]`):
            The sampling seed if sampling was activated.
        prefill (`List[InputToken]`, *optional*):
            The decoder input tokens. Empty if `decoder_input_details` is False. Defaults to an empty list.
        tokens (`List[Token]`):
            The generated tokens. Defaults to an empty list.
        best_of_sequences (`Optional[List[BestOfSequence]]`):
            Additional sequences when using the `best_of` parameter.
    """
    finish_reason: FinishReason
    generated_tokens: int
    seed: int | None = ...
    prefill: List[InputToken] = ...
    tokens: List[Token] = ...
    best_of_sequences: List[BestOfSequence] | None = ...

@dataclass
class TextGenerationResponse:
    """
    Represents a response for text generation.

    Only returned when `details=True`, otherwise a string is returned.

    Args:
        generated_text (`str`):
            The generated text.
        details (`Optional[Details]`):
            Generation details. Returned only if `details=True` is sent to the server.
    """
    generated_text: str
    details: Details | None = ...

@dataclass
class StreamDetails:
    """
    Represents details of a text generation stream.

    Args:
        finish_reason (`FinishReason`):
            The reason for the generation to finish, represented by a `FinishReason` value.
        generated_tokens (`int`):
            The number of generated tokens.
        seed (`Optional[int]`):
            The sampling seed if sampling was activated.
    """
    finish_reason: FinishReason
    generated_tokens: int
    seed: int | None = ...

@dataclass
class TextGenerationStreamResponse:
    """
    Represents a response for streaming text generation.

    Only returned when `details=True` and `stream=True`.

    Args:
        token (`Token`):
            The generated token.
        generated_text (`Optional[str]`, *optional*):
            The complete generated text. Only available when the generation is finished.
        details (`Optional[StreamDetails]`, *optional*):
            Generation details. Only available when the generation is finished.
    """
    token: Token
    generated_text: str | None = ...
    details: StreamDetails | None = ...

class TextGenerationError(HTTPError):
    """Generic error raised if text-generation went wrong."""
class ValidationError(TextGenerationError):
    """Server-side validation error."""
class GenerationError(TextGenerationError): ...
class OverloadedError(TextGenerationError): ...
class IncompleteGenerationError(TextGenerationError): ...
class UnknownError(TextGenerationError): ...

def raise_text_generation_error(http_error: HTTPError) -> NoReturn:
    """
    Try to parse text-generation-inference error message and raise HTTPError in any case.

    Args:
        error (`HTTPError`):
            The HTTPError that have been raised.
    """
