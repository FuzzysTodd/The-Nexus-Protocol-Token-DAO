from _typeshed import Incomplete
from typing import Dict

ISO8601: str
ISO8601_PAT: Incomplete
PNG: bytes
PNG64: bytes
JPEG: bytes
JPEG64: bytes
GIF_64: bytes
GIF89_64: bytes
PDF64: bytes

def encode_images(format_dict: Dict) -> Dict[str, str]:
    """b64-encodes images in a displaypub format dict

    Perhaps this should be handled in json_clean itself?

    Parameters
    ----------

    format_dict : dict
        A dictionary of display data keyed by mime-type

    Returns
    -------

    format_dict : dict
        A copy of the same dictionary,
        but binary image data ('image/png', 'image/jpeg' or 'application/pdf')
        is base64-encoded.

    """
def json_clean(obj):
    """Clean an object to ensure it's safe to encode in JSON.

    Atomic, immutable objects are returned unmodified.  Sets and tuples are
    converted to lists, lists are copied and dicts are also copied.

    Note: dicts whose keys could cause collisions upon encoding (such as a dict
    with both the number 1 and the string '1' as keys) will cause a ValueError
    to be raised.

    Parameters
    ----------
    obj : any python object

    Returns
    -------
    out : object

      A version of the input which will not cause an encoding error when
      encoded as JSON.  Note that this function does not *encode* its inputs,
      it simply sanitizes it so that there will be no encoding errors later.

    """
