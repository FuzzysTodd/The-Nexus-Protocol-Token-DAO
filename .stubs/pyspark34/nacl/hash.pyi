import nacl.encoding
from _typeshed import Incomplete

BLAKE2B_BYTES: Incomplete
BLAKE2B_BYTES_MIN: Incomplete
BLAKE2B_BYTES_MAX: Incomplete
BLAKE2B_KEYBYTES: Incomplete
BLAKE2B_KEYBYTES_MIN: Incomplete
BLAKE2B_KEYBYTES_MAX: Incomplete
BLAKE2B_SALTBYTES: Incomplete
BLAKE2B_PERSONALBYTES: Incomplete
SIPHASH_BYTES: Incomplete
SIPHASH_KEYBYTES: Incomplete
SIPHASHX_AVAILABLE: Incomplete
SIPHASHX_BYTES: Incomplete
SIPHASHX_KEYBYTES: Incomplete

def sha256(message: bytes, encoder: nacl.encoding.Encoder = ...) -> bytes:
    """
    Hashes ``message`` with SHA256.

    :param message: The message to hash.
    :type message: bytes
    :param encoder: A class that is able to encode the hashed message.
    :returns: The hashed message.
    :rtype: bytes
    """
def sha512(message: bytes, encoder: nacl.encoding.Encoder = ...) -> bytes:
    """
    Hashes ``message`` with SHA512.

    :param message: The message to hash.
    :type message: bytes
    :param encoder: A class that is able to encode the hashed message.
    :returns: The hashed message.
    :rtype: bytes
    """
def blake2b(data: bytes, digest_size: int = ..., key: bytes = b'', salt: bytes = b'', person: bytes = b'', encoder: nacl.encoding.Encoder = ...) -> bytes:
    """
    Hashes ``data`` with blake2b.

    :param data: the digest input byte sequence
    :type data: bytes
    :param digest_size: the requested digest size; must be at most
                        :const:`BLAKE2B_BYTES_MAX`;
                        the default digest size is
                        :const:`BLAKE2B_BYTES`
    :type digest_size: int
    :param key: the key to be set for keyed MAC/PRF usage; if set, the key
                must be at most :data:`~nacl.hash.BLAKE2B_KEYBYTES_MAX` long
    :type key: bytes
    :param salt: an initialization salt at most
                 :const:`BLAKE2B_SALTBYTES` long;
                 it will be zero-padded if needed
    :type salt: bytes
    :param person: a personalization string at most
                   :const:`BLAKE2B_PERSONALBYTES` long;
                   it will be zero-padded if needed
    :type person: bytes
    :param encoder: the encoder to use on returned digest
    :type encoder: class
    :returns: The hashed message.
    :rtype: bytes
    """
generichash = blake2b

def siphash24(message: bytes, key: bytes = b'', encoder: nacl.encoding.Encoder = ...) -> bytes:
    """
    Computes a keyed MAC of ``message`` using the short-input-optimized
    siphash-2-4 construction.

    :param message: The message to hash.
    :type message: bytes
    :param key: the message authentication key for the siphash MAC construct
    :type key: bytes(:const:`SIPHASH_KEYBYTES`)
    :param encoder: A class that is able to encode the hashed message.
    :returns: The hashed message.
    :rtype: bytes(:const:`SIPHASH_BYTES`)
    """
shorthash = siphash24

def siphashx24(message: bytes, key: bytes = b'', encoder: nacl.encoding.Encoder = ...) -> bytes:
    """
    Computes a keyed MAC of ``message`` using the 128 bit variant of the
    siphash-2-4 construction.

    :param message: The message to hash.
    :type message: bytes
    :param key: the message authentication key for the siphash MAC construct
    :type key: bytes(:const:`SIPHASHX_KEYBYTES`)
    :param encoder: A class that is able to encode the hashed message.
    :returns: The hashed message.
    :rtype: bytes(:const:`SIPHASHX_BYTES`)
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.

    .. versionadded:: 1.2
    """
