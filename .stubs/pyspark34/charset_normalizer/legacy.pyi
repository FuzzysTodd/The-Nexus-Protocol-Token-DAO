from .api import from_bytes as from_bytes
from .constant import CHARDET_CORRESPONDENCE as CHARDET_CORRESPONDENCE
from typing import Any, Dict

def detect(byte_str: bytes, should_rename_legacy: bool = False, **kwargs: Any) -> Dict[str, str | float | None]:
    """
    chardet legacy method
    Detect the encoding of the given byte string. It should be mostly backward-compatible.
    Encoding name will match Chardet own writing whenever possible. (Not on encoding name unsupported by it)
    This function is deprecated and should be used to migrate your project easily, consult the documentation for
    further information. Not planned for removal.

    :param byte_str:     The byte sequence to examine.
    :param should_rename_legacy:  Should we rename legacy encodings
                                  to their more modern equivalents?
    """
