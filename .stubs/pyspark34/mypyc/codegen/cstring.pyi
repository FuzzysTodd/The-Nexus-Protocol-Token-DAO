from _typeshed import Incomplete
from typing import Final

CHAR_MAP: Final[Incomplete]
escaped: Incomplete
decoded: Incomplete

def encode_bytes_as_c_string(b: bytes) -> str:
    """Produce contents of a C string literal for a byte string, without quotes."""
def c_string_initializer(value: bytes) -> str:
    '''Create initializer for a C char[]/ char * variable from a string.

    For example, if value if b\'foo\', the result would be \'"foo"\'.
    '''
