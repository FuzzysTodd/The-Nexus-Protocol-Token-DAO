from _typeshed import Incomplete

class InvalidKeyError(Exception):
    """Raises an error when given key is of invalid datatype."""
    prefix: str
    err_msg: Incomplete
    suffix: str
    def __init__(self, hash_data) -> None: ...

class DuplicatedKeysError(Exception):
    """Raise an error when duplicate key found."""
    key: Incomplete
    duplicate_key_indices: Incomplete
    fix_msg: Incomplete
    prefix: str
    err_msg: Incomplete
    suffix: Incomplete
    def __init__(self, key, duplicate_key_indices, fix_msg: str = '') -> None: ...

class KeyHasher:
    """KeyHasher class for providing hash using md5"""
    def __init__(self, hash_salt: str) -> None: ...
    def hash(self, key: str | int | bytes) -> int:
        """Returns 128-bits unique hash of input key

        Args:
        key: the input key to be hashed (should be str, int or bytes)

        Returns: 128-bit int hash key"""
