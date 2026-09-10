from _typeshed import Incomplete
from typing import Dict, List, Sequence

ASCII_LETTERS_AND_DIGITS: Incomplete
ENCODE_DEFAULT_CHARS: str
ENCODE_COMPONENT_CHARS: str
encode_cache: Dict[str, List[str]]

def get_encode_cache(exclude: str) -> Sequence[str]: ...
def encode(string: str, exclude: str = ..., *, keep_escaped: bool = True) -> str: ...
