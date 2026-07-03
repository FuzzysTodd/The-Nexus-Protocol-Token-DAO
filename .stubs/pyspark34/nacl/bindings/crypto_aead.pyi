from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure

crypto_aead_chacha20poly1305_ietf_KEYBYTES: int
crypto_aead_chacha20poly1305_ietf_NSECBYTES: int
crypto_aead_chacha20poly1305_ietf_NPUBBYTES: int
crypto_aead_chacha20poly1305_ietf_ABYTES: int
crypto_aead_chacha20poly1305_ietf_MESSAGEBYTES_MAX: int
crypto_aead_chacha20poly1305_KEYBYTES: int
crypto_aead_chacha20poly1305_NSECBYTES: int
crypto_aead_chacha20poly1305_NPUBBYTES: int
crypto_aead_chacha20poly1305_ABYTES: int
crypto_aead_chacha20poly1305_MESSAGEBYTES_MAX: int
crypto_aead_xchacha20poly1305_ietf_KEYBYTES: int
crypto_aead_xchacha20poly1305_ietf_NSECBYTES: int
crypto_aead_xchacha20poly1305_ietf_NPUBBYTES: int
crypto_aead_xchacha20poly1305_ietf_ABYTES: int
crypto_aead_xchacha20poly1305_ietf_MESSAGEBYTES_MAX: int

def crypto_aead_chacha20poly1305_ietf_encrypt(message: bytes, aad: bytes | None, nonce: bytes, key: bytes) -> bytes:
    """
    Encrypt the given ``message`` using the IETF ratified chacha20poly1305
    construction described in RFC7539.

    :param message:
    :type message: bytes
    :param aad:
    :type aad: Optional[bytes]
    :param nonce:
    :type nonce: bytes
    :param key:
    :type key: bytes
    :return: authenticated ciphertext
    :rtype: bytes
    """
def crypto_aead_chacha20poly1305_ietf_decrypt(ciphertext: bytes, aad: bytes | None, nonce: bytes, key: bytes) -> bytes:
    """
    Decrypt the given ``ciphertext`` using the IETF ratified chacha20poly1305
    construction described in RFC7539.

    :param ciphertext:
    :type ciphertext: bytes
    :param aad:
    :type aad: Optional[bytes]
    :param nonce:
    :type nonce: bytes
    :param key:
    :type key: bytes
    :return: message
    :rtype: bytes
    """
def crypto_aead_chacha20poly1305_encrypt(message: bytes, aad: bytes | None, nonce: bytes, key: bytes) -> bytes:
    '''
    Encrypt the given ``message`` using the "legacy" construction
    described in draft-agl-tls-chacha20poly1305.

    :param message:
    :type message: bytes
    :param aad:
    :type aad: Optional[bytes]
    :param nonce:
    :type nonce: bytes
    :param key:
    :type key: bytes
    :return: authenticated ciphertext
    :rtype: bytes
    '''
def crypto_aead_chacha20poly1305_decrypt(ciphertext: bytes, aad: bytes | None, nonce: bytes, key: bytes) -> bytes:
    '''
    Decrypt the given ``ciphertext`` using the "legacy" construction
    described in draft-agl-tls-chacha20poly1305.

    :param ciphertext: authenticated ciphertext
    :type ciphertext: bytes
    :param aad:
    :type aad: Optional[bytes]
    :param nonce:
    :type nonce: bytes
    :param key:
    :type key: bytes
    :return: message
    :rtype: bytes
    '''
def crypto_aead_xchacha20poly1305_ietf_encrypt(message: bytes, aad: bytes | None, nonce: bytes, key: bytes) -> bytes:
    """
    Encrypt the given ``message`` using the long-nonces xchacha20poly1305
    construction.

    :param message:
    :type message: bytes
    :param aad:
    :type aad: Optional[bytes]
    :param nonce:
    :type nonce: bytes
    :param key:
    :type key: bytes
    :return: authenticated ciphertext
    :rtype: bytes
    """
def crypto_aead_xchacha20poly1305_ietf_decrypt(ciphertext: bytes, aad: bytes | None, nonce: bytes, key: bytes) -> bytes:
    """
    Decrypt the given ``ciphertext`` using the long-nonces xchacha20poly1305
    construction.

    :param ciphertext: authenticated ciphertext
    :type ciphertext: bytes
    :param aad:
    :type aad: Optional[bytes]
    :param nonce:
    :type nonce: bytes
    :param key:
    :type key: bytes
    :return: message
    :rtype: bytes
    """
