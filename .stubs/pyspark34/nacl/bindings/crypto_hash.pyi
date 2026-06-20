from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure

crypto_hash_BYTES: int
crypto_hash_sha256_BYTES: int
crypto_hash_sha512_BYTES: int

def crypto_hash(message: bytes) -> bytes:
    """
    Hashes and returns the message ``message``.

    :param message: bytes
    :rtype: bytes
    """
def crypto_hash_sha256(message: bytes) -> bytes:
    """
    Hashes and returns the message ``message``.

    :param message: bytes
    :rtype: bytes
    """
def crypto_hash_sha512(message: bytes) -> bytes:
    """
    Hashes and returns the message ``message``.

    :param message: bytes
    :rtype: bytes
    """
