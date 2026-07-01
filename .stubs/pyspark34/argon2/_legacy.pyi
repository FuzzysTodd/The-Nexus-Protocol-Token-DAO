from ._password_hasher import DEFAULT_HASH_LENGTH as DEFAULT_HASH_LENGTH, DEFAULT_MEMORY_COST as DEFAULT_MEMORY_COST, DEFAULT_PARALLELISM as DEFAULT_PARALLELISM, DEFAULT_RANDOM_SALT_LENGTH as DEFAULT_RANDOM_SALT_LENGTH, DEFAULT_TIME_COST as DEFAULT_TIME_COST
from ._typing import Literal as Literal
from .low_level import Type as Type, hash_secret as hash_secret, hash_secret_raw as hash_secret_raw, verify_secret as verify_secret

def hash_password(password: bytes, salt: bytes | None = None, time_cost: int = ..., memory_cost: int = ..., parallelism: int = ..., hash_len: int = ..., type: Type = ...) -> bytes:
    """
    Legacy alias for :func:`argon2.low_level.hash_secret` with default
    parameters.

    .. deprecated:: 16.0.0
        Use :class:`argon2.PasswordHasher` for passwords.
    """
def hash_password_raw(password: bytes, salt: bytes | None = None, time_cost: int = ..., memory_cost: int = ..., parallelism: int = ..., hash_len: int = ..., type: Type = ...) -> bytes:
    """
    Legacy alias for :func:`argon2.low_level.hash_secret_raw` with default
    parameters.

    .. deprecated:: 16.0.0
        Use :class:`argon2.PasswordHasher` for passwords.
    """
def verify_password(hash: bytes, password: bytes, type: Type = ...) -> Literal[True]:
    """
    Legacy alias for :func:`argon2.low_level.verify_secret` with default
    parameters.

    .. deprecated:: 16.0.0
        Use :class:`argon2.PasswordHasher` for passwords.
    """
