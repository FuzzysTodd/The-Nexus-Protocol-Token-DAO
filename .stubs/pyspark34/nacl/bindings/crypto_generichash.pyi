from _typeshed import Incomplete
from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure
from typing import NoReturn

crypto_generichash_BYTES: int
crypto_generichash_BYTES_MIN: int
crypto_generichash_BYTES_MAX: int
crypto_generichash_KEYBYTES: int
crypto_generichash_KEYBYTES_MIN: int
crypto_generichash_KEYBYTES_MAX: int
crypto_generichash_SALTBYTES: int
crypto_generichash_PERSONALBYTES: int
crypto_generichash_STATEBYTES: int

def generichash_blake2b_salt_personal(data: bytes, digest_size: int = ..., key: bytes = b'', salt: bytes = b'', person: bytes = b'') -> bytes:
    """One shot hash interface

    :param data: the input data to the hash function
    :type data: bytes
    :param digest_size: must be at most
                        :py:data:`.crypto_generichash_BYTES_MAX`;
                        the default digest size is
                        :py:data:`.crypto_generichash_BYTES`
    :type digest_size: int
    :param key: must be at most
                :py:data:`.crypto_generichash_KEYBYTES_MAX` long
    :type key: bytes
    :param salt: must be at most
                 :py:data:`.crypto_generichash_SALTBYTES` long;
                 will be zero-padded if needed
    :type salt: bytes
    :param person: must be at most
                   :py:data:`.crypto_generichash_PERSONALBYTES` long:
                   will be zero-padded if needed
    :type person: bytes
    :return: digest_size long digest
    :rtype: bytes
    """

class Blake2State:
    """
    Python-level wrapper for the crypto_generichash_blake2b state buffer
    """
    digest_size: Incomplete
    def __init__(self, digest_size: int) -> None: ...
    def __reduce__(self) -> NoReturn:
        """
        Raise the same exception as hashlib's blake implementation
        on copy.copy()
        """
    def copy(self) -> _Blake2State: ...

def generichash_blake2b_init(key: bytes = b'', salt: bytes = b'', person: bytes = b'', digest_size: int = ...) -> Blake2State:
    """
    Create a new initialized blake2b hash state

    :param key: must be at most
                :py:data:`.crypto_generichash_KEYBYTES_MAX` long
    :type key: bytes
    :param salt: must be at most
                 :py:data:`.crypto_generichash_SALTBYTES` long;
                 will be zero-padded if needed
    :type salt: bytes
    :param person: must be at most
                   :py:data:`.crypto_generichash_PERSONALBYTES` long:
                   will be zero-padded if needed
    :type person: bytes
    :param digest_size: must be at most
                        :py:data:`.crypto_generichash_BYTES_MAX`;
                        the default digest size is
                        :py:data:`.crypto_generichash_BYTES`
    :type digest_size: int
    :return: a initialized :py:class:`.Blake2State`
    :rtype: object
    """
def generichash_blake2b_update(state: Blake2State, data: bytes) -> None:
    """Update the blake2b hash state

    :param state: a initialized Blake2bState object as returned from
                     :py:func:`.crypto_generichash_blake2b_init`
    :type state: :py:class:`.Blake2State`
    :param data:
    :type data: bytes
    """
def generichash_blake2b_final(state: Blake2State) -> bytes:
    """Finalize the blake2b hash state and return the digest.

    :param state: a initialized Blake2bState object as returned from
                     :py:func:`.crypto_generichash_blake2b_init`
    :type state: :py:class:`.Blake2State`
    :return: the blake2 digest of the passed-in data stream
    :rtype: bytes
    """
