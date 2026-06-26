from _typeshed import Incomplete

PWHASH_SIZE: Incomplete
SALTBYTES: Incomplete
PASSWD_MIN: Incomplete
PASSWD_MAX: Incomplete
BYTES_MAX: Incomplete
BYTES_MIN: Incomplete
ALG_ARGON2I13: Incomplete
ALG_ARGON2ID13: Incomplete
ALG_ARGON2_DEFAULT: Incomplete

def verify(password_hash: bytes, password: bytes) -> bool:
    """
    Takes a modular crypt encoded argon2i or argon2id stored password hash
    and checks if the user provided password will hash to the same string
    when using the stored parameters

    :param password_hash: password hash serialized in modular crypt() format
    :type password_hash: bytes
    :param password: user provided password
    :type password: bytes
    :rtype: boolean

    .. versionadded:: 1.2
    """
