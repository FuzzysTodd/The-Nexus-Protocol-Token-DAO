import functools
from _typeshed import Incomplete
from typing import AbstractSet, Collection, Literal, NoReturn

class Encoding:
    name: Incomplete
    max_token_value: Incomplete
    def __init__(self, name: str, *, pat_str: str, mergeable_ranks: dict[bytes, int], special_tokens: dict[str, int], explicit_n_vocab: int | None = None) -> None:
        """Creates an Encoding object.

        See openai_public.py for examples of how to construct an Encoding object.

        Args:
            name: The name of the encoding. It should be clear from the name of the encoding
                what behaviour to expect, in particular, encodings with different special tokens
                should have different names.
            pat_str: A regex pattern string that is used to split the input text.
            mergeable_ranks: A dictionary mapping mergeable token bytes to their ranks. The ranks
                must correspond to merge priority.
            special_tokens: A dictionary mapping special token strings to their token values.
            explicit_n_vocab: The number of tokens in the vocabulary. If provided, it is checked
                that the number of mergeable tokens and special tokens is equal to this number.
        """
    def encode_ordinary(self, text: str) -> list[int]:
        '''Encodes a string into tokens, ignoring special tokens.

        This is equivalent to `encode(text, disallowed_special=())` (but slightly faster).

        ```
        >>> enc.encode_ordinary("hello world")
        [31373, 995]
        '''
    def encode(self, text: str, *, allowed_special: Literal['all'] | AbstractSet[str] = ..., disallowed_special: Literal['all'] | Collection[str] = 'all') -> list[int]:
        '''Encodes a string into tokens.

        Special tokens are artificial tokens used to unlock capabilities from a model,
        such as fill-in-the-middle. So we want to be careful about accidentally encoding special
        tokens, since they can be used to trick a model into doing something we don\'t want it to do.

        Hence, by default, encode will raise an error if it encounters text that corresponds
        to a special token. This can be controlled on a per-token level using the `allowed_special`
        and `disallowed_special` parameters. In particular:
        - Setting `disallowed_special` to () will prevent this function from raising errors and
          cause all text corresponding to special tokens to be encoded as natural text.
        - Setting `allowed_special` to "all" will cause this function to treat all text
          corresponding to special tokens to be encoded as special tokens.

        ```
        >>> enc.encode("hello world")
        [31373, 995]
        >>> enc.encode("<|endoftext|>", allowed_special={"<|endoftext|>"})
        [50256]
        >>> enc.encode("<|endoftext|>", allowed_special="all")
        [50256]
        >>> enc.encode("<|endoftext|>")
        # Raises ValueError
        >>> enc.encode("<|endoftext|>", disallowed_special=())
        [27, 91, 437, 1659, 5239, 91, 29]
        ```
        '''
    def encode_ordinary_batch(self, text: list[str], *, num_threads: int = 8) -> list[list[int]]:
        '''Encodes a list of strings into tokens, in parallel, ignoring special tokens.

        This is equivalent to `encode_batch(text, disallowed_special=())` (but slightly faster).

        ```
        >>> enc.encode_ordinary_batch(["hello world", "goodbye world"])
        [[31373, 995], [11274, 16390, 995]]
        ```
        '''
    def encode_batch(self, text: list[str], *, num_threads: int = 8, allowed_special: Literal['all'] | AbstractSet[str] = ..., disallowed_special: Literal['all'] | Collection[str] = 'all') -> list[list[int]]:
        '''Encodes a list of strings into tokens, in parallel.

        See `encode` for more details on `allowed_special` and `disallowed_special`.

        ```
        >>> enc.encode_batch(["hello world", "goodbye world"])
        [[31373, 995], [11274, 16390, 995]]
        ```
        '''
    def encode_with_unstable(self, text: str, *, allowed_special: Literal['all'] | AbstractSet[str] = ..., disallowed_special: Literal['all'] | Collection[str] = 'all') -> tuple[list[int], list[list[int]]]:
        '''Encodes a string into stable tokens and possible completion sequences.

        Note that the stable tokens will only represent a substring of `text`.

        See `encode` for more details on `allowed_special` and `disallowed_special`.

        This API should itself be considered unstable.

        ```
        >>> enc.encode_with_unstable("hello fanta")
        ([31373], [(277, 4910), (5113, 265), ..., (8842,)])

        >>> text = "..."
        >>> stable_tokens, completions = enc.encode_with_unstable(text)
        >>> assert text.encode().startswith(enc.decode_bytes(stable_tokens))
        >>> assert all(enc.decode_bytes(stable_tokens + seq).startswith(text.encode()) for seq in completions)
        ```
        '''
    def encode_single_token(self, text_or_bytes: str | bytes) -> int:
        '''Encodes text corresponding to a single token to its token value.

        NOTE: this will encode all special tokens.

        Raises `KeyError` if the token is not in the vocabulary.

        ```
        >>> enc.encode_single_token("hello")
        31373
        ```
        '''
    def decode_bytes(self, tokens: list[int]) -> bytes:
        """Decodes a list of tokens into bytes.

        ```
        >>> enc.decode_bytes([31373, 995])
        b'hello world'
        ```
        """
    def decode(self, tokens: list[int], errors: str = 'replace') -> str:
        """Decodes a list of tokens into a string.

        WARNING: the default behaviour of this function is lossy, since decoded bytes are not
        guaranteed to be valid UTF-8. You can control this behaviour using the `errors` parameter,
        for instance, setting `errors=strict`.

        ```
        >>> enc.decode([31373, 995])
        'hello world'
        ```
        """
    def decode_single_token_bytes(self, token: int) -> bytes:
        """Decodes a token into bytes.

        NOTE: this will decode all special tokens.

        Raises `KeyError` if the token is not in the vocabulary.

        ```
        >>> enc.decode_single_token_bytes(31373)
        b'hello'
        ```
        """
    def decode_tokens_bytes(self, tokens: list[int]) -> list[bytes]:
        """Decodes a list of tokens into a list of bytes.

        Useful for visualising tokenisation.
        >>> enc.decode_tokens_bytes([31373, 995])
        [b'hello', b' world']
        """
    def decode_with_offsets(self, tokens: list[int]) -> tuple[str, list[int]]:
        """Decodes a list of tokens into a string and a list of offsets.

        Each offset is the index into text corresponding to the start of each token.
        If UTF-8 character boundaries do not line up with token boundaries, the offset is the index
        of the first character that contains bytes from the token.

        This will currently raise if given tokens that decode to invalid UTF-8; this behaviour may
        change in the future to be more permissive.

        >>> enc.decode_with_offsets([31373, 995])
        ('hello world', [0, 5])
        """
    def decode_batch(self, batch: list[list[int]], *, errors: str = 'replace', num_threads: int = 8) -> list[str]:
        """Decodes a batch (list of lists of tokens) into a list of strings."""
    def decode_bytes_batch(self, batch: list[list[int]], *, num_threads: int = 8) -> list[bytes]:
        """Decodes a batch (list of lists of tokens) into a list of bytes."""
    def token_byte_values(self) -> list[bytes]:
        """Returns the list of all token byte values."""
    @property
    def eot_token(self) -> int: ...
    @functools.cached_property
    def special_tokens_set(self) -> set[str]: ...
    @property
    def n_vocab(self) -> int:
        """For backwards compatibility. Prefer to use `enc.max_token_value + 1`."""

def raise_disallowed_special_token(token: str) -> NoReturn: ...
