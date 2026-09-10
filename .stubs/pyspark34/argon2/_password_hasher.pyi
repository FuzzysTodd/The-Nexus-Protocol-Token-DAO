from ._typing import Literal as Literal
from ._utils import Parameters as Parameters, extract_parameters as extract_parameters
from .exceptions import InvalidHashError as InvalidHashError
from .low_level import Type as Type, hash_secret as hash_secret, verify_secret as verify_secret
from .profiles import RFC_9106_LOW_MEMORY as RFC_9106_LOW_MEMORY
from _typeshed import Incomplete

DEFAULT_RANDOM_SALT_LENGTH: Incomplete
DEFAULT_HASH_LENGTH: Incomplete
DEFAULT_TIME_COST: Incomplete
DEFAULT_MEMORY_COST: Incomplete
DEFAULT_PARALLELISM: Incomplete

class PasswordHasher:
    """
    High level class to hash passwords with sensible defaults.

    Uses Argon2\\ **id** by default and always uses a random salt_ for hashing.
    But it can verify any type of Argon2 as long as the hash is correctly
    encoded.

    The reason for this being a class is both for convenience to carry
    parameters and to verify the parameters only *once*.  Any unnecessary
    slowdown when hashing is a tangible advantage for a brute force attacker.

    :param int time_cost: Defines the amount of computation realized and
        therefore the execution time, given in number of iterations.
    :param int memory_cost: Defines the memory usage, given in kibibytes_.
    :param int parallelism: Defines the number of parallel threads (*changes*
        the resulting hash value).
    :param int hash_len: Length of the hash in bytes.
    :param int salt_len: Length of random salt to be generated for each
        password.
    :param str encoding: The Argon2 C library expects bytes.  So if
        :meth:`hash` or :meth:`verify` are passed a ``str``, it will be
        encoded using this encoding.
    :param Type type: Argon2 type to use.  Only change for interoperability
        with legacy systems.

    .. versionadded:: 16.0.0
    .. versionchanged:: 18.2.0
       Switch from Argon2i to Argon2id based on the recommendation by the
       current RFC draft. See also :doc:`parameters`.
    .. versionchanged:: 18.2.0
       Changed default *memory_cost* to 100 MiB and default *parallelism* to 8.
    .. versionchanged:: 18.2.0 ``verify`` now will determine the type of hash.
    .. versionchanged:: 18.3.0 The Argon2 type is configurable now.
    .. versionadded:: 21.2.0 :meth:`from_parameters`
    .. versionchanged:: 21.2.0
       Changed defaults to :data:`argon2.profiles.RFC_9106_LOW_MEMORY`.

    .. _salt: https://en.wikipedia.org/wiki/Salt_(cryptography)
    .. _kibibytes: https://en.wikipedia.org/wiki/Binary_prefix#kibi
    """
    encoding: str
    def __init__(self, time_cost: int = ..., memory_cost: int = ..., parallelism: int = ..., hash_len: int = ..., salt_len: int = ..., encoding: str = 'utf-8', type: Type = ...) -> None: ...
    @classmethod
    def from_parameters(cls, params: Parameters) -> PasswordHasher:
        """
        Construct a `PasswordHasher` from *params*.

        .. versionadded:: 21.2.0
        """
    @property
    def time_cost(self) -> int: ...
    @property
    def memory_cost(self) -> int: ...
    @property
    def parallelism(self) -> int: ...
    @property
    def hash_len(self) -> int: ...
    @property
    def salt_len(self) -> int: ...
    @property
    def type(self) -> Type: ...
    def hash(self, password: str | bytes, *, salt: bytes | None = None) -> str:
        """
        Hash *password* and return an encoded hash.

        Parameters:

            password: Password to hash.

            salt: If None, a random salt is securely created.

                .. danger::

                    You should **not** pass a salt unless you really know what
                    you are doing.

        Raises:

            argon2.exceptions.HashingError: If hashing fails.

        Returns:

            Hashed *password*.

        .. versionadded:: 23.1.0 *salt* parameter
        """
    def verify(self, hash: str | bytes, password: str | bytes) -> Literal[True]:
        """
        Verify that *password* matches *hash*.

        .. warning::

            It is assumed that the caller is in full control of the hash.  No
            other parsing than the determination of the hash type is done by
            *argon2-cffi*.

        :param hash: An encoded hash as returned from
            :meth:`PasswordHasher.hash`.
        :type hash: ``bytes`` or ``str``

        :param password: The password to verify.
        :type password: ``bytes`` or ``str``

        :raises argon2.exceptions.VerifyMismatchError: If verification fails
            because *hash* is not valid for *password*.
        :raises argon2.exceptions.VerificationError: If verification fails for
            other reasons.
        :raises argon2.exceptions.InvalidHashError: If *hash* is so clearly
            invalid, that it couldn't be passed to Argon2.

        :return: ``True`` on success, raise
            :exc:`~argon2.exceptions.VerificationError` otherwise.
        :rtype: bool

        .. versionchanged:: 16.1.0
            Raise :exc:`~argon2.exceptions.VerifyMismatchError` on mismatches
            instead of its more generic superclass.
        .. versionadded:: 18.2.0 Hash type agility.
        """
    def check_needs_rehash(self, hash: str) -> bool:
        """
        Check whether *hash* was created using the instance's parameters.

        Whenever your Argon2 parameters -- or *argon2-cffi*'s defaults! --
        change, you should rehash your passwords at the next opportunity.  The
        common approach is to do that whenever a user logs in, since that
        should be the only time when you have access to the cleartext
        password.

        Therefore it's best practice to check -- and if necessary rehash --
        passwords after each successful authentication.

        :rtype: bool

        .. versionadded:: 18.2.0
        """
