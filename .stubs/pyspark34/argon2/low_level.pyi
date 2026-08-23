from ._typing import Literal
from _argon2_cffi_bindings import ffi as ffi
from _typeshed import Incomplete
from enum import Enum

__all__ = ['ARGON2_VERSION', 'Type', 'ffi', 'hash_secret', 'hash_secret_raw', 'verify_secret']

ARGON2_VERSION: Incomplete

class Type(Enum):
    """
    Enum of Argon2 variants.

    Please see :doc:`parameters` on how to pick one.
    """
    D: Incomplete
    I: Incomplete
    ID: Incomplete

def hash_secret(secret: bytes, salt: bytes, time_cost: int, memory_cost: int, parallelism: int, hash_len: int, type: Type, version: int = ...) -> bytes:
    """
    Hash *secret* and return an **encoded** hash.

    An encoded hash can be directly passed into :func:`verify_secret` as it
    contains all parameters and the salt.

    :param bytes secret: Secret to hash.
    :param bytes salt: A salt_.  Should be random and different for each
        secret.
    :param Type type: Which Argon2 variant to use.
    :param int version: Which Argon2 version to use.

    For an explanation of the Argon2 parameters see
    :class:`argon2.PasswordHasher`.

    :rtype: bytes

    :raises argon2.exceptions.HashingError: If hashing fails.

    .. versionadded:: 16.0.0

    .. _salt: https://en.wikipedia.org/wiki/Salt_(cryptography)
    .. _kibibytes: https://en.wikipedia.org/wiki/Binary_prefix#kibi
    """
def hash_secret_raw(secret: bytes, salt: bytes, time_cost: int, memory_cost: int, parallelism: int, hash_len: int, type: Type, version: int = ...) -> bytes:
    """
    Hash *password* and return a **raw** hash.

    This function takes the same parameters as :func:`hash_secret`.

    .. versionadded:: 16.0.0
    """
def verify_secret(hash: bytes, secret: bytes, type: Type) -> Literal[True]:
    """
    Verify whether *secret* is correct for *hash* of *type*.

    :param bytes hash: An encoded Argon2 hash as returned by
        :func:`hash_secret`.
    :param bytes secret: The secret to verify whether it matches the one
        in *hash*.
    :param Type type: Type for *hash*.

    :raises argon2.exceptions.VerifyMismatchError: If verification fails
        because *hash* is not valid for *secret* of *type*.
    :raises argon2.exceptions.VerificationError: If verification fails for
        other reasons.

    :return: ``True`` on success, raise
        :exc:`~argon2.exceptions.VerificationError` otherwise.
    :rtype: bool

    .. versionadded:: 16.0.0
    .. versionchanged:: 16.1.0
        Raise :exc:`~argon2.exceptions.VerifyMismatchError` on mismatches
        instead of its more generic superclass.
    """
