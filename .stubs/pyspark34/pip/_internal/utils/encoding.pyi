from _typeshed import Incomplete
from typing import List, Tuple

BOMS: List[Tuple[bytes, str]]
ENCODING_RE: Incomplete

def auto_decode(data: bytes) -> str:
    """Check a bytes string for a BOM to correctly detect the encoding

    Fallback to locale.getpreferredencoding(False) like open() on Python3"""
