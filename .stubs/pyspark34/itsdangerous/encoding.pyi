from .exc import BadData as BadData

def want_bytes(s: _t_str_bytes, encoding: str = 'utf-8', errors: str = 'strict') -> bytes: ...
def base64_encode(string: _t_str_bytes) -> bytes:
    """Base64 encode a string of bytes or text. The resulting bytes are
    safe to use in URLs.
    """
def base64_decode(string: _t_str_bytes) -> bytes:
    """Base64 decode a URL-safe string of bytes or text. The result is
    bytes.
    """
def int_to_bytes(num: int) -> bytes: ...
def bytes_to_int(bytestr: bytes) -> int: ...
