import re
from typing import Dict, List, Sequence

DECODE_DEFAULT_CHARS: str
DECODE_COMPONENT_CHARS: str
decode_cache: Dict[str, List[str]]

def get_decode_cache(exclude: str) -> Sequence[str]: ...
def decode(string: str, exclude: str = ...) -> str: ...
def repl_func_with_cache(match: re.Match, cache: Sequence[str]) -> str: ...
