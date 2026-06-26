from _typeshed import Incomplete

class SimpleBytePairEncoding:
    pat_str: Incomplete
    mergeable_ranks: Incomplete
    def __init__(self, *, pat_str: str, mergeable_ranks: dict[bytes, int]) -> None:
        """Creates an Encoding object."""
    def encode(self, text: str, visualise: str | None = 'colour') -> list[int]:
        '''Encodes a string into tokens.

        >>> enc.encode("hello world")
        [388, 372]
        '''
    def decode_bytes(self, tokens: list[int]) -> bytes:
        """Decodes a list of tokens into bytes.

        >>> enc.decode_bytes([388, 372])
        b'hello world'
        """
    def decode(self, tokens: list[int]) -> str:
        '''Decodes a list of tokens into a string.

        Decoded bytes are not guaranteed to be valid UTF-8. In that case, we replace
        the invalid bytes with the replacement character "�".

        >>> enc.decode([388, 372])
        \'hello world\'
        '''
    def decode_tokens_bytes(self, tokens: list[int]) -> list[bytes]:
        """Decodes a list of tokens into a list of bytes.

        Useful for visualising how a string is tokenised.

        >>> enc.decode_tokens_bytes([388, 372])
        [b'hello', b' world']
        """
    @staticmethod
    def train(training_data: str, vocab_size: int, pat_str: str):
        """Train a BPE tokeniser on some data!"""
    @staticmethod
    def from_tiktoken(encoding): ...

def bpe_encode(mergeable_ranks: dict[bytes, int], input: bytes, visualise: str | None = 'colour') -> list[int]: ...
def bpe_train(data: str, vocab_size: int, pat_str: str, visualise: str | None = 'colour') -> dict[bytes, int]: ...
def visualise_tokens(token_values: list[bytes]) -> None: ...
def train_simple_encoding(): ...
