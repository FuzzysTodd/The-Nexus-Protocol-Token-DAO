from _typeshed import Incomplete
from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure

has_crypto_shorthash_siphashx24: Incomplete
BYTES: int
KEYBYTES: int
XBYTES: int
XKEYBYTES: int

def crypto_shorthash_siphash24(data: bytes, key: bytes) -> bytes:
    """Compute a fast, cryptographic quality, keyed hash of the input data

    :param data:
    :type data: bytes
    :param key: len(key) must be equal to
                :py:data:`.KEYBYTES` (16)
    :type key: bytes
    """
def crypto_shorthash_siphashx24(data: bytes, key: bytes) -> bytes:
    """Compute a fast, cryptographic quality, keyed hash of the input data

    :param data:
    :type data: bytes
    :param key: len(key) must be equal to
                :py:data:`.XKEYBYTES` (16)
    :type key: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
