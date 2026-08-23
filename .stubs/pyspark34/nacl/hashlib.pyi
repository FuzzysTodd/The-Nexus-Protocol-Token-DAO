from _typeshed import Incomplete
from nacl.utils import bytes_as_string as bytes_as_string
from typing import NoReturn

BYTES: Incomplete
BYTES_MIN: Incomplete
BYTES_MAX: Incomplete
KEYBYTES: Incomplete
KEYBYTES_MIN: Incomplete
KEYBYTES_MAX: Incomplete
SALTBYTES: Incomplete
PERSONALBYTES: Incomplete
SCRYPT_AVAILABLE: Incomplete

class blake2b:
    """
    :py:mod:`hashlib` API compatible blake2b algorithm implementation
    """
    MAX_DIGEST_SIZE = BYTES
    MAX_KEY_SIZE = KEYBYTES_MAX
    PERSON_SIZE = PERSONALBYTES
    SALT_SIZE = SALTBYTES
    def __init__(self, data: bytes = b'', digest_size: int = ..., key: bytes = b'', salt: bytes = b'', person: bytes = b'') -> None:
        """
        :py:class:`.blake2b` algorithm initializer

        :param data:
        :type data: bytes
        :param int digest_size: the requested digest size; must be
                                at most :py:attr:`.MAX_DIGEST_SIZE`;
                                the default digest size is :py:data:`.BYTES`
        :param key: the key to be set for keyed MAC/PRF usage; if set,
                    the key must be at most :py:data:`.KEYBYTES_MAX` long
        :type key: bytes
        :param salt: a initialization salt at most
                     :py:attr:`.SALT_SIZE` long; it will be zero-padded
                     if needed
        :type salt: bytes
        :param person: a personalization string at most
                       :py:attr:`.PERSONAL_SIZE` long; it will be zero-padded
                       if needed
        :type person: bytes
        """
    @property
    def digest_size(self) -> int: ...
    @property
    def block_size(self) -> int: ...
    @property
    def name(self) -> str: ...
    def update(self, data: bytes) -> None: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def copy(self) -> blake2b: ...
    def __reduce__(self) -> NoReturn:
        """
        Raise the same exception as hashlib's blake implementation
        on copy.copy()
        """

def scrypt(password: bytes, salt: bytes = b'', n: int = ..., r: int = 8, p: int = 1, maxmem: int = ..., dklen: int = 64) -> bytes:
    """
    Derive a cryptographic key using the scrypt KDF.

    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.

    Implements the same signature as the ``hashlib.scrypt`` implemented
    in cpython version 3.6
    """
