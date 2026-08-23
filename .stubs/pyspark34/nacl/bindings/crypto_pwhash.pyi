from _typeshed import Incomplete
from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure
from typing import Tuple

has_crypto_pwhash_scryptsalsa208sha256: Incomplete
crypto_pwhash_scryptsalsa208sha256_STRPREFIX: bytes
crypto_pwhash_scryptsalsa208sha256_SALTBYTES: int
crypto_pwhash_scryptsalsa208sha256_STRBYTES: int
crypto_pwhash_scryptsalsa208sha256_PASSWD_MIN: int
crypto_pwhash_scryptsalsa208sha256_PASSWD_MAX: int
crypto_pwhash_scryptsalsa208sha256_BYTES_MIN: int
crypto_pwhash_scryptsalsa208sha256_BYTES_MAX: int
crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MIN: int
crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MAX: int
crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MIN: int
crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MAX: int
crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_INTERACTIVE: int
crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_INTERACTIVE: int
crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_SENSITIVE: int
crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_SENSITIVE: int
crypto_pwhash_ALG_ARGON2I13: int
crypto_pwhash_ALG_ARGON2ID13: int
crypto_pwhash_ALG_DEFAULT: int
crypto_pwhash_SALTBYTES: int
crypto_pwhash_STRBYTES: int
crypto_pwhash_PASSWD_MIN: int
crypto_pwhash_PASSWD_MAX: int
crypto_pwhash_BYTES_MIN: int
crypto_pwhash_BYTES_MAX: int
crypto_pwhash_argon2i_STRPREFIX: bytes
crypto_pwhash_argon2i_MEMLIMIT_MIN: int
crypto_pwhash_argon2i_MEMLIMIT_MAX: int
crypto_pwhash_argon2i_OPSLIMIT_MIN: int
crypto_pwhash_argon2i_OPSLIMIT_MAX: int
crypto_pwhash_argon2i_OPSLIMIT_INTERACTIVE: int
crypto_pwhash_argon2i_MEMLIMIT_INTERACTIVE: int
crypto_pwhash_argon2i_OPSLIMIT_MODERATE: int
crypto_pwhash_argon2i_MEMLIMIT_MODERATE: int
crypto_pwhash_argon2i_OPSLIMIT_SENSITIVE: int
crypto_pwhash_argon2i_MEMLIMIT_SENSITIVE: int
crypto_pwhash_argon2id_STRPREFIX: bytes
crypto_pwhash_argon2id_MEMLIMIT_MIN: int
crypto_pwhash_argon2id_MEMLIMIT_MAX: int
crypto_pwhash_argon2id_OPSLIMIT_MIN: int
crypto_pwhash_argon2id_OPSLIMIT_MAX: int
crypto_pwhash_argon2id_OPSLIMIT_INTERACTIVE: int
crypto_pwhash_argon2id_MEMLIMIT_INTERACTIVE: int
crypto_pwhash_argon2id_OPSLIMIT_MODERATE: int
crypto_pwhash_argon2id_MEMLIMIT_MODERATE: int
crypto_pwhash_argon2id_OPSLIMIT_SENSITIVE: int
crypto_pwhash_argon2id_MEMLIMIT_SENSITIVE: int
SCRYPT_OPSLIMIT_INTERACTIVE = crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_INTERACTIVE
SCRYPT_MEMLIMIT_INTERACTIVE = crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_INTERACTIVE
SCRYPT_OPSLIMIT_SENSITIVE = crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_SENSITIVE
SCRYPT_MEMLIMIT_SENSITIVE = crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_SENSITIVE
SCRYPT_SALTBYTES = crypto_pwhash_scryptsalsa208sha256_SALTBYTES
SCRYPT_STRBYTES = crypto_pwhash_scryptsalsa208sha256_STRBYTES
SCRYPT_PR_MAX: Incomplete
LOG2_UINT64_MAX: int
UINT64_MAX: Incomplete
SCRYPT_MAX_MEM: Incomplete

def nacl_bindings_pick_scrypt_params(opslimit: int, memlimit: int) -> Tuple[int, int, int]:
    """Python implementation of libsodium's pickparams"""
def crypto_pwhash_scryptsalsa208sha256_ll(passwd: bytes, salt: bytes, n: int, r: int, p: int, dklen: int = 64, maxmem: int = ...) -> bytes:
    """
    Derive a cryptographic key using the ``passwd`` and ``salt``
    given as input.

    The work factor can be tuned by by picking different
    values for the parameters

    :param bytes passwd:
    :param bytes salt:
    :param bytes salt: *must* be *exactly* :py:const:`.SALTBYTES` long
    :param int dklen:
    :param int opslimit:
    :param int n:
    :param int r: block size,
    :param int p: the parallelism factor
    :param int maxmem: the maximum available memory available for scrypt's
                       operations
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
def crypto_pwhash_scryptsalsa208sha256_str(passwd: bytes, opslimit: int = ..., memlimit: int = ...) -> bytes:
    """
    Derive a cryptographic key using the ``passwd`` and ``salt``
    given as input, returning a string representation which includes
    the salt and the tuning parameters.

    The returned string can be directly stored as a password hash.

    See :py:func:`.crypto_pwhash_scryptsalsa208sha256` for a short
    discussion about ``opslimit`` and ``memlimit`` values.

    :param bytes passwd:
    :param int opslimit:
    :param int memlimit:
    :return: serialized key hash, including salt and tuning parameters
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
def crypto_pwhash_scryptsalsa208sha256_str_verify(passwd_hash: bytes, passwd: bytes) -> bool:
    """
    Verifies the ``passwd`` against the ``passwd_hash`` that was generated.
    Returns True or False depending on the success

    :param passwd_hash: bytes
    :param passwd: bytes
    :rtype: boolean
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
def crypto_pwhash_alg(outlen: int, passwd: bytes, salt: bytes, opslimit: int, memlimit: int, alg: int) -> bytes:
    """
    Derive a raw cryptographic key using the ``passwd`` and the ``salt``
    given as input to the ``alg`` algorithm.

    :param outlen: the length of the derived key
    :type outlen: int
    :param passwd: The input password
    :type passwd: bytes
    :param salt:
    :type salt: bytes
    :param opslimit: computational cost
    :type opslimit: int
    :param memlimit: memory cost
    :type memlimit: int
    :param alg: algorithm identifier
    :type alg: int
    :return: derived key
    :rtype: bytes
    """
def crypto_pwhash_str_alg(passwd: bytes, opslimit: int, memlimit: int, alg: int) -> bytes:
    """
    Derive a cryptographic key using the ``passwd`` given as input
    and a random salt, returning a string representation which
    includes the salt, the tuning parameters and the used algorithm.

    :param passwd: The input password
    :type passwd: bytes
    :param opslimit: computational cost
    :type opslimit: int
    :param memlimit: memory cost
    :type memlimit: int
    :param alg: The algorithm to use
    :type alg: int
    :return: serialized derived key and parameters
    :rtype: bytes
    """
def crypto_pwhash_str_verify(passwd_hash: bytes, passwd: bytes) -> bool:
    """
    Verifies the ``passwd`` against a given password hash.

    Returns True on success, raises InvalidkeyError on failure
    :param passwd_hash: saved password hash
    :type passwd_hash: bytes
    :param passwd: password to be checked
    :type passwd: bytes
    :return: success
    :rtype: boolean
    """
crypto_pwhash_argon2i_str_verify = crypto_pwhash_str_verify
