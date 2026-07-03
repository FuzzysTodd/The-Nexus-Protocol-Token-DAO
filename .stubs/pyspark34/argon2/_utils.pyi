from .exceptions import InvalidHashError as InvalidHashError
from .low_level import Type as Type
from _typeshed import Incomplete
from dataclasses import dataclass

NoneType: Incomplete

@dataclass
class Parameters:
    """
    Argon2 hash parameters.

    See :doc:`parameters` on how to pick them.

    :ivar Type type: Hash type.
    :ivar int version: Argon2 version.
    :ivar int salt_len: Length of the salt in bytes.
    :ivar int hash_len: Length of the hash in bytes.
    :ivar int time_cost: Time cost in iterations.
    :ivar int memory_cost: Memory cost in kibibytes.
    :ivar int parallelism: Number of parallel threads.

    .. versionadded:: 18.2.0
    """
    type: Type
    version: int
    salt_len: int
    hash_len: int
    time_cost: int
    memory_cost: int
    parallelism: int
    def __init__(self, type, version, salt_len, hash_len, time_cost, memory_cost, parallelism) -> None: ...

def extract_parameters(hash: str) -> Parameters:
    """
    Extract parameters from an encoded *hash*.

    :param str params: An encoded Argon2 hash string.

    :rtype: Parameters

    .. versionadded:: 18.2.0
    """
