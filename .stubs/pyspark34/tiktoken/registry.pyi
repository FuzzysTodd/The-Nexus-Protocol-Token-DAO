from tiktoken.core import Encoding as Encoding
from typing import Any, Callable

ENCODINGS: dict[str, Encoding]
ENCODING_CONSTRUCTORS: dict[str, Callable[[], dict[str, Any]]] | None

def get_encoding(encoding_name: str) -> Encoding: ...
def list_encoding_names() -> list[str]: ...
