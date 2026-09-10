import json
from typing import Any, Dict, List

__all__ = ['dumps', 'loads']

jsonmod = json

def dumps(o: Any, **kwargs) -> bytes:
    """Serialize object to JSON bytes (utf-8).

    Keyword arguments are passed along to :py:func:`json.dumps`.
    """
def loads(s: bytes | str, **kwargs) -> Dict | List | str | int | float:
    """Load object from JSON bytes (utf-8).

    Keyword arguments are passed along to :py:func:`json.loads`.
    """
