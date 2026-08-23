import nacl.encoding
from _typeshed import Incomplete
from nacl.exceptions import ensure as ensure

AVAILABLE: Incomplete
STRPREFIX: Incomplete
SALTBYTES: Incomplete
PASSWD_MIN: Incomplete
PASSWD_MAX: Incomplete
PWHASH_SIZE: Incomplete
BYTES_MIN: Incomplete
BYTES_MAX: Incomplete
MEMLIMIT_MIN: Incomplete
MEMLIMIT_MAX: Incomplete
OPSLIMIT_MIN: Incomplete
OPSLIMIT_MAX: Incomplete
OPSLIMIT_INTERACTIVE: Incomplete
MEMLIMIT_INTERACTIVE: Incomplete
OPSLIMIT_SENSITIVE: Incomplete
MEMLIMIT_SENSITIVE: Incomplete
OPSLIMIT_MODERATE: Incomplete
MEMLIMIT_MODERATE: Incomplete

def kdf(size: int, password: bytes, salt: bytes, opslimit: int = ..., memlimit: int = ..., encoder: nacl.encoding.Encoder = ...) -> bytes:
    """
    Derive a ``size`` bytes long key from a caller-supplied
    ``password`` and ``salt`` pair using the scryptsalsa208sha256
    memory-hard construct.


    the enclosing module provides the constants

        - :py:const:`.OPSLIMIT_INTERACTIVE`
        - :py:const:`.MEMLIMIT_INTERACTIVE`
        - :py:const:`.OPSLIMIT_SENSITIVE`
        - :py:const:`.MEMLIMIT_SENSITIVE`
        - :py:const:`.OPSLIMIT_MODERATE`
        - :py:const:`.MEMLIMIT_MODERATE`

    as a guidance for correct settings respectively for the
    interactive login and the long term key protecting sensitive data
    use cases.

    :param size: derived key size, must be between
                 :py:const:`.BYTES_MIN` and
                 :py:const:`.BYTES_MAX`
    :type size: int
    :param password: password used to seed the key derivation procedure;
                     it length must be between
                     :py:const:`.PASSWD_MIN` and
                     :py:const:`.PASSWD_MAX`
    :type password: bytes
    :param salt: **RANDOM** salt used in the key derivation procedure;
                 its length must be exactly :py:const:`.SALTBYTES`
    :type salt: bytes
    :param opslimit: the time component (operation count)
                     of the key derivation procedure's computational cost;
                     it must be between
                     :py:const:`.OPSLIMIT_MIN` and
                     :py:const:`.OPSLIMIT_MAX`
    :type opslimit: int
    :param memlimit: the memory occupation component
                     of the key derivation procedure's computational cost;
                     it must be between
                     :py:const:`.MEMLIMIT_MIN` and
                     :py:const:`.MEMLIMIT_MAX`
    :type memlimit: int
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.

    .. versionadded:: 1.2
    """
def str(password: bytes, opslimit: int = ..., memlimit: int = ...) -> bytes:
    """
    Hashes a password with a random salt, using the memory-hard
    scryptsalsa208sha256 construct and returning an ascii string
    that has all the needed info to check against a future password

    The default settings for opslimit and memlimit are those deemed
    correct for the interactive user login case.

    :param bytes password:
    :param int opslimit:
    :param int memlimit:
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.

    .. versionadded:: 1.2
    """
def verify(password_hash: bytes, password: bytes) -> bool:
    """
    Takes the output of scryptsalsa208sha256 and compares it against
    a user provided password to see if they are the same

    :param password_hash: bytes
    :param password: bytes
    :rtype: boolean
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.

    .. versionadded:: 1.2
    """
