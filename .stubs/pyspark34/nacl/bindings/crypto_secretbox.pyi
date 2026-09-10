from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure

crypto_secretbox_KEYBYTES: int
crypto_secretbox_NONCEBYTES: int
crypto_secretbox_ZEROBYTES: int
crypto_secretbox_BOXZEROBYTES: int
crypto_secretbox_MACBYTES: int
crypto_secretbox_MESSAGEBYTES_MAX: int

def crypto_secretbox(message: bytes, nonce: bytes, key: bytes) -> bytes:
    """
    Encrypts and returns the message ``message`` with the secret ``key`` and
    the nonce ``nonce``.

    :param message: bytes
    :param nonce: bytes
    :param key: bytes
    :rtype: bytes
    """
def crypto_secretbox_open(ciphertext: bytes, nonce: bytes, key: bytes) -> bytes:
    """
    Decrypt and returns the encrypted message ``ciphertext`` with the secret
    ``key`` and the nonce ``nonce``.

    :param ciphertext: bytes
    :param nonce: bytes
    :param key: bytes
    :rtype: bytes
    """
