import nacl.encoding
from _typeshed import Incomplete

ALG: Incomplete
STRPREFIX: Incomplete
SALTBYTES: Incomplete
PASSWD_MIN: Incomplete
PASSWD_MAX: Incomplete
PWHASH_SIZE: Incomplete
BYTES_MIN: Incomplete
BYTES_MAX: Incomplete
verify: Incomplete
MEMLIMIT_MAX: Incomplete
MEMLIMIT_MIN: Incomplete
OPSLIMIT_MAX: Incomplete
OPSLIMIT_MIN: Incomplete
OPSLIMIT_INTERACTIVE: Incomplete
MEMLIMIT_INTERACTIVE: Incomplete
OPSLIMIT_SENSITIVE: Incomplete
MEMLIMIT_SENSITIVE: Incomplete
OPSLIMIT_MODERATE: Incomplete
MEMLIMIT_MODERATE: Incomplete

def kdf(size: int, password: bytes, salt: bytes, opslimit: int = ..., memlimit: int = ..., encoder: nacl.encoding.Encoder = ...) -> bytes:
    """
    Derive a ``size`` bytes long key from a caller-supplied
    ``password`` and ``salt`` pair using the argon2i
    memory-hard construct.

    the enclosing module provides the constants

        - :py:const:`.OPSLIMIT_INTERACTIVE`
        - :py:const:`.MEMLIMIT_INTERACTIVE`
        - :py:const:`.OPSLIMIT_MODERATE`
        - :py:const:`.MEMLIMIT_MODERATE`
        - :py:const:`.OPSLIMIT_SENSITIVE`
        - :py:const:`.MEMLIMIT_SENSITIVE`

    as a guidance for correct settings.

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

    .. versionadded:: 1.2
    """
def str(password: bytes, opslimit: int = ..., memlimit: int = ...) -> bytes:
    """
    Hashes a password with a random salt, using the memory-hard
    argon2i construct and returning an ascii string that has all
    the needed info to check against a future password


    The default settings for opslimit and memlimit are those deemed
    correct for the interactive user login case.

    :param bytes password:
    :param int opslimit:
    :param int memlimit:
    :rtype: bytes

    .. versionadded:: 1.2
    """
